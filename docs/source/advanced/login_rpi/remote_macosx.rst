.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum mitmachen?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Für Mac OS X-Benutzer
==========================

Für Mac OS X-Benutzer bietet SSH (Secure Shell) eine sichere und bequeme Methode, um aus der Ferne auf einen Raspberry Pi zuzugreifen und ihn zu steuern. Dies ist besonders praktisch, wenn Sie mit dem Raspberry Pi arbeiten, während dieser nicht an einen Monitor angeschlossen ist. Mit der Terminal-Anwendung auf einem Mac können Sie diese sichere Verbindung herstellen. Der Prozess beinhaltet einen SSH-Befehl, der den Benutzernamen und Hostnamen des Raspberry Pi einbezieht. Bei der ersten Verbindung wird eine Sicherheitsaufforderung erscheinen, um die Authentizität des Raspberry Pi zu bestätigen.

#. Um eine Verbindung zum Raspberry Pi herzustellen, geben Sie den folgenden SSH-Befehl ein:

    .. code-block::

        ssh pi@raspberrypi.local

   .. image:: img/mac_vnc14.png

#. Eine Sicherheitsmeldung erscheint bei Ihrem ersten Login. Antworten Sie mit **yes**, um fortzufahren.

    .. code-block::

        Die Echtheit des Hosts 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' kann nicht bestätigt werden.
        Der ED25519-Schlüsselfingerabdruck ist SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Sind Sie sicher, dass Sie die Verbindung fortsetzen möchten (yes/no/[fingerprint])?

#. Geben Sie das Passwort für den Raspberry Pi ein. Beachten Sie, dass das Passwort beim Tippen nicht auf dem Bildschirm angezeigt wird, was ein übliches Sicherheitsmerkmal ist.

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        Die im Debian GNU/Linux-System enthaltenen Programme sind freie Software;
        die genauen Lizenzbestimmungen für jedes Programm finden Sie in den
        einzelnen Dateien unter /usr/share/doc/*/copyright.

        Debian GNU/Linux wird ABSOLUT OHNE GEWÄHRLEISTUNG geliefert, soweit
        dies gesetzlich zulässig ist.
        Letzte Anmeldung: Do Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 
