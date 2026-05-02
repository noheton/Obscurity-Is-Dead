#!/bin/bash
# SessionStart hook for Obscurity-Is-Dead.
#
# Provisions the LaTeX + SVG toolchain required by stage 4 of the agent
# pipeline (the Layout Scrutinizer in docs/prompts/layout-scrutinizer-prompt.md),
# which depends on `make -C paper pdf` succeeding.
#
# Idempotent: skips installation when latexmk and rsvg-convert are both on PATH.
set -euo pipefail

# Web-only: locally the user is expected to manage their own TeX install.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

if command -v latexmk >/dev/null 2>&1 \
   && command -v rsvg-convert >/dev/null 2>&1 \
   && command -v biber >/dev/null 2>&1; then
  echo "[session-start] LaTeX + SVG toolchain already present; skipping apt install."
else
  echo "[session-start] Installing LaTeX + SVG toolchain via apt-get..."
  export DEBIAN_FRONTEND=noninteractive

  SUDO=""
  if [ "$(id -u)" -ne 0 ]; then
    SUDO="sudo"
  fi

  # Some sandbox images carry third-party PPAs that intermittently 403.
  # We only need the main Ubuntu archive, so tolerate update failures.
  $SUDO apt-get update -y || true
  $SUDO apt-get install -y --no-install-recommends \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-bibtex-extra \
    lmodern \
    latexmk \
    biber \
    librsvg2-bin
fi

echo "[session-start] Verifying toolchain via 'make -C paper check'..."
make -C "${CLAUDE_PROJECT_DIR:-$(pwd)}/paper" check
