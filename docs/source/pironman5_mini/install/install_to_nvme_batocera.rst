.. note::

    こんにちは！SunFounder Raspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！Raspberry Pi、Arduino、ESP32に関する知識を、同じ情熱を持つ仲間たちと一緒に深めていきましょう。

    **Why Join?**

    - **Expert Support**：購入後のトラブルや技術的課題を、コミュニティおよび当社のサポートチームが支援します。
    - **Learn & Share**：ヒントやチュートリアルを共有しながら、スキルを向上させましょう。
    - **Exclusive Previews**：新製品の発表や先行情報をいち早く入手できます。
    - **Special Discounts**：最新製品を対象としたメンバー限定の特別割引をご利用いただけます。
    - **Festive Promotions and Giveaways**：プレゼント企画や季節のキャンペーンに参加しましょう。

    👉 私たちと一緒にものづくりの世界を探求してみませんか？[|link_sf_facebook|] をクリックして、今すぐ参加！

.. _install_to_nvme_ubuntu_mini:

NVMe SSDへのOSインストール
============================================

NVMe SSDを使用し、PCに接続するためのアダプターをお持ちの場合は、以下の手順で迅速にシステムをインストールできます。

**必要な機材**

* パーソナルコンピューター
* NVMe SSD
* NVMe to USBアダプター
* Micro SDカードおよびカードリーダー

.. _update_bootloader_mini:

1. ブートローダーの更新
----------------------------------

まず、USBやSDカードよりも先にNVMeから起動できるよう、Raspberry Pi 5のブートローダーを更新する必要があります。

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    このステップでは、予備のMicro SDカードを使用することを推奨します。まずブートローダーを書き込んだMicro SDカードを作成し、それをすぐにRaspberry Piに挿入して、NVMeデバイスからの起動を可能にします。

    あるいは、ブートローダーを直接NVMeデバイスに書き込んでからRaspberry Piに挿入し、起動方式を変更する方法もあります。その後、NVMe SSDをPCに接続してOSをインストールし、完了後に再びRaspberry Piに装着します。

#. 予備のMicro SDカードまたはNVMe SSDをカードリーダーでPCまたはノートPCに接続します。

#. |link_rpi_imager| を開き、 **Raspberry Pi Device** をクリックし、ドロップダウンから **Raspberry Pi 5** を選択します。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. **Operating System** タブで下にスクロールし、 **Misc utility images** を選択します。

   .. image:: img/nvme_misc.png
      :width: 90%

#. **Bootloader (Pi 5 family)** を選択します。

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. **NVMe/USB Boot** を選択し、Raspberry Pi 5がNVMe → USB → SDカードの順で起動するように設定します。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. **Storage** オプションで、インストール対象のデバイスを選択します。

   .. note::

      間違ったデバイスに書き込まないよう、他のストレージが接続されている場合は取り外しておくことをおすすめします。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. **NEXT** をクリックします。ストレージにデータがある場合は、必ずバックアップを取ってください。必要なければ **Yes** をクリックして続行します。

   .. image:: img/os_continue.png
      :width: 90%


#. **NVMe/USB Boot** がストレージに書き込まれた旨のメッセージが表示されます。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. その後、作成したMicro SDカードまたはNVMe SSDをRaspberry Piに挿入し、Type Cアダプターで電源を入れると、ブートローダーがRaspberry PiのEEPROMに書き込まれます。

.. note::

    これにより、Raspberry PiはNVMe → USB → SDカードの順で起動を試みるようになります。

    書き込みが完了したら、Raspberry Piの電源を切り、Micro SDカードまたはNVMe SSDを取り外してください。


2. NVMe SSDへのOSインストール
---------------------------------

続いて、NVMe SSDにOSをインストールします。

**手順**

#. |link_batocera_download| ページにアクセスし、 **Raspberry Pi 5 B** を選択してダウンロードを開始します。

   .. image:: img/batocera_download.png
      :width: 90%



#. ダウンロードした ``batocera-xxx-xx-xxxxxxxx.img.gz`` ファイルを解凍します。

#. 解凍後、カードリーダーを使ってSDカードをPCまたはノートPCに挿入します。

#. |link_rpi_imager| を開き、 **Operating System** タブをクリックします。

   .. image:: img/os_choose_os.png
      :width: 90%

#. 一番下までスクロールして **Use Custom** を選択します。

   .. image:: img/batocera_os_use_custom.png
      :width: 90%



#. 解凍したイメージファイル ``batocera-xxx-xx-xxxxxxxx.img`` を選択し、 **Open** をクリックします。


   .. image:: img/batocera_os_choose.png
      :width: 90%


#. **Storage** オプションで、書き込み先となる適切なストレージデバイスを選択します。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%

#. **NEXT** をクリックします。ストレージに既存データがある場合はバックアップを取りましょう。必要なければ **Yes** をクリックして続行します。



   .. image:: img/nvme_erase.png
      :width: 90%


#. 「Write Successful」のポップアップが表示されたら、イメージの書き込みと検証は完了です。これでNVMe SSDからRaspberry Piを起動する準備が整いました。
