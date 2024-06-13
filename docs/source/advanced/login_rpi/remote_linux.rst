.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Für Linux/Unix-Benutzer
==========================

#. Suchen und öffnen Sie das **Terminal** auf Ihrem Linux/Unix-System.

#. Stellen Sie sicher, dass Ihr Raspberry Pi mit demselben Netzwerk verbunden ist. Überprüfen Sie dies, indem Sie ``ping <hostname>.local`` eingeben. Zum Beispiel:

    .. code-block::

        ping raspberrypi.local

    Sie sollten die IP-Adresse des Raspberry Pi sehen, wenn er mit dem Netzwerk verbunden ist.

    * Wenn das Terminal eine Nachricht wie ``Ping request could not find host pi.local. Please check the name and try again.`` anzeigt, überprüfen Sie den eingegebenen Hostnamen.
    * Wenn Sie die IP-Adresse nicht abrufen können, überprüfen Sie Ihre Netzwerk- oder WLAN-Einstellungen auf dem Raspberry Pi.

#. Starten Sie eine SSH-Verbindung, indem Sie ``ssh <Benutzername>@<hostname>.local`` oder ``ssh <Benutzername>@<IP-Adresse>`` eingeben. Zum Beispiel:

    .. code-block::

        ssh pi@raspberrypi.local

#. Beim ersten Anmelden erhalten Sie eine Sicherheitsmeldung. Geben Sie ``yes`` ein, um fortzufahren.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Geben Sie das zuvor festgelegte Passwort ein. Beachten Sie, dass das Passwort aus Sicherheitsgründen beim Tippen nicht sichtbar ist.

    .. note::
        Es ist normal, dass die Passwortzeichen im Terminal nicht angezeigt werden. Stellen Sie einfach sicher, dass Sie das richtige Passwort eingeben.

#. Sobald Sie sich erfolgreich angemeldet haben, ist Ihr Raspberry Pi verbunden und Sie können mit dem nächsten Schritt fortfahren.

