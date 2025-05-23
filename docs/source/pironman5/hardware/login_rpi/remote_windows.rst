.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Per Utenti Windows
=======================

Per gli utenti di Windows 10 o superiore, l'accesso remoto a un Raspberry Pi può essere ottenuto seguendo questi passaggi:

#. Cerca ``powershell`` nella barra di ricerca di Windows. Fai clic con il tasto destro su ``Windows PowerShell`` e seleziona ``Esegui come amministratore``.

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. Determina l'indirizzo IP del tuo Raspberry Pi digitando ``ping -4 <hostname>.local`` in PowerShell.

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%
      

   L'indirizzo IP del Raspberry Pi verrà visualizzato una volta connesso alla rete.

   * Se il terminale visualizza ``Impossibile trovare l'host pi.local. Controlla il nome e riprova.``, verifica che il nome host inserito sia corretto.
   * Se l'indirizzo IP non è ancora recuperabile, controlla le impostazioni di rete o WiFi sul Raspberry Pi.

#. Una volta confermato l'indirizzo IP, accedi al tuo Raspberry Pi utilizzando ``ssh <username>@<hostname>.local`` o ``ssh <username>@<indirizzo IP>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Se appare un errore che indica ``Il termine 'ssh' non è riconosciuto come nome di un cmdlet...``, il tuo sistema potrebbe non avere gli strumenti SSH preinstallati. In questo caso, è necessario installare manualmente OpenSSH seguendo :ref:`openssh_powershell`, oppure utilizzare uno strumento di terze parti come |link_putty|.

#. Durante il primo accesso, apparirà un messaggio di sicurezza. Digita ``yes`` per procedere.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Inserisci la password che hai impostato in precedenza. Nota che i caratteri della password non verranno visualizzati sullo schermo, poiché è una funzione di sicurezza standard.

    .. note::
        L'assenza di caratteri visibili durante la digitazione della password è normale. Assicurati di inserire la password corretta.

#. Una volta connesso, il tuo Raspberry Pi è pronto per le operazioni remote.

   .. image:: img/sp221221_140628.png
      :width: 90%
      
