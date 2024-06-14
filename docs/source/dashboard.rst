.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _view_control_dashboard:

5. ダッシュボードからの表示と制御
=========================================

``pironman5`` モジュールを正常にインストールした後、再起動すると自動的に ``pironman5.service`` が開始されます。

次に、ブラウザで監視ページを開いて、Raspberry Piの情報を確認し、RGBを設定し、ファンを制御するなどができます。ページのリンクは ``http://<ip>:34001`` です。

このページには、 **Dashboard**、 **History**、 **Log**、 **Settings** ページがあります。

.. image:: img/dashboard_tab.png

ダッシュボード
-----------------------

Raspberry Piの関連ステータスを表示するための複数のカードがあります。以下の項目が含まれます：

* **Fan**: Raspberry PiのCPU温度とPWMファンスピードを表示します。 **GPIO Fan State** は、2つの側面にあるRGBファンの状態を示します。現在の温度では、2つのRGBファンはオフになっています。

.. image:: img/dashboard_pwm_fan.png
    :width: 600
    :align: center

* **Storage**: Raspberry Piのストレージ容量を表示し、使用済みと利用可能なスペースを示すさまざまなディスクパーティションを表示します。

.. image:: img/dashboard_storage.png
    :width: 600
    :align: center

* **Memory**: Raspberry PiのRAM使用量とパーセンテージを表示します。

.. image:: img/dashboard_memory.png
    :width: 600
    :align: center

* **Network**: 現在のネットワーク接続タイプ、アップロード速度、ダウンロード速度を表示します。

.. image:: img/dashboard_network.png
    :width: 600
    :align: center

* **Processor**: Raspberry PiのCPUパフォーマンスを表示し、4つのコアの状態、動作周波数、CPU使用率を含みます。

.. image:: img/dashboard_processor.png
    :width: 600
    :align: center

履歴
--------------

履歴ページでは、過去のデータを表示できます。左側のサイドバーで表示したいデータを選択し、時間範囲を選択すると、その期間のデータが表示され、ダウンロードすることもできます。

.. image:: img/dashboard_history.png
    :width: 700
    :align: center

ログ
------------

ログページは、現在実行中のPironman5サービスのログを表示するためのものです。Pironman5サービスには複数のサブサービスが含まれており、それぞれに独自のログがあります。表示したいログを選択すると、右側にログデータが表示されます。空白の場合、ログ内容がない可能性があります。

* 各ログのサイズは10MBに固定されています。このサイズを超えると、2つ目のログが作成されます。
* 同じサービスのログの数は10に制限されています。この制限を超えると、最も古いログが自動的に削除されます。
* 右側のログエリアにはフィルターツールがあります。ログレベルを選択したり、キーワードでフィルタリングしたり、 **Line Wrap**、 **Auto Scroll**、 **Auto Update** などの便利なツールを使用できます。
* ログをローカルにダウンロードすることもできます。

.. image:: img/dashboard_log.png
    :width: 600
    :align: center

設定
-----------------

ページの右上隅に設定メニューがあります。

.. note::
    
    修正後、設定を保存するには、下部の **SAVE** ボタンをクリックする必要があります。

.. image:: img/dashboard_settings.png
    :width: 600
    :align: center

* **Dark Mode**: ライトモードとダークモードのテーマを切り替えます。テーマのオプションはブラウザのキャッシュに保存されます。ブラウザを変更したり、キャッシュをクリアしたりすると、デフォルトのライトテーマに戻ります。
* **Temperature Unit**: システムが表示する温度単位を設定します。
* **Fan Mode**: 2つのRGBファンの動作モードを設定できます。これらのモードは、RGBファンが作動する条件を決定します。

    * **Quiet**: RGBファンは70°Cで作動します。
    * **Balanced**: RGBファンは67.5°Cで作動します。
    * **Cool**: RGBファンは60°Cで作動します。
    * **Performance**: RGBファンは50°Cで作動します。
    * **Always On**: RGBファンは常に作動します。

    例えば、 **Performance** モードに設定すると、RGBファンは50°Cで作動します。

    保存後、CPU温度が50°Cを超えると、ダッシュボードの **GPIO Fan State** がONに変わり、側面のRGBファンが回転し始めます。

    .. image:: img/dashboard_rgbfan_on.png
        :width: 300
        :align: center

* **RGB Brightness**: スライダーでRGB LEDの明るさを調整できます。
* **RGB Color**: RGB LEDの色を設定します。
* **RGB Style**: RGB LEDの表示モードを選択します。オプションには **Solid**、 **Breathing**、 **Flow**、 **Flow_reverse**、 **Rainbow**、 **Rainbow Reverse**、 **Hue Cycle** があります。

.. note::

   **RGB Style** を **Rainbow**、 **Rainbow Reverse**、 **Hue Cycle** に設定すると、色を設定することはできません。

* **RGB Speed**: RGB LEDの変化速度を設定します。
