.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと共に、Raspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームの支援を受けて、アフターサポートや技術的な課題を解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベントやプレゼント企画**: プレゼント企画や季節のプロモーションに参加できます。

    👉 探索と創造の旅に出る準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _install_to_nvme_rpi_max:

NVMe SSD への OS インストール
===================================

NVMe SSD を使用しており、NVMe SSD をコンピューターに接続してシステムをインストールするためのアダプターをお持ちの場合は、以下のチュートリアルを使用して簡単にインストールできます。

**必要なもの**

* パーソナルコンピューター
* NVMe SSD
* NVMe → USB アダプター
* Micro SD カードおよびカードリーダー


.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

.. start_update_bootloader

.. _update_bootloader_max:


2. ブートローダーの更新
--------------------------------

まず、Raspberry Pi 5 のブートローダーを更新し、**NVMe** を最優先、次に **USB**、最後に **SD カード** から起動するように設定します。

.. note::

    この手順では、**予備の Micro SD カード** を使用することを推奨します。
    
    - 方法 1（推奨）：ブートローダーを Micro SD カードに書き込み、Raspberry Pi に挿入して 1 回起動し、設定を適用します。
    - 方法 2：ブートローダーを直接 NVMe SSD に書き込みます。その後、NVMe をコンピューターに接続して OS をインストールし、再び Raspberry Pi に取り付けます。

#. カードリーダーまたはアダプターを使用して、予備の **Micro SD カード** または **NVMe SSD** をコンピューターに挿入します。

#. Raspberry Pi Imager を起動すると、**Device** ページが表示されます。リストから **Raspberry Pi 5** モデルを選択します。

   .. image:: img/imager_device.png
      :width: 90%

#. **OS** をクリックします。

   * 下にスクロールして **Misc utility images** を選択します。

     .. image:: img/nvme_misc.png
        :width: 90%

   * **Bootloader (Pi 5 family)** を選択します。

     .. image:: img/nvme_bootloader.png
        :width: 90%

   * 起動順を設定するため **NVMe/USB Boot** を選択し、**NEXT** をクリックします。

     .. image:: img/nvme_boot.png
        :width: 90%


#. **Storage** で正しい Micro SD カードまたは NVMe SSD を選択し、**NEXT** をクリックします。

   .. note::

      正しいデバイスが選択されていることを必ず確認してください。必要に応じて、他のストレージデバイスを取り外してください。

   .. image:: img/imager_storage.png
      :width: 90%


#. 設定内容を確認し、**WRITE** をクリックして開始します。

   .. image:: img/nvme_write.png
      :width: 90%

#. 警告を確認し、Raspberry Pi Imager にブートローダーの消去および書き込みを許可します。

   .. image:: img/imager_erase.png
      :width: 90%

#. **Write complete!** が表示されるまで待ち、その後ストレージデバイスを安全に取り外します。

   .. image:: img/nvme_finish.png
      :width: 90%

#. Micro SD カードを Raspberry Pi に挿入し、1 回電源を入れてブートローダーの更新を適用します。

   .. image:: img/os_sd_to_pi.jpg
      :width: 70%

#. Raspberry Pi の起動が完了してから **少なくとも 10 秒** 待ち、その後電源を切って Micro SD カードまたは NVMe SSD を取り外します。

これで Raspberry Pi 5 は **NVMe** から起動する準備が整いました。

.. end_update_bootloader

3. NVMe SSD に OS をインストールする
------------------------------------------

これで NVMe SSD にオペレーティングシステムをインストールできます。

#. アダプターを使用して **NVMe SSD** をコンピューターに挿入します。

2. Raspberry Pi Imager を起動すると、**Device** ページが表示されます。リストから **Raspberry Pi 5** モデルを選択します。

   .. image:: img/imager_device.png
      :width: 90%

3. **OS** セクションに移動し、推奨されている **Raspberry Pi OS (64-bit)** を選択します。

   .. image:: img/imager_os.png
      :width: 90%

4. **Storage** セクションで **NVMe SSD** を選択します。

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

