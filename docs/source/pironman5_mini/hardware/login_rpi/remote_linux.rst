.. note:: 

    Ciao, benvenuto nella community Facebook di appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e difficoltà tecniche grazie al supporto del nostro team e della community.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri ultimi prodotti.
    - **Promozioni festive e giveaway**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] ed entra oggi stesso!

Per Utenti Linux/Unix
===========================

#. Trova e apri il **Terminale** sul tuo sistema Linux/Unix.

#. Assicurati che il Raspberry Pi sia connesso alla stessa rete. Puoi verificarlo digitando `ping <hostname>.local`. Ad esempio:

    .. code-block::

        ping raspberrypi.local

    Se il dispositivo è connesso alla rete, dovresti vedere l’indirizzo IP del Raspberry Pi.

    * Se il terminale mostra un messaggio come ``Ping request could not find host pi.local. Please check the name and try again.``, verifica attentamente il nome host inserito.
    * Se non riesci a ottenere l’indirizzo IP, controlla le impostazioni di rete o Wi-Fi del Raspberry Pi.

#. Avvia una connessione SSH digitando ``ssh <username>@<hostname>.local`` oppure ``ssh <username>@<IP address>``. Per esempio:

    .. code-block::

        ssh pi@raspberrypi.local

#. Al primo accesso, riceverai un messaggio di sicurezza. Digita ``yes`` per continuare.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Inserisci la password che hai impostato in precedenza. Per motivi di sicurezza, la password non verrà visualizzata mentre la digiti.

    .. note::
        È normale che i caratteri della password non vengano mostrati nel terminale. Assicurati semplicemente di inserirla correttamente.

#. Dopo aver effettuato l’accesso con successo, il tuo Raspberry Pi è ora connesso e pronto per passare alla fase successiva.
