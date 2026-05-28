.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _openclaw_5_max:


.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw
   :end-before: end_using_openclaw

OpenClaw に Pironman5 Max を操作させる
----------------------------------------------

OpenClaw に Pironman5 Max を操作させるには、Pironman5 Max スキルをインストールする必要があります。

1.  Pironman5 Max がすでにインストールされていることを確認してください。インストールされていない場合は、:ref:`install_pironman5_module_max`. を参照してください。

2.  ターミナルで次のコマンドを実行します：

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-max-skill/ ~/.openclaw/skills/pironman5-max-skill/

3.  これで、 ``openclaw tui`` で Pironman5 Max を操作できるようになります。TUI でコマンドを送信してみてください。例えば、ケースの LED ライトをオンにしたり、色を変更したり、カメラで写真を撮らせたりしてみてください。GPIO17 に DHT11 モジュールが接続されていることを伝えて、温度を教えてもらうこともできます。

   .. note:: それでも OpenClaw がインポートしたスキルを認識できない場合は、rsync するように促してみてください。


-------------------------------------------------------------




.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_telegram
   :end-before: end_using_openclaw_telegram

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_faq
   :end-before: end_using_openclaw_faq