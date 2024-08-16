.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum mitmachen?**

    - **Fachkundige Unterstützung**: Lösen Sie nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

Für Windows-Benutzer
=======================

Für Benutzer von Windows 10 oder höher kann der Fernzugriff auf einen Raspberry Pi durch die folgenden Schritte erreicht werden:

#. Suchen Sie nach ``powershell`` in Ihrem Windows-Suchfeld. Klicken Sie mit der rechten Maustaste auf ``Windows PowerShell`` und wählen Sie ``Als Administrator ausführen``.

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. Bestimmen Sie die IP-Adresse Ihres Raspberry Pi, indem Sie ``ping -4 <hostname>.local`` in PowerShell eingeben.

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%
      

   Die IP-Adresse des Raspberry Pi wird angezeigt, sobald es mit dem Netzwerk verbunden ist.

   * Wenn das Terminal anzeigt ``Ping-Anforderung konnte den Host pi.local nicht finden. Bitte überprüfen Sie den Namen und versuchen Sie es erneut.``, vergewissern Sie sich, dass der eingegebene Hostname korrekt ist.
   * Wenn die IP-Adresse immer noch nicht abrufbar ist, überprüfen Sie die Netzwerkeinstellungen oder die WiFi-Konfiguration auf Ihrem Raspberry Pi.

#. Sobald die IP-Adresse bestätigt wurde, melden Sie sich mit ``ssh <username>@<hostname>.local`` oder ``ssh <username>@<IP-Adresse>`` bei Ihrem Raspberry Pi an.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Falls ein Fehler auftritt, der besagt ``Der Begriff 'ssh' wird nicht als Name eines Cmdlets erkannt...``, sind auf Ihrem System möglicherweise keine SSH-Tools vorinstalliert. In diesem Fall müssen Sie OpenSSH manuell installieren, indem Sie :ref:`openssh_powershell` folgen, oder ein Drittanbieter-Tool wie |link_putty| verwenden.

#. Eine Sicherheitsmeldung wird bei Ihrem ersten Login angezeigt. Geben Sie ``yes`` ein, um fortzufahren.

    .. code-block::

        Die Echtheit des Hosts 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' kann nicht bestätigt werden.
        Der ED25519-Schlüsselfingerabdruck ist SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Sind Sie sicher, dass Sie die Verbindung fortsetzen möchten (yes/no/[fingerprint])?

#. Geben Sie das zuvor festgelegte Passwort ein. Beachten Sie, dass die Passwortzeichen aus Sicherheitsgründen nicht auf dem Bildschirm angezeigt werden.

    .. note::
        Das Fehlen sichtbarer Zeichen beim Eingeben des Passworts ist normal. Stellen Sie sicher, dass Sie das korrekte Passwort eingeben.

#. Sobald die Verbindung hergestellt ist, ist Ihr Raspberry Pi bereit für den Fernzugriff.

   .. image:: img/sp221221_140628.png
      :width: 90%
      
