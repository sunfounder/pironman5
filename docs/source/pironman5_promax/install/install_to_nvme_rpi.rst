.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _install_to_nvme_rpi_promax:

NVMe SSDへのOSインストール
===================================

NVMe SSDを使用していて、システムインストールのためにNVMe SSDをコンピューターに接続するアダプターをお持ちの場合は、以下のチュートリアルを使用して迅速にインストールできます。

**必要なもの**

* パーソナルコンピューター
* NVMe SSD
* NVMe to USB アダプター
* Micro SDカードとリーダー


.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

.. start_update_bootloader

.. _update_bootloader_promax:


2. ブートローダーの更新
--------------------------------

まず、Raspberry Pi 5のブートローダーを更新して、 **NVMe**、次に **USB**、最後に **SDカード** の順序で起動を試みるように設定します。

.. note::

    この手順には **予備のMicro SDカード** を使用することを推奨します。

    - 方法1（推奨）：ブートローダーをMicro SDカードに書き込み、Raspberry Piに挿入して一度起動し、設定を適用します。
    - 方法2：ブートローダーを直接NVMe SSDに書き込みます。その後、NVMeをコンピューターに接続してOSをインストールし、Raspberry Piに戻します。

#. 予備の **Micro SDカードまたはNVMe SSD** をカードリーダーまたはアダプターを使用してコンピューターに挿入します。

#. Raspberry Pi Imagerが開くと、 **Device** ページが表示されます。リストからRaspberry Pi 5モデルを選択します。

   .. image:: img/imager_device.png
      :width: 90%

#. **OS** をクリックします。

   * スクロールして **Misc utility images** を選択します。

     .. image:: img/nvme_misc.png
        :width: 90%

   * **Bootloader (Pi 5 family)** を選択します。

     .. image:: img/nvme_bootloader.png
        :width: 90%

   * **NVMe/USB Boot** を選択して起動順序を設定し、 **NEXT** をクリックします。

     .. image:: img/nvme_boot.png
        :width: 90%


#. **Storage** で、正しいMicro SDカードまたはNVMe SSDを選択し、 **NEXT** をクリックします。

   .. note::

      正しいデバイスが選択されていることを確認してください。必要に応じて他のストレージデバイスを接続から外してください。

   .. image:: img/imager_storage.png
      :width: 90%

#. 設定を確認し、 **WRITE** をクリックして開始します。

   .. image:: img/nvme_write.png
      :width: 90%

#. 警告を確認し、Raspberry Pi Imagerがブートローダーを消去して書き込むことを許可します。

   .. image:: img/imager_erase.png
      :width: 90%

#. **Write complete!** が表示されるまで待ち、ストレージデバイスを安全に取り外します。

   .. image:: img/nvme_finish.png
      :width: 90%

#. Micro SDカードをRaspberry Piに挿入し、一度電源を入れてブートローダーの更新を適用します。

   .. image:: img/os_sd_to_pi.jpg
      :width: 70%

#. Raspberry Piの起動が完了してから **少なくとも10秒** 待ち、電源を切ってMicro SDカードまたはNVMe SSDを取り外します。

これでRaspberry Pi 5は **NVMe** からの起動準備が整いました。

.. end_update_bootloader

3. NVMe SSDへのOSインストール
-----------------------------------

これで、NVMe SSDにオペレーティングシステムをインストールできます。

#. アダプターを使用して **NVMe SSD** をコンピューターに挿入します。

2. Raspberry Pi Imagerが開くと、 **Device** ページが表示されます。リストからRaspberry Pi 5モデルを選択します。

   .. image:: img/imager_device.png
      :width: 90%

3. **OS** セクションに移動し、推奨される **Raspberry Pi OS (64-bit)** オプションを選択します。

   .. warning::

      必ず **64 ビット** 版を選択してください。**32 ビット** のシステムをインストールすると、一部のパッケージは ``aarch64``（64 ビット）版のみの提供となり、特定の機能がインストールできない、または正しく動作しない場合があります。

   .. image:: img/imager_os.png
      :width: 90%

4. **Storage** セクションで、 **NVMe SSD** を選択します。

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os