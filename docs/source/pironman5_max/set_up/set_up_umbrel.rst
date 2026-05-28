.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _set_up_umbrel_max:

Umbrel OSでのセットアップ
======================================================================

Raspberry Pi 5にUmbrel OSをインストールしている場合は、コマンドラインを使用してPironman 5 MAXを設定できます。以下の手順に従ってセットアップを完了してください：

#. Raspberry Pi 5をEthernetケーブルでネットワークに接続します。これはRaspberry Piがインターネットにアクセスできるようにするために必要です。

#. ブラウザを開き、次のURLにアクセスします： ``http://umbrel.local``。ページが開かない場合は、ルーターでUmbrelデバイスのIPアドレスを確認し、例： ``http://192.168.1.50`` にアクセスしてください。

   .. image:: img/umbrel_local.png

#. ユーザー名とパスワードを設定してUmbrelアカウントを作成します。このパスワードは今後リモートアクセスに必要となるため、安全に保管してください。

   .. image:: img/umbrel_account.png

#. **Next** をクリックしてUmbrelのセットアップを完了し、デスクトップ環境に入ります。

   .. image:: img/umbrel_desktop.png

#. **App Store** アイコンをクリックして開きます。

   .. image:: img/umbrel_app_store.png

#. Umbrel App Storeで、右上隅の **Community App Store** ボタンをクリックします。

   .. image:: img/umbrel_community_app.png

#. カスタムリポジトリURLを入力します： ``https://github.com/sunfounder/umbrel-community-app-store/``

   .. image:: img/umbrel_url.png

#. リポジトリを追加したら、 **Open** をクリックして **SunFounder Store** にアクセスします。

   .. image:: img/umbrel_open.png

#. **SunFounder App Store** には2つのアプリが表示されます。 **Pironman 5** または **Pironman 5 Max** のいずれかを選択します。

   .. image:: img/umbrel_sf_app.png

#. **Install** をクリックしてインストールを開始します。

   .. image:: img/umbrel_app_install.png

#. インストールが完了したら、 **Open** をクリックしてダッシュボードを起動します。

   .. image:: img/umbrel_dashboard.png
