.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと共に、Raspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームの支援を受けて、アフターサポートや技術的な課題を解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベントやプレゼント企画**: プレゼント企画や季節のプロモーションに参加できます。

    👉 探索と創造の旅に出る準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _install_to_nvme_ubuntu:

NVMe SSDにOSをインストールする
============================================

NVMe SSDを使用しており、システムインストールのためにNVMe SSDをコンピュータに接続するためのアダプターがある場合は、以下のチュートリアルを使用して迅速にインストールできます。

   .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**必要なコンポーネント**

* パーソナルコンピュータ
* NVMe SSD
* NVMeからUSBへのアダプター
* Micro SDカードおよびリーダー


1. ブートローダーの更新
----------------------------------

最初に、Raspberry Pi 5のブートローダーを更新して、USBおよびSDカードの前にNVMeからの起動を試行するように設定する必要があります。

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    このステップでは、予備のMicro SDカードを使用することをお勧めします。最初にこのMicro SDカードにブートローダーを書き込み、その後すぐにRaspberry Piに挿入して、NVMeデバイスからの起動を有効にします。
    
    または、ブートローダーを最初にNVMeデバイスに直接書き込み、Raspberry Piに挿入して起動方法を変更することも可能です。その後、NVMe SSDをコンピュータに接続してオペレーティングシステムをインストールし、インストールが完了したら再度Raspberry Piに挿入します。

#. 予備のMicro SDカードまたはNVMe SSDをリーダーを使用してコンピュータに挿入します。

#. |link_rpi_imager| 内で **Raspberry Piデバイス** をクリックし、ドロップダウンリストから **Raspberry Pi 5** モデルを選択します。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. **オペレーティングシステム**タブでスクロールして **Misc utility images** を選択します。

   .. image:: img/nvme_misc.png
      :width: 90%
   
#. **ブートローダー (Pi 5ファミリー)** を選択します。

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Raspberry Pi 5がUSBおよびSDカードの前にNVMeから起動するようにするには、 **NVMe/USB Boot** を選択します。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%
      


#. **ストレージ** オプションで、インストールする適切なストレージデバイスを選択します。

   .. note::

      正しいストレージデバイスを選択するようにしてください。混乱を避けるため、複数のストレージデバイスが接続されている場合は他のデバイスを切断することをお勧めします。

   .. image:: img/os_choose_sd.png
      :width: 90%
      

#. **次へ** をクリックできます。ストレージデバイスに既存のデータが含まれている場合は、データ損失を防ぐためにバックアップを確実に行ってください。バックアップが不要であれば、 **Yes** をクリックして続行します。

   .. image:: img/os_continue.png
      :width: 90%
      

#. **NVMe/USB Boot** がストレージデバイスに書き込まれたことが通知されます。

   .. image:: img/nvme_boot_finish.png
      :width: 90%
      

#. これで、Micro SDカードまたはNVMe SSDをRaspberry Piに挿入できます。Type CアダプターでRaspberry Piに電源を入れると、Micro SDカードまたはNVMe SSDからブートローダーがRaspberry PiのEEPROMに書き込まれます。

.. note::

    その後、Raspberry PiはUSBおよびSDカードの前にNVMeから起動するようになります。
    
    Raspberry Piの電源を切り、Micro SDカードまたはNVMe SSDを取り外してください。


2. NVMe SSDにOSをインストールする
-----------------------------------

これで、NVMe SSDにオペレーティングシステムをインストールする準備が整いました。

**手順**

#. まず、|link_batocera_download| ページにアクセスし、 **Raspberry Pi 5 B** を選択してダウンロードします。

   .. image:: img/batocera_download.png
      :width: 90%
      

#. リーダーを使用してSDカードをコンピュータに挿入します。

#. |link_rpi_imager| 内で、 **オペレーティングシステム** タブをクリックします。

   .. image:: img/os_choose_os.png
      :width: 90%
      
#. ページの一番下までスクロールし、 **カスタムを使用** を選択します。

   .. image:: img/batocera_os_use_custom.png
      :width: 90%
      

#. ダウンロードしたシステムファイル ``batocera-xxx-xx-xxxxxxxx.img.gz`` を選択し、 **開く** をクリックします。

   .. image:: img/batocera_os_choose.png
      :width: 90%
      

#. **ストレージ** オプションで、インストールする適切なストレージデバイスを選択します。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%
      


#. **次へ** をクリックできます。ストレージデバイスに既存のデータが含まれている場合は、データ損失を防ぐためにバックアップを確実に行ってください。バックアップが不要であれば、 **Yes** をクリックして続行します。

   .. image:: img/nvme_erase.png
      :width: 90%
      

#. 「書き込み成功」のポップアップが表示されたら、イメージが完全に書き込まれ、検証されています。これでNVMe SSDからRaspberry Piを起動する準備が整いました！
