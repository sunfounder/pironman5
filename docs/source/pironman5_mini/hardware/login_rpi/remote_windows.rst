.. note:: 

    Ciao, benvenuto nella community Facebook di appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche grazie al supporto del nostro team e della community.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri ultimi prodotti.
    - **Promozioni festive e giveaway**: Partecipa a concorsi e iniziative promozionali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] ed entra oggi stesso!

Per Utenti Windows
=======================

Per gli utenti Windows 10 o versioni successive, l’accesso remoto a un Raspberry Pi può essere effettuato seguendo questi passaggi:

#. Cerca ``powershell`` nella barra di ricerca di Windows. Fai clic con il tasto destro su ``Windows PowerShell`` e seleziona ``Esegui come amministratore``.

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. Identifica l’indirizzo IP del tuo Raspberry Pi digitando ``ping -4 <hostname>.local`` in PowerShell.

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%
      

   L’indirizzo IP del Raspberry Pi verrà mostrato una volta che il dispositivo è connesso alla rete.

   * Se il terminale visualizza ``Ping request could not find host pi.local. Please check the name and try again.``, verifica che il nome host inserito sia corretto.
   * Se l’indirizzo IP non viene trovato, controlla le impostazioni di rete o Wi-Fi del Raspberry Pi.

#. Una volta confermato l’indirizzo IP, accedi al tuo Raspberry Pi utilizzando ``ssh <username>@<hostname>.local`` oppure ``ssh <username>@<IP address>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Se compare un errore del tipo ``The term 'ssh' is not recognized as the name of a cmdlet...``, è possibile che il tuo sistema non abbia gli strumenti SSH preinstallati. In tal caso, installa manualmente OpenSSH seguendo :ref:`openssh_powershell_mini`, oppure utilizza un programma di terze parti come |link_putty|.

#. Al primo accesso verrà mostrato un messaggio di sicurezza. Digita ``yes`` per continuare.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Inserisci la password precedentemente impostata. Tieni presente che, per motivi di sicurezza, i caratteri della password non verranno visualizzati durante la digitazione.

    .. note::
        È normale che i caratteri della password non vengano mostrati nel terminale. Assicurati semplicemente di digitare la password corretta.

#. Una volta connesso, il tuo Raspberry Pi sarà pronto per l'uso remoto.

   .. image:: img/sp221221_140628.png
      :width: 90%

