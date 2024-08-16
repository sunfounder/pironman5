.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum mitmachen?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Für Linux/Unix-Benutzer
============================

#. Suchen und öffnen Sie das **Terminal** auf Ihrem Linux/Unix-System.

#. Stellen Sie sicher, dass Ihr Raspberry Pi mit demselben Netzwerk verbunden ist. Überprüfen Sie dies, indem Sie `ping <hostname>.local` eingeben. Zum Beispiel:

    .. code-block::

        ping raspberrypi.local

    Sie sollten die IP-Adresse des Raspberry Pi sehen, wenn er mit dem Netzwerk verbunden ist.

    * Wenn das Terminal eine Nachricht wie ``Ping-Anforderung konnte den Host pi.local nicht finden. Bitte überprüfen Sie den Namen und versuchen Sie es erneut.`` anzeigt, überprüfen Sie den eingegebenen Hostnamen.
    * Wenn Sie die IP-Adresse nicht abrufen können, überprüfen Sie die Netzwerkeinstellungen oder WiFi-Konfiguration Ihres Raspberry Pi.

#. Starten Sie eine SSH-Verbindung, indem Sie ``ssh <username>@<hostname>.local`` oder ``ssh <username>@<IP-Adresse>`` eingeben. Zum Beispiel:

    .. code-block::

        ssh pi@raspberrypi.local

#. Bei Ihrem ersten Login wird eine Sicherheitsmeldung angezeigt. Geben Sie ``yes`` ein, um fortzufahren.

    .. code-block::

        Die Echtheit des Hosts 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' kann nicht bestätigt werden.
        Der ED25519-Schlüsselfingerabdruck ist SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Sind Sie sicher, dass Sie die Verbindung fortsetzen möchten (yes/no/[fingerprint])?

#. Geben Sie das Passwort ein, das Sie zuvor festgelegt haben. Beachten Sie, dass aus Sicherheitsgründen das Passwort beim Tippen nicht angezeigt wird.

    .. note::
        Es ist normal, dass die Passwortzeichen nicht im Terminal angezeigt werden. Stellen Sie einfach sicher, dass Sie das korrekte Passwort eingeben.

#. Sobald Sie sich erfolgreich angemeldet haben, ist Ihr Raspberry Pi verbunden und Sie können mit dem nächsten Schritt fortfahren.
