.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_batocera:

Batocera.linuxのセットアップ
=========================================================

Batocera.linux OSをインストールした場合、SSH経由でこのシステムにリモートログインし、以下の手順に従って設定を完了することができます。

#. システムが起動したら、SSHを使用してPironman5にリモート接続します。Windowsでは **Powershell** を、Mac OS XやLinuxでは **Terminal** を直接開いてください。

   .. image:: img/batocera_powershell.png
      :width: 90%
      

#. Batoceraシステムのデフォルトホスト名は ``batocera`` 、デフォルトユーザー名は ``root`` 、パスワードは ``linux`` です。そのため、 ``ssh root@batocera.local`` と入力し、パスワード ``linux`` を入力してログインできます。

   .. image:: img/batocera_login.png
      :width: 90%

#. コマンド ``/etc/init.d/S92switch setup`` を実行して、メニュー設定ページに入ります。

   .. image:: img/batocera_configure.png  
      :width: 90%

#. 下矢印キーを使用して最後まで移動し、 **Pironman5** サービスを選択して有効化します。

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Pironman5サービスを有効化した後、 **OK** を選択します。

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. コマンド ``reboot`` を実行してPironman5を再起動します。

   .. code-block:: shell

      reboot

#. 再起動すると、 ``pironman5.service`` が自動的に起動します。ここでは、Pironman 5の主な設定を紹介します：

   * OLED画面には、CPU、RAM、ディスク使用量、CPU温度、Raspberry PiのIPアドレスが表示されます。
   * 4つのWS2812 RGB LEDが、青い呼吸モードで点灯します。
   * GPIOファンはデフォルトで **バランス** モードに設定されています。作動温度の調整に関する情報は、:ref:`cc_control_fan` を参照してください。

さあ、Pironman 5をスクリーン、ゲームコントローラー、ヘッドフォンなどに接続して、ゲームの世界に没頭しましょう。

.. note::

   この時点で、Pironman 5 のセットアップが正常に完了し、使用可能な状態になっています。
   
   各コンポーネントを高度に制御する方法については、:ref:`view_control_commands_5` を参照してください。
