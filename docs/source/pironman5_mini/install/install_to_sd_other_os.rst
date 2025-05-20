.. note::

    こんにちは！SunFounder Raspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！Raspberry Pi、Arduino、ESP32の世界を、同じ情熱を持つ仲間たちとともに深く探求しましょう。

    **Why Join?**

    - **Expert Support**：購入後の課題や技術的トラブルを、コミュニティおよびサポートチームがサポートします。
    - **Learn & Share**：ヒントやチュートリアルを共有し、スキルを高めましょう。
    - **Exclusive Previews**：新製品の発表や先行情報をいち早くチェックできます。
    - **Special Discounts**：最新製品を対象とした限定割引をご提供します。
    - **Festive Promotions and Giveaways**：季節限定のキャンペーンやプレゼント企画に参加しましょう。

    👉 私たちと一緒にものづくりを楽しみませんか？[|link_sf_facebook|] をクリックして今すぐ参加！

.. _install_to_sd_home_bridge_mini:

Micro SDカードへのOSインストール
=============================================

Micro SDカードをご利用の場合は、以下の手順に従ってシステムをカードにインストールしてください。

**必要な機材**

* パーソナルコンピューター
* Micro SDカードおよびカードリーダー

**手順**

#. カードリーダーを使って、SDカードをパソコンまたはノートPCに挿入します。

#. |link_rpi_imager| を開き、 **Raspberry Pi Device** をクリックして、ドロップダウンメニューから **Raspberry Pi 5** を選択します。


   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. **Operating System** タブをクリックします。

   .. image:: img/os_choose_os.png
      :width: 90%

#. ページの一番下までスクロールして、使用するオペレーティングシステムを選択します。

   .. note::

      * **Ubuntu** を使用する場合は、 **Other general-purpose OS** → **Ubuntu** をクリックし、 **Ubuntu Desktop 24.04 LTS (64 bit)** または **Ubuntu Server 24.04 LTS (64 bit)** を選択してください。
      * **Kali Linux**、 **Home Assistant**、 **Homebridge** を使用する場合は、 **Other specific-purpose OS** をクリックし、該当のシステムを選択してください。

   .. image:: img/os_other_os.png
      :width: 90%

#. **Storage** オプションで、インストール先の適切なストレージデバイスを選択します。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. **NEXT** をクリックします。

   .. note::

      * 事前設定ができないシステムの場合は、 **NEXT** をクリックした後に保存内容の確認が表示されます。バックアップを済ませている場合は **Yes** を選択してください。

      * ホスト名やWi-Fi設定、SSHの有効化などを事前に設定できるシステムでは、カスタマイズ設定を適用するかどうかの確認が表示されます。 **Yes** または **No** を選択するか、戻って編集することもできます。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Raspberry Piの **ホスト名** を定義します。ホスト名はネットワーク上の識別子で、 ``<hostname>.local`` または ``<hostname>.lan`` でアクセスできます。

     .. image:: img/os_set_hostname.png  

   * 管理者アカウント用の **ユーザー名** と **パスワード** を作成します。Raspberry Piにはデフォルトのパスワードが存在しないため、セキュリティ確保のために必要です。

     .. image:: img/os_set_username.png

   * ネットワークの **SSID** と **パスワード** を入力して、無線LANを設定します。

     .. note::

       ``Wireless LAN country`` には、お住まいの地域に対応する2文字の `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ を設定してください。

     .. image:: img/os_set_wifi.png

   * Raspberry Piへリモート接続するために、 **Services** タブでSSHを有効にします。

     * **パスワード認証** を使用する場合は、Generalタブで設定したユーザー名とパスワードを使用します。
     * 公開鍵認証を使用する場合は、「Allow public-key authentication only」を選択します。RSA鍵があればそれが使われ、なければ「Run SSH-keygen」で新しい鍵ペアを生成できます。

     .. image:: img/os_enable_ssh.png

   * **Options** メニューでは、書き込み完了後に音を鳴らす、メディアを自動排出する、テレメトリを有効にするなどの動作を設定できます。

     .. image:: img/os_options.png

#. OSのカスタマイズ設定が完了したら、 **Save** をクリックして設定を保存し、次に **Yes** をクリックして書き込み時に適用します。

   .. image:: img/os_click_yes.png
      :width: 90%


#. SDカードに既存データがある場合は、データ損失を避けるため事前にバックアップを行ってください。バックアップが不要であれば **Yes** をクリックして続行します。

   .. image:: img/os_continue.png
      :width: 90%


#. 「Write Successful」と表示されたら、イメージの書き込みと検証は正常に完了しています。これでMicro SDカードからRaspberry Piを起動する準備が整いました！
