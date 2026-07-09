.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _install_os_sd_rpi_promax:

Installazione del Sistema Operativo
===================================================

Prima di utilizzare il tuo Raspberry Pi, devi installare **Raspberry Pi OS** su una scheda microSD.
Questa guida spiega come farlo usando **Raspberry Pi Imager** in modo semplice e adatto ai principianti.

**Componenti Richiesti**

* Un computer (Windows, macOS o Linux)
* Una scheda microSD (16GB o superiore; marche consigliate: SanDisk, Samsung)
* Un lettore di schede microSD

-------------------

.. start_install_imager

1. Installare Raspberry Pi Imager
-------------------------------------------

.. |shared_link_rpi_imager| raw:: html

    <a href="https://www.raspberrypi.com/software/" target="_blank">Raspberry Pi Imager</a>

#. Visita la pagina ufficiale di download di Raspberry Pi Imager: |shared_link_rpi_imager|. Scarica l'installer corretto per il tuo sistema operativo.

   .. image:: img/imager_download.png
      :width: 70%

#. Segui le istruzioni di installazione (lingua, percorso di installazione, conferma). Dopo l'installazione, avvia **Raspberry Pi Imager** dal desktop o dal menu delle applicazioni.

   .. image:: img/imager_install.png
      :width: 90%

.. end_install_imager

-------------------

2. Installare il Sistema Operativo sulla scheda microSD
----------------------------------------------------------------------------------

1. Inserisci la tua scheda microSD nel tuo computer usando un lettore di schede. Esegui il backup di tutti i dati importanti prima di procedere.

   .. image:: img/insert_sd.png
      :width: 90%

2. Quando Raspberry Pi Imager si apre, vedrai la pagina **Device**. Seleziona il tuo modello Raspberry Pi 5 dall'elenco.

   .. image:: img/imager_device.png
      :width: 90%

3. Vai alla sezione **OS** e scegli l'opzione consigliata **Raspberry Pi OS (64-bit)**.

   .. warning::

      Assicurati di scegliere una versione a **64 bit**. Se installi un sistema a **32 bit**, alcuni pacchetti sono disponibili solo per ``aarch64`` (64 bit) e alcune funzionalità potrebbero non installarsi o non funzionare correttamente.

   .. image:: img/imager_os.png
      :width: 90%

4. Nella sezione **Storage**, seleziona la tua scheda microSD.

   .. image:: img/imager_storage.png
      :width: 90%

   .. start_install_os

5. Clicca su **Next** per continuare al passaggio di personalizzazione.

   .. note::

      * Se collegherai un monitor, una tastiera e un mouse direttamente al tuo Raspberry Pi, puoi cliccare su **SKIP CUSTOMISATION**.
      * Se prevedi di configurare il Raspberry Pi in modalità *headless* (accesso remoto Wi-Fi), devi completare le impostazioni di personalizzazione.

   .. image:: img/imager_custom_skip.png
      :width: 90%

#. **Imposta Hostname**

   * Dai al tuo Raspberry Pi un hostname univoco.
   * Puoi connetterti ad esso successivamente usando ``hostname.local``.

   .. image:: img/imager_custom_hostname.png
      :width: 90%

#. **Imposta Localizzazione**

   * Scegli la tua città di riferimento.
   * Imager completerà automaticamente il fuso orario e la disposizione della tastiera in base alla tua selezione, anche se puoi modificarli se necessario. Seleziona Next.

   .. image:: img/imager_custom_local.png
      :width: 90%

#. **Imposta Nome Utente e Password**

   Crea un account utente per il tuo Raspberry Pi.

   .. image:: img/imager_custom_user.png
      :width: 90%

#. **Configura Wi-Fi**

   * Inserisci il tuo **SSID** Wi-Fi (nome della rete) e la **password**.
   * Il tuo Raspberry Pi si connetterà automaticamente al primo avvio.

   .. image:: img/imager_custom_wifi.png
      :width: 90%

#. **Abilita SSH (Opzionale ma Consigliato)**

   * Abilitare SSH ti consente di accedere da remoto dal tuo computer.
   * Puoi accedere usando il tuo nome utente/password o configurare chiavi SSH.

   .. image:: img/imager_custom_ssh.png
      :width: 90%

#. **Abilita Raspberry Pi Connect (Opzionale)**

   Raspberry Pi Connect ti permette di accedere al desktop del tuo Raspberry Pi da un browser web.

   * Attiva **Raspberry Pi Connect**, quindi clicca su **OPEN RASPBERRY PI CONNECT**.

     .. image:: img/imager_custom_connect.png
        :width: 90%

   * Il sito web di Raspberry Pi Connect si aprirà nel tuo browser predefinito. Accedi al tuo account Raspberry Pi ID o registrati se non ne hai ancora uno.

     .. image:: img/imager_custom_open.png
        :width: 90%

   * Nella pagina **New auth key**, crea la tua chiave di autenticazione monouso.

      * Se il tuo account Raspberry Pi ID non fa parte di alcuna organizzazione, seleziona **Create auth key and launch Raspberry Pi Imager**.
      * Se appartieni a una o più organizzazioni, scegline una, quindi crea la chiave e avvia Imager.
      * Assicurati di accendere il tuo Raspberry Pi e collegarlo a Internet prima che la chiave scada.

     .. image:: img/imager_custom_authkey.png
        :width: 90%

   * Il tuo browser potrebbe chiedere di aprire Raspberry Pi Imager — consentilo.

     * Imager si aprirà nella scheda Raspberry Pi Connect, mostrando il token di autenticazione.
     * Se il token non viene trasferito automaticamente, apri la sezione **Having trouble?** sulla pagina Raspberry Pi Connect, copia il token e incollalo manualmente in Imager.

     .. image:: img/imager_custom_connect_token.png
        :width: 90%

#. Rivedi tutte le impostazioni e clicca su **WRITE**.

   .. image:: img/imager_writing.png
      :width: 90%

#. Se la scheda contiene già dati, Raspberry Pi Imager mostrerà un avviso che tutti i dati sul dispositivo verranno cancellati. Ricontrolla di aver selezionato l'unità corretta, quindi clicca su **I UNDERSTAND, ERASE AND WRITE** per continuare.

   .. image:: img/imager_erase.png
      :width: 90%

#. Attendere il completamento della scrittura e della verifica. Quando è finito, Raspberry Pi Imager mostrerà **Write complete!** e un riepilogo delle tue scelte. Il dispositivo di archiviazione verrà espulso automaticamente in modo da poterlo rimuovere in sicurezza.

   .. image:: img/imager_finish.png
        :width: 90%

   .. end_install_os

#. Rimuovi la scheda microSD e inseriscila nello slot sul lato inferiore del tuo Raspberry Pi. Il tuo Raspberry Pi è ora pronto per avviarsi con il nuovo sistema operativo!

   .. image:: img/os_sd_to_pi.jpg
        :width: 70%