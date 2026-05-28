.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


NextCloudPi の設定
=======================================

NextCloudは、Google DriveやDropboxに似たオープンソースの個人用クラウドストレージソリューションです。
ファイルの保存、ドキュメントの共有、写真の同期、カレンダーや連絡先の管理に使用できます。
公開クラウドサービスとは異なり、NextCloudはユーザーにデータの完全なコントロールを提供するため、プライバシーとデータセキュリティを重視する個人や小規模チームに理想的なソリューションです。

Raspberry Piを基盤とするPironman5シリーズは、低消費電力、コンパクトサイズ、そして信頼性の高い性能を備えており、家庭用の個人クラウドサーバーとして優れた選択肢となります。NextCloudと組み合わせることで、低コストのNASシステムとして機能します。

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

4.  Raspberry Piの起動後、ウェブブラウザを開き、あなたのRaspberry PiのアドレスでPortainerにアクセスします： ``https://<あなたのRPIのIPアドレス>:9443`` 。

5.  デフォルトでは、サイトが認証局（CA）によって発行されていない自己署名済みのSSL/TLS証明書を使用しているという警告が表示されます。ほとんどのブラウザはこのような警告を表示します。この場合、警告は安全に無視し、リスクを受け入れて進むことができます。

   .. image:: img/home_server_app/private_save.png

#.  初回ログイン時には、管理者パスワードを設定する必要があります。

   .. image:: img/home_server_app/ptn_new_admin.png

#.  管理者アカウントを登録後、Portainerのインターフェースにアクセスできます。左側のナビゲーションバーから **設定 -> 一般** をクリックし、 **アプリケーションテンプレート** を見つけて、以下のURLを入力欄に入力します： ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#.  **アプリケーション設定を保存** をクリックします。設定には約10秒かかります。

**NextCloud のインストール**

1.  左側のナビゲーションバーで、 **ホーム -> local** をクリックします。

   .. image:: img/home_server_app/ptn_home_local.png

2.  **テンプレート -> アプリケーション** に移動します。右上の検索バーに *nextcloud* と入力してクリックします。

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

3.  **スタックをデプロイ** をクリックし、デプロイが完了するまで待ちます。通常、約2分かかります。

   .. image:: img/home_server_app/ptn_temp_deploy.png

4.  完了すると、NextCloudがインストールされます。

   .. image:: img/home_server_app/ptn_temp_nextcloud_deploy_finish.png

**NextCloud の使用**

1.  ブラウザを開き、あなたのRaspberry PiのアドレスでNextCloudにアクセスします： ``https://<あなたのRPIのIPアドレス>:32768`` 。

.. note::

   同様に、サイトが認証局（CA）によって発行されていない自己署名済みのSSL/TLS証明書を使用しているという警告が表示されます。ほとんどのブラウザはこのような警告を表示します。
   この場合、警告は安全に無視し、リスクを受け入れて進むことができます。

   .. image:: img/home_server_app/private_save.png

2.  初回ログイン時には、管理者パスワードを設定する必要があります。

   .. image:: img/home_server_app/nc_admin_install.png

3.  登録後、NextCloudの使用を開始できます。

   .. image:: img/home_server_app/nc_dashboard.png