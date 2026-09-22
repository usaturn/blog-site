# 旧ブログの移植記録

移植元: [usaturn/blog](https://github.com/usaturn/blog/tree/d9d8360659e4b7019a6df54ea502541a94911d61)（アーカイブ済み）
対象コミット: `d9d8360659e4b7019a6df54ea502541a94911d61`
確認日: 2026-09-22

## 移植方針と資産一覧

旧サイトの公開 URL と記事間参照を保つため、コンテンツは `source/contents/` に配置した。
MaatLog 0.4.0 と現在のビルド環境を使用し、旧リポジトリの開発環境は取り込んでいない。

| 対象 | 数 | 移植先・扱い |
|---|---:|---|
| 記事 | 34 | `source/contents/{2012,2016,2024,2025}/`。公開日時・slug・タグ・カテゴリ・著者を維持 |
| アドベントカレンダー説明 | 1 | `contents/2012/at_the_beginning.rst`。日付を推測せず補助ページのまま保持、toctree に追加 |
| 古い記事への注意書き | 1 | `contents/2012/warning.rst`。include 専用として単独ビルドから除外し、不要な `:orphan:` を除去 |
| 記事内画像 | 66 | 年別の画像ディレクトリを保持。未参照画像も原稿用資産として保持 |
| 添付・include 用ファイル | 7 | 下記一覧。バイト単位で原本と一致 |
| ロゴ・アイコン | 2 | `source/_static/usaturn_logo.png` と `usaturn_icon.png`。ヘッダー、favicon、著者プロフィールに使用 |
| プロフィール | 1 | `source/about.rst` と `maatlog_author_profiles`。旧肩書きを維持し、Twitter を X 表記へ更新、GitHub と記事の主題を追加 |
| サイト名 | 1 | 「星のダンスを見においで」を復元 |
| 分類と表示設定 | 18 タグ / 5 カテゴリ / 1 著者 | `source/conf.py`。Asia/Tokyo、10 件単位のアーカイブ、20 件の Atom フィード、分類別フィードを保持 |
| トップページ | 1 | MaatLog 標準ホーム。最新記事・全記事一覧・分類・著者・年月アーカイブから過去記事を辿れる |

添付・include 用ファイル:

- `contents/2012/files/build_and_browsing.vbs`
- `contents/2012/files/build_and_browsing.zip`
- `contents/2012/files/lexers.txt`
- `contents/2012/files/yes_or_no.sh`
- `contents/2016/kernel_parameter.txt`
- `contents/files/setup-config.yaml.template`
- `contents/include_files/resonite_headless_link.txt`

旧 `images/` には上記 2 画像のみがあり、独立したバナー画像はない。
旧 `_static/custom.css` のメタデータ隠蔽は現在の MaatLog では不要で、本文の正当な field-list を消す危険もあるため移植しない。
旧テーマ依存の背景色・文字色も標準テーマと干渉するため移植しない。独自 CSS は追加していない。
旧 `conf.py` の拡張のうち、現行構成で使用するのは `maatlog` のみである。
旧サイトでコードブロックのコピーボタンを提供していた `sphinx_copybutton` は移植しておらず、現行構成ではそのボタンを提供しない。
`column` ディレクティブ、旧 `_templates/layout.html` の Universal Analytics も移植しない。
`.devcontainer/`、Makefile、pyproject.toml、uv.lock、旧スクリプト、CLAUDE.md、.mcp.json は対象外。
現行の疎通確認記事 `posts/hello.rst` は実記事への置換に伴い削除した。

## RST とリンクの調整

- 本文の句点・改行、インライン記法の空白、見出し幅に `wabun-rst-ulint` の自動整形を適用した。句点・改行には検査漏れが残っている（検証記録を参照）
- 相対画像参照、`:ref:`、toctree、literalinclude、download を維持した
- pyhack、pyhackcon、Secret Manager の埋め込み参照に不足していた `_` を補い、誤ったローカルリンク 3 件を修正した
- サクラエディタの公式サイト・ヘルプ・ダウンロード先を現行の公式サイト／GitHub Releases へ更新した
- Python 2.7.3 のリンクを同じバージョンの公式リリースページへ更新した
- Claude Code CLI の参照先を現行の `cli-reference` へ更新した
- 過去記事の手順や公開日時は現在の内容に書き換えていない

## 記事一覧

公開パスは表の docname に `.html` を付けた旧形式を保持する。
Cloudflare Pages は `.html` 付き URL を拡張子なしへリダイレクトする。
元記事の公開日時に従うため、ディレクトリが `2024` の uv 記事もアーカイブ上は `2025-01` に現れる。

| docname | 公開日時 | 記事 |
|---|---|---|
| `contents/2012/first_time` | 2012-12-01T00:00:00+09:00 | 第1日目 Sphinx環境を構築しよう！ |
| `contents/2012/make_on_sakura` | 2012-12-10T00:00:00+09:00 | 本家 Sphinx Advent Calendar 2012 10日目 ～サクラエディタから make html～ |
| `contents/2012/start_sphinx_project` | 2012-12-02T00:00:00+09:00 | 第2日目 Sphinxでドキュメント作成を開始する |
| `contents/2012/write_rest1` | 2012-12-04T00:00:00+09:00 | 第4日目 Sphinxドキュメントを編集する その１ |
| `contents/2012/write_rest10` | 2012-12-13T00:00:00+09:00 | 第13日目 Sphinxドキュメントを編集する その１０ |
| `contents/2012/write_rest2` | 2012-12-05T00:00:00+09:00 | 第5日目 Sphinxドキュメントを編集する その２ |
| `contents/2012/write_rest3` | 2012-12-06T00:00:00+09:00 | 第6日目 Sphinxドキュメントを編集する その３ |
| `contents/2012/write_rest4` | 2012-12-07T00:00:00+09:00 | 第7日目 Sphinxドキュメントを編集する その４ |
| `contents/2012/write_rest5` | 2012-12-08T00:00:00+09:00 | 第8日目 Sphinxドキュメントを編集する その５ |
| `contents/2012/write_rest6` | 2012-12-09T00:00:00+09:00 | 第9日目 Sphinxドキュメントを編集する その６ |
| `contents/2012/write_rest7` | 2012-12-10T00:00:00+09:00 | 第10日目 Sphinxドキュメントを編集する その７ |
| `contents/2012/write_rest8` | 2012-12-11T00:00:00+09:00 | 第11日目 Sphinxドキュメントを編集する その８ |
| `contents/2012/write_rest9` | 2012-12-12T00:00:00+09:00 | 第12日目 Sphinxドキュメントを編集する その９ |
| `contents/2012/writing_tool` | 2012-12-03T00:00:00+09:00 | 第3日目 Sphinxドキュメントを書く道具 |
| `contents/2016/about_kiban` | 2016-09-11T00:00:00+09:00 | 基板覚書 |
| `contents/2016/build_uefi_for_qemu` | 2016-09-03T00:00:00+09:00 | QEMU の為の UEFI ファームウェアのビルド手順 |
| `contents/2016/installing_gentoo_modernly` | 2016-12-11T00:00:00+09:00 | Gentoo Linux を sysytemd でインストールする（裏） |
| `contents/2016/manage_spawn_container` | 2016-12-13T00:00:00+09:00 | systemd-nspawn コンテナを便利に使おう |
| `contents/2016/setting_libvirt_for_uefi` | 2016-09-04T00:00:00+09:00 | libvirt の UEFI 設定 |
| `contents/2016/start_nspawn_on_gentoo` | 2016-12-12T00:00:00+09:00 | Gentoo に systemd-nspawn を導入する |
| `contents/2024/about_a_resonite_headless_server_on_compute_engine` | 2024-12-02T00:00:00+09:00 | resonite ヘッドレスサーバを Google Cloud で建てるオススメ |
| `contents/2024/about_operating_a_resonite_headless_server_on_gce_for_one_year` | 2024-12-11T00:00:00+09:00 | Google Cloud Compute Engine で resonite ヘッドレスサーバを運用しての感想（駄文） |
| `contents/2024/access_a_headless_server_interactive_shell` | 2024-12-05T00:00:00+09:00 | GCE インスタンスの resonite ヘッドレスサーバ対話シェルにアクセスしよう |
| `contents/2024/check_the_price_and_choose_an_instance` | 2024-12-09T00:00:00+09:00 | ヘッドレスサーバ に使うマシンタイプの選び方と費用感 |
| `contents/2024/clone_a_headless_server_instance` | 2024-12-08T00:00:00+09:00 | resonite ヘッドレスサーバの GCE インスタンスを複製しよう |
| `contents/2024/explaining_resonite_headless_server_on_compute_engine` | 2024-12-04T00:00:00+09:00 | Google Cloud で resonite ヘッドレスサーバ を構築する ～解説編～ |
| `contents/2024/explanation_of_setup_config` | 2024-12-10T00:00:00+09:00 | setup-config.yaml の解説 |
| `contents/2024/pyhack_snow_mountain_camp` | 2024-01-24T00:00:00+09:00 | Python mini hack-a-thon 雪山合宿 2024 |
| `contents/2024/schedule_gce_instance` | 2024-12-07T00:00:00+09:00 | GCE インスタンスのスケジュール設定をしよう |
| `contents/2024/set_up_a_resonite_headless_server_on_compute_engine` | 2024-12-03T00:00:00+09:00 | Google Cloud で resonite ヘッドレスサーバ を構築する |
| `contents/2024/setup_mise` | 2024-11-30T00:00:00+09:00 | mise をセットアップする |
| `contents/2024/setup_python_environment_using_uv` | 2025-01-04T00:00:00+09:00 | uv を利用した Python 環境のセットアップメモ |
| `contents/2024/update_a_resonite_headless_server_config` | 2024-12-06T00:00:00+09:00 | GCE インスタンス上の resonite ヘッドレスサーバ の Config を更新しよう |
| `contents/2025/How_to_use_claude_code` | 2025-06-28T00:00:00+09:00 | 初心者が Claude Code を使い始めたメモ |

## 検証記録

- `uv run sphinx-build -b html -W --keep-going -n -E source _build/html`: warning / error なし
- `wabun-rst-ulint` の `inline-spacing` / `heading-width`: 違反なし
- `wabun-rst-ulint 0.0.1` の `sentence-breaks`: 終了コード 0。ただし、インラインリンクを含む行以降が検査されないケースを確認した。`contents/2016/start_nspawn_on_gentoo.rst` の「はじめに」には 1 行に複数文が残っており、全体の句点・改行の規約適合は確認できていない
- 生成 HTML 84 ページの内部リンク・画像・スクリプト・CSS・アンカー 6,529 件: 参照先の欠落なし
- ローカル Pages + Chromium: 全 34 記事、129 画像表示、4 ページのアーカイブから 34 記事へ到達、ZIP のバイト一致、旧 `.html` URL の 308、未存在 URL の 404 を確認
- 幅 1440 / 390 px でトップ・プロフィール・各年代の代表記事 7 ページを確認。横スクロールなし、ブラウザ例外なし
- `bash scripts/build.sh`: 本番と同一の手順でビルド成功
- 全 34 記事の MaatLog メタデータ: 移植元と一致
- 画像・添付・include ファイル: 移植元とバイト単位で一致（元の CRLF・末尾空白も保持）

外部リンクは Sphinx linkcheck（timeout 12 秒、retry 1 回、10 workers、外部アンカー検査なし）で検査した。
検査対象 107 URI の内訳は working 48、redirected 34、unchecked 18（mailto 1 件と内部アンカー 17 件）、broken 7。
以下は移植元から残る参照であり、代替を確定できないため元 URL を維持した。外部リンク検査は成功扱いにしていない。

| URL | 結果 | 対応 |
|---|---|---|
| `http://note.sicafe.net/sphinx_memo/installAtWinNoAdmin.html` | DNS 解決失敗 | 過去の参照を維持 |
| `http://usaturn.net/sample/01/` | DNS 解決失敗 | 過去の参照を維持 |
| `http://usaturn.net/sample/02/` | DNS 解決失敗 | 過去の参照を維持 |
| `http://sphinx-users.jp/gettingstarted/install_windows_standalone.html` | 403（アクセス拒否） | 過去の参照を維持 |
| `http://sphinx-users.jp/doc10/markup/toctree.html` | 403（アクセス拒否） | 過去の参照を維持 |
| `http://www.jus.or.jp/~hatano/` | 404 | 過去の参照を維持 |
| `https://wiki.resonite.com/Headless_Client` | 検査環境から接続不可 | 過去の参照を維持 |

`usaturn.net/sample/01/` と `sample/02/` の元データは旧リポジトリに含まれていないため復元していない。

## 公開手順

PR を手動でマージすると本番デプロイされる。自動マージは設定しない。
本番公開後に `/`、`/blog`、`/blog/author/usaturn`、表中の主要記事、画像、ZIP ダウンロード、`/blog/atom.xml` を再確認する。
この本番確認はマージ前の検証には含まれない。
