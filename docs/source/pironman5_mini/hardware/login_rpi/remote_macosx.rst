.. note::

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Entdecke gemeinsam mit anderen Technikbegeisterten die Welt von Raspberry Pi, Arduino und ESP32 noch intensiver.

    **Warum solltest du beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Problemen und Fragen nach dem Kauf – direkt von unserer Community und unserem Team.
    - **Lernen & Teilen**: Teile Tipps und Tutorials, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erfahre frühzeitig von neuen Produktankündigungen und erhalte exklusive Einblicke.
    - **Sonderrabatte**: Profitiere von exklusiven Angeboten auf unsere neuesten Produkte.
    - **Aktionen & Verlosungen**: Nimm an saisonalen Gewinnspielen und Sonderaktionen teil.

    👉 Bereit, mit uns gemeinsam zu entdecken und zu gestalten? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

Für macOS-Nutzer
==========================

Für Nutzer von macOS bietet SSH (Secure Shell) eine sichere und komfortable Möglichkeit, auf den Raspberry Pi aus der Ferne zuzugreifen und ihn zu steuern – besonders praktisch, wenn kein Monitor angeschlossen ist. Über das Terminal auf dem Mac lässt sich eine verschlüsselte Verbindung aufbauen. Dafür benötigst du den Benutzernamen und Hostnamen des Raspberry Pi. Beim ersten Verbindungsaufbau erscheint eine Sicherheitsabfrage zur Bestätigung der Verbindung.

#. Um die Verbindung zum Raspberry Pi herzustellen, gib folgenden SSH-Befehl ein:

    .. code-block::

        ssh pi@raspberrypi.local

   .. image:: img/mac_vnc14.png

#. Beim ersten Login erscheint eine Sicherheitsmeldung. Gib **yes** ein, um fortzufahren.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Gib anschließend das Passwort deines Raspberry Pi ein. Beachte, dass das Passwort beim Tippen aus Sicherheitsgründen nicht angezeigt wird.

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

