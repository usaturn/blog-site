#!/bin/bash
set -euo pipefail

# Cloudflare Pages のビルドイメージには uv が入っていない。
# uv に Python 3.14 を取得させることで、イメージ既定の Python から切り離す。
# 手元の devcontainer では uv が既にあるためこの分岐は通らない。
if ! command -v uv >/dev/null 2>&1; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="${HOME}/.local/bin:${PATH}"
fi

# --frozen は uv.lock と pyproject.toml のずれをビルド失敗として扱う。
# 本番で暗黙に依存バージョンが動くことを防ぐ。
# --no-dev は sphinx-autobuild とその依存を除く。手元のプレビュー専用であり
# 本番のビルドには要らない。
uv sync --frozen --no-dev
uv run sphinx-build -b html source _build/html
