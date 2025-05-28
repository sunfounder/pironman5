.. note:: 

    Ciao, benvenuto nella community Facebook degli appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Why Join?**

    - **Expert Support**: Risolvi problemi post-vendita e sfide tecniche con il supporto del nostro team e della community.
    - **Learn & Share**: Condividi suggerimenti e tutorial per migliorare le tue competenze.
    - **Exclusive Previews**: Ottieni accesso anticipato a nuovi annunci di prodotto e anteprime esclusive.
    - **Special Discounts**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Festive Promotions and Giveaways**: Partecipa a promozioni festive e giveaway.

    👉 Pronto a scoprire e creare con noi? Clicca su [|link_sf_facebook|] ed entra nella community oggi stesso!

Per utenti Linux/Unix
==========================

#. Trova e apri il **Terminale** sul tuo sistema Linux/Unix.

#. Assicurati che il tuo Raspberry Pi sia connesso alla stessa rete. Verifica digitando `ping <hostname>.local`. Ad esempio:

    .. code-block::

        ping raspberrypi.local

    Dovresti vedere l'indirizzo IP del Raspberry Pi se è correttamente connesso alla rete.

    * Se il terminale mostra un messaggio come ``Ping request could not find host pi.local. Please check the name and try again.``, controlla di nuovo il nome host inserito.
    * Se non riesci a ottenere l'indirizzo IP, verifica le impostazioni di rete o del WiFi sul Raspberry Pi.

#. Avvia una connessione SSH digitando ``ssh <username>@<hostname>.local`` oppure ``ssh <username>@<IP address>``. Ad esempio:

    .. code-block::

        ssh pi@raspberrypi.local

#. Al primo accesso, apparirà un messaggio di sicurezza. Digita ``yes`` per continuare.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Inserisci la password precedentemente impostata. Per motivi di sicurezza, non vedrai i caratteri mentre digiti la password.

    .. note::
        È normale che i caratteri della password non vengano mostrati nel terminale. Assicurati semplicemente di inserirla correttamente.

#. Una volta effettuato l’accesso con successo, il tuo Raspberry Pi sarà connesso e pronto per il passaggio successivo.
