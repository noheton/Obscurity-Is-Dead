#!/usr/bin/env python3
"""Sort docs/logbook.md entries chronologically (oldest first).

Strategy:
- Preserve the file's leading header (everything before the first `### `).
- Split the rest into entries (each entry starts at a `### ` heading and runs
  until the next `### ` or EOF).
- Extract a (date, secondary, original_index) sort key per entry and sort by
  (date asc, secondary asc, original_index asc).
- Concatenate header + sorted entries.

Secondary key tiebreakers within the same date:
- "Session N — ..." entries → use N (so Session 12 lands between 11 and 13).
- "pass N" / "loop N" / "round N" → use N.
- "(IoT Integrator ... Phase N ...)" → use N as a coarser secondary.
- Otherwise → original file order (so the existing reverse-chrono within day
  becomes oldest-first within day after we reverse the inter-day axis).

If a heading lacks a parseable date, we fall back to the previous parsed date
+ the original index (so "headers" like '### 2026-05-04 (...)' still group
correctly and unparseable entries stay near their neighbours).
"""
import re
from pathlib import Path

PATH = Path("/home/user/Obscurity-Is-Dead/docs/logbook.md")
text = PATH.read_text()

m = re.search(r"^### ", text, re.MULTILINE)
if not m:
    raise SystemExit("no entries found")
header_block = text[: m.start()]

# Split into entry blocks (each starts with `### `).
entry_pat = re.compile(r"^### .*?(?=^### |\Z)", re.MULTILINE | re.DOTALL)
entries = entry_pat.findall(text)

DATE_RE = re.compile(r"(20\d{2})-(\d{2})-(\d{2})")
SESSION_RE = re.compile(r"Session\s+(\d+)\s*[-—–]\s*(20\d{2})-(\d{2})-(\d{2})", re.IGNORECASE)
PASS_RE = re.compile(r"\b(?:pass|loop|round|session)\s*(\d+)\b", re.IGNORECASE)
PHASE_RE = re.compile(r"\bPhase\s*(\d+)\b", re.IGNORECASE)

def keyfor(idx, entry):
    head = entry.splitlines()[0]
    m_sess = SESSION_RE.search(head)
    if m_sess:
        sess_n = int(m_sess.group(1))
        date = (int(m_sess.group(2)), int(m_sess.group(3)), int(m_sess.group(4)))
        # within Session-style group, sort by Session number
        return (date, 0, sess_n, idx)
    m_date = DATE_RE.search(head)
    if not m_date:
        # fallback: cluster at end
        return ((9999, 12, 31), 9, 0, idx)
    date = (int(m_date.group(1)), int(m_date.group(2)), int(m_date.group(3)))
    # secondary: Phase / pass / loop / round if present, else 0
    m_phase = PHASE_RE.search(head)
    if m_phase:
        return (date, 1, int(m_phase.group(1)), idx)
    m_pass = PASS_RE.search(head)
    if m_pass:
        return (date, 1, int(m_pass.group(1)), idx)
    # No numeric subkey: within-day order is reverse of file order so the
    # existing reverse-chrono within day flips to chronological.
    return (date, 1, 0, -idx)

indexed = list(enumerate(entries))
indexed.sort(key=lambda ie: keyfor(*ie))
sorted_entries = [e for _, e in indexed]

new_text = header_block + "".join(sorted_entries)
# Make sure trailing newline exists.
if not new_text.endswith("\n"):
    new_text += "\n"

PATH.write_text(new_text)
print(f"sorted {len(entries)} entries")
