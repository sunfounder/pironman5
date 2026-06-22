.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


1. 使用 Espeak 和 Pico2Wave 进行文本转语音（TTS）
===================================================

在本课程中，我们将使用 Raspberry Pi 自带的两种文本转语音（TTS）引擎 —— **Espeak** 和 **Pico2Wave** —— 让 Pironman 5 Pro MAX “开口说话”。

这两种引擎都非常简单，并且可以离线运行，但它们的声音效果有明显差异：

* **Espeak**\ ：非常轻量且速度快，但声音较为机械化。可以调整语速、音调和音量等参数。  
* **Pico2Wave**\ ：语音听起来比 Espeak 更自然、更流畅，但可配置选项较少。  

通过本实验，您可以直观地听到 **语音质量** 和 **功能特性** 的差异。

----

1. 测试 Espeak
--------------------

Espeak 是 Raspberry Pi OS 自带的轻量级 TTS 引擎。  
虽然语音听起来比较机械，但它的可配置性很高，可以调节音量、音调、语速等参数。

**运行程序**

  .. code-block:: bash
  
      cd ~/sunfounder-voice-assistant/examples
      sudo python3 tts_espeak.py

  * 您将听到 Pironman 5 Pro MAX 说：“Hello! I'm Espeak TTS.”
  * 您可以尝试在代码中修改参数，观察 ``amp``\ 、 ``speed``\ 、 ``gap`` 和 ``pitch`` 对声音效果的影响。

**代码**

.. code-block:: python
  
  from sunfounder_voice_assistant.tts import Espeak

  # Create Espeak TTS instance
  tts = Espeak()
  # Set amplitude 0-200, default 100
  tts.set_amp(200)
  # Set speed 80-260, default 150
  tts.set_speed(150)
  # Set gap 0-200, default 1
  tts.set_gap(1)
  # Set pitch 0-99, default 80
  tts.set_pitch(80)

  tts.say("Hello! I’m Espeak TTS.")

**代码说明：**

* ``tts.set_amp()`` — 控制音量（0–200）。  
* ``tts.set_speed()`` — 调整语速（80–260）。  
* ``tts.set_gap()`` — 设置单词之间的停顿（0–200）。  
* ``tts.set_pitch()`` — 设置音调（0–99）。  
* ``tts.say()`` — 将文本转换为语音并播放。

💡 **提示：**  
尝试提高音调和语速，可以让机器人听起来更活泼；降低音调和语速，则会显得更沉稳。

----


2. 测试 Pico2Wave
---------------------

与 Espeak 相比，Pico2Wave 可以生成 **更自然、更接近人声的语音**\ 。  
它的使用非常简单，但灵活性较低 —— 您只能 **更改语言**\ ，而无法调整音调、语速或音量。  
因此，当您希望获得清晰流畅的语音效果且无需复杂配置时，Pico2Wave 是一个不错的选择。

**运行程序**

  .. code-block:: bash
  
      cd ~/sunfounder-voice-assistant/examples
      sudo python3 tts_pico2wave.py

* 您将听到 Pironman 5 Pro MAX 说：“Hello! I'm Pico2Wave TTS.”  
* 您可以尝试更改语言（例如 ``es-ES`` 表示西班牙语），听听语音效果的变化。

**代码**

.. code-block:: python

  from sunfounder_voice_assistant.tts import Pico2Wave

  # Create Pico2Wave TTS instance
  tts = Pico2Wave()

  # Set the language
  tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT
  
  # Quick hello (sanity check)
  tts.say("Hello! I'm Pico2Wave TTS.")

**代码说明：**

* ``tts.set_lang()`` — 设置语音合成的输出语言。

  - ``en-US`` （默认）
  - ``en-GB``
  - ``de-DE``
  - ``es-ES``
  - ``fr-FR``
  - ``it-IT``

* ``tts.say()`` — 将文本转换为语音并立即播放。


----

故障排查
-------------------

* **运行 Espeak 或 Pico2Wave 时没有声音**

  * 检查扬声器或耳机是否正确连接，并确认音量未被静音。  
  * 在终端中运行以下命令进行快速测试：

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  如果没有声音，则说明问题出在音频输出，而不是 Python 代码。

* **Espeak 的声音过快或过于机械**

  * 尝试在代码中调整参数：

    .. code-block:: python

       tts.set_speed(120)   # 降低语速
       tts.set_pitch(60)    # 调整音调

* **运行代码时出现 Permission denied**

  * 尝试使用 ``sudo`` 运行：

    .. code-block:: bash

       sudo python3 test_tts_espeak.py

对比：Espeak 与 Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - 特性
     - Espeak
     - Pico2Wave
   * - 语音质量
     - 机械化、合成感明显
     - 更自然、更接近人声
   * - 语言支持
     - 默认支持英语
     - 支持语言较少，但覆盖常见语言
   * - 可调节性
     - 是（语速、音调等）
     - 否（只能设置语言）
   * - 性能
     - 非常快、资源占用低
     - 稍慢，占用资源更多