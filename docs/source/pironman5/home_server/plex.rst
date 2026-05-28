.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Plex の設定
=======================================

Plexは、あなたの映画、テレビ番組、音楽、写真を整理、ストリーミング、複数デバイスからアクセスできる強力なメディアサーバープラットフォームです。
Raspberry Piを基盤とするPironman5シリーズ上にPlexを設定することで、手頃な価格で低消費電力、24時間365日稼働の家庭用メディアセンターを作成できます。
Raspberry Piのコンパクトサイズ、低消費電力、柔軟性はPlexをホストするのに優れた選択肢であり、あなたのPiを家庭内ネットワークから、またはリモートでさえアクセス可能な個人用エンターテインメントハブへと変えます。

**準備**

*  マイクロSDカード（16GB以上、クラス10を推奨）
*  Raspberry Pi OS 公式システム（またはRaspberry Pi OS Lite）
*  安定したネットワーク接続（有線Ethernet接続を推奨）
*  外付けハードディスクドライブまたはUSBメモリ（ストレージ拡張用）

**Portainer のインストール**

ターミナルを開き、以下のコマンドを入力します：

1.  Dockerをインストールする

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2.  Portainerをインストールする

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3.  Raspberry Piを再起動します。（その後、 **直ちに** 以下の手順を実行してください。）

4.  Raspberry Piの起動後、ウェブブラウザを開き、あなたのRaspberry PiのアドレスでPortainerにアクセスします： ``http://<あなたのRPIのIPアドレス>:9443`` 。

5.  デフォルトでは、サイトが認証局（CA）によって発行されていない自己署名済みのSSL/TLS証明書を使用しているという警告が表示される場合があります。ほとんどのブラウザはこのような警告を表示します。この場合、警告は安全に無視し、リスクを受け入れて進むことができます。

   .. image:: img/home_server_app/private_save.png

#.  初回ログイン時には、管理者パスワードを設定する必要があります。

   .. image:: img/home_server_app/ptn_new_admin.png

#.  管理者アカウントを登録後、Portainerのインターフェースにアクセスできます。左側のナビゲーションバーから **設定 -> 一般** をクリックし、 **アプリケーションテンプレート** を見つけて、以下のURLを入力欄に入力します： ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#.  **アプリケーション設定を保存** をクリックします。設定には約10秒かかります。

**Plex のインストール**

1.  左側のナビゲーションバーで、 **ホーム -> local** をクリックします。

   .. image:: img/home_server_app/ptn_home_local.png

2.  **テンプレート -> アプリケーション** に移動します。右上の検索バーに *plex* と入力してクリックします。

   .. image:: img/home_server_app/ptn_temp_plex.png

#.  ネットワークモードを **host (ホスト)** に設定します。

   .. image:: img/home_server_app/ptn_plex_network_host.png

#.  **詳細オプションを表示** を展開します。

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

#.  **ボリュームマッピング** セクションで、メディアファイルのストレージパスを設定し、Plexに読み書き権限を付与します。デフォルトのパスは ``/portainer/TV`` と ``/portainer/Movies`` で、両方とも読み書きアクセスが有効になっています。

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

#.  **デプロイ** をクリックし、Plexのインストールが完了するまで待ちます。

**Plex サーバーの設定**

1.  ブラウザを開き、以下を入力します： ``http://<あなたのIPアドレス>:32400/web`` 。これでPlexのインターフェースが表示されるはずです。

   .. image:: img/home_server_app/plex_visit.png

2.  プレミアムサブスクリプションのオファーはスキップします。

3.  次に、 **サーバー設定** 画面が表示されます。 *自宅外からメディアにアクセスすることを許可する* にチェックを入れることができます。現時点では、このオプションはチェックを外したままにし、必要に応じて後で設定することを推奨します。

   .. image:: img/home_server_app/plex_server_setup1.png

4.  次に、メディアの整理を求められます。 *スキップ* を選択して後から設定でメディアを追加することもできます。ただし、Portainerのボリュームマッピングで設定したストレージパスを直接追加することを推奨します。これにより、Plexが自動的にメディアをスキャンしてインポートできます。

   .. image:: img/home_server_app/plex_server_setup2.png

5.  メディアライブラリの種類を選択し、ライブラリに名前を付け、言語を選択します。

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6.  フォルダを追加します。前に定義したメディアのストレージパスを探し、 **ライブラリを追加** をクリックします。

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7.  **完了** をクリックします。これで、Raspberry Pi上のPlexサーバーが完全に設定されました。

   .. image:: img/home_server_app/plex_server_setup3.png

8.  これで、あなたのメディアファイルがPlexサーバーのホームページに表示されるはずです。

   .. image:: img/home_server_app/plex_index.png