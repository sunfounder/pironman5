
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _view_control_dashboard_mini:

ダッシュボードからの表示と操作
=========================================

``pironman5`` モジュールを正常にインストールすると、再起動時に ``pironman5.service`` が自動的に起動します。

ブラウザで ``http://<ip>:34001`` にアクセスすると、Raspberry Pi の情報を確認したり、RGB設定やファンの制御などを行うためのモニタリングページを開くことができます。

このページには **Dashboard**、 **History**、 **Log**、 **Settings** の各タブがあります。

.. image:: img/dashboard_tab.png
  :width: 90%

  
Dashboard（ダッシュボード）
-----------------------------

Raspberry Piの各種ステータスを確認するためのカードが複数用意されています：

* **Fan**：CPU温度およびCPUファンの回転速度を表示します。 **GPIO Fan State** はGPIOファンの状態を示します。現在の温度ではGPIOファンはオフです。

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%


* **Storage**：Raspberry Pi のストレージ使用状況を表示します。ディスクごとの使用容量と空き容量が確認できます。

  .. image:: img/dashboard_storage.png
    :width: 90%


* **Memory**：RAM使用量およびその割合を表示します。

  .. image:: img/dashboard_memory.png
    :width: 90%


* **Network**：現在のネットワーク接続方式、アップロード・ダウンロード速度を表示します。

  .. image:: img/dashboard_network.png
    :width: 90%


* **Processor**：CPUの動作状況を表示します。4コアの使用率、動作周波数、全体のCPU使用率が確認できます。

  .. image:: img/dashboard_processor.png
    :width: 90%


History（履歴）
------------------

履歴ページでは、過去のデータを確認できます。左のサイドバーで表示したいデータを選択し、期間を指定することで、指定期間のデータをグラフで確認できます。データのダウンロードも可能です。

.. image:: img/dashboard_history.png
  :width: 90%


Log（ログ）
--------------

ログページでは、現在動作中の pironman5 サービスのログを確認できます。pironman5 には複数のサブサービスが含まれており、それぞれにログがあります。閲覧したいログを選択すると、右側に内容が表示されます。何も表示されない場合は、ログが存在しない可能性があります。

* 各ログの最大サイズは10MBで、超えると次のログファイルが自動生成されます。
* 同一サービスのログは最大10ファイルまで保存され、それを超えると古いものから自動で削除されます。
* ログ表示画面には、ログレベル選択、キーワード検索、 **Line Wrap** 、 **Auto Scroll** 、 **Auto Update** などの便利なツールがあります。
* ログはローカルにダウンロードすることも可能です。

.. image:: img/dashboard_log.png
  :width: 90%


Settings（設定）
-------------------

画面右上に設定メニューがあります。

.. note::

    変更を加えた後は、画面下部の **SAVE** ボタンをクリックして保存してください。

.. image:: img/dashboard_settings.png
  :width: 90%


* **Dark Mode**：ライトテーマとダークテーマの切り替え。設定はブラウザのキャッシュに保存されます。ブラウザを変更したりキャッシュを削除するとデフォルトに戻ります。
* **Temperature Unit**：表示される温度の単位を設定します。
* **Fan Mode**：GPIOファンの動作モードを設定できます。設定に応じて、ファンが起動する温度が変わります。

    * **Quiet**：70°Cで起動
    * **Balanced**：67.5°Cで起動
    * **Cool**：60°Cで起動
    * **Performance**：50°Cで起動
    * **Always On**：常時オン

たとえば、 **Performance** モードに設定した場合、GPIOファンは50°Cで作動を開始します。

設定を保存した後、CPUの温度が50°Cを超えると、Dashboard上の **GPIO Fan State** がONに変わり、GPIOファンが回転を始めます。

  .. image:: img/dashboard_rgbfan_on.png
    :width: 300


* **RGB Brightness**：スライダーでRGB LEDの明るさを調整できます。
* **RGB Color**：RGB LEDのカラーを指定します。
* **RGB Style**：RGB LEDの表示モードを選択できます。モードは **Solid**、 **Breathing**、 **Flow**、 **Flow_reverse**、 **Rainbow**、 **Rainbow Reverse**、 **Hue Cycle** などがあります。

.. note::

  **RGB Style** を **Rainbow**、 **Rainbow Reverse**、 **Hue Cycle** に設定した場合、RGBカラーの個別設定はできません。


* **RGB Speed**：RGB LEDの変化スピードを設定します。


**コアファンについて**

コアファンは、ラズベリーパイ5の専用4ピンCPUファン端子に接続します。その標準の制御方式は、ファームウェアによって管理され、CPU温度に基づく多段階の知的回転数調整機構です。つまり、公式または互換性のあるCPUファンを正しく接続して使用する場合、システムはCPU温度の変化に応じてファン回転数を自動的に調整し（50℃以上で作動を開始）、利用者の手動介入は一切不要です。