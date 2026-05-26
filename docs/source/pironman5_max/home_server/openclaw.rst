.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _openclaw_5_max:


.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw
   :end-before: end_using_openclaw

Making OpenClaw Operate the Pironman5 Max
----------------------------------------------

To enable OpenClaw to operate the Pironman5 Max, we need to install the Pironman5 Max skill.

1.  Ensure you have already installed the Pironman5 Max. If not, please refer to :ref:`install_pironman5_module_max`.

2.  Run the following command in the terminal:

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-max-skill/ ~/.openclaw/skills/pironman5-max-skill/

3.  You can now operate the Pironman5 Max in ``openclaw tui``. Try sending commands in the TUI, such as attempting to turn on the LED lights on the case, change their color, or have the camera take a photo. You can even tell it that you have a DHT11 module connected to GPIO17 and let it tell you the temperature.

   .. note:: If OpenClaw is still unable to recognize the skill you imported, please remind it to rsync.

-------------------------------------------------------------




.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_telegram
   :end-before: end_using_openclaw_telegram

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_faq
   :end-before: end_using_openclaw_faq