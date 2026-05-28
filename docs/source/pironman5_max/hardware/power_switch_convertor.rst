.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


電源スイッチ変換モジュール
==============================

これは、Raspberry Pi 5 の電源スイッチ機能を外部に拡張するためのモジュールです。

.. image:: img/power_switch_conventor.jpeg

**電源ボタンの追加**

* Raspberry Pi 5 には、RTCバッテリーコネクタと基板端の間に **J2** ジャンパーがあり、ここにノーマルオープン（NO）タイプのモーメンタリースイッチを接続することで、外部電源ボタンとして利用できます。短く押すことで、オンボードの電源ボタンと同じ動作をします。

   .. image:: img/pi5_j2.jpg

* Pironman 5 には、 **Power Switch Converter** が搭載されており、 **J2** の信号を2つのポゴピンを介して外部電源ボタンに拡張します。

   .. image:: img/power_switch_convertor.png

* これにより、Raspberry Pi 5 を外部の電源ボタンで起動・停止できるようになります。

   .. image:: img/pironman_button.JPG

**電源操作について**

Raspberry Pi 5 に初めて電源を接続した際、自動的に電源が入り、OSが起動します。

Raspberry Pi Desktop 環境を使用している場合、電源ボタンを短く押すと、シャットダウンメニューが表示され、シャットダウン、再起動、ログアウトのいずれかを選択できます。再度ボタンを押すことでもシャットダウンが開始されます。

.. image:: img/button_shutdown.png

**シャットダウン**

* **Raspberry Pi OS Desktop** を使用している場合は、電源ボタンをすばやく2回押すとシャットダウンが実行されます。
* **Raspberry Pi OS Lite** （デスクトップなし）では、ボタンを1回押すことでシャットダウンが開始されます。
* 強制シャットダウンが必要な場合は、ボタンを長押ししてください。


**起動方法**

* Raspberry Pi がシャットダウン状態で電源が供給されている場合は、ボタンを1回押すことで起動します。

.. note::

    システムがシャットダウンボタンをサポートしていない場合でも、ボタンを5秒間長押しすれば強制シャットダウンが可能です。シャットダウン状態からの起動は、ボタンを1回押すことで行えます。

