:maatlog-post: true
:maatlog-published-at: 2012-12-10T00:00:00+09:00
:maatlog-slug: make-on-sakura
:maatlog-tags: sphinx
:maatlog-categories: it-technology
:maatlog-authors: usaturn

本家 Sphinx Advent Calendar 2012 10日目 ～サクラエディタから make html～
========================================================================

9日目の `波田野さん <http://www.jus.or.jp/~hatano/>`_ ( `@tcsh <https://twitter.com/tcsh>`_ )から受け取りました

`ドキュメント作成の歴史を紐解きながら、ドキュメントの構造化～システマティックなドキュメント作成への期待を語られていて興味深く感じました。 <http://rsh.csh.sh/misc/20121209-sphinx.html>`_

さて `本家 Sphinx Advent Calendar 2012 <http://connpass.com/event/1441/>`_ の10日目です。
全部俺版とは別に投稿したいと思います

.. _`サクラエディタ`: https://sakura-editor.github.io/

サクラエディタとマクロ
----------------------
最近では *Vim* や *Sublime Text 2* 、 *Emacs* だとかが流行っているらしいですが、Windows使ってるなら `サクラエディタ`_ でしょう

仕事柄、色々な現場に入るのですが、どこでも `サクラエディタ`_ は必ず使われています。
かくいう私も10年程 `サクラエディタ`_ を使っておりました。
:doc:`writing_tool` も参照して頂けると幸いです

この `サクラエディタ`_ 、マクロが `PPA <http://ht-deko.minim.ne.jp/ppa.html>`_ と WSHが使えます。
詳しくは `こちらへ <https://sakura-editor.github.io/help/HLP000269.html>`_


makeからブラウザ確認までを1動作で
---------------------------------
* タイトルの通りです。
  サクラエディタで編集する際に *編集* -> *make html* -> *ブラウザを起動して確認* ..... というサイクルの手間を少し省く事ができます

使い方
^^^^^^

1. :download:`これ <files/build_and_browsing.vbs>` をダウンロードし、任意のディレクトリに配置します

   例::

     C:\tools\Editor\macro\build_and_browsing.vbs

2. :guilabel:`設定` -> :guilabel:`共通設定` -> :guilabel:`マクロ` タブにて :guilabel:`マクロ一覧` にマクロを配置したディレクトリを指定します

   .. image:: /contents/2012/images/make_on_sakura01.png
      :scale: 80
      :alt: サクラエディタの共通設定のマクロタブでマクロのディレクトリを指定する画面

3. マクロの登録一覧の空欄の部分を選択します。
   初めて登録するならば *0* を選択しましょう

   .. image:: /contents/2012/images/make_on_sakura03.png
      :scale: 80
      :alt: サクラエディタのマクロの登録一覧で空欄を選択する画面

4. :guilabel:`名前` に任意の名前を付けます。
   とりあえず *make html* としておきましょう

   .. image:: /contents/2012/images/make_on_sakura04.png
      :scale: 80
      :alt: サクラエディタのマクロの名前を make html に設定する画面

5. :guilabel:`File` にてドロップダウンメニューからマクロのファイルを選択します

   .. image:: /contents/2012/images/make_on_sakura05.png
      :scale: 80
      :alt: サクラエディタの実行するマクロファイルを選択する画面

6. :guilabel:`設定` をクリックします

   .. image:: /contents/2012/images/make_on_sakura06.png
      :scale: 80
      :alt: サクラエディタのマクロを登録する設定ボタン

7. :guilabel:`マクロ一覧` の *0* に *make html* が登録された事を確認します

   .. image:: /contents/2012/images/make_on_sakura07.png
      :scale: 80
      :alt: サクラエディタのマクロ一覧に登録された make html

8. :guilabel:`キー割り当て` タブをクリックします

   .. image:: /contents/2012/images/make_on_sakura071.png
      :scale: 80
      :alt: サクラエディタの共通設定のキー割り当てタブ

9. :guilabel:`種別` を **外部マクロ** にします

   .. image:: /contents/2012/images/make_on_sakura08.png
      :scale: 80
      :alt: サクラエディタのキー割り当ての種別を外部マクロに変更する画面

10. *make html* をクリックします

   .. image:: /contents/2012/images/make_on_sakura09.png
      :scale: 80
      :alt: サクラエディタのキーを割り当てる make html マクロの選択

11. 任意のキーを割付して下さい

    例 ``Alt + B`` を設定する場合

    i. :guilabel:`Alt` にチェックを入れる

       .. image:: /contents/2012/images/make_on_sakura10.png
          :scale: 80
          :alt: サクラエディタのキー割り当てで Alt にチェックを入れる画面

    ii. キー欄をスクロールして :guilabel:`Alt+B` をクリック

       .. image:: /contents/2012/images/make_on_sakura11.png
          :scale: 80
          :alt: サクラエディタのキー一覧で Alt+B を選択する画面

    iii. :guilabel:`割付` を押下します

       .. image:: /contents/2012/images/make_on_sakura12.png
          :scale: 80
          :alt: サクラエディタのAlt+B をマクロに割り付けるボタン

    iv. :guilabel:`機能に割り当てられているキー` に **Alt+B** が、 :guilabel:`機能に割り当てられている機能` に *make html* が表示されている事を確認し :guilabel:`OK` をクリックします

       .. image:: /contents/2012/images/make_on_sakura13.png
          :scale: 80
          :alt: サクラエディタのmake html に Alt+B が割り当てられた確認画面

12. **プロジェクト** 内のreSTファイルをサクラエディタで開き、おもむろに割付したキー(例では ``Alt+B`` )を押しましょう

13. *make html* の結果がポップアップされ、編集している *reSTファイル* のhtmlがWebブラウザで開かれれば成功です

   .. image:: /contents/2012/images/make_on_sakura14.png
      :scale: 50
      :alt: サクラエディタのマクロで実行した make html の結果を表示するダイアログ

マクロの中身
------------
.. literalinclude:: files/build_and_browsing.vbs
   :language: vbnet
   :linenos:
   :encoding: sjis

さ～て、明日のSphinxアドベントカレンダーは？
--------------------------------------------
* 明日は `@grimroseさん <https://twitter.com/grimrose>`_ が `担当 <http://grimrose.blogspot.jp/>`_ です。
  手順書を作成した時の過程を書かれるそうです。
  楽しみですね！
