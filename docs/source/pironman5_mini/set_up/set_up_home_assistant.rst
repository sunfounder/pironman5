.. note::

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32について、同じ興味を持つ仲間たちと一緒に深く探究しましょう。

    **Why Join?**

    - **Expert Support**：購入後の問題や技術的な課題を、コミュニティやSunFounderチームと一緒に解決できます。
    - **Learn & Share**：ヒントやチュートリアルを共有し合い、スキルを高めましょう。
    - **Exclusive Previews**：新製品情報をいち早く入手できます。
    - **Special Discounts**：最新製品を対象とした特別割引が受けられます。
    - **Festive Promotions and Giveaways**：季節イベントやプレゼントキャンペーンにも参加可能！

    👉 一緒に創造と探究の旅に出かけましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

Seting Up on Home Assistant
============================================

Home Assistantシステムをインストール済みの場合、必要なアドオンを追加して起動することで、Pironman 5 Miniを使用可能にします。

.. note::

    以下の方法は、Home Assistantをネイティブにインストールしたシステムにのみ適用されます。Raspberry Pi上で後からHome Assistantをインストールした場合や、Docker版のHome Assistantには対応していません。

1. Home Assistant にログインする
----------------------------------------

* Pironman 5 Miniを起動後、イーサネットケーブルを直接接続することを推奨します。この方法で、PCのブラウザから ``homeassistant.local:8123`` にアクセスできます。

  .. image:: img/home_login.png
   :width: 90%


* **CREATE MY SMART HOME** を選択し、アカウントを作成します。

  .. image:: img/home_account.png
   :width: 90%

* 指示に従って地域やその他の設定を行うと、Home Assistantのダッシュボードにアクセスできます。

  .. image:: img/home_dashboard.png
   :width: 90%


2. SunFounderアドオンリポジトリを追加する
----------------------------------------------------

Pironman 5 Miniの機能は、Home Assistant上でアドオンとして提供されています。まずは **SunFounder** のアドオンリポジトリを追加しましょう。

#. **設定** -> **アドオン** を開きます。

   .. image:: img/home_setting_addon.png
      :width: 90%

#. 右下の「＋」アイコンをクリックして、アドオンストアに入ります。

   .. image:: img/home_addon.png
      :width: 90%

#. アドオンストアの右上メニューから **Repositories** を選択。

   .. image:: img/home_add_res.png
      :width: 90%

#. 以下のSunFounderアドオンリポジトリURLを入力し、 **ADD** をクリックします： ``https://github.com/sunfounder/home-assistant-addon``

   .. image:: img/home_res_add.png
      :width: 90%

#. 正常に追加できたら、ポップアップを閉じてページを更新し、SunFounderアドオン一覧を確認します。

   .. image:: img/home_addon_list.png
         :width: 90%

3. **Pi Config Wizard** アドオンをインストールする
------------------------------------------------------

**Pi Config Wizard** は、I2CやSPIなど、Pironman 5 Miniに必要な設定を有効化するためのアドオンです。設定完了後は削除しても構いません。

#. SunFounderアドオン一覧から **Pi Config Wizard** を見つけてクリック。

   .. image:: img/home_pi_config.png
      :width: 90%

#. **Pi Config Wizard** ページで **INSTALL** をクリックし、インストール完了まで待ちます。

   .. image:: img/home_config_install.png
      :width: 90%

#. インストール完了後、 **ログ** ページに切り替えてエラーがないか確認します。

   .. image:: img/home_log.png
      :width: 90%

#. エラーがなければ、 **情報** ページに戻り、 **START** をクリックしてアドオンを起動します。

   .. image:: img/home_start.png
      :width: 90%

#. 次に、WEB UIを開きます。

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. Web UI上でBootパーティションのマウントオプションが表示されるので、 **MOUNT** をクリックしてマウントします。

   .. image:: img/home_mount_boot.png
      :width: 90%

#. マウントに成功すると、I2CやSPIの設定、config.txtの編集などのオプションが表示されます。I2CとSPIをチェックして有効にし、下部の再起動ボタンをクリックしてRaspberry Piを再起動します。

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. 再起動後、ページを更新して再びマウント画面に戻り、再度 **MOUNT** をクリック。

   .. image:: img/home_mount_boot.png
      :width: 90%

#. 通常、SPIは有効化されますが、I2Cは2回の再起動が必要です。もう一度I2Cを有効にして、再度再起動します。

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. 再起動後、再び **MOUNT** ページに戻ると、I2CとSPIの両方が有効化されていることが確認できます。

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * ページ更新後にマウント画面が表示されない場合は、 **設定** -> **アドオン** -> **Pi Config Wizard** を開き直してください。
    * アドオンが起動しているか確認し、起動していなければ **START** をクリックしてください。
    * 起動後、 **OPEN WEB UI** をクリックし、 **MOUNT** を押してI2CおよびSPIの状態を確認してください。



.. .. 这里要改PIRONMAN5 MINI的ADD ON 图


4. **Pironman 5 Mini** アドオンをインストールする
---------------------------------------------------

いよいよ、 **Pironman 5 Mini** アドオンのインストールを開始します。

#. **設定** -> **アドオン** を開きます。

   .. image:: img/home_setting_addon.png
      :width: 90%

#. 右下の「＋」をクリックしてアドオンストアに入ります。

   .. image:: img/home_addon.png
      :width: 90%

#. **SunFounder** アドオン一覧から **Pironman 5 Mini** を見つけてクリック。

   .. image:: img/home_pironman5_addon.png
      :width: 90%

#. Pironman 5アドオンをインストールします。

   .. image:: img/home_install_pironman5.png
      :width: 90%

#. インストール完了後、 **START** をクリックして起動します。4つのWS2812 RGB LEDが青色でブリージングモードになります。

   .. image:: img/home_start_pironman5.png
      :width: 90%

#. 次に **OPEN WEB UI** をクリックして、Pironman 5 MiniのWebページを開きます。サイドバー表示のオプションにもチェックを入れると、Home Assistantの左サイドバーにPironman 5 Miniの項目が表示され、すぐにアクセス可能になります。

   .. image:: img/home_web_ui.png
      :width: 90%

#. Web UIでは、Raspberry Piの情報を確認したり、RGBの設定やファンの制御などが可能です。

   .. image:: img/home_web.png
      :width: 90%

.. note::

    Pironman 5 MiniのWebページに関する詳細な使用方法については、:ref:`view_control_dashboard_mini` を参照してください。
