.. note:: 

    こんにちは！SunFounder の Facebook コミュニティ「Raspberry Pi & Arduino & ESP32 愛好者グループ」へようこそ！Raspberry Pi、Arduino、ESP32 に情熱を注ぐ仲間たちと一緒に、これらの技術をより深く探究しましょう。

    **参加するメリット**

    - **専門サポート**：購入後の技術的課題を、コミュニティとサポートチームが連携してサポートします。
    - **学びと共有**：チュートリアルやヒントを通じてスキルを向上。
    - **新製品の先行プレビュー**：製品発表や開発中の情報をいち早く入手できます。
    - **限定割引**：新製品に対する会員限定の特別割引をご利用いただけます。
    - **イベント＆プレゼント企画**：キャンペーンやプレゼントに参加してお得な体験を。

    👉 一緒に創造し、学びを深めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

.. _max_view_control_dashboard:

ダッシュボードからの表示と制御
=========================================

``pironman5`` モジュールのインストールが完了すると、 ``pironman5.service`` は再起動時に自動で起動します。

ブラウザで ``http://<ip>:34001`` にアクセスすると、Raspberry Pi の情報を確認したり、RGB の設定、ファンの制御などが行える監視ページが表示されます。

このページには **ダッシュボード**、 **履歴**、 **ログ**、 **設定** の各セクションがあります。

.. image:: img/dashboard_tab.png
  :width: 90%
  

ダッシュボード
-----------------------

ダッシュボードには、Raspberry Pi の状態を確認できる複数のカードが表示されます：

* **ファン**：CPU 温度と PWM ファンの回転速度を表示。 **GPIO Fan State** は左右の RGB ファンの状態を示します。現在の温度では、RGB ファンはオフです。

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%


* **ストレージ**：各パーティションの使用量と空き容量を含めたストレージ情報を表示します。

  .. image:: img/dashboard_storage.png
    :width: 90%


* **メモリ**：RAM の使用量と使用率を表示します。

  .. image:: img/dashboard_memory.png
    :width: 90%


* **ネットワーク**：接続中のネットワーク種別、アップロード／ダウンロード速度を表示します。

  .. image:: img/dashboard_network.png
    :width: 90%


* **プロセッサー**：4コアの状態、動作クロック、CPU 使用率を含むパフォーマンス情報を表示します。

  .. image:: img/dashboard_processor.png
    :width: 90%


履歴
--------------

履歴ページでは、過去のデータを確認できます。左側のサイドバーで確認したい項目を選択し、表示する期間を指定するとその期間のデータを表示・ダウンロードできます。

.. image:: img/dashboard_history1.png
  :width: 90%
  
.. image:: img/dashboard_history2.png
  :width: 90%

ログ
------------

ログページでは、現在動作中の pironman5 サービスに関連するログを確認できます。複数のサブサービスがあり、それぞれのログを個別に表示可能です。

* 各ログは10MBの固定サイズで保存され、超過時には新しいログファイルが作成されます。
* 同一サービスに対して最大10ファイルまで保存され、超えると古いログは自動で削除されます。
* ログ表示エリアにはフィルタ機能があり、ログレベルの選択、キーワード検索、 **Line Wrap**、 **Auto Scroll** 、 **Auto Update** などのツールを使用できます。
* ログはローカルにダウンロードも可能です。

.. image:: img/dashboard_log1.png
  :width: 90%
  
.. image:: img/dashboard_log2.png
  :width: 90%


設定
-----------------

画面右上にある設定メニューから、表示や動作に関する各種設定をカスタマイズできます。変更内容は自動で保存され、必要に応じて [CLEAR] ボタンで履歴データをクリア可能です。

.. image:: img/Dark_mode_and_Temperature.jpg
  :width: 600

* **ダークモード**：ライト／ダークテーマの切り替え。テーマ設定はブラウザのキャッシュに保存されます。ブラウザを変えたりキャッシュを削除すると、デフォルトのライトテーマに戻ります。
* **温度単位**：温度の表示単位を設定。

**OLED スクリーンの設定**

.. image:: img/OLED_Sreens.jpg
  :width: 600

* **OLED 有効化**：OLED 表示の有効／無効を設定
* **OLED ディスク**：表示するディスクを設定
* **OLED ネットワークインターフェース**：

  * **all**：Ethernet IP と Wi-Fi IP を順番に表示
  * **eth0**：Ethernet IP のみを表示
  * **wlan0**：Wi-Fi IP のみを表示

* **OLED 回転**：OLED 表示の回転角度を設定

**RGB LED の設定**

.. image:: img/RGB_LEDS.jpg
  :width: 600

* **RGB 有効化**：RGB LED のオン／オフ
* **RGB カラー**：RGB LED の色を設定
* **RGB 明るさ**：スライダーで明るさを調整
* **RGB スタイル**：LED の点灯モードを選択（ **Solid**, **Breathing**, **Flow**, **Flow_reverse**, **Rainbow**, **Rainbow Reverse**, **Hue Cycle**）

  .. note::

     **RGB スタイル** に **Rainbow**, **Rainbow Reverse**, **Hue Cycle** を選択した場合は、色の指定ができません。

* **RGB スピード**：RGB の変化速度を設定

**RGB ファンの設定**

.. image:: img/RGB_FAN2.png
  :width: 600

* **GPIO ファンモード**：2基の RGB ファンの動作モードを設定できます。

    * **Quiet**：70℃で起動
    * **Balanced**：67.5℃で起動
    * **Cool**：60℃で起動
    * **Performance**：50℃で起動
    * **常時オン**：常にファンが回転

たとえば、 **Performance** モードを選択すると、CPU温度が50℃を超えたときにRGBファンが起動します。

保存後、CPU 温度が 50℃ を超えると、ダッシュボード上の **GPIO Fan State** が ON に変わり、側面の RGB ファンが回転を始めます。

.. image:: img/dashboard_rgbfan_on.png
  :width: 300

