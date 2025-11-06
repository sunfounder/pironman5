.. note:: 

    こんにちは！SunFounder の Facebook コミュニティ「Raspberry Pi & Arduino & ESP32 愛好者グループ」へようこそ！Raspberry Pi、Arduino、ESP32 に熱中する仲間たちと一緒に、これらの技術をより深く探究していきましょう。

    **参加するメリット**

    - **専門サポート**：購入後の技術的トラブルを、コミュニティと当社チームがサポートします。
    - **学びと共有**：チュートリアルやヒントを共有し、スキルを高めましょう。
    - **新製品の先行プレビュー**：発売前の新製品情報やプロトタイプをいち早くチェック。
    - **限定割引**：最新製品に対する特別割引をご利用いただけます。
    - **イベント & プレゼント企画**：プレゼントやキャンペーンにご参加いただけます。

    👉 一緒に探求と創造を楽しみましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

.. _max_install_to_nvme_ubuntu:

NVMe SSD への OS インストール
============================================

NVMe SSD を使用し、PC に接続するためのアダプターがある場合は、以下の手順で素早くインストールを行うことができます。

**必要なもの**

* パーソナルコンピュータ
* NVMe SSD
* NVMe → USB アダプター
* Micro SD カードおよびカードリーダー


1. ブートローダーの更新
----------------------------------

Raspberry Pi 5 を NVMe から起動できるようにするためには、まずブートローダーを更新し、NVMe → USB → SD カードの優先順位に変更する必要があります。

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    このステップでは、予備の Micro SD カードの使用が推奨されます。まずこのカードにブートローダーを書き込み、すぐに Raspberry Pi に挿入して NVMe デバイスからの起動を有効化してください。

    または、ブートローダーを NVMe デバイスに直接書き込んでから Raspberry Pi に挿し、起動方法を変更することも可能です。その後、NVMe SSD を PC に接続して OS をインストールし、インストール完了後に Raspberry Pi に戻します。

#. 予備の Micro SD カードまたは NVMe SSD をカードリーダーで PC に接続します。

#. |link_rpi_imager| を起動し、 **Raspberry Pi Device** から **Raspberry Pi 5** を選択します。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. **Operating System** タブで下へスクロールし、 **Misc utility images** を選択します。

   .. image:: img/nvme_misc.png
      :width: 90%
   
#. **Bootloader (Pi 5 family)** を選択します。

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. **NVMe/USB Boot** を選択し、Raspberry Pi 5 を NVMe 優先で起動するよう設定します。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. **Storage** オプションでインストール対象のストレージを選択します。

   .. note::

      正しいストレージを選択してください。複数のデバイスが接続されている場合は誤選択防止のために他のデバイスを一時的に取り外すことを推奨します。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. **NEXT** をクリックします。ストレージに既存データがある場合は、必要に応じてバックアップを取りましょう。問題なければ **Yes** をクリックして続行。

   .. image:: img/os_continue.png
      :width: 90%


#. **NVMe/USB Boot** の書き込み完了通知が表示されます。

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Micro SD カードまたは NVMe SSD を Raspberry Pi に挿入し、Type C アダプターで電源を供給すると、ブートローダーが EEPROM に書き込まれます。

.. note::

    この作業完了後、Raspberry Pi は NVMe → USB → SD カードの順に起動を試みます。

    Raspberry Pi の電源をオフにし、Micro SD または NVMe SSD を取り外してください。


2. OS を NVMe SSD にインストールする
----------------------------------------

次に、オペレーティングシステムを NVMe SSD にインストールします。

**手順**

#. |link_batocera_download| にアクセスし、 **Raspberry Pi 5 B** を選んでダウンロードします。

   .. image:: img/batocera_download.png
      :width: 90%


#. ダウンロードした ``batocera-xxx-xx-xxxxxxxx.img.gz`` を解凍します。

#. SDカードをリーダー経由で PC に挿入します。

#. |link_rpi_imager| を起動し、 **Operating System** タブを開きます。

   .. image:: img/os_choose_os.png
      :width: 90%

#. ページ下部までスクロールし、 **Use Custom** を選択。

   .. image:: img/batocera_os_use_custom.png
      :width: 90%


#. 解凍した ``batocera-xxx-xx-xxxxxxxx.img`` を選び、 **Open** をクリック。

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. **Storage** でインストール先のストレージを選択。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%



#. **NEXT** をクリックします。データがある場合は事前にバックアップを取り、問題なければ **Yes** を押して続行。

   .. image:: img/nvme_erase.png
      :width: 90%


#. 「Write Successful」のポップアップが表示されれば、イメージの書き込みと検証が完了です。これで Raspberry Pi を NVMe SSD から起動する準備が整いました。
