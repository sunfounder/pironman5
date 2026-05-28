.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Batocera オペレーティングシステムのインストール
==========================================================

以下のチュートリアルに従って、マイクロSDカードにシステムをインストールしてください。

**必要な部品**

* パーソナルコンピュータ
* マイクロSDカードとカードリーダー

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. マイクロSDカードへのOSインストール
-------------------------------------------------------------------

1.  カードリーダーを使用して、マイクロSDカードをコンピュータに挿入します。  
    続行する前に、カード上の重要なデータはすべてバックアップしてください。すべて消去されます。

   .. image:: img/insert_sd.png
      :width: 90%

2.  **Raspberry Pi Imager** が開くと、 **デバイス** ページが表示されます。  
    リストからあなたの **Raspberry Pi 5** モデルを選択してください。

   .. image:: img/imager_device.png
      :width: 90%

3.  **OS** セクションに移動し、ページの下までスクロールして、あなたのオペレーティングシステムを選択してください。

   .. note::

      * **Ubuntu** の場合は、 **その他の汎用OS** → **Ubuntu** をクリックし、
        **Ubuntu Desktop 24.04 LTS (64-bit)** または **Ubuntu Server 24.04 LTS (64-bit)** を選択します。
      * **Kali Linux**、 **Home Assistant**、 **Homebridge** の場合は、
        **その他の特定目的向けOS** をクリックし、対応するシステムを選択してください。

   .. image:: img/imager_other_os.png
      :width: 90%

4.  **ストレージ** セクションで、あなたのマイクロSDカードを選択してください。  
    より安全のため、他のUSBストレージデバイスを取り外し、マイクロSDカードのみがリストに表示されるようにすることを推奨します。

   .. image:: img/imager_storage.png
      :width: 90%

#. **次へ** をクリックします。

   .. note::

      * **事前設定できない** システムの場合、 **次へ** をクリックすると **カスタマイズ** ステップをスキップし、OSがマイクロSDカードに書き込まれる **書き込み** に直接進みます。
      * **事前設定をサポートする** システムの場合は、 **カスタマイズ** ステップに従って、 **ホスト名**、 **WiFi**、 **SSHの有効化** などのオプションを設定してください。

   .. image:: img/imager_write_other_os.png
      :width: 90%
 
#. **「書き込み成功」** ポップアップウィンドウが表示されたら、イメージの書き込みと検証が完全に完了しました。これでマイクロSDカードを安全に取り外し、あなたのRaspberry Piを起動するために使用できます。