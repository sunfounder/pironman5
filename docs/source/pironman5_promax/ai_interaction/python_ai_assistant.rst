.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _ai_voice_assistant_car:

7. AI 语音助手
===========================

本课程将把您的 Pironman 5 Pro MAX 打造成一个 **以语音为核心的 AI 助手**\ 。  
通过提供的代码，机器人将能够：\ **等待唤醒词**\ 、使用 Vosk **识别语音并转写为文本**\ 、将内容发送到 **OpenAI LLM**\ ，并通过 **Piper TTS** **语音回复**\ 。

----

开始之前
----------------

请确保您已完成以下准备：

* :ref:`test_piper` — Piper 语音功能正常（例如可以播放 “Hello”）。  
* :ref:`test_vosk` — Vosk 语音识别在您的语言环境中可正常使用（例如 ``en-us``\ ）。  
* :ref:`py_online_llm` — 您的 **OpenAI API key** 已保存在 ``secret.py`` 中，变量名为 ``OPENAI_API_KEY``\ 。  
* Pironman 5 Pro MAX 已连接并可正常使用 **麦克风** 和 **扬声器**\ 。  
* 具备稳定的 **网络连接** （LLM 为在线服务）。

----

运行示例
---------------

.. code-block:: bash

   cd ~/sunfounder-voice-assistant/examples/
   sudo python3 voice_assistant.py

**代码使用的配置：**

* LLM：\ **OpenAI** （\ ``gpt-4o-mini``\ ）  
* TTS：\ **Piper** （\ ``en_US-ryan-low``\ ）  
* STT：\ **Vosk** （\ ``en-us``\ ）  
* 唤醒词： ``"hey buddy"``  
* 键盘输入：\ **已启用** （可选的手动输入方式）  
* 图像模式：\ **已启用** （\ ``WITH_IMAGE=True``\ ）—— 如果未来需要使用图像功能，需要支持多模态的 LLM

**运行流程：**

1. 助手启动后，会显示包含唤醒词的欢迎信息。  
2. 系统持续监听 **“hey buddy”** 唤醒词。  
3. 被唤醒后，您的语音将被转写为文本（Vosk → text）。  
4. 文本被发送到 **OpenAI（gpt-4o-mini）** 生成回复。  
5. 回复内容通过 **Piper** （\ ``en_US-ryan-low``\ ）转换为语音并播放。

**示例交互**

.. code-block:: text

   You: Hey Buddy
   Robot: Hi there!

   You: What’s the capital of Italy?
   Robot: The capital of Italy is Rome.

示例代码
-----------------

.. code-block:: python

  from sunfounder_voice_assistant.voice_assistant import VoiceAssistant
  from sunfounder_voice_assistant.llm import OpenAI as LLM
  from secret import OPENAI_API_KEY as API_KEY

  llm = LLM(
      api_key=API_KEY,
      model="gpt-4o-mini",
  )

  # Robot name
  NAME = "Buddy"

  # Enable image, need to set up a multimodal language model
  WITH_IMAGE = True

  # Set models and languages
  LLM_MODEL = "gpt-4o-mini"
  TTS_MODEL = "en_US-ryan-low"
  STT_LANGUAGE = "en-us"

  # Enable keyboard input
  KEYBOARD_ENABLE = True

  # Enable wake word
  WAKE_ENABLE = True
  WAKE_WORD = [f"hey {NAME.lower()}"]
  # Set wake word answer, set empty to disable
  ANSWER_ON_WAKE = "Hi there"

  # Welcome message
  WELCOME = f"Hi, I'm {NAME}. Wake me up with: " + ", ".join(WAKE_WORD)

  # Set instructions
  INSTRUCTIONS = f"""
  You are a helpful assistant, named {NAME}.
  """

  va = VoiceAssistant(
      llm,
      name=NAME,
      with_image=WITH_IMAGE,
      tts_model=TTS_MODEL,
      stt_language=STT_LANGUAGE,
      keyboard_enable=KEYBOARD_ENABLE,
      wake_enable=WAKE_ENABLE,
      wake_word=WAKE_WORD,
      answer_on_wake=ANSWER_ON_WAKE,
      welcome=WELCOME,
      instructions=INSTRUCTIONS,
  )

  if __name__ == "__main__":
      va.run()

**代码说明：**

* ``OpenAI(..., model="gpt-4o-mini")`` — 本课程中仅使用 **OpenAI** 作为 LLM。  
* ``NAME`` / ``WAKE_WORD`` — 用于自定义助手名称和唤醒词（例如 “Buddy” 和 “hey buddy”）。  
* ``WITH_IMAGE=True`` — 为助手启用图像模式（此处未包含图像输入/输出逻辑）。  
* ``TTS_MODEL="en_US-ryan-low"`` — 指定回复所使用的 Piper 语音模型。  
* ``STT_LANGUAGE="en-us"`` — 指定 Vosk 语音识别所使用的语言。  
* ``KEYBOARD_ENABLE=True`` — 允许在调试过程中通过键盘手动输入文本。  
* ``WELCOME`` / ``INSTRUCTIONS`` — 启动欢迎语以及助手的人设/System Prompt。  
* ``va.run()`` — 启动主循环：\ **唤醒 → 监听 → LLM 处理 → 语音播报**\ 。  


切换到其他 LLM 或 TTS
------------------------------

只需进行少量修改，您就可以轻松切换到其他 LLM、TTS 或 STT 语言：

* 支持的 LLM：

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — 查看 **Piper TTS** 支持的语言。  
* :ref:`test_vosk` — 查看 **Vosk STT** 支持的语言。  

如需切换，只需修改代码中的初始化部分：

.. code-block:: python

   from sunfounder_voice_assistant.llm import Gemini as LLM
   llm = LLM(api_key="YOUR_KEY", model="gemini-pro")

   # Set models and languages
   TTS_MODEL = "en_US-ryan-low"
   STT_LANGUAGE = "en-us"



----

故障排查
-----------------------------

* **机器人无法响应唤醒词**

  - 检查麦克风是否工作正常。  
  - 确认 ``WAKE_ENABLE = True``\ 。  
  - 根据您的发音调整唤醒词。  
  - 尽量减少背景噪音，并清晰发音。

* **扬声器没有声音输出**

  - 检查 TTS 模型名称是否正确（例如 ``en_US-ryan-low``\ ）。  
  - 手动测试 Piper 或 Espeak 是否可正常工作。  
  - 检查扬声器连接和音量设置。

* **API key 报错或请求超时**

  - 检查 ``secret.py`` 中配置的 key 是否正确。  
  - 确保网络连接稳定。  
  - 确认所使用的 LLM 模型受支持（例如 ``gpt-4o-mini``\ ）。

* **唤醒词可用，但没有回复**

  - 检查 STT 语言是否与您的口音匹配。  
  - 确认模型已正确下载。  
  - 尝试输出调试日志，以确认 STT 是否正在正常运行。

* **TTS 正常，但 LLM 没有回复**

  - 检查 API key 是否有效。  
  - 确认模型名称和 LLM 配置是否正确。  
  - 确保设备已连接互联网。 