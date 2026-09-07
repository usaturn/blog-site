# blog-site

usaturn の個人ブログ。Sphinx と [MaatLog](https://github.com/usaturn/maatlog) で生成し、Cloudflare Pages で配信する。

公開先: <https://blog.usaturn.net/>

## 制約

Python の実行は常に uv 経由で行う。`python` や `pip` を直接呼ばない。

## ビルド

```
bash scripts/build.sh
```

Cloudflare Pages のビルドも同じスクリプトを実行する。
uv がビルド環境に無ければ自前で導入し、`pyproject.toml` の `requires-python` に従って Python 3.14 を取得する。
`.python-version` は**置かない**。置くと Cloudflare 側が Python 3.14 をソースからコンパイルし、ビルドが 2 分ほど長くなる。

出力先は `_build/html` である。Cloudflare 側のビルド出力ディレクトリもこの値に設定する。

このリポジトリに `wrangler.jsonc` は**置かない**。置くと Pages がビルド設定をそこから読み、ダッシュボードのビルド変数（`SKIP_DEPENDENCY_INSTALL` など）を無視するためである。

## 執筆中のプレビュー

```
uv run sphinx-autobuild source _build/html --host 0.0.0.0 --port 8000
```

## Pages としての配信確認

URL の正規化や 404 の扱いは `sphinx-autobuild` では再現されない。
配信の挙動を確かめるときはこちらを使う。

```
npm ci
bash scripts/build.sh
npx wrangler pages dev _build/html
```

設定ファイルを置いていないため、配信するディレクトリを引数で渡す。
既定のポートは **8788** である（Workers の `wrangler dev` は 8787 なので混同しない）。

Pages は拡張子なしの URL を正とする。`/posts/hello.html` は `/posts/hello` へ 308 で誘導される。
存在しないパスには `404.html` が 404 で返る。Pages が `404.html` の存在を自動で検出するため、設定は要らない。

## 秘密情報の混入防止

`.githooks/pre-commit` が gitleaks で staged の差分を走査し、秘密情報が混ざったコミットを止める。

このフックは `core.hooksPath` を設定して初めて有効になる。開発環境リポジトリの Dev Container はコンテナ作成時にこれを設定するが、**このリポジトリを単体で clone した場合は自分で設定する必要がある**。

```
git config core.hooksPath .githooks
```

設定しないとフックは呼ばれず、警告も出ない。また gitleaks が PATH に無い環境では、フックは走査を省略して commit を通す。

## 公開

`main` への push で `blog.usaturn.net` に本番公開される。
それ以外のブランチへの push ではプレビューデプロイが作られ、ブランチ名に基づく安定した URL が PR にコメントされる。

独自ドメインは Cloudflare のネームサーバを必要としない。権威 DNS が外部にあるままでも、`blog` の CNAME を Pages プロジェクトの `*.pages.dev` ホストへ向ければ有効になる。
