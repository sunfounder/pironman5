.. note::

    こんにちは、Facebook の SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！  
    仲間と一緒に Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題を、コミュニティやチームの助けを借りて解決できます。  
    - **学びと共有**: ヒントやチュートリアルを交換してスキルを向上。  
    - **限定プレビュー**: 新製品発表や先行情報をいち早く入手。  
    - **特別割引**: 最新製品を会員限定価格で入手可能。  
    - **季節イベントとプレゼント企画**: ホリデーキャンペーンやプレゼントに参加できます。  

    👉 一緒に探求し、創造する準備はできましたか？ [|link_sf_facebook|] をクリックして今すぐ参加しましょう！

1. そのほかに準備するもの
===================================

Pironman 5 MAX を組み立てて使用する前に、以下のコンポーネントが揃っていることを確認してください。  
基本的な動作に必須のものと、Raspberry Pi の使用方法に応じて必要となるオプション品があります。

必須コンポーネント
------------------------------

* **Raspberry Pi 5**

  Pironman 5 MAX は Raspberry Pi 5 に完全対応しています。

  .. image:: img/need_pi5.jpg
     :width: 500

* **27W 電源アダプター**

  電力不足による Raspberry Pi 5 の再起動を防ぐため、Pironman 5 シリーズ製品では、公式の 27W 電源アダプターまたは |link_sf_27w_supply| の使用を推奨します。

  .. image:: img/need_power.png
     :width: 600

* **Micro SD カード**

  Raspberry Pi には内蔵ハードドライブがありません。  
  起動およびすべてのファイルの保存は **Micro SD カード** 上で行われます。  
  
  .. image:: img/need_sd.jpg
    :width: 200

  * 最小容量：**16GB**  
  * 推奨容量：**32GB** （安定性向上のため）  
  * ブランド：読み書きエラーを防ぐため、 **SanDisk** や **Samsung** などの信頼できる製品を使用してください  
  
オプションコンポーネント
------------------------

* **M.2 NVMe SSD**

  Pironman 5 MAX には NVMe PIP が搭載されており、2 つの M.2 SSD コネクタを備えています。  
  対応する NVMe M.2 SSD フォームファクターは、2230、2242、2260、2280 の 4 種類です。  
  インターフェースは PCIe Gen2.0 速度で動作し、Gen3 はサポートされていません。

  .. image:: img/need_nvme.png
    :width: 500

* **モニター（HDMI または TV）** 

  初心者の方には、HDMI 入力を備えたディスプレイを強くおすすめします。  
  Raspberry Pi OS の設定やグラフィカルなプログラムの実行が容易になります。  

  .. image:: img/need_screen.png
    :width: 400
    
* **HDMI ケーブル**

  Raspberry Pi 5 の HDMI ポートは、USB HDMI アダプターを介して標準の HDMI Type-A インターフェースに変換されています。  
  そのため、Pironman 5 MAX をディスプレイに接続するには、標準的な HDMI–HDMI ケーブルが必要です。

  .. image:: img/need_hdmi.png
    :width: 400
    
* **キーボード & マウス**

  Raspberry Pi OS の初期セットアップ時に非常に便利です。  
  その後はリモート接続（SSH / VNC）に切り替えることもできますが、初心者の方には USB またはワイヤレスの基本セットを用意することをおすすめします。  

  .. image:: img/need_keyboard_mouse.png
    :width: 500
 

**準備に関するヒント**

* このキットを購入した場合、多くのアクセサリーは同梱されていますが、Raspberry Pi 本体、Micro SD カード、電源アダプターは別途用意する必要があります。  
* 何を購入すればよいか迷った場合、最も安定して汎用性の高い構成は  
  **Raspberry Pi 5（2GB）＋公式電源アダプター＋32GB Micro SD カード** です。  
