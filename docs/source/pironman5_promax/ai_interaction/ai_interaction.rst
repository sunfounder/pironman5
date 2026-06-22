.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


9. Think · Talk · Drive — 基于多 LLM 的 AI 能力
------------------------------------------------------------


``sunfounder-voice-assistant`` 软件包提供了运行 Pironman 5 Pro MAX 硬件所需的相关库和工具。

运行以下安装命令：

.. code-block:: bash


    sudo apt install espeak libttspico-utils sox portaudio19-dev
    git clone https://github.com/sunfounder/sunfounder-voice-assistant.git
    sudo pip install ./sunfounder-voice-assistant --break


在本章节中，您将探索文本转语音（TTS）、语音转文本（STT）以及大语言模型（LLMs）的应用，使您的 Pironman 5 Pro MAX 能够像智能机器人一样进行语音输出、语音识别，甚至与您进行对话。


.. toctree:: 
    :maxdepth: 1

    python_tts_espeak_pico2wave
    python_tts_piper_openai
    python_stt_vosk
    python_llm_ollama
    python_online_llms
    python_local_chatbot
    python_ai_assistant
