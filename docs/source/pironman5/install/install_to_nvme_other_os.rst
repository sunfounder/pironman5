.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと共に、Raspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームの支援を受けて、アフターサポートや技術的な課題を解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベントやプレゼント企画**: プレゼント企画や季節のプロモーションに参加できます。

    👉 探索と創造の旅に出る準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _install_to_nvme_other_5:

NVMe SSD への OS インストール
============================================

NVMe SSD を使用しており、NVMe SSD をコンピューターに接続してシステムをインストールするためのアダプターをお持ちの場合は、以下のチュートリアルを使用して簡単にインストールできます。

   .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**必要なもの**

* パーソナルコンピューター
* NVMe SSD
* NVMe → USB アダプター
* Micro SD カードおよびカードリーダー

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. microSD カードに OS をインストールする
------------------------------------------------

#. アダプターを使用して **NVMe SSD** をコンピューターに接続します。

2. **Raspberry Pi Imager** を起動すると、**Device** ページが表示されます。  
   リストから **Raspberry Pi 5** モデルを選択します。

   .. image:: img/imager_device.png
      :width: 90%

3. **OS** セクションに移動し、ページの一番下までスクロールして、使用するオペレーティングシステムを選択します。

   .. note::

      * **Ubuntu** の場合は、**Other general-purpose OS** → **Ubuntu** をクリックし、  
        **Ubuntu Desktop 24.04 LTS (64-bit)** または **Ubuntu Server 24.04 LTS (64-bit)** を選択します。
      * **Kali Linux**、**Home Assistant**、**Homebridge** の場合は、  
        **Other specific-purpose OS** をクリックし、対応するシステムを選択します。

   .. image:: img/imager_other_os.png
      :width: 90%

4. **Storage** セクションで **NVMe SSD** を選択します。

   .. image:: img/nvme_storage.png
      :width: 90%

#. **NEXT** をクリックします。

   .. note::

      * **事前設定ができないシステム** の場合、**NEXT** をクリックすると **Customisation** 手順がスキップされ、  
        直接 **Writing** に進み、OS が microSD カードに書き込まれます。
      * **事前設定をサポートしているシステム** の場合は、**Customisation** 手順に従って  
        **Hostname**、**WiFi**、**Enable SSH** などのオプションを設定してください。

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. **「Write Successful」** のポップアップが表示されたら、イメージの書き込みと検証は完了です。  
   microSD カードを安全に取り外し、Raspberry Pi の起動に使用できます。
