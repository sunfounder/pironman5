.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _promax_openclaw_5_promax:


.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw
   :end-before: end_using_openclaw

Making OpenClaw Operate the Pironman5 Pro MAX
----------------------------------------------

To enable OpenClaw to operate the Pironman5 Pro MAX, we need to install the Pironman5 Pro MAX skill.

1.  Ensure you have already installed the Pironman5 Pro MAX. If not, please refer to :ref:`install_pironman5_module_promax`.

2.  Run the following command in the terminal:

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-promax-skill/ ~/.openclaw/skills/pironman5-promax-skill/

3.  You can now operate the Pironman5 Pro MAX in ``openclaw tui``. Try sending commands in the TUI, such as attempting to turn on the LED lights on the case, change their color, or have the camera take a photo. You can even tell it that you have a DHT11 module connected to GPIO17 and let it tell you the temperature.

   .. note:: If OpenClaw is still unable to recognize the skill you imported, please remind it to rsync.

-------------------------------------------------------------

Interacting with Voice
----------------------------------------------------

The Pro MAX case has a built-in microphone and speaker, so you can use the Pironman5 Pro MAX to interact with OpenClaw via voice. To achieve this, you need to install the ``sunfounder-voice-assistant`` package.

The ``sunfounder-voice-assistant`` package provides the necessary libraries and tools for operating the Pironman 5 Pro MAX hardware.

Run the following installation command:

.. code-block:: bash


   sudo apt install portaudio19-dev
   sudo pip install --break git+https://github.com/sunfounder/sunfounder-voice-assistant.git


Here you will explore text-to-speech (TTS), speech-to-text (STT), and large language models (LLMs) to make your Pironman 5 Pro MAX talk, listen, and even chat with you like a smart robot.

Then, run the following example:

.. code-block:: bash

   python3 ~/pironman5/openclaw_voice.py

Reboot. Then you can use the voice features of the Pironman5 Pro MAX to interact with OpenClaw. Try saying "Hi Amy" to wake it up.

---------------------------------------



.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_telegram
   :end-before: end_using_openclaw_telegram

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_faq
   :end-before: end_using_openclaw_faq