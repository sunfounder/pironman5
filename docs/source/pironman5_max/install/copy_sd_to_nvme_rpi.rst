.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと共に、Raspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームの支援を受けて、アフターサポートや技術的な課題を解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベントやプレゼント企画**: プレゼント企画や季節のプロモーションに参加できます。

    👉 探索と創造の旅に出る準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _copy_sd_to_nvme_max:

Micro SD から NVMe SSD へ OS をコピー
==================================================================

NVMe SSD はあるものの、コンピューターに接続するためのアダプターがない場合は、3 つ目の方法を選択できます。  
まず **Micro SD カード** にシステムをインストールし、Pironman 5 MAX が正常に起動した後で、Micro SD カードから **NVMe SSD** にシステムを転送します。

* まず :ref:`install_os_sd_rpi_max` を完了してください。
* 次に、Raspberry Pi を起動してログインします。ログイン方法が分からない場合は、Raspberry Pi 公式サイトをご覧ください： |link_rpi_get_start|。

以下の手順に進む前に、上記の手順を完了してください。


1. PCIe を有効にする
--------------------

デフォルトでは PCIe コネクタは有効になっていません。

* 有効にするには、``/boot/firmware/config.txt`` ファイルを開きます。

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* 次に、以下の行をファイルに追加します。

  .. code-block:: shell
  
    # PCIe 外部コネクタを有効化
    dtparam=pciex1
  
* ``pciex1`` には覚えやすい別名があり、代わりに ``dtparam=nvme`` を ``/boot/firmware/config.txt`` に追加することもできます。

  .. code-block:: shell
  
    dtparam=nvme

.. * この接続は Gen 2.0（5 GT/秒）での動作が認証されていますが、以下の行を ``/boot/firmware/config.txt`` に追加することで、Gen 3.0（10 GT/秒）に強制することもできます。

..   .. code-block:: shell
  
..     # Gen 3.0 速度を強制
..     dtparam=pciex1_gen=3
  
..   .. warning::
  
..     Raspberry Pi 5 は Gen 3.0 速度での動作が認証されておらず、この速度での PCIe デバイス接続は不安定になる可能性があります。

* PCIe スイッチの背後にある NVMe ドライブを起動時に Raspberry Pi が検出できるように、PCIe の起動遅延を無効にする必要があります。以下の行を ``/boot/firmware/config.txt`` に追加してください：

   .. code-block:: shell

      dtparam=pciex1_no_10s=on


* ``Ctrl + X``、``Y``、``Enter`` を押して変更を保存します。


**BOOT_ORDER**

2 台の NVMe システムドライブをインストールしており、起動するドライブを選択する必要がある場合は、  
``/boot/firmware/cmdline.txt`` ファイル内の ``ROOT=PARTUUID=xxxxxxxxx`` を、起動したいディスクの UUID に変更してください。  
ディスクの UUID は、以下のコマンドで確認できます。

.. code-block:: shell

   ls /dev/disk/by-id/

.. start_copy_nvme

2. SSD に OS をインストールする
----------------------------------------

SSD にオペレーティングシステムをインストールする方法は 2 つあります：

**Micro SD カードから SSD へシステムをコピーする**

#. ディスプレイを接続するか、VNC Viewer を使用して Raspberry Pi のデスクトップにアクセスします。次に **Raspberry Pi ロゴ** -> **アクセサリ** -> **SD Card Copier** をクリックします。

   .. image:: img/ssd_copy.png
      
    
#. **Copy From** と **Copy To** のデバイスが正しく選択されていることを確認してください。間違えないよう十分注意してください。

   .. image:: img/ssd_copy_from.png
      
#. デバイスを正しく識別し、マウント競合や起動問題を防ぐために、「NEW Partition UUIDs」を必ず選択してください。

   .. image:: img/ssd_copy_uuid.png
    
#. 選択後、**Start** をクリックします。

   .. image:: img/ssd_copy_click_start.png

#. SSD 上の内容が消去されるという警告が表示されます。**Yes** をクリックする前に必ずデータをバックアップしてください。しばらく待つと、コピーが完了します。

**Raspberry Pi Imager を使用してシステムをインストールする**

Micro SD カードにデスクトップ版のシステムがインストールされている場合、Raspberry Pi Imager などのイメージングツールを使用して SSD にシステムを書き込むことができます。この例では Raspberry Pi OS bookworm を使用していますが、他のシステムでは事前にイメージングツールのインストールが必要な場合があります。

#. ディスプレイを接続するか、VNC Viewer を使用して Raspberry Pi のデスクトップにアクセスします。次に **Raspberry Pi ロゴ** -> **アクセサリ** -> **Raspberry Pi Imager** をクリックします。

   .. image:: img/ssd_imager.png

#. カードリーダーを使用して microSD カードをコンピューターに挿入します。作業を進める前に、重要なデータは必ずバックアップしてください。

   .. image:: img/insert_sd.png
      :width: 90%

#. Raspberry Pi Imager を起動すると、**Device** ページが表示されます。リストからお使いの Raspberry Pi 5 モデルを選択します。

   .. image:: img/imager_device.png
      :width: 90%

#. **OS** セクションに移動し、推奨されている **Raspberry Pi OS (64-bit)** を選択します。

   .. image:: img/imager_os.png
      :width: 90%

#. **Storage** セクションで **NVMe SSD** を選択します。

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

.. _configure_boot_ssd_max:

3. SSD から起動するよう設定する
---------------------------------------

このセクションでは、Raspberry Pi が NVMe SSD から直接起動するように設定します。これにより、SD カードよりも高速な起動時間と優れたパフォーマンスを得ることができます。以下の手順を注意深く実行してください。

#. まず、Raspberry Pi でターミナルを開き、次のコマンドを実行して設定インターフェースにアクセスします。

   .. code-block:: shell

      sudo raspi-config

#. ``raspi-config`` メニューで、矢印キーを使って **Advanced Options** を選択し、``Enter`` を押して詳細設定に入ります。

   .. image:: img/nvme_open_config.png

#. **Advanced Options** 内で **Boot Order** を選択します。この設定では、Raspberry Pi が起動可能なデバイスを検索する順序を指定できます。

   .. image:: img/nvme_boot_order.png

#. 次に **NVMe/USB boot** を選択します。これにより、SD カードなど他のオプションよりも、USB 接続の SSD や NVMe ドライブからの起動が優先されます。

   .. image:: img/nvme_boot_nvme.png

#. 起動順序を選択したら、**Finish** を押して raspi-config を終了します。**Escape** キーを使用して設定ツールを閉じることもできます。

   .. image:: img/nvme_boot_ok.png

#. 新しい起動設定を適用するため、``sudo reboot`` を実行して Raspberry Pi を再起動します。

   .. code-block:: shell

      sudo raspi-config
   
   .. image:: img/nvme_boot_reboot.png

再起動後、Raspberry Pi は接続された NVMe SSD からの起動を試みるようになり、システムのパフォーマンスと耐久性が向上します。

.. end_copy_nvme
