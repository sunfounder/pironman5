.. note:: 

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Facebookで他の愛好者とともに、Raspberry Pi、Arduino、ESP32についてさらに深く学びましょう。

    **参加する理由**

    - **専門サポート**：コミュニティやチームによるサポートで、購入後の問題や技術的課題も安心して対応できます。
    - **学びと共有**：ヒントやチュートリアルを交換して、スキルを高め合いましょう。
    - **限定プレビュー**：新製品の情報や先行プレビューをいち早く入手できます。
    - **特別割引**：最新製品を対象にした特別割引が受けられます。
    - **フェスティブプロモーションとプレゼント企画**：季節限定のイベントやプレゼント企画に参加できます。

    👉 探索と創造を始める準備はできましたか？今すぐ [|link_sf_facebook|] をクリックしてご参加ください！

.. _set_up_batocera:

Home Assistantでのセットアップ
==============================================

Home Assistantをインストールしている場合は、必要なアドオンを追加して起動することで、Pironman 5を利用可能にできます。

.. note::

    この方法は、Home Assistantをネイティブにインストールしているシステム専用です。Raspberry Pi上にインストールしたHome Assistantや、Docker版には対応していません。

1. Home Assistantへログイン
-------------------------------

* Pironman 5の起動後、イーサネットケーブルの直接接続を推奨します。これにより、PCのブラウザで ``homeassistant.local:8123`` にアクセスしてHome Assistantを開くことができます。

  .. image:: img/home_login.png
   :width: 90%


* **CREATE MY SMART HOME** を選択してアカウントを作成します。

  .. image:: img/home_account.png
   :width: 90%

* 表示される手順に従って、地域設定やその他の設定を完了させると、Home Assistantのダッシュボードが表示されます。

  .. image:: img/home_dashboard.png
   :width: 90%


2. SunFounderアドオンリポジトリの追加
----------------------------------------------------

Pironman 5の機能は、Home Assistantにアドオンとして提供されます。まずは **SunFounder** アドオンリポジトリを追加します。

#. **設定** -> **アドオン** を開きます。

   .. image:: img/home_setting_addon.png
      :width: 90%

#. 右下の「＋」アイコンをクリックしてアドオンストアにアクセスします。

   .. image:: img/home_addon.png
      :width: 90%

#. ストア右上のメニューから **リポジトリ** を選択します。

   .. image:: img/home_add_res.png
      :width: 90%

#. リポジトリURL ``https://github.com/sunfounder/home-assistant-addon`` を入力し、 **ADD** をクリックします。

   .. image:: img/home_res_add.png
      :width: 90%

#. 追加が完了したら、ポップアップを閉じ、ページを更新してSunFounderアドオン一覧を表示します。

   .. image:: img/home_addon_list.png
         :width: 90%

3. **Pi Config Wizard** アドオンのインストール
------------------------------------------------------

**Pi Config Wizard** は、Pironman 5に必要な設定（I2CやSPIなど）を有効化するためのアドオンです。使用後に削除することも可能です。

#. SunFounderアドオン一覧から **Pi Config Wizard** を選択して開きます。

   .. image:: img/home_pi_config.png
      :width: 90%

#. ページ内の **INSTALL** をクリックし、インストール完了まで待ちます。

   .. image:: img/home_config_install.png
      :width: 90%

#. インストール後、 **ログ** タブに切り替えてエラーがないか確認します。

   .. image:: img/home_log.png
      :width: 90%

#. 問題がなければ、 **情報** タブに戻り、 **START** をクリックしてアドオンを起動します。

   .. image:: img/home_start.png
      :width: 90%

#. 続いて **OPEN WEB UI** をクリックしてWeb UIを開きます。

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. ブートパーティションのマウントオプションが表示されるので、 **MOUNT** をクリックしてマウントします。

   .. image:: img/home_mount_boot.png
      :width: 90%

#. マウントに成功すると、I2C・SPIの有効化や ``config.txt`` 編集オプションが表示されます。I2CとSPIを有効にしたら、表示が「有効」になっていることを確認し、再起動ボタンでRaspberry Piを再起動します。

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. 再起動後、ページを更新してもう一度 **MOUNT** をクリックします。

   .. image:: img/home_mount_boot.png
      :width: 90%

#. 通常、SPIは一度の再起動で有効になりますが、I2Cは2回目の再起動が必要です。再度I2Cを有効にして再起動してください。

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. 再起動後に再び **MOUNT** ページを開き、I2CとSPIの両方が「有効」と表示されていることを確認します。

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * ページ更新後にマウント画面が表示されない場合は、 **設定** -> **アドオン** -> **Pi Config Wizard** を再度開いてください。
    * アドオンが起動していることを確認し、起動していなければ **START** をクリックしてください。
    * 起動後に **OPEN WEB UI** をクリックし、 **MOUNT** を選択してI2CおよびSPIの状態を確認してください。

4. **Pironman 5** アドオンのインストール
---------------------------------------------

いよいよ、 **Pironman 5** アドオンのインストールです。

#. **設定** -> **アドオン** を開きます。

   .. image:: img/home_setting_addon.png
      :width: 90%

#. 右下の「＋」をクリックしてアドオンストアに入ります。

   .. image:: img/home_addon.png
      :width: 90%

#. **SunFounder** アドオン一覧から **Pironman 5** を選択して開きます。

   .. image:: img/home_pironman5_addon.png
      :width: 90%

#. **INSTALL** をクリックしてアドオンをインストールします。

   .. image:: img/home_install_pironman5.png
      :width: 90%

#. インストール後に **START** をクリックすると、Pironman 5のサービスが起動し、OLED画面にCPUや温度などの情報が表示され、4つのWS2812 RGB LEDが青いブリージングモードで点灯します。

   .. image:: img/home_start_pironman5.png
      :width: 90%

#. **OPEN WEB UI** をクリックして、Pironman 5のWebページを開きます。Web UIをサイドバーに表示するオプションを有効にすると、左サイドバーから直接アクセスできるようになります。

   .. image:: img/home_web_ui.png
      :width: 90%

#. Web UIでは、Raspberry Piの状態確認、RGB設定、ファン制御などの各種操作が行えます。

   .. image:: img/home_web_new.png
      :width: 90%

.. note::

    Pironman 5のWebページの詳細な使い方や機能については、:ref:`view_control_dashboard` をご覧ください。
