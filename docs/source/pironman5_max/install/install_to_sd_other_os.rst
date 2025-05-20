.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32愛好者向けFacebookコミュニティへようこそ！
    このコミュニティでは、Raspberry Pi、Arduino、ESP32についてさらに深く学び、同じ興味を持つ仲間と交流できます。

    **Why Join?**

    - **Expert Support**: ご購入後の問題や技術的なトラブルに対し、コミュニティメンバーやスタッフがサポートします。
    - **Learn & Share**: ノウハウやチュートリアルを共有し、スキルを向上させましょう。
    - **Exclusive Previews**: 新製品情報を先行して入手できます。
    - **Special Discounts**: 会員限定の割引価格で最新商品を購入できます。
    - **Festive Promotions and Giveaways**: プレゼント企画や季節限定のキャンペーンに参加できます。

    👉 一緒に学び、創造する準備はできましたか？[|link_sf_facebook|] をクリックして今すぐ参加！

.. _max_install_to_sd_home_bridge:

Micro SDカードへのOSインストール
=============================================

Micro SDカードを使用する場合は、以下の手順に従ってシステムをインストールしてください。


**必要なもの**

* パーソナルコンピュータ
* Micro SDカードとカードリーダー

**手順**

#. SDカードをカードリーダーに挿入し、パソコンまたはノートPCに接続します。

#. |link_rpi_imager| を起動し、 **Raspberry Pi Device** をクリックして **Raspberry Pi 5** を選択します。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. **Operating System** タブをクリックします。

   .. image:: img/os_choose_os.png
      :width: 90%

#. ページ最下部までスクロールして、お使いのオペレーティングシステムを選択します。

   .. note::

      * **Ubuntu** を使用する場合は、 **Other general-purpose OS** → **Ubuntu** をクリックし、 **Ubuntu Desktop 24.04 LTS（64bit）** または **Ubuntu Server 24.04 LTS（64bit）** を選択します。
      * **Kali Linux**、 **Home Assistant**、 **Homebridge** の場合は、 **Other specific-purpose OS** をクリックし、それぞれのシステムを選択します。

   .. image:: img/os_other_os.png
      :width: 90%

#. **Storage** オプションで、インストール先のストレージデバイスを選択します。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. **NEXT** をクリックします。

   .. note::

      * 事前設定できないシステムでは、 **NEXT** の後にストレージ内データの保存確認が表示されます。バックアップを確認済みであれば **Yes** を選択してください。

      * ホスト名、WiFi、SSHの有効化など事前設定可能なシステムでは、カスタム設定の適用を尋ねるポップアップが表示されます。 **Yes** または **No** を選ぶか、戻って編集できます。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * **hostname** （ホスト名）を定義します。これはRaspberry Piのネットワーク識別名です。 ``<hostname>.local`` や ``<hostname>.lan`` でアクセスできます。

     .. image:: img/os_set_hostname.png

   * 管理者アカウント用の **Username**（ユーザー名）と **Password** （パスワード）を作成します。Raspberry Piには初期パスワードが存在しないため、セキュリティのために必須です。

     .. image:: img/os_set_username.png

   * ワイヤレスLANの **SSID** と **Password** を入力して設定します。

     .. note::

       ``Wireless LAN country`` には、ご自身の国に対応する2文字の `ISO/IEC alpha2コード <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ を設定してください。

     .. image:: img/os_set_wifi.png

   * Raspberry Piへリモート接続するために、 **Services** タブでSSHを有効化します。

     * **パスワード認証** を使用する場合は、 **General** タブで設定したユーザー名とパスワードを使用してください。
     * **公開鍵認証** を使用する場合は、「Allow public-key authentication only」を選択します。RSAキーが存在する場合はそれが使用され、ない場合は「Run SSH-keygen」でキーを生成できます。

     .. image:: img/os_enable_ssh.png

   * **Options** メニューでは、書き込み時の動作（終了時の音、メディアの取り出し、テレメトリの有効化など）を設定できます。

     .. image:: img/os_options.png

#. カスタマイズ設定の入力が完了したら、 **Save** をクリックして保存し、次に **Yes** をクリックして書き込みに設定を適用します。

   .. image:: img/os_click_yes.png
      :width: 90%


#. SDカードに既存のデータがある場合は、データ損失を避けるためにバックアップを取ってください。バックアップが不要な場合は **Yes** をクリックして続行します。

   .. image:: img/os_continue.png
      :width: 90%


#. 「Write Successful」というポップアップが表示されたら、OSの書き込みと検証が完了です。これで、Raspberry PiをMicro SDカードから起動する準備が整いました！
