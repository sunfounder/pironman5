.. note:: 

    Ciao, benvenuto nella community Facebook degli appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e difficoltà tecniche con l’aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Condividi suggerimenti e tutorial per sviluppare al meglio le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotto e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti riservati sui prodotti più innovativi.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e concorsi a premi.

    👉 Pronto a scoprire e creare con noi? Clicca su [|link_sf_facebook|] ed entra a far parte della community oggi stesso!

Per utenti Windows
=======================

Gli utenti di Windows 10 o versioni successive possono accedere da remoto a un Raspberry Pi seguendo questi passaggi:

#. Cerca ``powershell`` nella barra di ricerca di Windows. Fai clic destro su ``Windows PowerShell`` e seleziona ``Esegui come amministratore``.

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. Ottieni l’indirizzo IP del tuo Raspberry Pi digitando ``ping -4 <hostname>.local`` in PowerShell.

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%
      

   L’indirizzo IP del Raspberry Pi verrà visualizzato non appena sarà connesso alla rete.

   * Se viene mostrato il messaggio ``Ping request could not find host pi.local. Please check the name and try again.``, verifica di aver digitato correttamente l’hostname.
   * Se non riesci ancora a recuperare l’indirizzo IP, controlla le impostazioni di rete o WiFi sul Raspberry Pi.

#. Una volta confermato l’indirizzo IP, accedi al tuo Raspberry Pi utilizzando ``ssh <username>@<hostname>.local`` oppure ``ssh <username>@<IP address>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Se compare un errore come ``The term 'ssh' is not recognized as the name of a cmdlet...``, il tuo sistema potrebbe non avere gli strumenti SSH preinstallati. In tal caso, installa manualmente OpenSSH seguendo le istruzioni in :ref:`max_openssh_powershell`, oppure utilizza uno strumento di terze parti come |link_putty|.

#. Al primo accesso, comparirà un messaggio di sicurezza. Digita ``yes`` per continuare.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Inserisci la password precedentemente impostata. Ricorda che, per motivi di sicurezza, i caratteri non verranno visualizzati durante la digitazione.

    .. note::
        È normale che i caratteri della password non siano visibili durante la digitazione. Assicurati semplicemente di inserirla correttamente.

#. Una volta connesso, il tuo Raspberry Pi sarà pronto per l’utilizzo da remoto.

   .. image:: img/sp221221_140628.png
      :width: 90%

