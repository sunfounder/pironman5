.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32愛好家向けFacebookコミュニティへようこそ！ラズパイ、Arduino、ESP32をより深く探求し、情熱を共有しましょう。

    **なぜ参加するのか？**

    - **エキスパートサポート**：購入後のトラブルや技術的課題を、コミュニティとチームがサポートします。
    - **学びと共有**：チュートリアルやヒントを交換しながらスキルを高めましょう。
    - **新製品の先行公開**：製品発表やプレビューをいち早くチェックできます。
    - **特別割引**：最新製品に適用される特別割引が利用可能です。
    - **季節のキャンペーンやプレゼント企画**：抽選や特別イベントに参加しましょう。

    👉 一緒に探求・創造したい方は、今すぐ [|link_sf_facebook|] をクリックしてご参加ください！


Umbrel OSのインストール
============================================

Umbrelは、オープンソースのセルフホスト型ホームサーバープラットフォーム／OSであり、自分のBitcoinノードを実行したり、ワンクリックでさまざまなセルフホストアプリをインストールしたりして、ハードウェアを自分専用のホームクラウドに変えることができます。自己管理とプライバシーを始めるのに最適な方法です。

**必要なコンポーネント**

* パーソナルコンピュータ
* NVMe SSD
* NVMe–USBアダプター
* microSDカードおよびカードリーダー

1. ブートローダーの更新
--------------------------------

まず、Raspberry Pi 5のブートローダーを更新し、NVMeからの起動を優先して、次にUSB、その後にSDカードから起動するように設定する必要があります。

.. note::

    * この手順では、予備のmicroSDカードを使用することを推奨します。まずこのmicroSDカードにブートローダーを書き込み、それをRaspberry Piに挿入して、NVMeデバイスからの起動を有効にします。
    * あるいは、最初にブートローダーをNVMeデバイスに直接書き込み、その後Raspberry Piに挿入して起動方法を変更することもできます。その後、NVMe SSDをパソコンに接続してOSをインストールし、インストール完了後に再びRaspberry Piに挿し直します。

#. 予備のmicroSDカードまたはNVMe SSDをカードリーダーを使ってパソコンに挿入します。

#. |link_rpi_imager| 内で **Raspberry Pi Device** をクリックし、ドロップダウンリストから **Raspberry Pi 5** モデルを選択します。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. **Operating System** タブで下にスクロールし、 **Misc utility images** を選択します。

   .. image:: img/nvme_misc.png
      :width: 90%

#. **Bootloader (Pi 5 family)** を選択します。

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. **NVMe/USB Boot** を選択し、Raspberry Pi 5がNVMeから起動し、次にUSB、その後にSDカードから起動するように設定します。

   .. image:: img/nvme_nvme_boot.png
      :width: 90%
      
#. **Storage** オプションで、インストールに使用する適切なストレージデバイスを選択します。

   .. note::

      正しいストレージデバイスを選択してください。複数のストレージデバイスが接続されている場合は、混乱を避けるために不要なデバイスを取り外すことを推奨します。

   .. image:: img/os_choose_sd.png
      :width: 90%
      

#. **NEXT** をクリックします。ストレージデバイスに既存のデータがある場合は、データ損失を防ぐためにバックアップを取ってください。バックアップが不要であれば **Yes** をクリックして続行します。

   .. image:: img/os_continue.png
      :width: 90%
      

#. まもなく、 **NVMe/USB Boot** がストレージデバイスに書き込まれたことが通知されます。

   .. image:: img/nvme_boot_finish.png
      :width: 90%
      

#. microSDカードまたはNVMe SSDをRaspberry Piに挿入します。Type-C電源アダプターを接続すると、microSDカードまたはNVMe SSDからブートローダーがRaspberry PiのEEPROMに書き込まれます。

   .. note::

      * 更新後、Raspberry PiはまずNVMeドライブから起動し、次にUSB、最後にmicroSDカードから起動します。
      * 1〜2分待ってから、Raspberry Piの電源を切り、microSDカードまたはNVMe SSDを取り外してください。

2. NVMe SSDへの OS インストール
-----------------------------------

**手順**

1. 最新の Umbrel OS イメージをダウンロードして解凍します。特定のバージョンを選択したい場合は、 `Umbrel リリースページ <https://github.com/getumbrel/umbrel/releases>`_ にアクセスしてください。

   * :download:`最新の Umbrel OS イメージ <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

2. |link_rpi_imager| 内で **Raspberry Pi Device** をクリックし、ドロップダウンリストから **Raspberry Pi 5** を選択します。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

3. **Raspberry Pi Imager** を起動し、 **CHOOSE OS** をクリックします。

   .. image:: img/umbrel_choose_os.png
       :width: 600
       :align: center

4. 一番下までスクロールして **Use custom** を選択します。

   .. image:: img/umbrel_use_custom.png
       :width: 600
       :align: center

5. 先ほどダウンロードした Umbrel OS イメージファイルを選択し、 **Open** をクリックします。

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

6. **Storage** オプションで、インストール先として NVMe SSD を選択します。

   .. image:: img/nvme_ssd_storage.png
      :width: 90%

7. **NEXT** をクリックし、次に **NO** を選択します。Umbrel OS は初回起動時に独自のシステムおよびユーザー設定を自動的に初期化するため、Raspberry Pi Imager で設定したユーザー名やパスワードは使用されません。

   .. image:: img/umbrel_clear_setting.png
      :width: 90%

8. NVMe SSD に既存のデータがある場合は、データ損失を防ぐためにバックアップを取ってください。バックアップが不要であれば **Yes** をクリックして続行します。

   .. image:: img/nvme_erase.png
      :width: 90%

9. 「Write Successful」と表示されたら、イメージの書き込みと検証が完了しています。これで NVMe SSD は Raspberry Pi の起動準備が整いました！

   .. image:: img/umbrel_finish.png
      :width: 90%


