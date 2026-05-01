#!/usr/bin/env bash
# Convenience wrapper around paper/Makefile.
#
# Usage:
#   scripts/build-paper.sh           # build PDF
#   scripts/build-paper.sh arxiv     # build arXiv submission tarball
#   scripts/build-paper.sh clean     # remove build artifacts

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root/paper"

target="${1:-pdf}"
exec make "$target"
