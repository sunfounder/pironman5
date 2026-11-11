.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



FAQ
============


Risoluzione rapida dei problemi
-------------------------------

* Il pulsante di accensione non funziona → :ref:`faq_power_button_not_work_mini`
* I LED RGB non funzionano → :ref:`faq_rgb_mini`
* La ventola della CPU non gira → :ref:`faq_pwm_fan_mini`
* Il pannello non mostra alcun dato → :ref:`faq_dashboard_mini`
* Il PI5 non si avvia → :ref:`faq_pi5_boot_fail_mini`



1. Hardware
-------------------------------


.. _com_os_mini:

Sistemi compatibili
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os


Pulsante di accensione
^^^^^^^^^^^^^^^^^^^^^^^^

Il pulsante esterno replica il pulsante di accensione del Raspberry Pi 5 e ne mantiene le stesse funzionalità.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Spegnimento**

  * Su **Raspberry Pi OS Desktop**, premi due volte rapidamente per spegnere.
  * Su **Raspberry Pi OS Lite**, premi una volta per iniziare lo spegnimento.
  * Tieni premuto per un arresto forzato.

* **Accensione**

  * Se il Raspberry Pi è spento ma alimentato, premi una volta per accendere.

* Se il sistema non supporta lo spegnimento tramite pulsante, tieni premuto 5 secondi per forzare lo spegnimento, poi premi una volta per accendere.


.. _faq_power_button_not_work_mini:

Il pulsante di accensione non funziona?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button_not_work
   :end-before: end_faq_power_button_not_work


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^

Il Raspberry Pi AI HAT+ non è compatibile con il Pironman 5.

.. image::  img/output3.png
    :width: 400

Il kit AI Raspberry Pi combina l'HAT+ M.2 e il modulo acceleratore AI Hailo.

.. image::  img/output2.jpg
    :width: 400

Puoi staccare il modulo acceleratore AI Hailo dal Raspberry Pi AI Kit e inserirlo direttamente nell'HAT del Pironman 5 Mini.


Cavo Micro HDMI
^^^^^^^^^^^^^^^^^

Si consiglia di utilizzare il cavo Micro HDMI ufficiale Raspberry Pi. Alcuni cavi di terze parti con una lunghezza del connettore inferiore a 65 mm potrebbero causare scarso contatto e problemi di visualizzazione.

.. image:: img/need_mini_hdmi.png
   :width: 400



2. Raffreddamento e ventole
-------------------------------


.. _faq_pwm_fan_mini:

La ventola della CPU non funziona?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan



3. RGB
-------------------------------


.. |link_compatible_systems| replace:: :ref:`com_os_mini`

.. _faq_rgb_mini:

I LED RGB non funzionano?
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb



4. Pannello e software
-------------------------------


.. _faq_dashboard_mini:

Il pannello non mostra alcun dato
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard


.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard_mini`

Come disabilitare il pannello web
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_disable_dashboard
   :end-before: end_faq_disable_dashboard


Come disinstallare e reinstallare il software Pironman 5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_reinstall_pironman5
   :end-before: end_faq_reinstall_pironman5


.. |link_view_control_commands| replace:: :ref:`view_control_commands_mini`

Come controllare i componenti con il comando ``pironman5``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command



5. Avvio e archiviazione
-------------------------------


.. |link_update_bootloader| replace:: :ref:`update_bootloader_mini`

.. _faq_pi5_boot_fail_mini:

PI5 non si avvia (LED rosso)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo problema può essere causato da un aggiornamento del sistema, da modifiche all'ordine di avvio o da un bootloader danneggiato. Puoi provare i seguenti passaggi per risolvere il problema:

#. Ricollega l'alimentazione e verifica se il PI5 si avvia correttamente.

#. Prova il PI5 al di fuori del case

   * Rimuovi il PI5 dal case Pironman 5 Mini.
   * Alimenta il PI5 direttamente con l'adattatore di alimentazione (senza il case).
   * Verifica se si avvia normalmente.

#. Ripristina il bootloader

   * Se il PI5 continua a non avviarsi, il bootloader potrebbe essere corrotto. Puoi seguire questa guida: |link_update_bootloader| e scegliere se avviare da SD card o da NVMe/USB.
   * Inserisci la scheda SD preparata nel PI5, accendilo e attendi almeno 10 secondi. Una volta completato il ripristino, rimuovi e riformatta la scheda SD.
   * Poi utilizza Raspberry Pi Imager per installare l'ultima versione del Raspberry Pi OS e prova ad avviare nuovamente.


.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_mini`

Come cambiare l'ordine di avvio da terminale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_command
   :end-before: end_faq_boot_order_command


Come cambiare l'ordine di avvio con Raspberry Pi Imager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_imager
   :end-before: end_faq_boot_order_imager


.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_mini`

Come copiare il sistema da SD a SSD NVMe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copy_sd_to_nvme
   :end-before: end_faq_copy_sd_to_nvme



6. Utilizzo avanzato
-------------------------------


Come rimuovere la pellicola protettiva
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_remove_film
   :end-before: end_faq_remove_film


.. _openssh_powershell_mini:

Come installare OpenSSH tramite Powershell?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quando provi a collegarti al tuo Raspberry Pi usando il comando ``ssh <username>@<hostname>.local`` (oppure ``ssh <username>@<IP address>``), ma compare il seguente messaggio di errore:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


Significa che il tuo sistema operativo è troppo vecchio e non ha `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstallato. In tal caso, segui il tutorial qui sotto per installarlo manualmente.

#. Digita ``powershell`` nella barra di ricerca del desktop di Windows, fai clic destro su ``Windows PowerShell`` e seleziona ``Esegui come amministratore`` dal menu che appare.

   .. image:: img/powershell_ssh.png
      :width: 90%


#. Utilizza il seguente comando per installare ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Dopo l'installazione, verrà restituito il seguente output:

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica l'installazione con il comando:

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ora ti verrà mostrato che ``OpenSSH.Client`` è stato installato correttamente:

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        Se questo messaggio non compare, significa che il tuo sistema Windows è ancora troppo obsoleto. In questo caso, ti consigliamo di installare uno strumento SSH di terze parti come |link_putty|.

#. Riavvia PowerShell e continua ad eseguirlo come amministratore. A questo punto potrai accedere al tuo Raspberry Pi con il comando ``ssh``, dove ti verrà chiesta la password che hai configurato precedentemente.

   .. image:: img/powershell_login.png
