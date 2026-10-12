.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _audio_ultra:

Audio Output
=================

Pironman 5 Ultra has built-in **4Ω 3W stereo speakers** and a **3.5mm headphone jack**. The audio signal is taken from the **HDMI0** interface and amplified by the amplifier on the HDMI adapter board.

**Output Mode**

The output mode can be set on the Dashboard (Settings → Speaker Mode) or with the ``pironman5`` command:

.. list-table::
   :header-rows: 1
   :widths: 20 60

   * - Mode
     - Description
   * - Auto (default)
     - Switches automatically. When a monitor is plugged into HDMI0 or headphones are inserted, the speaker output is turned off and audio is played through the external device.
   * - ON
     - The speakers stay on regardless of whether an external device is connected.

.. note::

   The speakers are mounted on the HDMI adapter board. If you are not using external audio, leave the mode at **Auto** so that the speakers turn off automatically when a monitor is connected to HDMI0.
