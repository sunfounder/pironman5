.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _promax_openclaw_5_promax:


.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw
   :end-before: end_using_openclaw
   
让 OpenClaw 操作 Pironman5 Pro MAX
----------------------------------------------

要让 OpenClaw 能够操作 Pironman5 Pro MAX，需要安装 Pironman5 Pro MAX 的技能（skill）。

1. 确保你已经安装了 Pironman5 Pro MAX。如果尚未安装，请参考 :ref:`install_pironman5_module_promax`。

2. 在终端中运行以下命令：

.. code-block:: bash

   mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-promax-skill/ ~/.openclaw/skills/pironman5-promax-skill/

3. 现在你可以在 ``openclaw tui`` 中操作 Pironman5 Pro MAX。尝试在 TUI 中发送指令，例如开启机箱 LED 灯、改变灯光颜色，或让摄像头拍照。你甚至可以告诉它你在 GPIO17 上连接了一个 DHT11 模块，让它读取并告诉你当前温度。

.. note::
   如果 OpenClaw 仍然无法识别你导入的技能，可以提醒它执行 rsync。


-------------------------------------------------------------

语音交互
----------------------------------------------------

Pro MAX 机箱内置麦克风和扬声器，因此可以通过语音与 OpenClaw 进行交互。要实现这一功能，需要安装 ``sunfounder-voice-assistant`` 软件包。

``sunfounder-voice-assistant`` 软件包提供了操作 Pironman 5 Pro MAX 硬件所需的库和工具。

运行以下安装命令：

.. code-block:: bash

   sudo apt install portaudio19-dev
   sudo pip install --break git+https://github.com/sunfounder/sunfounder-voice-assistant.git

通过该软件包，你可以体验文本转语音（TTS）、语音转文本（STT）以及大语言模型（LLM），让 Pironman 5 Pro MAX 能够说话、听你讲话，甚至像智能机器人一样与你聊天。

然后运行以下示例程序：

.. code-block:: bash

   python3 ~/pironman5/openclaw_voice.py

重启系统。之后你就可以使用 Pironman5 Pro MAX 的语音功能与 OpenClaw 进行交互。尝试说 “Hi Amy” 来唤醒它。


.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_telegram
   :end-before: end_using_openclaw_telegram

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_faq
   :end-before: end_using_openclaw_faq