.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _promax_openclaw_5_promax:


.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw
   :end-before: end_using_openclaw

OpenClawによるPironman5 Pro MAXの操作
----------------------------------------------

OpenClawがPironman5 Pro MAXを操作できるようにするには、Pironman5 Pro MAXスキルをインストールする必要があります。

1.  Pironman5 Pro MAXが既にインストールされていることを確認します。インストールされていない場合は、:ref:`install_pironman5_module_promax` を参照してください。

2.  ターミナルで以下のコマンドを実行します：

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-promax-skill/ ~/.openclaw/skills/pironman5-promax-skill/

3.  これで、 ``openclaw tui`` でPironman5 Pro MAXを操作できるようになりました。TUIでコマンドを送信してみてください。例えば、ケースのLEDライトを点灯させたり、色を変更したり、カメラで写真を撮らせたりすることができます。GPIO17にDHT11モジュールが接続されていることを伝え、温度を教えてもらうことさえ可能です。

   .. note:: OpenClawがインポートしたスキルをまだ認識できない場合は、rsyncを実行するよう促してください。

-------------------------------------------------------------

音声による対話
----------------------------------------------------

Pro MAXケースにはマイクとスピーカーが内蔵されているため、Pironman5 Pro MAXを使用して音声でOpenClawと対話することができます。これを実現するには、 ``sunfounder-voice-assistant`` パッケージをインストールする必要があります。

``sunfounder-voice-assistant`` パッケージは、Pironman 5 Pro MAXハードウェアを操作するために必要なライブラリとツールを提供します。

以下のインストールコマンドを実行してください：

.. code-block:: bash


   sudo apt install portaudio19-dev
   sudo pip install --break git+https://github.com/sunfounder/sunfounder-voice-assistant.git


ここでは、テキスト読み上げ（TTS）、音声認識（STT）、大規模言語モデル（LLM）を活用し、Pironman 5 Pro MAXがまるでスマートロボットのように話しかけ、聞き取り、さらには会話できるようにする方法を探求します。

次に、以下のサンプルを実行します：

.. code-block:: bash

   python3 ~/pironman5/openclaw_voice.py

再起動します。これで、Pironman5 Pro MAXの音声機能を使用してOpenClawと対話できるようになります。「Hi Amy」と言ってウェイクアップさせてみてください。

---------------------------------------



.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_telegram
   :end-before: end_using_openclaw_telegram

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_faq
   :end-before: end_using_openclaw_faq