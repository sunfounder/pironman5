.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32愛好者向けFacebookコミュニティへようこそ！
    このコミュニティでは、Raspberry Pi、Arduino、ESP32についてさらに深く学び、同じ趣味を持つ仲間たちと交流できます。

    **Why Join?**

    - **Expert Support**: 購入後の問題や技術的なトラブルを、コミュニティメンバーやサポートチームが解決します。
    - **Learn & Share**: ノウハウやチュートリアルを共有しながらスキルアップしましょう。
    - **Exclusive Previews**: 新製品のアナウンスや先行情報をいち早く入手できます。
    - **Special Discounts**: 最新商品を特別価格でご購入いただけます。
    - **Festive Promotions and Giveaways**: 季節ごとのプロモーションやプレゼント企画にご参加いただけます。

    👉 一緒に楽しみながら創造しましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

.. _max_install_os_sd_rpi:

Micro SDカードへのOSインストール
============================================================
Micro SDカードを使用している場合は、以下のチュートリアルに従ってシステムをインストールできます。

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**必要なもの**

* パーソナルコンピュータ
* Micro SDカードとカードリーダー

**手順**

#. SDカードをリーダーに挿入し、パソコンまたはノートパソコンに接続します。

#. |link_rpi_imager| を開き、 **Raspberry Pi Device** をクリックし、ドロップダウンから **Raspberry Pi 5** モデルを選択します。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. **Operating System** を選択し、推奨されるOSバージョンを選びます。

   .. image:: img/os_choose_os.png
      :width: 90%

#. **Choose Storage** をクリックし、インストール先となる適切なストレージデバイスを選択します。

   .. image:: img/os_choose_sd.png
      :width: 90%

#. **NEXT** をクリックし、続いて **EDIT SETTINGS** を選んでOS設定をカスタマイズします。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * **hostname** を設定します。これはRaspberry Piのネットワーク上での識別名で、 ``<hostname>.local`` や ``<hostname>.lan`` でアクセスできます。

     .. image:: img/os_set_hostname.png


   * 管理者用の **Username** と **Password** を設定します。初期パスワードが存在しないため、安全性を高めるために固有のアカウント情報を作成してください。

     .. image:: img/os_set_username.png

   * 無線LAN（Wi-Fi）を設定するには、ネットワークの **SSID** と **Password** を入力します。

     .. note::

       ``Wireless LAN country`` には、お住まいの国に対応する2文字の `ISO/IEC alpha2コード <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ を入力してください。

     .. image:: img/os_set_wifi.png


   * Raspberry Piにリモート接続するために、 **Services** タブでSSHを有効にします。

     * **パスワード認証** を使用する場合は、Generalタブで設定したユーザー名とパスワードを利用します。
     * **公開鍵認証** を使用する場合は、「Allow public-key authentication only」を選びます。RSAキーがある場合はそれが使用され、ない場合は「Run SSH-keygen」をクリックして新しいキーを生成してください。

     .. image:: img/os_enable_ssh.png

   * **Options** メニューでは、書き込み完了時の音声再生やメディアの取り出し、テレメトリの有効化などの動作を設定できます。

     .. image:: img/os_options.png

#. OSのカスタマイズ設定を入力し終えたら、 **Save** をクリックして保存し、続いて **Yes** をクリックして書き込み時に設定を適用します。

   .. image:: img/os_click_yes.png
      :width: 90%


#. SDカードに既存のデータがある場合は、データを失わないように事前にバックアップを取ってください。問題なければ **Yes** をクリックして続行します。

   .. image:: img/os_continue.png
      :width: 90%


#. 「Write Successful」と表示されたら、OSの書き込みと検証が完了です。これで、Raspberry PiをMicro SDカードから起動する準備が整いました！

   .. image:: img/os_finish.png
      :width: 90%
