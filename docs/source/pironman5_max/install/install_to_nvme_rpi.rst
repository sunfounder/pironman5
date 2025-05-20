.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32愛好家向けFacebookコミュニティへようこそ！ラズパイ、Arduino、ESP32をより深く探求し、情熱を共有しましょう。

    **なぜ参加するのか？**

    - **エキスパートサポート**：購入後のトラブルや技術的課題を、コミュニティとチームがサポートします。
    - **学びと共有**：チュートリアルやヒントを交換しながらスキルを高めましょう。
    - **新製品の先行公開**：製品発表やプレビューをいち早くチェックできます。
    - **特別割引**：最新製品に適用される特別割引が利用可能です。
    - **季節のキャンペーンやプレゼント企画**：抽選や特別イベントに参加しましょう。

    👉 一緒に探求・創造したい方は、今すぐ [|link_sf_facebook|] をクリックしてご参加ください！

.. _max_install_to_nvme_rpi:

NVMe SSDへのOSインストール
===================================

NVMe SSDを使用しており、PCに接続できるアダプターをお持ちであれば、以下の手順で簡単にOSをインストールできます。

**必要なもの**

* パーソナルコンピュータ
* NVMe SSD
* NVMe → USB アダプター
* Micro SDカードとリーダー

.. _max_update_bootloader:

1. ブートローダーを更新する
--------------------------------

まず、Raspberry Pi 5がNVMeから起動できるように、ブートローダーを更新する必要があります。

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

   このステップでは、予備のMicro SDカードを使用することを推奨します。まずブートローダーをこのMicro SDカードに書き込み、それをすぐにRaspberry Piに挿入して、NVMeデバイスからの起動を有効にします。

   または、最初にブートローダーをNVMeデバイスに直接書き込み、それをRaspberry Piに挿して起動方法を変更することも可能です。その後、NVMe SSDをパソコンに接続してオペレーティングシステムをインストールし、インストール完了後に再びRaspberry Piに挿し直してください。

#. 予備のMicro SDカードまたはNVMe SSDをリーダーを使ってパソコンに接続します。

#. |link_rpi_imager| を開き、 **Raspberry Pi Device** から **Raspberry Pi 5** を選択します。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. **Operating System** タブで下にスクロールし、 **Misc utility images** を選択します。

   .. image:: img/nvme_misc.png
      :width: 90%

#. **Bootloader (Pi 5 family)** を選択します。

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. **NVMe/USB Boot** を選択し、Raspberry Pi 5がNVMe → USB → SDカードの順に起動できるようにします。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. **Storage** でインストール先のストレージを選択します。

   .. note::

      正しいストレージデバイスを選択してください。複数のストレージが接続されている場合は、混乱を避けるために不要なデバイスを取り外しておきましょう。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. **NEXT** をクリックします。ストレージに既存データがある場合は、事前にバックアップを取り、バックアップ済みであれば **Yes** をクリックしてください。

   .. image:: img/os_continue.png
      :width: 90%


#. まもなく、 **NVMe/USB Boot** がストレージに書き込まれたことを示すメッセージが表示されます。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. その後、Micro SDカードまたはNVMe SSDをRaspberry Piに挿入します。Type-Cアダプターで電源を供給すると、ブートローダーがEEPROMに書き込まれます。

.. note::

    その後、Raspberry PiはNVMeからの起動を優先し、次にUSB、最後にSDカードを試行するようになります。

    Raspberry Piの電源を切り、Micro SDカードまたはNVMe SSDを取り外してください。


2. NVMe SSDへのOSインストール
-----------------------------------

次に、NVMe SSDへオペレーティングシステムをインストールします。


#. |link_rpi_imager| を開き、 **Raspberry Pi Device** から **Raspberry Pi 5** を選択します。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. **Operating System** を選び、推奨されるオペレーティングシステムを選択します。

   .. image:: img/os_choose_os.png
      :width: 90%


#. **Storage** で適切なストレージを選択します。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. **NEXT** をクリックし、続いて **EDIT SETTINGS** をクリックしてOS設定をカスタマイズします。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * **ホスト名** を設定してください。これはネットワーク上でRaspberry Piを識別する名前で、 ``<hostname>.local`` や ``<hostname>.lan`` でアクセスできます。
  
     .. image:: img/os_set_hostname.png

   * **ユーザー名** と **パスワード** を設定し、Raspberry Piの管理者アカウントを作成します。セキュリティのためにユニークな組み合わせを使用してください。

     .. image:: img/os_set_username.png

   * ワイヤレスLANの **SSID** と **パスワード** を設定します。

     .. note::

       ``Wireless LAN country`` には、現在の地域に対応する2文字の `ISO/IEC alpha2コード <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ を入力してください。

     .. image:: img/os_set_wifi.png

   * Raspberry Piへリモート接続するために、サービスタブで **SSHを有効化** します。

     * **パスワード認証** には、Generalタブで設定したユーザー名とパスワードを使用します。
     * 公開鍵認証を選ぶ場合は、「Allow public-key authentication only」を選択します。RSAキーがある場合はそれを使用し、なければ「Run SSH-keygen」で新規作成できます。

     .. image:: img/os_enable_ssh.png

   * **Options** メニューで、書き込み完了時の動作（音を鳴らす、メディアを取り出す、テレメトリの有効化）などを設定できます。

     .. image:: img/os_options.png

#. OSカスタマイズの入力が完了したら、 **Save** をクリックして保存し、次に **Yes** をクリックして設定を適用します。

   .. image:: img/os_click_yes.png
      :width: 90%


#. NVMe SSDに既存データがある場合は、事前にバックアップを取り、問題なければ **Yes** をクリックします。

   .. image:: img/nvme_erase.png
      :width: 90%


#. 「Write Successful」ポップアップが表示されたら、OSの書き込みと検証が完了です。これでRaspberry PiをNVMe SSDから起動する準備が整いました。

   .. image:: img/nvme_install_finish.png
      :width: 90%

