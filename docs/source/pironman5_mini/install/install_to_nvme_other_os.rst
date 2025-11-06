.. note::

    こんにちは！SunFounder Raspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！Raspberry Pi、Arduino、ESP32の世界を、同じ情熱を持つ仲間たちと共に深く探求しましょう。

    **なぜ参加するのか？**

    - **エキスパートサポート**：購入後の課題や技術的トラブルを、コミュニティとサポートチームが支援します。
    - **学びと共有**：チュートリアルやヒントを共有してスキルアップを図りましょう。
    - **新製品の先行公開**：新製品の発表や先行情報をいち早くチェックできます。
    - **特別割引**：最新製品を対象とした特別割引を受けられます。
    - **季節イベントとプレゼント企画**：季節限定のキャンペーンやプレゼント企画にもご参加いただけます。

    👉 ものづくりの冒険に参加しませんか？[|link_sf_facebook|] をクリックして、今すぐ参加！

.. _install_to_nvme_home_bridge_mini:

NVMe SSDへのOSインストール
============================================

NVMe SSDをお使いで、PCに接続するためのアダプターをお持ちの場合は、以下の手順でOSを簡単にインストールできます。

    .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**必要な機材**

* パーソナルコンピューター
* NVMe SSD
* NVMe to USBアダプター
* Micro SDカードとカードリーダー


1. ブートローダーの更新
----------------------------------

まず、Raspberry Pi 5がUSBやSDカードよりも先にNVMeから起動できるよう、ブートローダーを更新する必要があります。

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    この段階では、予備のMicro SDカードの使用を推奨します。まずこのMicro SDカードにブートローダーを書き込み、すぐにRaspberry Piへ挿入してNVMeデバイスからの起動を有効化します。

    あるいは、ブートローダーを直接NVMeデバイスに書き込んだ後、それをRaspberry Piに接続して起動方式を変更する方法もあります。その後、NVMe SSDをPCに接続してOSをインストールし、完了後に再度Raspberry Piに装着します。

#. 予備のMicro SDカードまたはNVMe SSDを、カードリーダーを使ってPCに接続します。

#. |link_rpi_imager| を開き、 **Raspberry Pi Device** をクリックして **Raspberry Pi 5** を選択します。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. **Operating System** タブで下にスクロールし、 **Misc utility images** を選びます。

   .. image:: img/nvme_misc.png
      :width: 90%

#. **Bootloader (Pi 5 family)** を選択します。

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. **NVMe/USB Boot** を選択して、Raspberry Pi 5がNVMe → USB → SDカードの順で起動するよう設定します。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. **Storage** オプションで、書き込み先のストレージデバイスを選択します。

   .. note::

      複数のストレージが接続されている場合は、誤操作を防ぐため他のストレージを取り外しておくことをおすすめします。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. **NEXT** をクリックします。既存データがある場合は、事前にバックアップを取りましょう。バックアップが不要であれば **Yes** をクリックして進めてください。

   .. image:: img/os_continue.png
      :width: 90%


#. **NVMe/USB Boot** が正常に書き込まれた旨の表示が出ます。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Micro SDカードまたはNVMe SSDをRaspberry Piに挿入し、Type Cアダプターで電源を入れます。ブートローダーがEEPROMに書き込まれます。

.. note::

    書き込み完了後、Raspberry PiはNVMe → USB → SDカードの順で起動を試みるようになります。

    電源を切り、Micro SDカードまたはNVMe SSDを取り外してください。


2. NVMe SSDへのOSインストール
---------------------------------

続いて、NVMe SSDにオペレーティングシステムをインストールします。

**手順**

#. カードリーダーを使ってSDカードをPCに挿入します。

#. |link_rpi_imager| を開き、 **Raspberry Pi Device** をクリックして **Raspberry Pi 5** を選択します。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. **Operating System** タブをクリックします。

   .. image:: img/os_choose_os.png
      :width: 90%

#. ページ下部までスクロールし、使用するオペレーティングシステムを選択します。

   .. note::

      * **Ubuntu** を使用する場合は、 **Other general-purpose OS** → **Ubuntu** を選び、 **Ubuntu Desktop 24.04 LTS（64bit）** または **Ubuntu Server 24.04 LTS（64bit）** を選択してください。
      * **Kali Linux**、 **Home Assistant**、 **Homebridge** の場合は、 **Other specific-purpose OS** を選び、該当のシステムを選択してください。

   .. image:: img/os_other_os.png
      :width: 90%

#. **Storage** オプションで、インストール先のストレージデバイスを選択します。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. **NEXT** をクリックします。

   .. note::

      * 事前設定ができないシステムの場合、 **NEXT** をクリックするとデータ保存の確認が表示されます。バックアップ済みであれば **Yes** を選択してください。

      * ホスト名やWiFi、SSHの有効化などを事前に設定できるシステムでは、カスタム設定を適用するかどうかの確認が表示されます。 **Yes** または **No** を選ぶか、編集に戻ることも可能です。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Raspberry Piの **ホスト名** を設定します。ホスト名はネットワーク識別名で、 ``<hostname>.local`` または ``<hostname>.lan`` でアクセス可能になります。

     .. image:: img/os_set_hostname.png

   * 管理者アカウント用の **ユーザー名** と **パスワード** を設定します。Raspberry Piは初期パスワードがないため、セキュリティ確保のために必須です。

     .. image:: img/os_set_username.png

   * 無線LANの **SSID** と **パスワード** を入力します。

     .. note::

       ``Wireless LAN country`` には、お住まいの地域に対応する2文字の `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ を設定してください。

     .. image:: img/os_set_wifi.png

   * Raspberry Piへリモート接続するため、 **Services** タブでSSHを有効化します。

     * **パスワード認証** を使う場合は、Generalタブで設定したユーザー名とパスワードを使用します。
     * 公開鍵認証のみを許可するには、「Allow public-key authentication only」を選択。RSAキーがある場合はそれが使われ、ない場合は「Run SSH-keygen」で新しい鍵ペアを生成します。

     .. image:: img/os_enable_ssh.png

   * **Options** メニューでは、書き込み完了時に音を鳴らす、メディアを自動排出する、テレメトリを有効にするなどの設定が可能です。

     .. image:: img/os_options.png



#. カスタム設定の入力が完了したら **Save** をクリックして保存し、次に **Yes** をクリックして書き込み時に適用します。

   .. image:: img/os_click_yes.png
      :width: 90%


#. NVMe SSDに既存データがある場合は、必ずバックアップを取りましょう。不要であれば **Yes** をクリックして続行します。

   .. image:: img/nvme_erase.png
      :width: 90%


#. 「Write Successful」と表示されたら、イメージの書き込みと検証は完了です。NVMe SSDからRaspberry Piを起動する準備が整いました。
