.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _cpn_camera_module:

カメラモジュール
====================================


**説明**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

これは、OV5647 センサーを搭載した 5MP Raspberry Pi カメラモジュールです。プラグアンドプレイ対応で、付属のリボンケーブルを Raspberry Pi の CSI（カメラシリアルインターフェース）ポートに接続するだけで使用できます。

ボードは小型で、約 25mm x 23mm x 9mm、重量は 3g であり、モバイル用途やサイズ・重量が重要なアプリケーションに最適です。このカメラモジュールのネイティブ解像度は 5 メガピクセルで、オンボードの固定焦点レンズを備え、2592 x 1944 ピクセルの静止画撮影が可能で、1080p30、720p60、640x480p90 のビデオにも対応しています。

.. note:: 

   このモジュールは、画像とビデオのキャプチャのみが可能で、音声の録音はできません。



**仕様**

* **静止画解像度**: 2592×1944
* **対応ビデオ解像度**: 1080p/30 fps、720p/60fps、640 x480p 60/90 ビデオ録画
* **絞り（F）**: 1.8
* **画角**: 65度
* **寸法**: 24mm x 23.5mm x 8mm
* **重量**: 3g
* **インターフェース**: CSI コネクタ
* **対応OS**: Raspberry Pi OS（最新バージョン推奨）



**カメラモジュールの組み立て**
-------------------------------------


カメラモジュールまたは Raspberry Pi には、平らなプラスチック製のコネクタがあります。黒い固定スイッチを慎重に引き出し、固定スイッチが部分的に引き出された状態にします。FFC ケーブルを図の方向に従ってプラスチックコネクタに挿入し、固定スイッチを元の位置に押し戻します。

FFC ケーブルが正しく取り付けられている場合、ケーブルはまっすぐになり、軽く引っ張っても抜けません。そうでない場合は、再度取り付け直してください。

.. raw:: html

    <div style="text-align: center; margin: 16px 0;">
        <iframe width="560" height="315"
            src="https://www.youtube.com/embed/riUNPxS7sHs"
            title="Pironman 5 Pro MAX Camera Module Assembly"
            frameborder="0"
            allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen>
        </iframe>
    </div>

.. image:: img/connect_ffc.png

   
.. image:: img/1.10_camera.png
   :width: 700

.. warning::

   電源が入った状態でカメラを取り付けないでください。カメラが破損する恐れがあります。