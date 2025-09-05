.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと一緒に、Raspberry Pi、Arduino、ESP32についてさらに深く掘り下げていきましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームのサポートを受け、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品発表や先行情報に早期アクセスできます。
    - **特別割引**: 最新製品の特別割引を楽しめます。
    - **フェスティブプロモーションとプレゼント企画**: プレゼント企画や季節ごとのプロモーションに参加できます。

    👉 探索と創造の準備ができましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！


Plex の設定
=======================================

Plex は強力な家庭用の映像音声配信サーバーであり、映画、連続ドラマ、音楽、写真を整理し、配信し、複数の端末から利用できるようにします。  
Raspberry Pi を搭載した Pironman5 シリーズに Plex を導入することで、安価で省電力な家庭用映像音声センターを 24 時間体制で構築できます。  
Raspberry Pi の小型さ、低消費電力、柔軟性は Plex を運用するのに最適であり、自宅内の通信網や外部からでも利用できる個人用の娯楽拠点に変えることができます。


**準備**

* MicroSD カード（16GB 以上、Class 10 推奨）  
* 正規の Raspberry Pi OS（または Raspberry Pi OS Lite）  
* 安定した通信網（有線接続推奨）  
* 外付け記憶装置または USB 記憶装置（追加の保存領域用）  


**Portainer を導入**

端末を開き、次の命令を入力します：

1. Docker を導入

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Portainer を導入

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. 通信閲覧ソフトを開き、Portainer の所在に移動します: ``http://<your-rpi-ip-address>:9443`` .

.. note::

   標準では、この所在は自署名の証明書を用いているため、認証局によって発行されていないという注意が表示されます。  
   多くの通信閲覧ソフトはこのような証明について警告を示します。  
   この場合、注意を無視し、危険を承知で進んでも問題はありません。

   .. image:: img/home_server_app/private_save.png


4. 最初の利用時に管理者の暗証を設定する必要があります。

   .. image:: img/home_server_app/ptn_new_admin.png

5. 管理者の登録後、Portainer の画面に入ります。左側の案内欄から **Setting -> General** を押し、 **App Templates** を探して、次の所在を入力します:  
   ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

6. **Save Application Settings** を押します。設定が完了するまでにおよそ十秒かかります。


**Plex を導入**

1. 左の案内欄から **Home -> local -> Templates -> Application** を押します。右上の探索欄に *plex* と入力し、それを選びます。

   .. image:: img/home_server_app/ptn_temp_plex.png

2. 通信網の様式を **host** に設定します。

   .. image:: img/home_server_app/ptn_plex_network_host.png

3. **Show advanced options** を展開します。

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

4. **volume mapping** の区画で、映像音声資料の所在を設定し、Plex に読込／書込の許可を与えます。  
   標準の所在は ``/portainer/TV`` と ``/portainer/Movies`` であり、両方に読込／書込の権限が与えられています。

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

5. **Deploy** を押し、Plex の導入が終わるのを待ちます。


**Plex サーバーの設定**

1. 通信閲覧ソフトを開き、所在を入力します: ``http://<your_ip>:32400/`` 。ここで Plex の画面が表示されるはずです。

   .. image:: img/home_server_app/plex_visit.png

2. 有料契約の案内は飛ばします。

3. 次に **Server Setup** の画面が表示されます。*Allow me to access my media outside my home* を選ぶことができます。  
   ただし、今のところは外しておき、必要に応じて後で設定するのが勧められます。

   .. image:: img/home_server_app/plex_server_setup1.png

4. その後、映像音声を整理するよう求められます。*Skip* を選んで後で設定から追加してもよいですが、Portainer の volume mapping で設定した所在を直接追加し、Plex が自動で読み込みできるようにすることが勧められます。

   .. image:: img/home_server_app/plex_server_setup2.png

5. 映像音声の種類を選び、名をつけ、言語を選びます。

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6. 資料の所在を追加します。先に設定した所在を選び、 **Add Library** を押します。

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7. **Finish** を押します。これで Raspberry Pi 上の Plex サーバーが完全に設定されました。

   .. image:: img/home_server_app/plex_server_setup3.png

8. Plex サーバーの最初の画面に、あなたの映像音声資料が表示されるはずです。

   .. image:: img/home_server_app/plex_index.png
