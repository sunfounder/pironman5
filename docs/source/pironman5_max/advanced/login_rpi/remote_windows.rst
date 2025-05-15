.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Enthusiasten aus.

    **Warum beitreten?**

    - **Expertensupport**: Löse nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Einblicke**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Vorschauen.
    - **Sonderrabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und saisonalen Sonderaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

Für Windows-Benutzer
=======================

Für Windows 10 oder neuere Versionen kann der Remote-Login auf einen Raspberry Pi mit den folgenden Schritten durchgeführt werden:

#. Suche nach ``powershell`` im Windows-Suchfeld. Klicke mit der rechten Maustaste auf ``Windows PowerShell`` und wähle ``Run as administrator`` aus.

   .. image:: img/powershell_ssh.png
      :width: 90%


#. Bestimme die IP-Adresse deines Raspberry Pi, indem du ``ping -4 <hostname>.local`` in PowerShell eingibst.

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%



   Die IP-Adresse des Raspberry Pi wird angezeigt, sobald er mit dem Netzwerk verbunden ist.

   * Wenn das Terminal ``Ping request could not find host pi.local. Please check the name and try again.`` anzeigt, überprüfe den eingegebenen Hostnamen auf Richtigkeit.
   * Wenn die IP-Adresse immer noch nicht abgerufen werden kann, überprüfe die Netzwerk- oder WiFi-Einstellungen auf dem Raspberry Pi.

#. Sobald die IP-Adresse bestätigt wurde, melde dich mit ``ssh <username>@<hostname>.local`` oder ``ssh <username>@<IP address>`` an.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Wenn eine Fehlermeldung erscheint, dass ``The term 'ssh' is not recognized as the name of a cmdlet...`` erkannt wird, könnten die SSH-Tools auf deinem System nicht vorinstalliert sein. In diesem Fall musst du OpenSSH manuell installieren, wie unter :ref:`max_openssh_powershell` beschrieben, oder ein Drittanbieter-Tool wie |link_putty| verwenden.

#. Bei deiner ersten Anmeldung erscheint eine Sicherheitsnachricht. Gib ``yes`` ein, um fortzufahren.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Gib das Passwort ein, das du zuvor festgelegt hast. Beachte, dass das Passwort während der Eingabe nicht angezeigt wird, was eine gängige Sicherheitsmaßnahme ist.

    .. note::
        Es ist normal, dass die Zeichen des Passworts beim Tippen nicht angezeigt werden. Achte darauf, das richtige Passwort einzugeben.

#. Sobald die Verbindung hergestellt ist, ist dein Raspberry Pi bereit für Remote-Operationen.

   .. image:: img/sp221221_140628.png
      :width: 90%
      
