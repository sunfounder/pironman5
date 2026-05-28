.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _openclaw_5_standard:

.. start_using_openclaw

Verwendung von OpenClaw
========================================

**Was ist OpenClaw?**

Stellen Sie es sich als eine verbesserte Version von ChatGPT vor. Während traditionelle Chatbots nur sprechen (Text generieren) können, kann OpenClaw handeln. Es versteht Ihre Anweisungen in natürlicher Sprache und kann tatsächlich Aktionen auf Ihrem Computer ausführen, wie z.B. Befehle ausführen, Dateien verwalten und verschiedene Werkzeuge aufrufen.

Hier sind einige fantastische Anwendungsszenarien:

* **Persönlicher Allround-Assistent:** Lassen Sie es Ihnen helfen, Ihren Zeitplan zu verwalten, Erinnerungen einzurichten und Aufgaben zu verfolgen. Sie müssen es nur in einer Chat-App (wie Telegram, WhatsApp) anweisen, und es wird sich daran erinnern und die Aktion ausführen.
* **Automatisierungs-"Kleber":** Es kann als Bindeglied für Ihre verschiedenen Dienste fungieren. Sie können es zum Beispiel anweisen, eine Website auf Preisänderungen zu überwachen. Sobald ein Preisverfall erkannt wird, kann es automatisch einen n8n-Automatisierungsworkflow auslösen, um Ihnen eine E-Mail-Benachrichtigung zu senden.
* **Dedizierter Entwicklungsassistent:** Lassen Sie es Ihnen bei der Serververwaltung, dem Ausführen von Skripten und dem Überprüfen von Protokollen helfen. Sie können einfach sagen: "Überprüfe für mich die Systemlast", und es kann eine SSH-Verbindung zu Ihrem Server herstellen, den Befehl ausführen und die Ergebnisse zurückgeben.
* **Hardware-"Spielkamerad":** Dies ist ein sehr interessanter Anwendungsfall. Sie können OpenClaw verwenden, um Hardware zu steuern, die mit einem Raspberry Pi verbunden ist. Ein Entwickler nutzte es beispielsweise, um einen Staubsaugerroboter mit einem Roboterarm zu steuern, oder ließ es sogar helfen, Renndaten zu analysieren und auf einem LED-Bildschirm anzuzeigen. Das offizielle Raspberry Pi-Team nutzte es sogar, um eine automatische Fotobox für eine Hochzeit zu bauen – nur durch Konversation, ohne eine einzige Zeile Code zu schreiben!

**Warum OpenClaw auf einem Raspberry Pi installieren?**

Die Installation auf einem Raspberry Pi hat zwei Hauptvorteile:

* **Sicherheitsisolierung:** OpenClaw benötigt höhere Systemberechtigungen, was auf einem Hauptcomputer ein Risiko darstellt. Die Verwendung eines Raspberry Pi als dediziertes Gerät ist wie eine "Sandkasten"-Umgebung; selbst wenn etwas schiefgeht, hat dies keine Auswirkungen auf Ihr Hauptsystem.
* **24/7 online:** Der Raspberry Pi hat einen extrem geringen Stromverbrauch, sodass er dauerhaft eingeschaltet bleiben kann, um jederzeit Aufgaben auszuführen.

----------------------------------------------------------------

Schnellstart mit OpenClaw
------------------------------

Wenn Sie die Leistungsfähigkeit von OpenClaw so schnell wie möglich erleben möchten, verwenden Sie diese Methode. Sie installiert automatisch und startet einen interaktiven Setup-Assistenten.

1.  Öffnen Sie das Terminal auf Ihrem Raspberry Pi und führen Sie den folgenden Befehl direkt aus. Dieser Befehl lädt das Installationsskript von der offiziellen Website herunter und führt es aus:

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash
   
    .. note:: Da neue Versionen schnell aktualisiert werden, ist es normal, dass Ihre Installationsschritte leicht abweichen.

2.  Das Skript lädt OpenClaw automatisch herunter und installiert es.

    .. image:: /pironman5/home_server/img/openclaw/install_open_claw.png


3.  Anschließend sehen Sie eine Sicherheitsabfrage, ob Sie OpenClaw vertrauen. Wenn Sie sicher sind, dass es sicher und zuverlässig ist, navigieren Sie mit den Pfeiltasten zu "Yes" und drücken Sie die Eingabetaste.

    .. image:: /pironman5/home_server/img/openclaw/security_open_claw.png


4.  Wählen Sie "Quick Start" und drücken Sie die Eingabetaste.

    .. image:: /pironman5/home_server/img/openclaw/quickstart_open_claw.png

5.  Wählen Sie Ihr Modell (Model) und drücken Sie die Eingabetaste. Hier verwenden wir OpenAI als Beispiel.

    .. image:: /pironman5/home_server/img/openclaw/model_provider_open_claw.png

6.  Wählen Sie "OpenAI API Key".

    .. image:: /pironman5/home_server/img/openclaw/api_key_open_claw.png

7.  Fügen Sie jetzt den API-Schlüssel ein.

    .. image:: /pironman5/home_server/img/openclaw/paste_api_key_open_claw.png

8.  Gehen Sie zur |link_openai_platform| und melden Sie sich an. Klicken Sie auf der Seite **API keys** auf **Create new secret key**.

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_create.png

9.  Füllen Sie die Details aus (Owner, Name, Project und bei Bedarf Berechtigungen) und klicken Sie dann auf **Create secret key**.

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_create_confirm.png

10. Sobald der Schlüssel erstellt wurde, kopieren Sie ihn sofort – Sie werden ihn nicht wieder sehen können. Wenn Sie ihn verlieren, müssen Sie einen neuen generieren.

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_copy.png

11. Fügen Sie den Schlüssel in die OpenClaw-Konfiguration ein.

    .. image:: /pironman5/home_server/img/openclaw/paste_api_key_enter_open_claw.png

12. Wählen Sie das Modell (Model) aus, das Sie verwenden möchten. In diesem Beispiel werden wir **Keep current** verwenden.

    .. image:: /pironman5/home_server/img/openclaw/model_config_open_claw.png

13. Als nächstes folgt die Kanalauswahl (Channel). Kanäle beziehen sich auf die von OpenClaw unterstützten Kommunikationsdienste wie Telegram, WhatsApp, Discord und mehr. Verwenden Sie die Pfeiltaste nach unten, um die Option "Skip for now" auszuwählen, und drücken Sie dann die Eingabetaste.

    .. image:: /pironman5/home_server/img/openclaw/channel_open_claw.png

14. Als Nächstes werden Sie gefragt, ob Sie jetzt Fähigkeiten (Skills) konfigurieren möchten. Wählen Sie "Yes" und drücken Sie die Eingabetaste.

    .. image:: /pironman5/home_server/img/openclaw/config_skill_open_claw.png

15. Installieren Sie die benötigten Fähigkeiten. Im folgenden Beispiel wählen wir die Option "Skip for now" (drücken Sie die Leertaste zur Auswahl) und drücken dann die Eingabetaste.

    .. image:: /pironman5/home_server/img/openclaw/install_skill_open_claw.png


16. Als nächstes kommen die Hooks; wir werden "command-logger" und "session-memory" auswählen.

    .. image:: /pironman5/home_server/img/openclaw/hooks2_open_claw.png


17. Die Installation ist nun abgeschlossen. Sie können OpenClaw starten, indem Sie "Hatch in TUI" auswählen und die Eingabetaste drücken.

   .. image:: /pironman5/home_server/img/openclaw/hatch_open_claw.png


.. note:: 
   
   Sie können OpenClaw auch starten, indem Sie den folgenden Befehl eingeben:

    .. code-block:: bash

       openclaw tui

   Sie können die TUI-Oberfläche durch zweimaliges Drücken von Strg+c verlassen.




-----------------------------------------------------

.. end_using_openclaw

OpenClaw zur Bedienung des Pironman5 befähigen
----------------------------------------------------

Um OpenClaw zu ermöglichen, den Pironman5 zu bedienen, müssen wir die Pironman5-Fähigkeit (Skill) installieren.

1.  Stellen Sie sicher, dass Sie Pironman5 bereits installiert haben. Falls nicht, lesen Sie bitte :ref:`install_pironman5_module_5`.

2.  Führen Sie den folgenden Befehl im Terminal aus:

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-skill/ ~/.openclaw/skills/pironman5-skill/

3.  Sie können nun den Pironman5 in ``openclaw tui`` bedienen. Versuchen Sie, Befehle in der TUI zu senden, z.B. versuchen Sie, die LED-Leuchten am Gehäuse einzuschalten, deren Farbe zu ändern oder die Kamera ein Foto machen zu lassen. Sie können ihm sogar sagen, dass Sie ein DHT11-Modul an GPIO17 angeschlossen haben, und es die Temperatur auslesen lassen.

   .. note:: Wenn OpenClaw den importierten Skill immer noch nicht erkennt, erinnern Sie es bitte an rsync.

---------------------------------------

.. start_using_openclaw_telegram

Bedienen Sie Ihr System mit Telegram
---------------------------------------


**Überblick**

Über OpenClaw können Sie gängige Messaging-Apps nutzen, um Ihr System zu bedienen (hier verwenden wir Telegram als Beispiel). Sie können OpenClaw sogar diese Konfiguration für Sie erledigen lassen.

Fragen Sie einfach in ``openclaw tui``: *"Ich möchte dich mit Telegram verbinden, was soll ich tun?"*

Es wird Sie Schritt für Schritt durch den Prozess führen, und Sie können seinen Anweisungen folgen, um die Einrichtung abzuschließen.


**Voraussetzungen**

Bevor Sie beginnen, stellen Sie sicher, dass Sie Folgendes haben:

- Ein **Telegram-Konto**
- Netzwerkzugang zu Telegram
- OpenClaw läuft erfolgreich (überprüfen mit ``openclaw status``)

**Schritt 1: Einen Telegram-Bot erstellen**

1. **Finden Sie @BotFather auf Telegram** (den offiziellen Bot-Ersteller)
2. **Erstellen Sie einen neuen Bot**: Senden Sie den Befehl ``/newbot``
3. **Folgen Sie den Anweisungen**:

   - Geben Sie Ihrem Bot einen Namen (z.B. ``Mein OpenClaw Helfer``)
   - Legen Sie einen Benutzernamen für Ihren Bot fest (muss auf ``bot`` enden, z.B. ``mein_openclaw_bot``)

4. **Bei Erfolg erhalten Sie eine Nachricht** mit Ihrem **Bot-Token**, ähnlich wie:

   .. code-block:: text

      1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

   .. warning:: Hüten Sie dieses Token wie ein Passwort!

**Schritt 2: Telegram in OpenClaw konfigurieren**

Sagen Sie in ``openclaw tui`` direkt:

> *"Ich möchte meinen Telegram-Bot mit OpenClaw verbinden. Hier ist mein Bot-Token: <ihr-token-hier>. Bitte helfen Sie mir, die Konfiguration abzuschließen."*

OpenClaw wird automatisch:

- Notwendige Abhängigkeiten installieren (wie ``node-telegram-bot-api``)
- Die Telegram-Gateway-Konfigurationsdatei erstellen
- Testen, ob die Verbindung erfolgreich ist


**Schritt 3: Die Verbindung testen**

1. Finden Sie Ihren neu erstellten Bot auf Telegram
2. Senden Sie den Befehl ``/start``
3. Der Bot sollte mit einem Pairing-Code antworten, senden Sie diesen Code an die OpenClaw TUI (z.B. ``Pairing code: ZAN4XI34``)
4. Warten Sie, bis es korrekt konfiguriert ist
5. Versuchen Sie, einfache Befehle wie "Hallo" zu senden
6. Wenn alles richtig konfiguriert ist, sollten Sie die Antwort von Ihrem Bot sehen

**Schritt 4: Genießen Sie es!**

Nach Abschluss dieser Konfiguration können Sie:

* Ihren Raspberry Pi jederzeit und überall über Telegram steuern
* Befehle remote ausführen und den Systemstatus überprüfen
* Physische Geräte durch Integration von GPIO steuern (wie das Einschalten von LEDs)
* Eine intelligente interaktive Erfahrung mit Ihrem KI-Assistenten genießen


**Sicherheitskonfiguration (Entscheidend!)**

Um zu verhindern, dass Fremde Ihr System steuern, implementieren Sie unbedingt die folgenden Sicherheitsmaßnahmen:

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Sicherheitsmaßnahme
     - Konfigurationsmethode
     - Beschreibung
   * - Benutzer einschränken
     - Setzen Sie ``allowedUsers`` in der Konfiguration
     - Erlauben Sie nur bestimmten Telegram-Benutzern den Zugriff
   * - Passwort festlegen
     - Fügen Sie ``"password": "ihr-passwort"`` in die Konfiguration ein
     - Erfordert Passwortverifizierung vor Befehlen
   * - Befehle einschränken
     - Erstellen Sie eine Befehls-Weißliste
     - Erlauben Sie nur bestimmte vordefinierte Befehle
   * - Audit-Logs
     - Aktivieren Sie den ``command-logger`` Hook
     - Protokollieren Sie alle über Telegram ausgeführten Befehle


**Denken Sie daran: Sicherheit geht vor!** Schränken Sie Benutzer und Befehlsumfang immer angemessen ein. Wenn Sie bei der Konfiguration auf spezifische Probleme stoßen, zögern Sie nicht, um Hilfe zu bitten.

-------------------------------------

.. end_using_openclaw_telegram

.. start_using_openclaw_faq

OpenClaw Fehlerbehebung
-------------------------------------

F. Während der Installation erhalte ich den Fehler ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``. Was soll ich tun?

   Sie können dies vorerst ignorieren, könnten aber in den nächsten Schritten auf Probleme stoßen. Bitte beheben Sie diese dann Schritt für Schritt.


F. Wenn ich ``openclaw tui`` ausführe, erhalte ich den Fehler ``-bash: openclaw: command not found``. Was soll ich tun?

   Führen Sie den folgenden Befehl aus:

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   Sie sollten nun in der Lage sein, die TUI-Oberfläche mit ``openclaw tui`` zu starten.



F. In ``openclaw tui`` erhalte ich die Meldung ``not connected to gateway — message not sent`` oder die Meldung ``gateway disconnected: closed``.

   Das liegt daran, dass Ihr OpenClaw Gateway-Dienst nicht gestartet ist. Öffnen Sie ein weiteres Terminal und führen Sie den folgenden Befehl aus, um das OpenClaw Gateway zu starten:

   .. code-block:: bash

      openclaw gateway

   Starten Sie dann ``openclaw tui`` neu, und Sie können es direkt verwenden.


F. Ich möchte den OpenClaw Gateway-Dienst so einrichten, dass er im Hintergrund läuft / automatisch beim Booten startet. Wie mache ich das?

   Normalerweise sollte Ihr OpenClaw Gateway-Dienst automatisch beim Booten starten. Falls nicht, können Sie ihn mit dem folgenden Befehl manuell starten.

   1. Erstellen Sie das Verzeichnis ``~/.config/systemd/user``:

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user


   2. Erstellen Sie die Datei ``openclaw-gateway.service``:

   .. code-block:: bash

      cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
      [Unit]
      Description=OpenClaw Gateway
      After=network.target

      [Service]
      Type=simple
      ExecStart=$HOME/.npm-global/bin/openclaw gateway run
      Restart=on-failure
      RestartSec=10
      Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
      Environment="NODE_ENV=production"

      [Install]
      WantedBy=default.target
      EOF


   3. Laden Sie dann die systemd-Konfiguration neu:

   .. code-block:: bash

      systemctl --user daemon-reload

   4. Starten Sie den Dienst:

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   Starten Sie nun ``openclaw tui`` neu, und Sie können es direkt verwenden.

   5. Aktivieren Sie den automatischen Start beim Booten:

   .. code-block:: bash

      systemctl --user enable openclaw-gateway


F. Mein OpenClaw kann das System nicht bedienen, was soll ich tun?

   Ein neu installiertes OpenClaw hat standardmäßig möglicherweise keine Berechtigung, Ihr Raspberry-Pi-System zu bedienen; es kann nur chatten. Wir müssen die Berechtigungen manuell konfigurieren.

   1.  Öffnen Sie die OpenClaw-Konfigurationsdatei:

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  Suchen Sie die Option ``tools`` und ändern Sie das ``profile`` und ``exec`` wie folgt.

      .. code-block:: json

        "tools": {
            "profile": "coding",
            "exec": {
               "secrity": "full"
            }
        },


   3.  Speichern und schließen.

   4.  Geben Sie den folgenden Befehl im Terminal ein, um das OpenClaw Gateway neu zu starten:

      .. code-block:: bash

         openclaw gateway restart

   Jetzt sollte OpenClaw Lese- und Schreibrechte haben und in der Lage sein, Ihr Raspberry-Pi-System zu bedienen.

.. end_using_openclaw_faq