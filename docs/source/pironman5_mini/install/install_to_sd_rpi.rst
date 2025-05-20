.. note::

    こんにちは！SunFounder Raspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！Raspberry Pi、Arduino、ESP32の世界を、同じ情熱を持つ仲間たちと一緒にさらに深く探求しましょう。

    **Why Join?**

    - **Expert Support**：購入後の問題や技術的課題を、コミュニティと当社のサポートチームがサポートします。
    - **Learn & Share**：ヒントやチュートリアルを共有し、スキルを高めましょう。
    - **Exclusive Previews**：新製品の発表や先行情報を誰よりも早く入手できます。
    - **Special Discounts**：最新製品を対象にした限定割引をご提供します。
    - **Festive Promotions and Giveaways**：季節限定のキャンペーンやプレゼント企画にご参加いただけます。

    👉 私たちと一緒に創造の旅を始めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

.. _install_os_sd_rpi_mini:

Micro SDカードへのOSインストール
============================================================
.. If you are using a Micro SD card, you can follow the tutorial below to install the system onto your Micro SD card.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**必要な機材**

* パーソナルコンピューター
* Micro SDカードおよびカードリーダー

**手順**

#. カードリーダーを使用して、Micro SDカードをパソコンまたはノートパソコンに挿入します。

#. |link_rpi_imager| を起動し、 **Raspberry Pi Device** をクリックして、ドロップダウンから **Raspberry Pi 5** を選択します。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. **Operating System** を選択し、推奨されているOSバージョンを選びます。

   .. image:: img/os_choose_os.png
      :width: 90%

#. **Choose Storage** をクリックして、インストール対象のストレージデバイスを選択します。

   .. image:: img/os_choose_sd.png
      :width: 90%

#. **NEXT** をクリックし、次に **EDIT SETTINGS** をクリックして、OS設定をカスタマイズします。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Raspberry Piの **ホスト名** を設定します。これはネットワーク上での識別名となり、 ``<hostname>.local`` や ``<hostname>.lan`` でアクセス可能です。

     .. image:: img/os_set_hostname.png


   * 管理者アカウント用の **ユーザー名** と **パスワード** を設定します。初期状態ではパスワードが存在しないため、セキュリティを確保するために必ず設定してください。

     .. image:: img/os_set_username.png

   * ネットワークの **SSID** と **パスワード** を入力して、無線LANを設定します。

     .. note::

       ``Wireless LAN country`` には、お住まいの地域に対応する2文字の `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ を入力してください。

     .. image:: img/os_set_wifi.png


   * Raspberry Piへのリモート接続を有効にするには、 **Services** タブでSSHを有効にします。

     * **パスワード認証** を使用する場合は、Generalタブで設定したユーザー名とパスワードを使用します。
     * **公開鍵認証** のみを許可する場合は、「Allow public-key authentication only」を選択します。RSA鍵があればそれが使用され、ない場合は「Run SSH-keygen」で新しい鍵ペアを生成します。

     .. image:: img/os_enable_ssh.png

   * **Options** メニューでは、書き込み後の音声通知、メディアの自動排出、テレメトリの有効化など、Imagerの動作をカスタマイズできます。

     .. image:: img/os_options.png

#. OSのカスタマイズ設定が完了したら、 **Save** をクリックして保存し、 **Yes** をクリックして書き込み時に適用します。

   .. image:: img/os_click_yes.png
      :width: 90%


#. SDカードに既存のデータがある場合は、データ損失を防ぐために事前にバックアップを行ってください。バックアップが不要な場合は **Yes** をクリックして続行します。

   .. image:: img/os_continue.png
      :width: 90%


#. 「Write Successful」のポップアップが表示されたら、イメージの書き込みと検証は正常に完了しています。これでMicro SDカードからRaspberry Piを起動する準備が整いました！

   .. image:: img/os_finish.png
      :width: 90%
