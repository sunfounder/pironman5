.. note::

    Hallo und herzlich willkommen in der SunFounder-Community für Raspberry Pi-, Arduino- und ESP32-Enthusiasten auf Facebook! Tauche gemeinsam mit anderen Technikbegeisterten noch tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum solltest du beitreten?**

    - **Expertenhilfe**: Erhalte Unterstützung bei technischen Problemen und Fragen nach dem Kauf – direkt durch unsere Community und unser Support-Team.
    - **Lernen & Teilen**: Teile Tipps und Tutorials, um dein Wissen zu erweitern.
    - **Exklusive Vorschauen**: Erfahre als Erste:r von neuen Produktankündigungen und erhalte exklusive Einblicke.
    - **Sonderrabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Aktionen & Verlosungen**: Nimm an saisonalen Gewinnspielen und Sonderaktionen teil.

    👉 Bereit, mit uns gemeinsam zu entdecken und kreativ zu werden? Klicke auf [|link_sf_facebook|] und werde noch heute Mitglied!

Für Windows-Nutzer
=======================

Für Nutzer von Windows 10 oder höher ist der Fernzugriff auf den Raspberry Pi über die folgenden Schritte möglich:

#. Gib im Suchfeld von Windows ``powershell`` ein. Klicke mit der rechten Maustaste auf ``Windows PowerShell`` und wähle ``Run as administrator``.

   .. image:: img/powershell_ssh.png
      :width: 90%


#. Ermittle die IP-Adresse deines Raspberry Pi, indem du in PowerShell den Befehl ``ping -4 <hostname>.local`` eingibst.

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%


   Sobald der Raspberry Pi mit dem Netzwerk verbunden ist, wird seine IP-Adresse angezeigt.

   * Falls die Meldung ``Ping request could not find host pi.local. Please check the name and try again.`` erscheint, überprüfe den eingegebenen Hostnamen sorgfältig.
   * Wenn weiterhin keine IP-Adresse ermittelt werden kann, kontrolliere die Netzwerk- oder WLAN-Einstellungen deines Raspberry Pi.

#. Sobald die IP-Adresse bestätigt wurde, melde dich mit dem Befehl ``ssh <username>@<hostname>.local`` oder ``ssh <username>@<IP address>`` bei deinem Raspberry Pi an.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Falls eine Fehlermeldung erscheint wie ``The term 'ssh' is not recognized as the name of a cmdlet...``, ist SSH auf deinem System nicht vorinstalliert. In diesem Fall musst du OpenSSH manuell installieren – siehe :ref:`openssh_powershell_mini` – oder ein Drittanbieter-Tool wie |link_putty| verwenden.

#. Beim ersten Login erscheint eine Sicherheitsabfrage. Gib ``yes`` ein, um fortzufahren.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Gib das zuvor vergebene Passwort ein. Beachte, dass bei der Eingabe keine Zeichen im Terminal erscheinen – das ist ein Sicherheitsmechanismus.

    .. note::
        Es ist normal, dass beim Eintippen des Passworts keine Zeichen angezeigt werden. Achte einfach darauf, das richtige Passwort einzugeben.

#. Nach erfolgreicher Verbindung ist dein Raspberry Pi bereit für den Fernzugriff.

   .. image:: img/sp221221_140628.png
      :width: 90%

