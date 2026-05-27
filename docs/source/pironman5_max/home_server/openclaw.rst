


.. _openclaw_5_max:


.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw
   :end-before: end_using_openclaw


让 OpenClaw 操作 Pironman5 Max
----------------------------------------------

为了让 OpenClaw 能够操作 Pironman5 Max，我们需要安装 Pironman5 Max 技能。

1.  确保你已经安装了 Pironman5 Max。如果没有，请参考 :ref:`install_pironman5_module_max`。

2.  在终端中运行以下命令：

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-max-skill/ ~/.openclaw/skills/pironman5-max-skill/

3.  现在你可以在 ``openclaw tui`` 中操作 Pironman5 Max 了。尝试在 TUI 中发送命令，例如尝试打开机箱上的 LED 灯、改变它们的颜色，或者让摄像头拍照。你甚至可以告诉它你有一个连接到 GPIO17 的 DHT11 模块，让它告诉你温度。

    .. note:: 如果 OpenClaw 仍然无法识别你导入的技能，请提醒它进行 rsync。

-------------------------------------------------------------




.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_telegram
   :end-before: end_using_openclaw_telegram

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_faq
   :end-before: end_using_openclaw_faq