.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Perché unirsi?**

    - **Supporto esperto**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Impara e condividi**: Exchange tips and tutorials to enhance your skills.
    - **Anteprime esclusive**: Get early access to new product announcements and sneak peeks.
    - **Sconti speciali**: Enjoy exclusive discounts on our newest products.
    - **Promozioni festive e giveaway**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _set_up_umbrel:

Configurazione su Umbrel OS
======================================================================

Se hai installato Umbrel OS sul tuo Raspberry Pi 5, dovrai configurare il Pironman 5 utilizzando la riga di comando. Di seguito sono fornite le istruzioni dettagliate:

#. Collega il tuo Raspberry Pi 5 alla rete utilizzando un cavo Ethernet. Questo passaggio è essenziale per garantire che il Raspberry Pi abbia accesso a Internet.

#. Nel tuo browser, visita: ``http://umbrel.local``.  
   Se la pagina non si apre, controlla nel router l’indirizzo IP del dispositivo Umbrel, ad esempio: ``http://192.168.1.50``

   .. image:: img/umbrel_local.png

#. Crea il tuo account Umbrel impostando un nome utente e una password.  
   Questa password verrà utilizzata per futuri accessi remoti a Umbrel, quindi assicurati di ricordarla.

   .. image:: img/umbrel_account.png

#. Clicca su **Next** per completare la configurazione di Umbrel ed entrare nell’ambiente desktop.

   .. image:: img/umbrel_desktop.png

#. Apri il Terminale. Dal desktop, fai clic sull’icona **Settings**, poi seleziona **Advanced Settings** e clicca su **Open**.

   .. image:: img/umbrel_setting.png

#. Clicca su **Open Terminal**.

   .. image:: img/umbrel_open_terminal.png

#. Puoi scegliere di aprire il terminale in Umbrel OS o all’interno di un’app specifica. Entrambe le opzioni ti porteranno all’interfaccia del terminale.

   .. image:: img/umbrel_terminal.png

#. Procedi a scaricare il codice da GitHub e installare il modulo ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b base https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

#. Dopo aver completato l’installazione, inserisci il seguente comando per riavviare il tuo Raspberry Pi.

   .. code-block:: shell

      sudo reboot

#. Al riavvio, il servizio ``pironman5.service`` verrà avviato automaticamente.  
   Ecco le configurazioni principali di Pironman 5:
   
   * Lo schermo OLED mostra CPU, RAM, utilizzo del disco, temperatura della CPU e indirizzo IP del Raspberry Pi.  
   * Quattro LED WS2812 RGB si illumineranno di blu con un effetto di respirazione.
   * Le ventole RGB sono impostate di default sulla modalità **Always On**. Per temperature di attivazione diverse, consulta :ref:`cc_control_fan`.

#. Puoi utilizzare lo strumento ``systemctl`` per ``start``, ``stop``, ``restart`` o controllare lo ``status`` del servizio ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Usa questo comando per applicare eventuali modifiche alle impostazioni di Pironman 5.  
   * ``start/stop``: Abilita o disabilita il servizio ``pironman5.service``.  
   * ``status``: Controlla lo stato operativo del programma ``pironman5`` utilizzando lo strumento ``systemctl``.

.. note::

   A questo punto hai configurato con successo il Pironman 5 ed è pronto per l’uso.  
   Per il controllo avanzato dei suoi componenti, consulta :ref:`control_commands_dashboard_5`.



