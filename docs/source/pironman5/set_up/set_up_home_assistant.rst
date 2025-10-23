.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと一緒に、Raspberry Pi、Arduino、ESP32についてさらに深く掘り下げていきましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームのサポートを受け、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品発表や先行情報に早期アクセスできます。
    - **特別割引**: 最新製品の特別割引を楽しめます。
    - **フェスティブプロモーションとプレゼント企画**: プレゼント企画や季節ごとのプロモーションに参加できます。

    👉 探索と創造の準備ができましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _set_up_batocera:

Home Assistantでのセットアップ
==============================================

Home Assistantシステムをインストールした場合、必要なアドオンを追加して起動し、Pironman 5を稼働させる必要があります。

.. note::

    次の方法は、Home Assistantがネイティブにインストールされているシステムにのみ適用されます。Home AssistantがRaspberry Pi上にインストールされているシステムや、Home AssistantのDockerバージョンには適用されません。

1. Home Assistantにログイン
-------------------------------

* Pironman 5の起動後、直接イーサネットケーブルを接続することをお勧めします。これにより、コンピュータのブラウザを開き、 ``homeassistant.local:8123`` と入力してHome Assistantにアクセスできます。

  .. image:: img/home_login.png
   :width: 90%


* **CREATE MY SMART HOME** を選択し、アカウントを作成します。

  .. image:: img/home_account.png
   :width: 90%

* 指示に従って、場所やその他の設定を選択します。完了すると、Home Assistantのダッシュボードに移動します。

  .. image:: img/home_dashboard.png
   :width: 90%


2. SunFounderアドオンリポジトリを追加
----------------------------------------------------

Pironman 5の機能は、Home Assistantにアドオンの形でインストールされます。まず、 **SunFounder** アドオンリポジトリを追加する必要があります。

#. **設定** -> **アドオン** を開きます。

   .. image:: img/home_setting_addon.png
      :width: 90%

#. 右下のプラス記号をクリックしてアドオンストアに入ります。

   .. image:: img/home_addon.png
      :width: 90%

#. アドオンストア内で、右上のメニューをクリックし、 **リポジトリ** を選択します。

   .. image:: img/home_add_res.png
      :width: 90%

#. **SunFounder**アドオンリポジトリのURL ``https://github.com/sunfounder/home-assistant-addon`` を入力し、 **ADD** をクリックします。

   .. image:: img/home_res_add.png
      :width: 90%

#. 追加に成功したら、ポップアップウィンドウを閉じ、ページをリフレッシュします。SunFounderアドオンリストを見つけます。

   .. image:: img/home_addon_list.png
         :width: 90%

3. **Pi Config Wizard** アドオンのインストール
------------------------------------------------------

**Pi Config Wizard** は、Pironman 5に必要な設定（I2CやSPIなど）を有効にするのに役立ちます。必要ない場合は、後で削除できます。

#. SunFounderアドオンリストで **Pi Config Wizard** を見つけ、クリックして開きます。

   .. image:: img/home_pi_config.png
      :width: 90%

#. **Pi Config Wizard** ページで **INSTALL** をクリックします。インストールが完了するまで待ちます。

   .. image:: img/home_config_install.png
      :width: 90%

#. インストールが完了したら、 **ログ** ページに切り替えてエラーがないか確認します。

   .. image:: img/home_log.png
      :width: 90%

#. エラーがなければ、 **情報** ページに戻り、 **START** をクリックしてこのアドオンを開始します。

   .. image:: img/home_start.png
      :width: 90%

#. WEB UIを開きます。

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. Web UIでは、ブートパーティションをマウントするオプションが表示されます。 **MOUNT** をクリックしてパーティションをマウントします。

   .. image:: img/home_mount_boot.png
      :width: 90%

#. マウントに成功すると、I2CとSPIの設定やconfig.txtファイルの編集オプションが表示されます。I2CとSPIを有効にし、表示が「有効」となったら、下部の再起動ボタンをクリックしてRaspberry Piを再起動します。

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. 再起動後、ページをリフレッシュします。再びブートパーティションのマウントページに戻ります。再度 **MOUNT** をクリックします。

   .. image:: img/home_mount_boot.png
      :width: 90%

#. 通常、SPIは有効になりますが、I2Cは有効になりません。I2Cは再起動が2回必要です。再度I2Cを有効にしてから、Raspberry Piを再起動します。

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. 再起動後、再び **MOUNT** ページに戻ります。I2CとSPIの両方が有効になっていることが確認できます。

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * ページをリフレッシュしてもマウントパーティションページに戻らない場合は、 **設定**  -> **アドオン** -> **Pi Config Wizard** を再度クリックします。
    * このアドオンが起動しているか確認します。起動していない場合は、 **START** をクリックします。
    * 起動したら、 **OPEN WEB UI** をクリックし、 **MOUNT** をクリックしてI2CとSPIが有効か確認します。

4. **Pironman 5** アドオンのインストール
---------------------------------------------

次に、正式に **Pironman 5** アドオンをインストールします。

#. **設定** -> **アドオン** を開きます。

   .. image:: img/home_setting_addon.png
      :width: 90%

#. 右下のプラス記号をクリックしてアドオンストアに入ります。

   .. image:: img/home_addon.png
      :width: 90%

#. **SunFounder**アドオンリストで **Pironman 5** を見つけ、クリックして開きます。

   .. image:: img/home_pironman5_addon.png
      :width: 90%

#. **Pironman 5** アドオンをインストールします。

   .. image:: img/home_install_pironman5.png
      :width: 90%

#. インストールが完了したら、 **START** をクリックしてこのアドオンを起動します。Raspberry PiのCPUや温度などの関連情報がOLED画面に表示され、4つのWS2812 RGB LEDが青い呼吸モードで点灯します。

   .. image:: img/home_start_pironman5.png
      :width: 90%

#. **OPEN WEB UI** をクリックしてPironman 5のウェブページを開きます。また、Web UIをサイドバーに表示するオプションをチェックすることもできます。これにより、Home Assistantの左サイドバーにPironman 5のオプションが表示され、クリックしてPironman 5のページを開くことができます。

   .. image:: img/home_web_ui.png
      :width: 90%

#. これで、Raspberry Piの情報を確認したり、RGBの設定やファンの制御などが行えます。

   .. image:: img/home_web_new.png
      :width: 90%

.. note::

   この時点で、Pironman 5 のセットアップが正常に完了し、使用可能な状態になっています。
   
   各コンポーネントを高度に制御する方法については、:ref:`control_commands_dashboard_5` を参照してください。
