.. note::

    こんにちは！SunFounder Raspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！Raspberry Pi、Arduino、ESP32に情熱を持つ仲間たちとともに、より深く学び、楽しみましょう。

    **Why Join?**

    - **Expert Support**：購入後のトラブルや技術的な課題を、コミュニティおよび当社のサポートチームが支援します。
    - **Learn & Share**：ヒントやチュートリアルを共有し、スキルを高めましょう。
    - **Exclusive Previews**：新製品の発表や先行情報をいち早くキャッチ。
    - **Special Discounts**：最新製品を対象とした限定割引をご提供。
    - **Festive Promotions and Giveaways**：季節限定のキャンペーンやプレゼント企画に参加できます。

    👉 一緒にものづくりの世界を探求しませんか？[|link_sf_facebook|] をクリックして今すぐ参加！

.. _install_to_nvme_rpi_mini:

NVMe SSDへのOSインストール
===================================

NVMe SSDを使用していて、システムインストール用にPCへ接続できるアダプターをお持ちの場合は、以下の手順で簡単にインストールできます。

**必要な機材**

* パーソナルコンピューター
* NVMe SSD
* NVMe to USBアダプター
* Micro SDカードおよびカードリーダー

.. _update_bootloader_mini:

1. ブートローダーの更新
--------------------------------

まず、Raspberry Pi 5がUSBやSDカードよりも先にNVMeから起動できるよう、ブートローダーを更新する必要があります。

.. note::

    この手順では、予備のMicro SDカードの使用を推奨します。まずこのカードにブートローダーを書き込み、すぐにRaspberry Piへ挿入することで、NVMeデバイスからの起動が有効になります。

    あるいは、ブートローダーを最初にNVMeデバイスに書き込み、その後Raspberry Piに接続して起動方法を変更することも可能です。その後、NVMe SSDをパソコンに接続してOSをインストールし、完了後に再びRaspberry Piに装着してください。

#. 予備のMicro SDカードまたはNVMe SSDをリーダー経由でPCに接続します。

#. |link_rpi_imager| を開き、 **Raspberry Pi Device** をクリックし、ドロップダウンから **Raspberry Pi 5** を選択します。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. **Operating System** タブで下にスクロールし、 **Misc utility images** を選択します。

   .. image:: img/nvme_misc.png
      :width: 90%

#. **Bootloader (Pi 5 family)** を選択します。

   .. image:: img/nvme_bootloader.png
      :width: 90%

#. **NVMe/USB Boot** を選択して、NVMe → USB → SDカードの順に起動されるようにします。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%

#. **Storage** オプションで、書き込み対象のストレージを選択します。

   .. note::

      接続されているストレージが複数ある場合は、誤認防止のため他のストレージを一時的に取り外しておくことをおすすめします。

   .. image:: img/os_choose_sd.png
      :width: 90%

#. **NEXT** をクリックします。ストレージに既存データがある場合は、事前にバックアップを取っておきましょう。不要な場合は **Yes** をクリックして続行します。

   .. image:: img/os_continue.png
      :width: 90%

#. 数秒後、**NVMe/USB Boot** が正常に書き込まれたことを知らせるメッセージが表示されます。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Micro SDカードまたはNVMe SSDをRaspberry Piに挿入し、Type Cアダプターで電源を投入すると、ブートローダーがEEPROMに書き込まれます。

.. note::

    書き込み後は、Raspberry PiがNVMe → USB → SDカードの順で起動を試みます。

    電源を切り、Micro SDカードまたはNVMe SSDを取り外してください。

2. NVMe SSDへのOSインストール
-----------------------------------

次に、NVMe SSDにオペレーティングシステムをインストールします。


#. |link_rpi_imager| を開き、 **Raspberry Pi Device** をクリックして **Raspberry Pi 5** を選択します。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. **Operating System** を選択し、推奨されるOSバージョンを選びます。

   .. image:: img/os_choose_os.png
      :width: 90%


#. **Storage** オプションで、インストール先のストレージを選択します。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. **NEXT** をクリックし、 **EDIT SETTINGS** を選んでOS設定をカスタマイズします。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Raspberry Piの **ホスト名** を設定します。ホスト名はネットワーク上の識別子であり、 ``<hostname>.local`` や ``<hostname>.lan`` でアクセス可能になります。

     .. image:: img/os_set_hostname.png

   * 管理者アカウント用の **ユーザー名** と **パスワード** を作成します。初期状態ではパスワードが設定されていないため、セキュリティ上の理由から必ず設定してください。

     .. image:: img/os_set_username.png

   * 無線LANの設定として、ネットワークの **SSID** と **パスワード** を入力します。

     .. note::

       ``Wireless LAN country`` には、お住まいの国に対応する2文字の `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ を設定してください。

     .. image:: img/os_set_wifi.png

   * Raspberry Piへのリモート接続を行うには、 **Services** タブでSSHを有効にします。

     * **パスワード認証** の場合は、Generalタブで設定したユーザー名とパスワードを使用します。
     * 公開鍵認証を使用する場合は、「Allow public-key authentication only」を選びます。RSAキーがあればそれが使用され、なければ「Run SSH-keygen」で新たにキーを生成できます。

     .. image:: img/os_enable_ssh.png

   * **Options** メニューでは、書き込み完了時の動作（音を鳴らす、メディアの取り出し、テレメトリの有効化など）を設定できます。

     .. image:: img/os_options.png

#. OSのカスタマイズ設定が完了したら **Save** をクリックして保存し、 **Yes** をクリックして書き込み時に設定を反映させます。

   .. image:: img/os_click_yes.png
      :width: 90%


#. NVMe SSDに既存のデータがある場合は、事前にバックアップを取りましょう。不要であれば **Yes** をクリックして続行します。

   .. image:: img/nvme_erase.png
      :width: 90%


#. 「Write Successful」のポップアップが表示されたら、イメージの書き込みと検証は正常に完了しています。これでRaspberry PiをNVMe SSDから起動する準備が整いました。

   .. image:: img/nvme_install_finish.png
      :width: 90%