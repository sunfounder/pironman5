.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

FAQ
============


Risoluzione rapida dei problemi
---------------------------------

* Pulsante di accensione non funziona -> :ref:`faq_power_button_not_work_5`
* Schermo OLED non funziona -> :ref:`faq_oled_5`
* LED RGB non funzionano -> :ref:`faq_rgb_5`
* Ventole GPIO non funzionano -> :ref:`faq_gpio_fans_5`
* Ventola CPU non gira -> :ref:`faq_pwm_fan_5`
* Dashboard non mostra dati -> :ref:`faq_dashboard_5`
* SSD NVMe non rilevato -> :ref:`faq_nvme_5`
* SSD NVMe rilevato ma causa riavvio del sistema -> :ref:`faq_nvme_link_down_5`



1. Hardware
-------------------------------


.. _compatible_systems_5:

Sistemi compatibili
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_com_os

Sistemi testati su Raspberry Pi 5:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

.. end_faq_com_os

Pulsante di accensione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_5`

.. start_faq_power_button

Il pulsante di accensione estende il pulsante originale del Raspberry Pi 5 e si comporta in modo simile.

* Pressione breve: Accensione / riattivazione OLED / cambio pagina OLED.
* Tieni premuto 2 secondi: Arresto sicuro (richiede |link_safe_shutdown|).
* Tieni premuto 5 secondi: Arresto forzato.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

.. end_faq_power_button


.. _faq_power_button_not_work_5:

Il pulsante di accensione non funziona?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_power_button_not_work

#. Per prima cosa, conferma il comportamento previsto del pulsante di accensione:

   * **Raspberry Pi OS Desktop**: Premi il pulsante di accensione due volte rapidamente per spegnere. Tieni premuto 5 secondi per forzare lo spegnimento. Premi una volta per accendere dallo stato di spegnimento.
   * **Raspberry Pi OS Lite**: Premi il pulsante di accensione una volta per spegnere. Tieni premuto 5 secondi per forzare lo spegnimento. Premi una volta per accendere.

#. Verifica che i pin del convertitore di alimentazione siano correttamente allineati con i pad J2 del Raspberry Pi 5 (tra il connettore della batteria RTC e il bordo della scheda).

#. Verifica che i pin all'interno della presa del convertitore di alimentazione siano correttamente allineati con il connettore del pulsante di accensione. Ricollega il cavo del pulsante di accensione se necessario.

#. Usa un cacciavite per cortocircuitare brevemente i due pin sulla presa del convertitore di alimentazione dove si collega il pulsante. Se il Pi si accende, il pulsante stesso potrebbe essere difettoso; in caso contrario, il problema probabilmente riguarda la scheda del convertitore o la connessione al Pi 5.

.. end_faq_power_button_not_work


Direzione del flusso d'aria
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_airflow_direction

Il flusso d'aria all'interno del Pironman 5 è progettato per massimizzare l'efficienza di raffreddamento. L'aria fresca entra attraverso l'apertura GPIO e altre feritoie, passa attraverso il dissipatore a torre e viene espulsa dalle due ventole GPIO laterali.

Per una dimostrazione dettagliata, guarda il seguente video:

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="../_static/video/airflow_direction.mp4"  type="video/mp4">
            Il tuo browser non supporta il tag video.
        </video>
    </div>

.. end_faq_airflow_direction


Estremità dei tubi di rame sul dissipatore a torre
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_copper_pipe_ends

Le estremità appiattite dei tubi di calore in rame a forma di U fanno parte del normale processo di produzione e sono progettate per permettere ai tubi di calore di passare attraverso le alette in alluminio.

.. image:: img/tower_cooler1.png

.. end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_ai_hat

Il Raspberry Pi AI HAT+ non è compatibile con il Pironman 5.

.. image:: img/output3.png
    :width: 400

Il kit Raspberry Pi AI combina il Raspberry Pi M.2 HAT+ e il modulo acceleratore AI Hailo.

.. image:: img/output2.jpg
    :width: 400

Puoi staccare il modulo acceleratore AI Hailo dal kit Raspberry Pi AI e inserirlo direttamente nel modulo NVMe PIP del Pironman 5.

.. image:: img/output4.png
    :width: 800

.. end_faq_ai_hat



2. Raffreddamento e ventole
-------------------------------


.. _faq_pwm_fan_5:

La ventola CPU non gira?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_pwm_fan

La ventola CPU del Pironman 5 è controllata dal sistema Raspberry Pi. La velocità della ventola CPU dipende dalla temperatura della CPU del Raspberry Pi 5.

Curva predefinita della ventola CPU:

* < 50°C: Spenta (0%)
* 50°C+: Velocità bassa (30%)
* 60°C+: Velocità media (50%)
* 67,5°C+: Velocità alta (70%)
* 75°C+: Velocità massima (100%)

Controlla la temperatura attuale della CPU (esempio di output: ``temp=48.7'C``):

.. code-block:: shell

   vcgencmd measure_temp

Puoi controllare manualmente la ventola CPU con i seguenti comandi:

.. code-block:: shell

   pinctrl FAN_PWM op dl   # Attiva ventola (attivo basso)
   pinctrl FAN_PWM op dh   # Disattiva ventola (attivo alto)
   pinctrl FAN_PWM a0      # Modalità automatica

Puoi anche regolare le soglie di temperatura della ventola CPU modificando:

.. code-block:: shell

   nano /boot/firmware/config.txt

Aggiungi:

.. code-block:: text

   dtparam=cooling_fan=on
   dtparam=fan_temp0=40000
   dtparam=fan_temp0_hyst=10000
   dtparam=fan_temp0_speed=125

Questa configurazione avvia la ventola CPU a 40°C con livello di velocità PWM 125.

Dopo aver salvato il file, riavvia il Raspberry Pi per applicare le modifiche.

.. end_faq_pwm_fan


.. _faq_gpio_fans_5:

Le ventole GPIO non funzionano?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_gpio_fans

Per prima cosa, controlla se il ponticello FAN sulla scheda IO Expander è installato correttamente.

.. image:: hardware/img/io_board_fan_j9.png

Quindi imposta le ventole GPIO in modalità ``Sempre attive`` e verifica se iniziano a girare.

.. code-block:: shell

   sudo pironman5 -gm 0

Puoi anche collegare le ventole GPIO direttamente ai pin ``5V`` e ``GND`` del Raspberry Pi per testarle.

Se le ventole girano normalmente quando collegate direttamente, il problema potrebbe essere legato alla scheda IO Expander. Contattaci per ulteriore assistenza.

Se il problema persiste, apri la pagina **Log** della Dashboard e verifica i messaggi di errore. Puoi anche inviarci il seguente file di log:

.. code-block:: shell

   cat /var/log/pironman5/pironman5.log

.. end_faq_gpio_fans

3. OLED e RGB
-------------------------------


.. _faq_oled_5:

Lo schermo OLED non funziona?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_set_up_pironman5| replace:: :ref:`set_up_pironman5_5`
.. |link_compatible_systems| replace:: :ref:`compatible_systems_5`

.. start_faq_oled

Se lo schermo OLED non visualizza nulla o mostra informazioni errate, segui questi passaggi di risoluzione:

#. Assicurati che il cavo FPC dello schermo OLED sia collegato saldamente. Si consiglia di ricollegare lo schermo OLED e poi accendere il dispositivo.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_oled_screen.mp4" type="video/mp4">
               Il tuo browser non supporta il tag video.
           </video>
       </div>

#. Verifica che il Raspberry Pi esegua un sistema operativo supportato.

   Vedi |link_compatible_systems|.

#. Al primo avvio, lo schermo OLED potrebbe mostrare solo blocchi di pixel. Segui le istruzioni in |link_set_up_pironman5| per completare la configurazione prima che possa visualizzare informazioni corrette.

#. Usa il seguente comando per verificare se l'indirizzo I2C ``0x3C`` dell'OLED viene rilevato:

   .. code-block:: shell

      sudo i2cdetect -y 1

   * Se l'indirizzo I2C ``0x3C`` viene rilevato, riavvia il servizio Pironman 5:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * Se l'indirizzo non viene rilevato, abilita I2C:

     .. code-block:: shell

        sudo nano /boot/firmware/config.txt

     Aggiungi:

     .. code-block:: shell

        dtparam=i2c_arm=on

     Salva il file e riavvia il Raspberry Pi.

#. Se il problema persiste, inviaci il seguente file di log:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_oled


.. _faq_rgb_5:

I LED RGB non funzionano?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. start_faq_rgb

#. I due pin sull'IO Expander sopra J9 sono usati per collegare i LED RGB a GPIO10. Assicurati che il ponticello su questi due pin sia installato correttamente.

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Verifica che il Raspberry Pi esegua un sistema operativo supportato.

   Vedi |link_compatible_systems|.

#. Esegui il seguente comando per abilitare SPI:

   .. code-block:: shell

      sudo raspi-config

   Vai a:

   ``3 Opzioni di interfaccia`` -> ``I3 SPI`` -> ``SÌ``

   Quindi riavvia il Raspberry Pi.

#. Se il problema persiste, inviaci il seguente file di log:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_rgb

.. _faq_customize_oled_5:

Come personalizzare il display OLED?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_customize_oled

Se vuoi personalizzare il display OLED, ad esempio aggiungendo visualizzazioni di immagini personalizzate a 2-4 cifre, puoi modificare i file delle pagine OLED in uno dei seguenti modi.

* **Metodo 1: Modificare direttamente i file installati**

  #. Elenca i file delle pagine OLED:

     .. code-block:: shell

        ls /opt/pironman5/venv/lib/python3.13/site-packages/pm_auto/addons/oled/pages/

  #. Modifica i file Python desiderati.

  #. Riavvia il servizio per applicare le modifiche:

     .. code-block:: shell

        sudo systemctl restart pironman5.service


* **Metodo 2: Clonare e reinstallare ``pm_auto``**

  #. Clona il repository ``pm_auto``:

     .. code-block:: shell

        git clone -b 1.4.x https://github.com/sunfounder/pm_auto/

  #. Dopo aver apportato le modifiche, reinstalla il pacchetto modificato:

     .. code-block:: shell

        sudo /opt/pironman5/venv/bin/pip3 uninstall pm_auto -y && \
        sudo /opt/pironman5/venv/bin/pip3 install ~/pm_auto --no-build-isolation && \
        sudo chown -R pironman5:pironman5 /opt/pironman5

  #. Riavvia il servizio:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

* **Test e debug**

  Per visualizzare i log di esecuzione:

  .. code-block:: shell

     journalctl -xefu pironman5.service

  Puoi anche fermare il servizio ed eseguirlo manualmente per test più rapidi:

  .. code-block:: shell

     sudo systemctl stop pironman5.service
     sudo systemctl restart pironman5.service

.. end_faq_customize_oled

4. Dashboard e software
-------------------------------


.. _faq_dashboard_5:

La Dashboard non mostra dati
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_dashboard

Se la Dashboard non mostra dati, apri prima la pagina **Log** della Dashboard e verifica se ci sono messaggi di errore relativi a ``influxdb``.

Gli errori comuni includono:

* ``database not found``
* ``failed to connect to influxdb``
* ``connection refused``
* ``timeout``

Puoi provare i seguenti passaggi per risolvere il problema.

#. Pulisci la cache del browser o riapri la pagina Dashboard in modalità **Incognito/Privata**.

#. Verifica se i seguenti servizi sono in esecuzione:

   .. code-block:: shell

      sudo systemctl status pironman5 --no-pager
      sudo systemctl status influxdb --no-pager

   Entrambi i servizi dovrebbero mostrare:

   .. code-block:: text

      active (running)

#. Se uno dei servizi non funziona correttamente, riavviali:

   .. code-block:: shell

      sudo systemctl restart influxdb
      sudo systemctl restart pironman5

   Quindi attendi circa 30 secondi e aggiorna la pagina Dashboard.

#. Verifica se il database ``pironman5`` esiste:

   .. code-block:: shell

      influx

   Quindi esegui:

   .. code-block:: text

      SHOW DATABASES;

   Dovresti vedere:

   .. code-block:: text

      pironman5
      _internal

#. Se il database è mancante o corrotto, prova a cancellare i dati storici dalla Dashboard usando:

   ``Impostazioni -> Cancella tutti i dati``

#. Se il problema persiste dopo aver provato tutti i passaggi precedenti, consigliamo di reinstallare Raspberry Pi OS e il software Pironman 5.

.. end_faq_dashboard


Come disabilitare la Dashboard web
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard_5`

.. start_faq_disable_dashboard

Una volta completata l'installazione del modulo ``pironman5``, potrai accedere alla |link_view_control_dashboard|.

Se non hai bisogno di questa funzione e vuoi ridurre l'uso di CPU e RAM, puoi disabilitare la dashboard durante l'installazione aggiungendo il flag ``--disable-dashboard``.

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Se hai già installato ``pironman5``, puoi rimuovere il modulo Dashboard e ``influxdb``:

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

.. end_faq_disable_dashboard


Come disinstallare e reinstallare il software Pironman 5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_reinstall_pironman5

#. Disinstalla il software ``pironman5`` attuale:

   .. code-block:: shell

      cd ~/pironman5
      sudo python3 install.py --uninstall

#. Riavvia il Raspberry Pi come richiesto, quindi rimuovi la directory ``pironman5``:

   .. code-block:: shell

      cd ~/
      sudo rm -rf pironman5

#. Esegui il seguente comando per reinstallare il software per il tuo modello Pironman 5:

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/pironman5/v1/install.sh" | sudo bash

.. end_faq_reinstall_pironman5


Come controllare i componenti con il comando ``pironman5``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_commands| replace:: :ref:`view_control_commands_5`

.. start_faq_pironman5_command

Puoi fare riferimento al seguente tutorial per controllare i componenti della serie Pironman 5 usando il comando ``pironman5``.

* |link_view_control_commands|

.. end_faq_pironman5_command



5. Avvio e archiviazione
-------------------------------


Il PI5 non si avvia (LED rosso)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_update_bootloader| replace:: :ref:`update_bootloader_5`

.. start_faq_pi5_boot_fail

Questo problema può essere causato da un aggiornamento di sistema, modifiche all'ordine di avvio o un bootloader corrotto. Prova i seguenti passaggi per risolvere il problema:

#. Controlla la connessione dell'adattatore USB-HDMI

   * Verifica attentamente se l'adattatore USB-HDMI è collegato saldamente al PI5.
   * Prova a scollegare e ricollegare l'adattatore USB-HDMI.
   * Quindi ricollega l'alimentazione e verifica se il PI5 si avvia correttamente.

#. Testa il PI5 fuori dal case

   * Se ricollegare l'adattatore non risolve il problema:
   * Rimuovi il PI5 dal case della serie Pironman 5.
   * Alimenta il PI5 direttamente con l'adattatore di alimentazione (senza il case).
   * Verifica se può avviarsi normalmente.

#. Ripristina il bootloader

   * Se il PI5 ancora non si avvia, il bootloader potrebbe essere corrotto. Segui questa guida: |link_update_bootloader| e scegli se avviare da scheda SD o NVMe/USB.
   * Inserisci la scheda SD preparata nel PI5, accendilo e attendi almeno 10 secondi. Una volta completato il ripristino, rimuovi e riformatta la scheda SD.
   * Quindi usa Raspberry Pi Imager per flashare l'ultimo Raspberry Pi OS e prova ad avviare di nuovo.

.. end_faq_pi5_boot_fail


.. _faq_nvme_5:

Il modulo NVMe PIP non funziona?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_install_the_os| replace:: :ref:`install_the_os_5`
.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_5`

.. start_faq_nvme_pip

#. Assicurati che il tuo SSD NVMe sia compatibile. Fai riferimento all'elenco degli :ref:`SSD NVMe compatibili <compitable_nvme_ssd_5>` per unità verificate, stabili e compatibili.

#. Assicurati che il cavo FPC che collega il modulo NVMe PIP al Raspberry Pi 5 sia fissato saldamente.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Il tuo browser non supporta il tag video.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Il tuo browser non supporta il tag video.
           </video>
       </div>

#. Verifica che il tuo SSD sia correttamente fissato al modulo NVMe PIP.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_ssd.mp4" type="video/mp4">
               Il tuo browser non supporta il tag video.
           </video>
       </div>

#. Controlla lo stato dei LED del modulo NVMe PIP:

   * **LED PWR**: Dovrebbe essere acceso.
   * **LED STA**: Dovrebbe lampeggiare durante il normale funzionamento.

   .. image:: img/nvme_pip_leds.png

   * Se il **LED PWR** è acceso ma il **LED STA** non lampeggia, l'SSD NVMe non è riconosciuto.
   * Se il **LED PWR** è spento, cortocircuita i pin ``Force Enable`` (J4). Se il **LED PWR** si accende dopo il cortocircuito, il problema potrebbe essere un cavo FPC allentato o una configurazione di sistema non supportata per NVMe.

     .. image:: img/nvme_pip_j4.png

#. Verifica che il tuo SSD NVMe contenga un sistema operativo valido.

   Vedi |link_install_the_os|.

#. Se l'SSD ancora non si avvia, prova ad avviare prima da una scheda Micro SD, quindi configura l'avvio NVMe:

   * |link_configure_boot_ssd|

#. Se il problema persiste, inviaci il seguente file di log:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_nvme_pip


.. _faq_nvme_link_down_5:

SSD NVMe rilevato ma causa riavvio del sistema in lettura/scrittura?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_nvme_link_down

In alcuni casi (specialmente con WD Blue SN5000), l'SSD NVMe può essere rilevato dal Raspberry Pi 5 ma causare il riavvio del sistema durante le operazioni di lettura/scrittura. Si tratta di un problema di compatibilità/stabilità PCIe tra l'SSD e il Raspberry Pi 5, **non** un difetto hardware del Pironman 5.

Prova i seguenti passaggi per risolvere il problema:

#. Aggiorna il bootloader del Raspberry Pi 5 all'ultima versione:

   .. code-block:: shell

      sudo rpi-eeprom-update -a
      sudo reboot

#. Forza la velocità PCIe Gen3 aggiungendo la seguente riga a ``/boot/firmware/config.txt``:

   .. code-block:: text

      dtparam=pciex1_gen=3

#. Disabilita ASPM (Active State Power Management) aggiungendo ``pcie_aspm=off`` alla riga di comando del kernel. Modifica ``/boot/firmware/cmdline.txt`` e aggiungilo alla riga esistente (**non** creare una nuova riga):

   .. code-block:: text

      pcie_aspm=off

   .. note::

      ``pcie_aspm=off`` spesso rappresenta la soluzione critica — i problemi ASPM PCIe sono molto comuni sul Raspberry Pi 5 e possono causare la disconnessione casuale degli NVMe o il riavvio del sistema durante I/O intensivi.

#. Dopo aver applicato le modifiche sopra, riavvia il Raspberry Pi:

   .. code-block:: shell

      sudo reboot

#. Se il problema persiste, ripartiziona e riformatta l'SSD NVMe, poi reinstalla il sistema operativo.

.. end_faq_nvme_link_down


Come cambiare l'ordine di avvio del Raspberry Pi usando i comandi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_boot_order_command

Se hai già effettuato l'accesso al tuo Raspberry Pi, puoi cambiare l'ordine di avvio usando i comandi.

* |link_configure_boot_ssd|

.. end_faq_boot_order_command


Come modificare l'ordine di avvio con Raspberry Pi Imager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_boot_order_imager

Oltre a modificare ``BOOT_ORDER`` nella configurazione EEPROM, puoi anche usare Raspberry Pi Imager per cambiare l'ordine di avvio.

* |link_update_bootloader|

.. end_faq_boot_order_imager


Come copiare il sistema dalla scheda SD a un SSD NVMe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_5`

.. start_faq_copy_sd_to_nvme

Se non disponi di un adattatore NVMe-USB, puoi prima installare il sistema su una scheda Micro SD, quindi copiare il sistema sull'SSD NVMe dopo aver avviato con successo.

* |link_copy_sd_to_nvme|

.. end_faq_copy_sd_to_nvme



6. Utilizzo avanzato
-------------------------------


Come rimuovere la pellicola protettiva
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_remove_film

Due pannelli in acrilico sono inclusi nella confezione, entrambi coperti da pellicola protettiva gialla/trasparente su entrambi i lati per prevenire graffi.

La pellicola protettiva potrebbe essere difficile da rimuovere. Usa un cacciavite per sollevare delicatamente un angolo, quindi stacca con attenzione l'intera pellicola.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. end_faq_remove_film
