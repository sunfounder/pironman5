.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _view_control_dashboard:

ダッシュボードからの表示と操作
=========================================

``pironman5`` モジュールを正常にインストールすると、再起動時に ``pironman5.service`` が自動的に起動します。

次に、ブラウザでモニタリングページを開き、Raspberry Piの情報を確認したり、RGBを設定したり、ファンを制御したりできます。このページのリンクは ``http://<ip>:34001`` です。

このページには、 **ダッシュボード** 、 **履歴** 、 **ログ** 、 **設定** ページがあります。

.. image:: img/dashboard_home.png


ダッシュボード
-----------------------

Raspberry Piの状態を確認できる複数のカードが用意されています：

* **温度**: Raspberry PiのCPU/GPU温度とCPUファン速度を表示します。 **GPIO Fan State** は、2つの側面GPIOファンの状態を示します。

  .. image:: img/dashboard_tem.png
    :width: 90%

* **ストレージ**: Raspberry Piのストレージ容量を表示し、使用済みと空き容量を各ディスクパーティションごとに示します。

  .. image:: img/dashboard_storage.png
    :width: 90%

* **メモリ**: Raspberry PiのRAM使用量と使用率を表示します。

  .. image:: img/dashboard_memory.png
    :width: 90%


* **ネットワーク**: 現在のネットワーク接続タイプ、アップロード速度、ダウンロード速度を表示します。

  .. image:: img/dashboard_network.png
    :width: 90%


* **プロセッサ**: Raspberry PiのCPUパフォーマンスを表示します。これには、4つのコアの状態、動作周波数、CPU使用率が含まれます。

  .. image:: img/dashboard_processor.png
    :width: 90%


履歴
--------------

履歴ページでは、過去のデータを表示できます。左のサイドバーで表示したいデータを選択し、時間範囲を指定すると、その期間のデータが表示されます。また、ダウンロードも可能です。

.. image:: img/dashboard_history1.png
  :width: 90%

.. image:: img/dashboard_history2.png
  :width: 90%

ログ
------------

ログページでは、Pironman5サービスの実行ログを表示します。

* ログエントリはレベル（Debug、Info、Warning、Error、Critical）でフィルタリングできます。
* ログファイルをローカルにダウンロードすることもできます。

.. image:: img/dashboard_log.png
  :width: 90%

設定
------------

設定ページでは、ダッシュボードの表示、システム設定、OLEDスクリーン、RGBライティング、ファンの動作をカスタマイズできます。また、MACアドレスやIPアドレスなどのネットワーク情報も表示されます。

.. image:: img/dashboard_setting.png
    :width: 600


* **インターフェース**

  ダッシュボードの外観と表示動作を設定します。

  .. image:: img/dashboard_setting_interface.png
      :width: 600

  * **ダークモード**: ダークテーマを有効または無効にします。
  * **アンマウントされたディスクを表示**: ストレージカードにアンマウントされたストレージデバイスを表示します。
  * **すべてのコアを表示**: プロセッサカードにすべてのCPUコアを表示します。
  * **カードレイアウト**: ダッシュボードのカードレイアウトをカスタマイズします。
  * **温度単位**: 摂氏と華氏を切り替えます。
  * **Web UIバージョン**: 現在のダッシュボードバージョンを表示します。


* **OLED**

  OLEDスクリーンの表示と動作を設定します。

  .. image:: img/dashboard_setting_oled.png
      :width: 600

  * **OLED有効化**: OLEDスクリーンを有効または無効にします。
  * **OLED回転**: OLED表示を ``0°`` と ``180°`` の間で回転します。
  * **OLEDスリープタイムアウト**: OLEDスクリーンが自動的に消灯するまでの時間を設定します。
  * **OLEDページ**: OLEDスクリーンに表示するページを設定し、表示順序を調整します。

    利用可能なページ：

    * **IPアドレス**: すべての物理ネットワークインターフェースのIPアドレスを表示します。
    * **ディスク使用量**: すべてのディスクのディスク使用量情報を表示します。
    * **パフォーマンスメトリクス**: CPU使用率、CPU温度、RAM使用量、ファン速度を表示します。
    * **システムミックス**: CPU使用率、CPU温度、IPアドレスを表示します。


* **RGB**

  RGB LEDのライティング効果と動作を設定します。

  .. image:: img/dashboard_setting_rgb.png
      :width: 600

  * **RGB有効化**: RGB LEDを有効または無効にします。
  * **RGBカラー**: RGB LEDの色を設定します。
  * **RGB明るさ**: RGB LEDの明るさを調整します。
  * **RGBスタイル**: RGBライティング効果を選択します。 ``None``、 ``Solid``、 ``Breathing``、 ``Flow``、 ``Flow Reverse``、 ``Rainbow``、 ``Rainbow Reverse``、 ``Hue Cycle`` から選択できます。
  * **RGB速度**: 選択したRGB効果のアニメーション速度を調整します。
  * **RGB LED数**: アクティブなRGB LEDの数を設定します。


* **GPIOファン**

  2つのGPIOファンの動作モードとLED動作を設定します。

  .. image:: img/dashboard_setting_fan.png
      :width: 600

  * **ファンLED**

    GPIOファンのRGBライティング動作を制御します。

    * **ON**: ファンLEDは常に点灯します。
    * **OFF**: ファンLEDは消灯します。
    * **FOLLOW**: ファンLEDはシステムのRGBライティング効果に追随します。

  * **GPIOファンモード**

    選択したモードは、GPIOファンが作動する条件を決定します。

    * **静音**: GPIOファンは70°Cで作動します。
    * **バランス**: GPIOファンは67.5°Cで作動します。
    * **冷却**: GPIOファンは60°Cで作動します。
    * **パフォーマンス**: GPIOファンは50°Cで作動します。
    * **常時オン**: GPIOファンは常に作動します。


* **システム**

  システムの動作を設定し、デバイス情報を表示します。

  .. image:: img/dashboard_setting_system.png
      :width: 600

  * **デバッグレベル**: Pironman 5サービスのログレベルを設定します。
  * **MACアドレス**: Raspberry PiのネットワークインターフェースのMACアドレスを表示します。
  * **IPアドレス**: Raspberry PiのネットワークインターフェースのIPアドレスを表示します。
  * **履歴保持期間**: 履歴データを保存する日数を設定します。
  * **すべてのデータをクリア**: 記録されたすべての履歴データを消去します。
  * **再起動**: ダッシュボードからリモートでRaspberry Piを再起動します。
  * **シャットダウン**: ダッシュボードからリモートでRaspberry Piを安全にシャットダウンします。
