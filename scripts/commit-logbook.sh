#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "Staging grouped changes and creating commits..."

# Commit 1: logbook governance
git add docs/logbook.md
git commit -m "chore(logbook): enforce commit-corresponding logbook entries"

# Commit 2: research protocol prompt and methodology references
git add docs/research-protocol-prompt.md docs/methodology.md
git commit -m "feat(methodology): add executable research protocol agent prompt"

# Commit 3: AI governance and ethics documentation
git add .instructions.md copilot-instructions.md CLAUDE_CODE_INSTRUCTIONS.md docs/ethics.md docs/sources.md
git commit -m "docs(governance): add AI instruction policy and ethics documentation"

# Commit 4: paper skeleton and publication support
git add README.md paper/main.md paper/references.bib scripts/README.md
git commit -m "docs(paper): add paper skeleton and publication metadata"

# Commit 5: experiment artifacts and raw conversation exports
git add "experiments/spider-farmer/README.md" "experiments/ecoflow-powerocean/README.md" "experiments/spider-farmer/raw_conversations (copy&paste, web)" "experiments/ecoflow-powerocean/raw_conversations (copy&paste, web)"
git commit -m "chore(experiments): add case study readmes and preserved conversation exports"

# Commit 6: KPI framework and logbook provenance
git add docs/methodology.md docs/logbook.md
git commit -m "feat(methodology): add KPI framework and logbook provenance entry"

echo "Done. Please copy the resulting commit SHAs into docs/logbook.md to complete the provenance record."
