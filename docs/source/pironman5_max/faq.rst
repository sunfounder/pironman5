.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

FAQ
============


Risoluzione rapida dei problemi
-------------------------------

* Schermo OLED non funziona → :ref:`faq_oled_max`
* LED RGB non funzionano → :ref:`faq_rgb_max`
* Ventole GPIO non funzionano → :ref:`faq_gpio_fans_max`
* Ventola CPU non gira → :ref:`faq_pwm_fan_max`
* Dashboard non mostra dati → :ref:`faq_dashboard_max`
* SSD NVMe non rilevato → :ref:`faq_nvme_max`



1. Hardware
-------------------------------


.. _com_os_max:

Sistemi compatibili
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os

Pulsante di accensione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button
   :end-before: end_faq_power_button

Estremità dei tubi di rame sul dissipatore a torre
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copper_pipe_ends
   :end-before: end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_ai_hat
   :end-before: end_faq_ai_hat

Posso usare la funzione di interruttore a vibrazione del Pironman5 Max?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dalla v1.3.6, la riattivazione OLED usa il pulsante di accensione. Devi rimuovere il ponticello dell'interruttore a vibrazione per evitare di occupare i pin GPIO del Raspberry Pi e prevenire potenziali conflitti. Verifica se questo ponticello esiste; in caso contrario, ignora questo avviso.

.. image:: /pironman5_max/img/remove_vib_jumper.jpg

2. Raffreddamento e ventole
-----------------------------------------------

.. _faq_pwm_fan_max:

La ventola CPU non gira?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan


.. _faq_gpio_fans_max:

Le ventole GPIO non funzionano?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_gpio_fans
   :end-before: end_faq_gpio_fans


3. OLED e RGB
-------------------------------


.. _faq_oled_max:

Lo schermo OLED non funziona?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_compatible_systems| replace:: :ref:`com_os_max`
.. |link_set_up_pironman5| replace:: :ref:`max_set_up_pironman5`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_oled
   :end-before: end_faq_oled

.. _faq_rgb_max:

I LED RGB non funzionano?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb


.. _faq_customize_oled_max:

Come personalizzare il display OLED?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_customize_oled
   :end-before: end_faq_customize_oled


4. Dashboard e software
-------------------------------


.. _faq_dashboard_max:

La Dashboard non mostra dati
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard

Come disabilitare la Dashboard web
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_disable_dashboard
   :end-before: end_faq_disable_dashboard


Come disinstallare e reinstallare il software Pironman 5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_reinstall_pironman5
   :end-before: end_faq_reinstall_pironman5


Come controllare i componenti con il comando ``pironman5``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_commands| replace:: :ref:`max_view_control_commands`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command


5. Avvio e archiviazione
-------------------------------

Se configuro OMV, posso ancora usare le funzioni del Pironman5?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sì, OpenMediaVault è configurato sul sistema Raspberry Pi. Segui i passaggi di :ref:`set_up_os_max` per continuare la configurazione.


Il PI5 non si avvia (LED rosso)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_update_bootloader| replace:: :ref:`update_bootloader_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pi5_boot_fail
   :end-before: end_faq_pi5_boot_fail

.. _faq_nvme_max:

Il modulo NVMe PIP non funziona?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Assicurati che il cavo FPC che collega il modulo NVMe PIP al Raspberry Pi 5 sia fissato saldamente.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(1)-11.mp4" type="video/mp4">
               Il tuo browser non supporta il tag video.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(2)-11.mp4" type="video/mp4">
               Il tuo browser non supporta il tag video.
           </video>
       </div>

#. Verifica che il tuo SSD sia correttamente fissato al modulo NVMe PIP.

#. Controlla lo stato dei LED del modulo NVMe PIP:

   Dopo aver verificato tutti i collegamenti, accendi il Pironman 5 MAX e osserva i due indicatori sul modulo NVMe PIP:

   * **LED PWR**: Dovrebbe essere acceso.
   * **LED STA**: Dovrebbe lampeggiare per indicare il normale funzionamento.

   .. image:: img/dual_nvme_pip_leds.png

   * Se il **LED PWR** è acceso ma il **LED STA** non lampeggia, indica che l'SSD NVMe non è riconosciuto dal Raspberry Pi.
   * Se il **LED PWR** è spento, cortocircuita i pin "Force Enable" sul modulo. Se il **LED PWR** si accende, potrebbe indicare un cavo FPC allentato o una configurazione di sistema non supportata per NVMe.

   .. image:: img/dual_nvme_pip_j4.png


#. Verifica che il tuo SSD NVMe abbia un sistema operativo correttamente installato. Vedi: :ref:`install_the_os_max`.

#. Se il problema persiste, inviaci il seguente file di log:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

Come cambiare l'ordine di avvio del Raspberry Pi usando i comandi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_command
   :end-before: end_faq_boot_order_command


Come modificare l'ordine di avvio con Raspberry Pi Imager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_imager
   :end-before: end_faq_boot_order_imager

Come copiare il sistema dalla scheda SD a un SSD NVMe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copy_sd_to_nvme
   :end-before: end_faq_copy_sd_to_nvme

6. Utilizzo avanzato
-------------------------------

Come rimuovere la pellicola protettiva
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_remove_film
   :end-before: end_faq_remove_film
