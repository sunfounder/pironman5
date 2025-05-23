.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Per utenti Linux/Unix
==========================

#. Individua e apri il **Terminale** sul tuo sistema Linux/Unix.

#. Assicurati che il tuo Raspberry Pi sia connesso alla stessa rete. Verifica digitando `ping <hostname>.local`. Ad esempio:

    .. code-block::

        ping raspberrypi.local

    Dovresti vedere l'indirizzo IP del Raspberry Pi se è connesso alla rete.

    * Se il terminale mostra un messaggio come ``Impossibile trovare l'host pi.local. Controllare il nome e riprovare.``, ricontrolla il nome host che hai inserito.
    * Se non riesci a recuperare l'indirizzo IP, controlla le impostazioni di rete o WiFi sul Raspberry Pi.

#. Avvia una connessione SSH digitando ``ssh <username>@<hostname>.local`` oppure ``ssh <username>@<indirizzo IP>``. Ad esempio:

    .. code-block::

        ssh pi@raspberrypi.local

#. Al primo accesso, riceverai un messaggio di sicurezza. Digita ``yes`` per procedere.

    .. code-block::

        L'autenticità dell'host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' non può essere verificata.
        L'impronta digitale della chiave ED25519 è SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Sei sicuro di voler continuare la connessione (yes/no/[fingerprint])?

#. Inserisci la password che hai impostato in precedenza. Nota che, per motivi di sicurezza, la password non sarà visibile mentre la digiti.

    .. note::
        È normale che i caratteri della password non vengano visualizzati nel terminale. Assicurati solo di inserire la password corretta.

#. Una volta effettuato l'accesso con successo, il tuo Raspberry Pi è ora connesso e sei pronto a procedere al passaggio successivo.

