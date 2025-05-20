.. note:: 

    こんにちは！SunFounder の Facebook コミュニティ「Raspberry Pi & Arduino & ESP32 愛好者グループ」へようこそ！Raspberry Pi、Arduino、ESP32 に熱中する仲間たちと一緒に、これらの技術をもっと深く学び、共有し、楽しみましょう。

    **参加するメリット**

    - **専門サポート**：購入後の技術的課題を、コミュニティとチームの協力で解決します。
    - **学びと共有**：チュートリアルやヒントを交換し、スキルを向上させましょう。
    - **新製品の先行情報**：新製品の発表やプレビューをいち早く入手できます。
    - **特別割引**：最新製品に対して特別な割引を受けられます。
    - **イベント・プレゼント企画**：季節限定のキャンペーンや抽選プレゼントに参加できます。

    👉 今すぐ参加して、私たちと一緒に探求と創造を楽しみましょう！[|link_sf_facebook|] をクリック！

.. _max_install_to_nvme_home_bridge:

NVMe SSD に OS をインストールする
============================================

NVMe SSD を使用し、パソコンに接続するためのアダプターをお持ちの場合、以下のチュートリアルで素早くインストールできます。

**必要なもの**

* パーソナルコンピュータ
* NVMe SSD
* NVMe → USB アダプター
* Micro SD カードおよびカードリーダー

.. _max_update_bootloader:

1. ブートローダーの更新
----------------------------------

Raspberry Pi 5 を NVMe → USB → SDカード の順に起動できるように、ブートローダーを更新する必要があります。

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    このステップでは予備の Micro SD カードの使用を推奨します。まずこのカードにブートローダーを書き込み、すぐに Raspberry Pi に挿入して NVMe 起動を有効にします。

    あるいは、ブートローダーを NVMe デバイスに直接書き込み、それを Raspberry Pi に挿すことでも起動方法を変更可能です。その後、NVMe SSD をパソコンに接続して OS をインストールし、完了後に再び Raspberry Pi に戻します。

#. 予備の Micro SD カードまたは NVMe SSD をパソコンに挿入します。

#. |link_rpi_imager| を開き、 **Raspberry Pi Device** で **Raspberry Pi 5** を選択。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. **Operating System** タブで下にスクロールし、 **Misc utility images** を選択。

   .. image:: img/nvme_misc.png
      :width: 90%

#. **Bootloader (Pi 5 family)** を選択。

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. **NVMe/USB Boot** を選択し、NVMe を優先して起動する設定に。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. **Storage** オプションでインストール先のストレージを選択。

   .. note::

      接続されているストレージが複数ある場合は、誤選択防止のため不要なデバイスを取り外してください。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. **NEXT** をクリック。データがある場合は事前にバックアップをとり、問題なければ **Yes** をクリック。

   .. image:: img/os_continue.png
      :width: 90%


#. **NVMe/USB Boot** の書き込み完了通知が表示されます。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. 書き込みが終わった Micro SD または NVMe SSD を Raspberry Pi に挿入し、Type C アダプターで給電すると、ブートローダーが EEPROM に書き込まれます。

.. note::

   その後、Raspberry Pi は NVMe → USB → SDカード の順に起動を試みるようになります。

   Raspberry Pi の電源を切り、Micro SD カードまたは NVMe SSD を取り外してください。


2. OS を NVMe SSD にインストールする
---------------------------------------

次に、NVMe SSD にオペレーティングシステムをインストールします。

**手順**

#. SDカードをパソコンに挿入します。

#. |link_rpi_imager| を起動し、 **Raspberry Pi Device** で **Raspberry Pi 5** を選択。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. **Operating System** タブをクリック。

   .. image:: img/os_choose_os.png
      :width: 90%

#. 一番下までスクロールし、インストールする OS を選択。

   .. note::

      * **Ubuntu** の場合は、 **Other general-purpose OS** → **Ubuntu** → **Ubuntu Desktop 24.04 LTS (64 bit)** または **Ubuntu Server 24.04 LTS (64 bit)** を選択。
      * **Kali Linux** 、 **Home Assistant** 、 **Homebridge** の場合は、 **Other specific-purpose OS** から選択。

   .. image:: img/os_other_os.png
      :width: 90%

#. **Storage** でインストール先のストレージを選択。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. **NEXT** をクリック。

   .. note::

      * 事前設定ができないシステムでは、 **NEXT** をクリックした後に、デバイス内のデータを保存するかどうかの確認が表示されます。バックアップをすでに取っている場合は、 **Yes** を選択してください。

      * ホスト名や Wi-Fi、SSH を設定可能な OS の場合、設定を適用するかの確認が表示されます。 **Yes** または **No** を選択するか、戻って編集できます。

   .. image:: img/os_enter_setting.png
      :width: 90%


   * **hostname** を設定。ネットワーク経由で ``<hostname>.local`` や ``<hostname>.lan`` でアクセス可能です。

     .. image:: img/os_set_hostname.png

   * **Username** と **Password** を設定。Raspberry Pi には初期パスワードがないため、セキュリティ上必須です。

     .. image:: img/os_set_username.png

   * 無線 LAN の **SSID** と **Password** を設定。

     .. note::

        ``Wireless LAN country`` には、所在地に対応した2文字の `ISO/IEC alpha2 コード <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ を指定してください。

     .. image:: img/os_set_wifi.png

   * SSH を有効にするには **Services** タブで設定。

     * **パスワード認証** の場合、General タブで設定したユーザー名とパスワードを使用。
     * 公開鍵認証のみを使用する場合は「Allow public-key authentication only」を選択し、必要に応じて SSH キーを生成。

     .. image:: img/os_enable_ssh.png

   * **Options** メニューでは、書き込み完了時の音通知やメディアの自動取り出し、テレメトリの有効化などが設定可能。

     .. image:: img/os_options.png



#. カスタマイズ設定を終えたら **Save** をクリックし保存。次に **Yes** をクリックして書き込みを開始。

   .. image:: img/os_click_yes.png
      :width: 90%


#. NVMe SSD に既存データがある場合はバックアップを行い、不要であれば **Yes** をクリックして続行。

   .. image:: img/nvme_erase.png
      :width: 90%


#. 「Write Successful」のポップアップが表示されれば、書き込みおよび検証は完了です。これで Raspberry Pi を NVMe SSD から起動する準備が整いました。
