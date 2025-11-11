.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Enthusiasten aus.

    **Warum beitreten?**

    - **Expertensupport**: Löse nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Einblicke**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und saisonalen Sonderaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

Für Linux/Unix-Benutzer
==========================

#. Finde und öffne das **Terminal** auf deinem Linux/Unix-System.

#. Stelle sicher, dass dein Raspberry Pi mit dem gleichen Netzwerk verbunden ist. Überprüfe dies, indem du `ping <hostname>.local` eingibst. Zum Beispiel:

    .. code-block::

        ping raspberrypi.local

    Du solltest die IP-Adresse deines Raspberry Pi sehen, wenn er mit dem Netzwerk verbunden ist.

    * Wenn das Terminal eine Nachricht wie ``Ping request could not find host pi.local. Please check the name and try again.`` anzeigt, überprüfe den eingegebenen Hostnamen.
    * Wenn du die IP-Adresse nicht abrufen kannst, überprüfe deine Netzwerk- oder WiFi-Einstellungen auf dem Raspberry Pi.

#. Starte eine SSH-Verbindung, indem du ``ssh <username>@<hostname>.local`` oder ``ssh <username>@<IP address>`` eingibst. Zum Beispiel:

    .. code-block::

        ssh pi@raspberrypi.local

#. Bei deiner ersten Anmeldung wirst du eine Sicherheitsnachricht erhalten. Gib ``yes`` ein, um fortzufahren.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Gib das Passwort ein, das du zuvor festgelegt hast. Beachte, dass aus Sicherheitsgründen das Passwort nicht angezeigt wird, während du es eingibst.

    .. note::
        Es ist normal, dass die Zeichen des Passworts nicht im Terminal angezeigt werden. Achte einfach darauf, das richtige Passwort einzugeben.

#. Sobald du dich erfolgreich angemeldet hast, ist dein Raspberry Pi jetzt verbunden und du kannst mit dem nächsten Schritt fortfahren.
