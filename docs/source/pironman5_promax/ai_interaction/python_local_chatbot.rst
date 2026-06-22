.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


6. 本地语音聊天机器人
===========================

在本课程中，您将把之前学习的所有内容整合起来 —— **语音识别（STT）**\ 、  
**文本转语音（TTS）** 以及 **本地 LLM（Ollama）** —— 构建一个完全离线运行的 **语音聊天机器人**\ ，  
使其能够在您的 Pironman 5 Pro MAX 上运行。

其工作流程非常简单：

#. **Listen** — 麦克风采集您的语音，并通过 **Vosk** 将其转写为文本。  
#. **Think** — 文本被发送到运行在 Ollama 上的本地 **LLM** （例如 ``llama3.2:3b``\ ）。  
#. **Speak** — 聊天机器人通过 **Piper TTS** 以语音形式进行回答。  

这样，您就可以打造一个 **免手动操作的对话机器人**\ ，能够实时理解并回应您的语音指令。

----

开始之前
----------------

请确保您已完成以下准备：

* 已测试 **Piper TTS** （:ref:`test_piper`），并选择了可用的语音模型。  
* 已测试 **Vosk STT** （:ref:`test_vosk`），并选择了正确的语言包（例如 ``en-us``\ ）。  
* 已在您的 Pi 或另一台计算机上安装 **Ollama** （:ref:`download_ollama`），并下载了一个模型，例如 ``llama3.2:3b`` （如果内存有限，也可以使用更小的模型，例如 ``moondream:1.8b``\ ）。

----

运行代码
--------------

#. 打开示例脚本：

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo nano local_voice_chatbot.py

#. 根据需要修改参数：

   * ``stt = Vosk(language="en-us")``\ ：将其修改为与您的口音或语言包相匹配的设置（例如 ``en-us``\ 、 ``zh-cn``\ 、 ``es``\ ）。  
   * ``tts.set_model("en_US-amy-low")``\ ：将其替换为您在 :ref:`test_piper` 中已验证可用的 Piper 语音模型。  
   * ``llm = Ollama(ip="localhost", model="llama3.2:3b")``\ ：请根据您的实际环境修改 ``ip`` 和 ``model``\ 。  

     * ``ip``\ ：如果 Ollama 运行在 **同一台 Pi** 上，请使用 ``localhost``\ 。如果 Ollama 运行在局域网中的另一台计算机上，请在 Ollama 中启用 **Expose to network**\ ，并将 ``ip`` 设置为该计算机的局域网 IP 地址。  
     * ``model``\ ：必须与您在 Ollama 中已下载并启用的模型名称完全一致。  

#. 运行脚本：

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples/
      sudo python3 local_voice_chatbot.py

#. 运行后，您将看到：

   * 机器人会先通过语音向您播放欢迎信息。  
   * 然后等待您的语音输入。  
   * Vosk 会将您的语音转写为文本。  
   * 文本会被发送到 Ollama，由其流式生成回复。  
   * 回复内容会经过清理（移除隐藏推理内容），然后由 Piper 以语音形式播报。  
   * 您可以随时按 ``Ctrl+C`` 停止程序。

----

代码
------

.. code-block:: python

   import re
   import time
   from sunfounder_voice_assistant.llm import Ollama
   from sunfounder_voice_assistant.stt import Vosk
   from sunfounder_voice_assistant.tts import Piper

   # Initialize speech recognition
   stt = Vosk(language="en-us")

   # Initialize TTS
   tts = Piper()
   tts.set_model("en_US-amy-low")

   # Instructions for the LLM
   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

   # Initialize Ollama connection
   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

   # Utility: clean hidden reasoning
   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

   def main():
       print(WELCOME)
       tts.say(WELCOME)

       try:
           while True:
               print("\n🎤 Listening... (Press Ctrl+C to stop)")

               # Collect final transcript from Vosk
               text = ""
               for result in stt.listen(stream=True):
                   if result["done"]:
                       text = result["final"].strip()
                       print(f"[YOU] {text}")
                   else:
                       print(f"[YOU] {result['partial']}", end="\r", flush=True)

               if not text:
                   print("[INFO] Nothing recognized. Try again.")
                   time.sleep(0.1)
                   continue

               # Query Ollama with streaming
               reply_accum = ""
               response = llm.prompt(text, stream=True)
               for next_word in response:
                   if next_word:
                       print(next_word, end="", flush=True)
                       reply_accum += next_word
               print("")

               # Clean and speak
               clean = strip_thinking(reply_accum)
               if clean:
                   tts.say(clean)
               else:
                   tts.say("Sorry, I didn't catch that.")

               time.sleep(0.05)

       except KeyboardInterrupt:
           print("\n[INFO] Stopping...")
       finally:
           tts.say("Goodbye!")
           print("Bye.")

   if __name__ == "__main__":
       main()

----

代码解析
-------------

**导入模块与全局初始化**

.. code-block:: python

   import re
   import time
   from sunfounder_voice_assistant.llm import Ollama
   from sunfounder_voice_assistant.stt import Vosk
   from sunfounder_voice_assistant.tts import Piper

导入之前构建的三个核心子系统：  
**Vosk** 用于语音转文本（STT），\ **Ollama** 用于本地大语言模型（LLM），\ **Piper** 用于文本转语音（TTS）。 :contentReference[oaicite:0]{index=0}



**初始化 STT（Vosk）**

.. code-block:: python

   stt = Vosk(language="en-us")

加载 Vosk 的美式英语语音识别模型。  
可以根据需要修改语言代码（例如 ``zh-cn``\ 、 ``es``\ ），以匹配对应的语音包并提高识别准确率。 :contentReference[oaicite:1]{index=1}



**初始化 TTS（Piper）**

.. code-block:: python

   tts = Piper()
   tts.set_model("en_US-amy-low")

创建 Piper 语音引擎并选择指定的语音模型。  
请选择您在 :ref:`test_piper` 中测试过的模型。质量较低的语音模型通常运行更快、占用更少 CPU。 :contentReference[oaicite:2]{index=2}



**LLM 指令与欢迎信息**

.. code-block:: python

   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

这里定义了两个关键的交互设计：

* 保持 **回答简短且直接** （有助于提高 TTS 的语音清晰度）。
* 明确禁止输出隐藏的“思维链”标签，以避免产生冗余内容。 :contentReference[oaicite:3]{index=3}



**连接 Ollama 并设置对话范围**

.. code-block:: python

   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

* ``ip="localhost"`` 表示 Ollama 服务器运行在同一台 Raspberry Pi 上。如果 Ollama 运行在局域网中的另一台设备，请填写该设备的 **LAN IP**\ ，并在 Ollama 中启用 *Expose to network*。
* ``set_max_messages(20)`` 用于限制对话历史长度。如果设备内存或响应速度受限，可以适当降低该值。 :contentReference[oaicite:4]{index=4}

**在语音播报前清理隐藏推理或标签**

.. code-block:: python

   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

有些模型可能会输出内部推理标签（例如 ``<think>…``\ ）。  
该函数会移除这些内容，从而确保 TTS **只朗读最终回答**\ 。 :contentReference[oaicite:5]{index=5}

**提示：**  
如果终端中仍然看到部分原始 token（因为启用了流式输出），该函数仍能确保 **语音播报内容保持干净**\ 。 :contentReference[oaicite:6]{index=6}



**主循环：启动问候，然后执行“听 → 思考 → 说”**

.. code-block:: python

   print(WELCOME)
   tts.say(WELCOME)

程序启动时会在终端和扬声器中输出欢迎信息。该步骤只在程序启动时执行一次。 :contentReference[oaicite:7]{index=7}



**监听语音（流式 STT，带实时部分识别）**

.. code-block:: python

   print("\n🎤 Listening... (Press Ctrl+C to stop)")

   text = ""
   for result in stt.listen(stream=True):
       if result["done"]:
           text = result["final"].strip()
           print(f"[YOU] {text}")
       else:
           print(f"[YOU] {result['partial']}", end="\r", flush=True)

* ``stream=True`` 会持续输出 **部分识别结果** （partial transcript），并在语音结束时给出 **最终识别结果**\ 。
* 最终识别文本会存储在 ``text`` 中，并在终端打印一次。 :contentReference[oaicite:8]{index=8}



**保护机制：如果没有识别到语音则跳过**

.. code-block:: python

   if not text:
       print("[INFO] Nothing recognized. Try again.")
       time.sleep(0.1)
       continue

这样可以避免向模型发送空请求，从而节省时间和计算资源。 :contentReference[oaicite:9]{index=9}



**思考阶段（LLM），使用流式输出**

.. code-block:: python

   reply_accum = ""
   response = llm.prompt(text, stream=True)
   for next_word in response:
       if next_word:
           print(next_word, end="", flush=True)
           reply_accum += next_word
   print("")

* 将识别到的文本发送到本地 LLM，并 **实时打印生成的 token**\ ，以降低响应延迟。
* 同时将完整回复累积到 ``reply_accum`` 中，以便后续处理。 :contentReference[oaicite:10]{index=10}

**说明：**  
如果您不希望显示原始 token，可以将 ``stream=False``\ ，只输出最终结果。 :contentReference[oaicite:11]{index=11}



**语音播报（先清理文本，再进行一次 TTS）**

.. code-block:: python

   clean = strip_thinking(reply_accum)
   if clean:
       tts.say(clean)
   else:
       tts.say("Sorry, I didn't catch that.")

* 在语音播放之前先清理文本中的隐藏标签，然后 **只播放一次完整回答**\ 。
* 保持单次 TTS 输出可以避免重复提示，例如 “[LLM] / [SAY]”。 :contentReference[oaicite:12]{index=12}



**退出与资源释放**

.. code-block:: python

   except KeyboardInterrupt:
       print("\n[INFO] Stopping...")
   finally:
       tts.say("Goodbye!")
       print("Bye.")

按 **Ctrl+C** 可停止程序。  
程序退出时机器人会说一声 “Goodbye!” 作为结束提示。 :contentReference[oaicite:13]{index=13}


----

故障排查与常见问题
---------------------

* **模型过大（内存错误）**

  请使用更小的模型，例如 ``moondream:1.8b``\ ，或在性能更强的计算机上运行 Ollama。  

* **Ollama 没有返回响应**

  请确保 Ollama 正在运行（执行 ``ollama serve`` 或已打开桌面应用）。如果使用远程主机，请启用 **Expose to network** 并检查 IP 地址是否正确。  

* **Vosk 无法识别语音** 

  请确认麦克风工作正常。如有需要，可尝试使用其他语言包（例如 ``zh-cn``\ 、 ``es`` 等）。  

* **Piper 没有声音或出现错误**  

  请确认所选择的语音模型已下载，并已在 :ref:`test_piper` 中成功测试。  

* **回答过长或偏离主题**

  可以修改 ``INSTRUCTIONS``\ ，添加：\ **“Keep answers short and to the point.”**  


