.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Enthusiasten aus.

    **Warum beitreten?**

    - **Expertensupport**: Löse nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Einblicke**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und saisonalen Sonderaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

Für Mac OS X Benutzer
==========================

Für Mac OS X-Benutzer bietet SSH (Secure Shell) eine sichere und bequeme Methode, um remote auf einen Raspberry Pi zuzugreifen und ihn zu steuern. Dies ist besonders nützlich, wenn der Raspberry Pi nicht mit einem Monitor verbunden ist oder wenn du ihn aus der Ferne verwalten möchtest. Mit der Terminal-Anwendung auf einem Mac kannst du diese sichere Verbindung herstellen. Der Prozess beinhaltet einen SSH-Befehl, der den Benutzernamen und den Hostnamen des Raspberry Pi enthält. Bei der ersten Verbindung wirst du nach einer Bestätigung der Authentizität des Raspberry Pi gefragt.

#. Um eine Verbindung zum Raspberry Pi herzustellen, gib den folgenden SSH-Befehl ein:

    .. code-block::

        ssh pi@raspberrypi.local

   .. image:: img/mac_vnc14.png

#. Bei deiner ersten Anmeldung erscheint eine Sicherheitsnachricht. Antworte mit **yes**, um fortzufahren.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Gib das Passwort für den Raspberry Pi ein. Beachte, dass das Passwort während der Eingabe nicht auf dem Bildschirm angezeigt wird, was eine standardmäßige Sicherheitsmaßnahme ist.

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $

