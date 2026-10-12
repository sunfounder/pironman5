.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _ai_hat_ultra:

HAT Expansion and AI HAT+
==============================

**Standard HAT Expansion**

Pironman 5 Ultra supports standard HAT-size HATs (such as the AI HAT series). Plug the HAT directly onto the Raspberry Pi 40-pin GPIO header above the PiPower 5 module. Because the PiPower 5 module has some height, use standoffs of a suitable height to secure the HAT.

* Supports the standard HAT size (65 x 56 mm)
* Plugs directly onto the PiPower 5 module (Raspberry Pi 40-pin GPIO header)
* Requires standoffs of a suitable height (not included)

To connect a Raspberry Pi standard PCIe HAT (such as the AI HAT+ / AI HAT+ 2), the **DET** pin switches the PCIe interface automatically when it is connected. See :ref:`nvme_pip_ultra`.

**Running LLMs with the AI HAT+ 2 (Hailo-10H)**

The polling interval of ``hailo-ollama`` must be adjusted, otherwise LLM inference will be unstable (silent failures). Edit ``/etc/xdg/hailo-ollama/hailo-ollama.json`` and change ``main_poll_time_ms`` from ``200`` to ``2000``:

.. code-block:: json

   {
       "server": {"host": "0.0.0.0", "port": 8000},
       "library": {"host": "dev-public.hailo.ai", "port": 443},
       "main_poll_time_ms": 2000
   }

Restart ``hailo-ollama`` for the change to take effect.

.. note::

   On a Gen2 link (through the PCIe switch chip), the default 200 ms polling creates a race condition that causes LLM inference requests to fail silently. After increasing the polling interval, there is no obvious difference between Gen2 and Gen3 performance (LLM ~2.6 t/s, vision yolov8m ~75 FPS).
