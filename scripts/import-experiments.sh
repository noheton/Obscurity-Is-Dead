#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p experiments/spider-farmer/original experiments/ecoflow-powerocean/original

if [ -n "${GH_TOKEN:-}" ]; then
  auth_url_sf="https://x-access-token:${GH_TOKEN}@github.com/noheton/spider_farmer.git"
  auth_url_ef="https://x-access-token:${GH_TOKEN}@github.com/noheton/powerocean-dev.git"
  export GIT_TERMINAL_PROMPT=0
fi

if [ -d experiments/spider-farmer/original/.git ] || [ -f experiments/spider-farmer/original/README.md ]; then
  echo "Spider Farmer repo may already be present in experiments/spider-farmer/original."
else
  echo "Cloning Spider Farmer..."
  if [ -n "${GH_TOKEN:-}" ]; then
    git clone --depth 1 "$auth_url_sf" experiments/spider-farmer/original
  else
    git clone --depth 1 https://github.com/noheton/spider_farmer experiments/spider-farmer/original
  fi
fi

if [ -d experiments/ecoflow-powerocean/original/.git ] || [ -f experiments/ecoflow-powerocean/original/README.md ]; then
  echo "EcoFlow PowerOcean repo may already be present in experiments/ecoflow-powerocean/original."
else
  echo "Cloning EcoFlow PowerOcean..."
  if [ -n "${GH_TOKEN:-}" ]; then
    git clone --depth 1 "$auth_url_ef" experiments/ecoflow-powerocean/original
  else
    git clone --depth 1 https://github.com/noheton/powerocean-dev experiments/ecoflow-powerocean/original
  fi
fi

echo "Import complete."
