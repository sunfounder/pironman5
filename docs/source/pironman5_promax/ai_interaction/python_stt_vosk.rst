.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


3. 使用 Vosk 进行语音识别（离线）
==============================================

Vosk 是一个轻量级的语音转文本（STT）引擎，支持多种语言，并可在 Raspberry Pi 上\ **完全离线运行**\ 。  
您只需在首次下载语言模型时连接网络，之后即可在无网络环境下正常使用。  

在本课程中，我们将安装并测试 Vosk，并选择合适的语言模型。  

.. _test_vosk:

测试 Vosk
--------------------------

**运行程序**

   .. code-block:: bash

      cd ~/sunfounder-voice-assistant/examples
      sudo python3 stt_vosk_stream.py

首次使用某种语言运行该程序时，Vosk 将会：

* **自动下载语言模型** （默认下载轻量版本）。  
* **输出支持的语言列表**\ 。  
* 开始通过麦克风\ **监听音频输入**\ 。

终端中将显示类似以下内容：

.. code-block:: text

         vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
         ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
         Say something

这表示：

   * 语言模型文件（\ ``vosk-model-small-en-us-0.15``\ ）已成功下载。  
   * 已输出支持的语言列表。  
   * 系统已进入监听状态——请对着 Pironman 5 Pro MAX 的麦克风说话，识别结果会显示在终端中。

**提示：**

* 将麦克风保持在 **15–30 cm** 距离内，以获得更好的识别效果。  
* 选择与您的语言和口音匹配的模型。  
* 在安静环境中使用可提高识别准确率。

**代码**

.. code-block:: python

   from sunfounder_voice_assistant.stt import Vosk as STT

   stt = STT(language="en-us")

   while True:
      print("Say something")
      for result in stt.listen(stream=True):
         if result["done"]:
               print(f"final:   {result['final']}")
         else:
               print(f"partial: {result['partial']}", end="\r", flush=True)


**代码说明：**

* ``stt.listen(stream=True)`` — 启动流式语音识别，在您说话的过程中持续返回中间识别结果。  
* ``result["partial"]`` — 显示\ **实时识别文本** （会不断更新）。  
* ``result["final"]`` — 当您停止说话时，显示\ **最终识别出的完整句子**\ 。  
* 循环会持续运行，从而实现\ **免手动操作的实时语音转写**\ 。

提示：这种流式模式非常适合用于 **语音助手**\ 、\ **语音命令控制** 或 **实时语音转写**\ 。

故障排查
-----------------

* **No such file or directory（运行 `arecord` 时出现）**

  可能是使用了错误的声卡/设备编号。  
  运行：

  .. code-block:: bash

     arecord -l

  然后将 ``1,0`` 替换为您 USB 麦克风对应的设备编号。

* **录音文件没有声音**

  打开混音器并检查麦克风音量：

  .. code-block:: bash

     alsamixer

  * 按 **F6** 选择您的 USB 麦克风。  
  * 确保 **Mic/Capture** 未被静音（显示为 **[OO]** 而不是 **[MM]**\ ）。  
  * 使用 ↑ 键提高音量。

* **Vosk 无法识别语音**

  * 确保 **语言代码** 与模型一致（例如英语使用 ``en-us``\ ，中文使用 ``zh-cn``\ ）。  
  * 将麦克风保持在 15–30 cm 距离，并避免背景噪声。  
  * 说话清晰、语速适中。

* **识别延迟较高 / 速度较慢**

  * 默认自动下载的是 **small 模型** （速度较快，但准确率略低）。  
  * 如果仍然较慢，可以关闭其他程序以释放 CPU 资源。