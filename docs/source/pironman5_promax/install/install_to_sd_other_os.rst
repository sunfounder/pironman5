.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _install_to_sd_other_promax:

Micro SDカードへのOSインストール
=============================================

Micro SDカードを使用する場合は、以下のチュートリアルに従ってシステムをMicro SDカードにインストールできます。

**必要なもの**

* パーソナルコンピューター
* Micro SDカードとリーダー

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. OSをmicroSDカードにインストールする
------------------------------------------------

1. カードリーダーを使用してmicroSDカードをコンピューターに挿入します。
   続行する前に、カード上の重要なデータは消去されるため、バックアップしてください。

   .. image:: img/insert_sd.png
      :width: 90%

2. **Raspberry Pi Imager** が開くと、 **Device** ページが表示されます。
   リストから **Raspberry Pi 5** モデルを選択します。

   .. image:: img/imager_device.png
      :width: 90%

3. **OS** セクションに移動し、ページの下部までスクロールして、お使いのオペレーティングシステムを選択します。

   .. note::

      * **Ubuntu** の場合は、 **Other general-purpose OS** → **Ubuntu** をクリックし、次に
        **Ubuntu Desktop 24.04 LTS (64-bit)** または **Ubuntu Server 24.04 LTS (64-bit)** を選択します。
      * **Kali Linux** および **Homebridge** の場合は、
        **Other specific-purpose OS** をクリックし、対応するシステムを選択します。

   .. warning::

      どのシステムを選ぶ場合でも、必ず **64 ビット** 版を選択してください。**32 ビット** のシステムでは、一部のパッケージは ``aarch64``（64 ビット）版のみの提供となり、特定の機能がインストールできない、または正しく動作しない場合があります。

   .. image:: img/imager_other_os.png
      :width: 90%

4. **Storage** セクションで、microSDカードを選択します。
   安全のため、他のUSBストレージデバイスを抜いて、リストにmicroSDカードのみが表示されるようにすることをお勧めします。

   .. image:: img/imager_storage.png
      :width: 90%

#. **NEXT** をクリックします。

   .. note::

      * **事前設定ができない** システムの場合、 **NEXT** をクリックすると **Customisation** ステップをスキップして直接 **書き込み** に進み、OSがmicroSDカードに書き込まれます。
      * **事前設定をサポートしている** システムの場合は、 **Customisation** の手順に従って **ホスト名**、 **WiFi**、 **SSHの有効化** などのオプションを設定します。

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. **“Write Successful”** のポップアップが表示されたら、イメージの書き込みと検証が完了しています。これでmicroSDカードを安全に取り外し、Raspberry Piを起動するために使用できます。