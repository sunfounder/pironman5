.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと共に、Raspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームの支援を受けて、アフターサポートや技術的な課題を解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベントやプレゼント企画**: プレゼント企画や季節のプロモーションに参加できます。

    👉 探索と創造の旅に出る準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

カメラモジュール
===========================================

.. note::

    Pironman 5 シリーズにはカメラモジュールは含まれていません。  
    ご自身で用意するか、公式サイトから購入してください:

    * `カメラモジュール <https://www.sunfounder.com/products/ov5647-camera-module>`_

このセクションでは、以下の内容を学びます:

* Pironman 5 の分解方法。  
* Raspberry Pi 5 へのカメラモジュールの取り付け方法。  
* ケースの再組み立て方法。  
* 写真撮影や動画録画によるカメラモジュールのテスト方法。

このセクションを終える頃には、プロジェクトに使用できる完全に取り付け済みで動作するカメラモジュールを手にしているでしょう。

カメラモジュールの組み立て
------------------------------------

次の手順に従ってカメラモジュールを組み立てます:

1. ケースから2枚のアクリルパネルを取り外します。

   .. image:: img/IN.CMR.1.png
      :align: center

2. 画像のように2ピンワイヤーとFPCを取り外します。

   .. image:: img/IN.CMR.2.png
      :align: center

3. 4本のネジを外して NVMe PIP と電源スイッチコンバータモジュール群を取り外します。

   .. image:: img/IN.CMR.3.png
      :align: center

4. モジュール群を分解します。これにはリベットの取り外しが含まれます。リベット中央の軸をドライバーで押し出し、その後リベット全体を取り外してください。

   .. image:: img/IN.CMR.4.png
      :align: center

5. カメラモジュールを FPC ケーブルに接続します。

   .. image:: img/IN.CMR.5.png
      :align: center

6. ケースの CAMERA ホールに FPC を通します。

   .. image:: img/IN.CMR.6.png
      :align: center

7. 引き続き FPC をケースの CAMERA ホールに通します。

   .. image:: img/IN.CMR.7.png
      :align: center

8. FPC を Raspberry Pi に接続します。この作業は非常に狭い空間で行うため、慎重に操作してください。

   .. image:: img/IN.CMR.8.png
      :align: center

9. Raspberry Pi 5 の電源を入れ、カメラモジュールが正しく接続されているか確認します。

   * まず、ディスプレイを Raspberry Pi に接続するか、VNC 接続を確立してください。  
   * システムが起動したら、次のコマンドを実行してカメラの動作を確認します: ``libcamera-hello``  
   * プレビューウィンドウが表示されれば、カメラは正しく動作しています。

10. 電源スイッチコンバータをケースに戻して組み立てます。

   .. image:: img/IN.CMR.9.png
      :align: center

   .. image:: img/IN.CMR.10.png
      :align: center

11. NVMe PIP をケースに戻して組み立てます。

   .. image:: img/IN.CMR.11.png
      :align: center

   .. image:: img/IN.CMR.12.png
      :align: center

12. ケースカバーを再組み立てします。

   .. image:: img/IN.CMR.13.png
      :align: center


カメラモジュールの使用
---------------------------

**カメラのテスト**

Raspberry Pi OS (Bookworm 以降) では **libcamera** スタックが使用されています。  
システム起動後、以下のコマンドを実行してカメラが動作するか確認します:

.. code-block:: bash

    libcamera-hello

プレビューウィンドウが表示されれば、カメラは正しく動作しています。

**写真を撮る**

.. code-block:: bash

    libcamera-jpeg -o test.jpg

これにより静止画が撮影され、 ``test.jpg`` として保存されます。

**動画を撮る**

.. code-block:: bash

    libcamera-vid -t 10000 -o test.h264

* ``-t 10000`` は 10 秒間録画することを意味します。  
* ``-o test.h264`` は出力を H.264 動画として保存します。

動画を MP4 形式に変換するには:

.. code-block:: bash

    ffmpeg -i test.h264 -c copy test.mp4

**Python の例**

``picamera2`` ライブラリを使って Python でカメラを制御することもできます。

依存関係をインストール:

.. code-block:: bash

    sudo apt install python3-picamera2 -y

Python ファイルを作成:

.. code-block:: bash

    nano camera_test.py

次に以下のコードを貼り付けます:

.. code-block:: python

    from picamera2 import Picamera2
    import time

    picam2 = Picamera2()
    picam2.start()
    time.sleep(2)
    picam2.capture_file("image.jpg")

nano を保存して終了するには ``CTRL+O`` を押し、 ``ENTER`` を押してから ``CTRL+X`` を押します。

スクリプトを実行:

.. code-block:: bash

    python3 camera_test.py

