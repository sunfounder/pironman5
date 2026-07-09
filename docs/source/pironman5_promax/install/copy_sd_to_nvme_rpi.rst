.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _copy_sd_to_nvme_promax:

Micro SDからNVMe SSDへのOSコピー
==================================================================

NVMe SSDはあるものの、それをコンピューターに接続するアダプターがない場合は、別の方法を選択できます。最初にMicro SDカードにシステムをインストールします。Pironman 5 Pro MAXが正常に起動した後、Micro SDカードからNVMe SSDにシステムを転送できます。

* まず、:ref:`install_os_sd_rpi_promax` を実行する必要があります。
* その後、起動してRaspberry Piにログインします。ログイン方法がわからない場合は、Raspberry Piの公式ウェブサイト |link_rpi_get_start| にアクセスしてください。

以下の手順に進む前に、上記の手順を完了してください。


1. PCIeの有効化
--------------------

デフォルトではPCIeコネクタは有効になっていません。

* 有効にするには、 ``/boot/firmware/config.txt`` ファイルを開きます。

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* 次に、以下の行をファイルに追加します。

  .. code-block:: shell
  
    # Enable the PCIe External connector.
    dtparam=pciex1
  
* ``pciex1`` のより覚えやすいエイリアスが存在するため、代わりに ``dtparam=nvme`` を ``/boot/firmware/config.txt`` ファイルに追加することもできます。

  .. code-block:: shell
  
    dtparam=nvme

.. * 接続はGen 2.0速度（5 GT/秒）で認定されていますが、以下の行を ``/boot/firmware/config.txt`` に追加することでGen 3.0（10 GT/秒）に強制することもできます。

..   .. code-block:: shell
  
..     # Force Gen 3.0 speeds
..     dtparam=pciex1_gen=3
  
..   .. warning::
  
..     Raspberry Pi 5はGen 3.0速度での認定を受けておらず、これらの速度でのPCIeデバイスへの接続は不安定になる可能性があります。

* 起動時にRaspberry PiがPCIeスイッチの背後にあるNVMeドライブを検出できるように、PCIe起動遅延を無効にする必要があります。以下の行を ``/boot/firmware/config.txt`` に追加します：

   .. code-block:: shell

      dtparam=pciex1_no_10s=on


* ``Ctrl + X``、 ``Y``、 ``Enter`` を押して変更を保存します。


**BOOT_ORDER**

2台のNVMeシステムドライブをインストールし、どちらかから起動する必要がある場合は、
 ``/boot/firmware/cmdline.txt`` ファイル内の ``ROOT=PARTUUID=xxxxxxxxx`` を起動したいディスクのUUIDに変更します。ディスクのUUIDは以下のコマンドで確認できます：

.. code-block:: shell

   ls /dev/disk/by-id/


.. start_copy_nvme

2. SSDへのOSインストール
----------------------------------------

SSDにオペレーティングシステムをインストールするには2つの方法があります：

**Micro SDカードからSSDへのシステムコピー**

#. ディスプレイを接続するか、VNC ViewerからRaspberry Piデスクトップにアクセスします。次に **Raspberry Piロゴ** -> **アクセサリ** -> **SD Card Copier** をクリックします。

   .. image:: img/ssd_copy.png
      
    
#. 正しい **コピー元** と **コピー先** のデバイスを選択してください。間違えないように注意してください。

   .. image:: img/ssd_copy_from.png
      
#. 「新しいパーティションUUID」を選択して、システムがデバイスを正しく識別し、マウントの競合や起動の問題を回避できるようにすることを忘れないでください。

   .. image:: img/ssd_copy_uuid.png
    
#. 選択後、 **開始** をクリックします。

   .. image:: img/ssd_copy_click_start.png

#. SSD上のコンテンツが消去されるというプロンプトが表示されます。データをバックアップしてから「はい」をクリックしてください。しばらく待つと、コピーが完了します。

**Raspberry Pi Imagerによるシステムのインストール**

Micro SDカードにデスクトップ版のシステムがインストールされている場合は、イメージングツール（Raspberry Pi Imagerなど）を使用してシステムをSSDに書き込むことができます。この例ではRaspberry Pi OS bookwormを使用していますが、他のシステムでは最初にイメージングツールをインストールする必要がある場合があります。

#. ディスプレイを接続するか、VNC ViewerからRaspberry Piデスクトップにアクセスします。次に **Raspberry Piロゴ** -> **アクセサリ** -> **Raspberry Pi Imager** をクリックします。

   .. image:: img/ssd_imager.png

#. カードリーダーを使用してmicroSDカードをコンピューターに挿入します。続行する前に、重要なデータをバックアップしてください。

   .. image:: img/insert_sd.png
      :width: 90%

#. Raspberry Pi Imagerが開いたら、 **Device** ページが表示されます。リストからお使いのRaspberry Pi 5モデルを選択します。

   .. image:: img/imager_device.png
      :width: 90%

#. **OS** セクションに移動し、推奨される **Raspberry Pi OS (64-bit)** オプションを選択します。

   .. warning::

      必ず **64 ビット** 版を選択してください。**32 ビット** のシステムをインストールすると、一部のパッケージは ``aarch64``（64 ビット）版のみの提供となり、特定の機能がインストールできない、または正しく動作しない場合があります。

   .. image:: img/imager_os.png
      :width: 90%

#. **Storage** セクションで、 **NVMe SSD** を選択します。

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

.. _configure_boot_ssd_promax:

3. SSDからの起動設定
---------------------------------------

このセクションでは、Raspberry PiがNVMe SSDから直接起動するように設定します。これにより、SDカードよりも高速な起動時間と改善されたパフォーマンスが得られます。以下の手順に慎重に従ってください：

#. まず、Raspberry Piでターミナルを開き、以下のコマンドを実行して設定インターフェースにアクセスします：

   .. code-block:: shell

      sudo raspi-config

#. ``raspi-config`` メニューで、矢印キーを使用して **Advanced Options** に移動します。 ``Enter`` を押して詳細設定にアクセスします。

   .. image:: img/nvme_open_config.png

#. **Advanced Options** 内で、 **Boot Order** を選択します。この設定により、Raspberry Piが起動可能なデバイスを検索する順序を指定できます。

   .. image:: img/nvme_boot_order.png

#. 次に、 **NVMe/USB boot** を選択します。これにより、Raspberry PiはSDカードなどの他のオプションよりも、USB接続のSSDやNVMeドライブからの起動を優先するようになります。

   .. image:: img/nvme_boot_nvme.png

#. 起動順序を選択したら、 **Finish** を押してraspi-configを終了します。 **Escape** キーを使用して設定ツールを閉じることもできます。

   .. image:: img/nvme_boot_ok.png

#. 新しい起動設定を適用するには、 ``sudo reboot`` を実行してRaspberry Piを再起動します。

   .. code-block:: shell

      sudo raspi-config
   
   .. image:: img/nvme_boot_reboot.png

再起動後、Raspberry Piは接続されているNVMe SSDからの起動を試み、システムのパフォーマンスと耐久性が向上します。

.. end_copy_nvme