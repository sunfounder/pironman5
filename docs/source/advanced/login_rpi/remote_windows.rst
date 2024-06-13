.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Für Windows-Benutzer
=======================

Für Benutzer von Windows 10 oder höher kann die Remote-Anmeldung an einem Raspberry Pi durch die folgenden Schritte erreicht werden:

#. Suchen Sie nach ``powershell`` in Ihrer Windows-Suchleiste. Klicken Sie mit der rechten Maustaste auf ``Windows PowerShell`` und wählen Sie ``Als Administrator ausführen``.

    .. image:: img/powershell_ssh.png
        :align: center

#. Bestimmen Sie die IP-Adresse Ihres Raspberry Pi, indem Sie ``ping -4 <hostname>.local`` in PowerShell eingeben.

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    Die IP-Adresse des Raspberry Pi wird angezeigt, sobald er mit dem Netzwerk verbunden ist.

    * Wenn das Terminal ``Ping request could not find host pi.local. Please check the name and try again.`` anzeigt, überprüfen Sie den eingegebenen Hostnamen.
    * Wenn die IP-Adresse weiterhin nicht abrufbar ist, überprüfen Sie Ihre Netzwerk- oder WLAN-Einstellungen auf dem Raspberry Pi.

#. Sobald die IP-Adresse bestätigt ist, melden Sie sich mit ``ssh <Benutzername>@<hostname>.local`` oder ``ssh <Benutzername>@<IP-Adresse>`` auf Ihrem Raspberry Pi an.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Wenn ein Fehler erscheint, der besagt ``The term 'ssh' is not recognized as the name of a cmdlet...``, sind die SSH-Tools möglicherweise nicht vorinstalliert. In diesem Fall müssen Sie OpenSSH manuell installieren, wie unter :ref:`openssh_powershell` beschrieben, oder ein Drittanbieter-Tool wie |link_putty| verwenden.

#. Bei der ersten Anmeldung erscheint eine Sicherheitsmeldung. Geben Sie ``yes`` ein, um fortzufahren.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Geben Sie das zuvor festgelegte Passwort ein. Beachten Sie, dass die Passwortzeichen aus Sicherheitsgründen nicht auf dem Bildschirm angezeigt werden.

    .. note::
        Das Fehlen sichtbarer Zeichen beim Eingeben des Passworts ist normal. Stellen Sie sicher, dass Sie das richtige Passwort eingeben.

#. Sobald die Verbindung hergestellt ist, ist Ihr Raspberry Pi bereit für Remote-Operationen.

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center
