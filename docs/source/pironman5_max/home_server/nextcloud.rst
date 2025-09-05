.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと一緒に、Raspberry Pi、Arduino、ESP32についてさらに深く掘り下げていきましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームのサポートを受け、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品発表や先行情報に早期アクセスできます。
    - **特別割引**: 最新製品の特別割引を楽しめます。
    - **フェスティブプロモーションとプレゼント企画**: プレゼント企画や季節ごとのプロモーションに参加できます。

    👉 探索と創造の準備ができましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！


NextCloudPi の設定
=======================================

NextCloud は、Google Drive や Dropbox に似たオープンソースのプライベートクラウドストレージソリューションです。  
ファイルの保存、ドキュメントの共有、写真の同期、カレンダーや連絡先の管理に利用できます。  
パブリッククラウドサービスとは異なり、NextCloud はユーザーにデータの完全なコントロールを提供するため、プライバシーやデータセキュリティを重視する個人や小規模チームに最適です。

Raspberry Pi 搭載の Pironman5 シリーズは、低消費電力、コンパクトなサイズ、信頼性の高いパフォーマンスを提供し、家庭用プライベートクラウドサーバーとして最適な選択肢です。NextCloud と組み合わせることで、コスト効率の高い NAS システムとして利用できます。


**準備**

* MicroSD カード (16GB 以上、Class 10 推奨)  
* Raspberry Pi 公式システム Raspberry Pi OS (または Raspberry Pi OS Lite)  
* 安定したネットワーク接続 (有線 Ethernet 推奨)  
* 外付けハードドライブまたは USB メモリ (拡張ストレージ用)  


**Portainer のインストール**

ターミナルを開き、次のコマンドを入力します：

1. Docker のインストール

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Portainer のインストール

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. ブラウザを開き、Portainer のアドレスにアクセスします: ``http://<your-rpi-ip-address>:9443`` .

.. note::

   デフォルトでは、サイトが自己署名 SSL/TLS 証明書を使用しているため、認証局 (CA) によって発行されていないという警告が表示されます。  
   ほとんどのブラウザはこのような証明書について警告を表示します。  
   この場合、警告を無視してリスクを受け入れ、続行して問題ありません。

   .. image:: img/home_server_app/private_save.png


4. 初回ログイン時に管理者パスワードを設定する必要があります。

   .. image:: img/home_server_app/ptn_new_admin.png

5. 管理者アカウントを登録すると、Portainer のインターフェイスに入ります。左側のナビゲーションバーから **Setting -> General** をクリックし、 **App Templates** を探して、次の URL を入力します: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

6. **Save Application Settings** をクリックします。設定の完了には約 10 秒かかります。


**NextCloud のインストール**

1. 左側のナビゲーションバーから **Home -> local -> Templates -> Application** をクリックします。右上の検索バーに *nextcloud* と入力し、クリックします。

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

2. **Deploy the stack** をクリックし、デプロイが完了するまで待ちます。通常は約 2 分かかります。

   .. image:: img/home_server_app/ptn_temp_deploy.png

完了すると、NextCloud がインストールされます。


**NextCloud の使用**

1. ブラウザを開き、NextCloud のアドレスにアクセスします: ``http://<your-rpi-ip-address>:32768`` .

.. note::

   同様に、サイトが自己署名 SSL/TLS 証明書を使用しているため、認証局 (CA) によって発行されていないという警告が表示されます。  
   ほとんどのブラウザはこのような証明書について警告を表示します。  
   この場合、警告を無視してリスクを受け入れ、続行して問題ありません。

   .. image:: img/home_server_app/private_save.png

2. 初回ログイン時に管理者パスワードを設定する必要があります。

   .. image:: img/home_server_app/nc_admin_install.png

3. 登録後、NextCloud を使用開始できます。

   .. image:: img/home_server_app/nc_dashboard.png
