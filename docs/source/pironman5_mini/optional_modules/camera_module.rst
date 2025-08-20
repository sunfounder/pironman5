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

このセクションでは、カメラモジュールをテストするために、写真を撮影し動画を録画する方法を学びます。

このセクションを終える頃には、プロジェクトに使用できる完全に取り付け済みで動作するカメラモジュールを手にしているでしょう。



**カメラのテスト**

Raspberry Pi OS (Bookworm 以降) では **libcamera** スタックが使用されています。  
システム起動後、以下のコマンドを実行してカメラが動作するか確認します:

.. code-block:: bash

    libcamera-hello

プレビューウィンドウが表示されれば、カメラは正しく動作しています。

**写真を撮る**

.. code-block:: bash

    libcamera-jpeg -o test.jpg

これにより静止画が撮影され、``test.jpg`` として保存されます。

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

nano を保存して終了するには ``CTRL+O`` を押し、``ENTER`` を押してから ``CTRL+X`` を押します。

スクリプトを実行:

.. code-block:: bash

    python3 camera_test.py

