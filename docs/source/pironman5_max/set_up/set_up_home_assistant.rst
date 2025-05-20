.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32愛好者向けFacebookコミュニティへようこそ！同じ興味を持つ仲間たちと一緒に、Raspberry Pi・Arduino・ESP32の世界をさらに深く探究しましょう。

    **Why Join?**

    - **Expert Support**：購入後のトラブルや技術的な課題を、コミュニティやサポートチームと一緒に解決。
    - **Learn & Share**：ヒントやチュートリアルを共有し、スキルをさらに磨きましょう。
    - **Exclusive Previews**：新製品情報や先行公開をいち早くチェック。
    - **Special Discounts**：最新製品を対象とした限定割引をお楽しみください。
    - **Festive Promotions and Giveaways**：季節のキャンペーンやプレゼント企画に参加できます。

    👉 一緒に探究と創造の旅を始めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

Home Assistant のセットアップ
============================================

Home Assistant をインストール済みの場合、Pironman 5 を動作させるには、必要なアドオンを追加して起動する必要があります。

.. note::

    以下の手順は、Home Assistant をネイティブにインストールしているシステムのみが対象です。Raspberry Pi 上で後から Home Assistant を導入した環境や Docker 版の Home Assistant には適用されません。

1. Home Assistant にログイン
------------------------------

* Pironman 5 を起動後、Ethernet ケーブルを直接接続することを推奨します。PC のブラウザで ``homeassistant.local:8123`` にアクセスすると、Home Assistant の画面が開きます。

  .. image:: img/home_login.png
   :width: 90%


* **CREATE MY SMART HOME** を選択し、アカウントを作成します。

  .. image:: img/home_account.png
   :width: 90%

* 表示される案内に従い、位置情報や各種設定を行います。完了すると、Home Assistant のダッシュボードに入ります。

  .. image:: img/home_dashboard.png
   :width: 90%


2. SunFounder アドオンリポジトリの追加
----------------------------------------------------

Pironman 5 の機能は、Home Assistant のアドオンとして提供されます。まずは **SunFounder** のアドオンリポジトリを追加します。

#. **設定** → **アドオン** を開きます。

   .. image:: img/home_setting_addon.png
      :width: 90%

#. 右下の「＋」をクリックしてアドオンストアに入ります。

   .. image:: img/home_addon.png
      :width: 90%

#. アドオンストアの右上メニューから **リポジトリ** を選択します。

   .. image:: img/home_add_res.png
      :width: 90%

#. リポジトリURLとして ``https://github.com/sunfounder/home-assistant-addon`` を入力し、 **ADD** をクリックします。

   .. image:: img/home_res_add.png
      :width: 90%

#. 追加が成功したら、ポップアップを閉じてページを更新します。SunFounder のアドオンリストが表示されます。

   .. image:: img/home_addon_list.png
         :width: 90%

3. **Pi Config Wizard** アドオンのインストール
------------------------------------------------------

**Pi Config Wizard** は、Pironman 5 に必要な I2C や SPI の設定を有効化するためのアドオンです。設定後は削除しても構いません。

#. SunFounder のアドオンリストから **Pi Config Wizard** を見つけ、クリックして開きます。

   .. image:: img/home_pi_config.png
      :width: 90%

#. **Pi Config Wizard** ページで **INSTALL** をクリックし、インストールが完了するのを待ちます。

   .. image:: img/home_config_install.png
      :width: 90%

#. インストール完了後、 **Log** ページでエラーがないか確認します。

   .. image:: img/home_log.png
      :width: 90%

#. 問題がなければ **Info** ページに戻り、 **START** をクリックしてアドオンを起動します。

   .. image:: img/home_start.png
      :width: 90%

#. WEB UI を開きます。

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. Web UI 内で「Bootパーティションをマウント」するオプションが表示されるので、 **MOUNT** をクリックします。

   .. image:: img/home_mount_boot.png
      :width: 90%

#. マウントが成功すると、I2C と SPI の有効化や config.txt の編集オプションが表示されます。I2C と SPI にチェックを入れて有効にし、表示が「Enabled」になったら、画面下部の再起動ボタンをクリックして Raspberry Pi を再起動します。

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. 再起動後、ページを更新すると再びマウント画面になります。再度 **MOUNT** をクリックします。

   .. image:: img/home_mount_boot.png
      :width: 90%

#. SPI は有効になっていても、I2C はもう一度再起動が必要な場合があります。再度 I2C を有効にして再起動してください。

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. 最後の再起動後、 **MOUNT** ページに戻ると I2C と SPI の両方が有効になっていることが確認できます。

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * ページを更新してもマウント画面に戻らない場合は、 **設定** → **Settings** → **Pi Config Wizard** を再度開いてください。
    * アドオンが起動していない場合は **START** をクリック。
    * 起動後に **OPEN WEB UI** をクリックし、 **MOUNT** を実行して I2C および SPI の状態を確認してください。

4. **Pironman 5** アドオンのインストール
---------------------------------------------

いよいよ **Pironman 5** アドオンをインストールします。

#. **Settings** -> **Add-ons** を開きます。

   .. image:: img/home_setting_addon.png
      :width: 90%

#. 右下の「＋」をクリックしてアドオンストアに入ります。

   .. image:: img/home_addon.png
      :width: 90%

#. **SunFounder** アドオンリストから **Pironman 5** を探してクリックします。

   .. image:: img/home_pironman5_addon.png
      :width: 90%

#. **Pironman 5** アドオンをインストールします。

   .. image:: img/home_install_pironman5.png
      :width: 90%

#. インストール完了後、 **START** をクリックしてアドオンを起動します。OLEDディスプレイにRaspberry PiのCPU温度やその他情報が表示され、4つのWS2812 RGB LEDが青色で呼吸モードになります。

   .. image:: img/home_start_pironman5.png
      :width: 90%

#. 次に **OPEN WEB UI** をクリックして Pironman 5 の Web ページを開きます。Web UI をサイドバーに表示するオプションを有効にすると、Home Assistant の左サイドバーからも Pironman 5 ページにアクセスできます。

   .. image:: img/home_web_ui.png
      :width: 90%

#. ここでは Raspberry Pi の各種情報を確認したり、RGB の設定やファンの制御などが行えます。

   .. image:: img/home_web.png
      :width: 90%

.. note::

    Pironman 5 Web ページのより詳しい使い方については、:ref:`max_view_control_dashboard` を参照してください。
