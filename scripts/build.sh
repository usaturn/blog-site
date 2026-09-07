#!/bin/bash
set -euo pipefail

# Cloudflare Workers Builds のビルドイメージには uv が入っていない。
# uv に Python 3.14 を取得させることで、イメージ既定の Python (3.13.3) から
# 切り離す。手元の devcontainer では uv が既にあるためこの分岐は通らない。
if ! command -v uv >/dev/null 2>&1; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="${HOME}/.local/bin:${PATH}"
fi

# --frozen は uv.lock と pyproject.toml のずれをビルド失敗として扱う。
# 本番で暗黙に依存バージョンが動くことを防ぐ。
uv sync --frozen
uv run sphinx-build -b html source _build/html
