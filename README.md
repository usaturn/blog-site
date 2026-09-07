# blog-site

usaturn の個人ブログ。Sphinx と [MaatLog](https://github.com/usaturn/maatlog) で生成し、Cloudflare Workers で配信する。

公開先: <https://blog.usaturn.net/>

## 制約

Python の実行は常に uv 経由で行う。`python` や `pip` を直接呼ばない。

## ビルド

```
bash scripts/build.sh
```

Cloudflare Workers Builds も同じスクリプトを実行する。
uv がビルド環境に無ければ自前で導入し、`.python-version` に従って Python 3.14 を取得する。

## 執筆中のプレビュー

```
uv run sphinx-autobuild source _build/html --host 0.0.0.0 --port 8000
```

## Workers としての配信確認

`not_found_handling` やアセットのルーティングは `sphinx-autobuild` では再現されない。
配信の挙動を確かめるときはこちらを使う。

```
npm ci
bash scripts/build.sh
npx wrangler dev
```

## 公開

`main` への push で `blog.usaturn.net` に本番公開される。
それ以外のブランチへの push では preview URL が生成され、PR にコメントされる。
