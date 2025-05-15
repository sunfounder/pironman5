.. note::

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Entdecke gemeinsam mit anderen Technikbegeisterten noch mehr rund um Raspberry Pi, Arduino und ESP32.

    **Warum solltest du beitreten?**

    - **Expertenhilfe**: Erhalte Unterstützung bei technischen Problemen und Fragen nach dem Kauf – direkt durch unsere Community und unser Team.
    - **Lernen & Teilen**: Teile Tipps und Tutorials, um deine Fähigkeiten auszubauen.
    - **Exklusive Vorschauen**: Erfahre frühzeitig von neuen Produkten und erhalte exklusive Einblicke.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Aktionen & Verlosungen**: Nimm an saisonalen Aktionen und Gewinnspielen teil.

    👉 Bereit, mit uns zu entdecken und kreativ zu werden? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

Für Linux-/Unix-Nutzer
==========================

#. Öffne das **Terminal** auf deinem Linux- oder Unix-System.

#. Stelle sicher, dass dein Raspberry Pi mit demselben Netzwerk verbunden ist. Überprüfe dies mit folgendem Befehl: `ping <hostname>.local`. Zum Beispiel:

    .. code-block::

        ping raspberrypi.local

    Wenn der Raspberry Pi korrekt verbunden ist, wird seine IP-Adresse angezeigt.

    * Falls die Meldung erscheint: ``Ping request could not find host pi.local. Please check the name and try again.``, überprüfe bitte den eingegebenen Hostnamen sorgfältig.
    * Wenn keine IP-Adresse zurückgegeben wird, kontrolliere die Netzwerk- oder WLAN-Einstellungen deines Raspberry Pi.

#. Stelle die SSH-Verbindung her, indem du ``ssh <username>@<hostname>.local`` oder ``ssh <benutzername>@<IP-Adresse>`` eingibst. Zum Beispiel:

    .. code-block::

        ssh pi@raspberrypi.local

#. Beim ersten Verbindungsaufbau erscheint eine Sicherheitsabfrage. Bestätige mit ``yes``, um fortzufahren.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Gib nun das zuvor gesetzte Passwort ein. Aus Sicherheitsgründen wird bei der Eingabe nichts im Terminal angezeigt.

    .. note::
        Es ist völlig normal, dass beim Eingeben des Passworts keine Zeichen im Terminal erscheinen. Gib es einfach korrekt ein und bestätige mit Enter.

#. Nach erfolgreicher Anmeldung bist du mit deinem Raspberry Pi verbunden und kannst mit dem nächsten Schritt fortfahren.
