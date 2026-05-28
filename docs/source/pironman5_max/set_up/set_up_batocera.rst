.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_batocera_max:

Batocera.linuxのセットアップ
=========================================================

Batocera.linux OSをインストールした場合、SSH経由でこのシステムにリモートログインし、以下の手順で設定を完了させることができます。

#. システムが起動したら、sshでPironman5にリモート接続します。Windowsでは **Powershell** を開き、Mac OS XやLinuxでは **Terminal** を使用してください。

   .. image:: img/batocera_powershell.png
      :width: 90%


#. Batoceraシステムのデフォルトホスト名は ``batocera``、ユーザー名は ``root``、パスワードは ``linux`` です。そのため、以下のように入力してログインできます： ``ssh root@batocera.local`` パスワードには ``linux`` を入力してください。

   .. image:: img/batocera_login.png
      :width: 90%

#. 次に、以下のコマンドを実行して設定メニューに入ります： ``/etc/init.d/S92switch setup``

   .. image:: img/batocera_configure.png  
      :width: 90%

#. ↓キーを使って最後までスクロールし、 **Pironman5** サービスを選択・有効化してください。

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Pironman5サービスを有効化したら、 **OK** を選択します。

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. ``reboot`` コマンドを実行して、Pironman5 を再起動します。

   .. code-block:: shell

      reboot

#. 再起動後、自動的に ``pironman5.service`` が起動します。Pironman 5 MAXの主な構成は以下の通りです：

   * OLEDスクリーンには、CPU・RAM・ディスク使用量・CPU温度・Raspberry PiのIPアドレスが表示されます。
   * 4つのWS2812 RGB LEDは、青色のブリージングモードで点灯します。
   * GPIOファンはデフォルトで **バランス** モードに設定されています。作動温度の調整に関する情報は、:ref:`cc_control_fan_max` を参照してください。

Pironman 5 MAXにディスプレイ、ゲームコントローラー、ヘッドホンなどを接続し、ゲームの世界に没入しましょう。


.. note::

   この時点で、Pironman 5 MAX のセットアップが正常に完了し、使用可能な状態になっています。
   
   各コンポーネントを高度に制御する方法については、:ref:`max_view_control_commands` を参照してください。
