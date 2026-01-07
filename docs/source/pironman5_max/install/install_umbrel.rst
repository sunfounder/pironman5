.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと共に、Raspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームの支援を受けて、アフターサポートや技術的な課題を解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベントやプレゼント企画**: プレゼント企画や季節のプロモーションに参加できます。

    👉 探索と創造の旅に出る準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！


Umbrel OS のインストール
============================================

Umbrel は、Bitcoin ノードの運用や、ワンクリックでさまざまなセルフホスト型アプリをインストールできる、オープンソースのセルフホスト型ホームサーバープラットフォーム／OS です。  
ハードウェアを個人用のホームクラウドに変えることができ、セルフカストディやプライバシー重視の運用を始めるのに最適な選択肢です。

**必要なもの**

* パーソナルコンピューター
* NVMe SSD
* NVMe → USB アダプター
* Micro SD カードおよびカードリーダー

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. NVMe SSD に OS をインストールする
------------------------------------------

これで **NVMe SSD** にオペレーティングシステムをインストールする準備が整いました。  
以下の手順に注意して進めてください。本ガイドは初心者向けに分かりやすく書かれています。

.. |link_umbrel_release| raw:: html

    <a href="https://github.com/getumbrel/umbrel/releases" target="_blank">Umbrel OS Releases</a>

#. 最新の **Umbrel OS** イメージをダウンロードし、ファイルを展開します。特定のバージョンを使用したい場合は、|link_umbrel_release| ページにアクセスしてください。

   * :download:`最新の Umbrel OS イメージ <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

#. **NVMe → USB アダプター** を使用して、**NVMe SSD** をコンピューターに接続します。

#. **Raspberry Pi Imager** を起動します。**Device** 画面で、リストから **Raspberry Pi 5** のモデルを選択します。

   .. image:: img/imager_device.png
      :width: 90%

#. **OS** セクションに移動し、下までスクロールして **Use custom** を選択します。

   .. image:: img/imager_use_custom.png
      :width: 90%

#. 先ほどダウンロードして展開した **Umbrel OS のイメージファイル** を選択し、**Open** をクリックします。

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

#. **Next** をクリックして続行します。

   .. image:: img/imager_custom_next.png
      :width: 90%

#. **Storage** セクションで **NVMe SSD** を選択します。コンピューター内の別のドライブではなく、必ず NVMe SSD を選択してください。

   .. image:: img/nvme_storage.png
      :width: 90%

#. すべての設定をよく確認し、**WRITE** をクリックします。

   .. image:: img/imager_write_umbrel.png
      :width: 90%

#. NVMe SSD に既存のデータがある場合、Raspberry Pi Imager はすべてのデータが消去されるという警告を表示します。正しいドライブが選択されていることを再確認し、**I UNDERSTAND, ERASE AND WRITE** をクリックします。

   .. image:: img/imager_erase.png
      :width: 90%

#. **「Write Complete」** と表示されたら、イメージの書き込みと検証は正常に完了しています。

   .. image:: img/imager_umbrel_finish.png
      :width: 90%

