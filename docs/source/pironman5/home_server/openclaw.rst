.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _openclaw_5_standard:

.. start_using_openclaw


En utilisant OpenClaw
========================================

**Qu'est-ce qu'OpenClaw ?**

Considérez-le comme une version améliorée de ChatGPT. Alors que les chatbots traditionnels ne peuvent que parler (générer du texte), OpenClaw peut agir. Il comprend vos instructions en langage naturel et peut effectuer des opérations sur votre ordinateur, comme exécuter des commandes, gérer des fichiers et utiliser divers outils.

Voici quelques scénarios d'application fantastiques :

* **Assistant personnel polyvalent :** Laissez-le vous aider à gérer votre emploi du temps, définir des rappels et suivre vos tâches. Il vous suffit de le lui dire dans une application de chat (comme Telegram, WhatsApp), et il s'en souviendra et exécutera.
* **"Colle" d'automatisation :** Il peut agir comme un liant pour vos différents services. Par exemple, vous pouvez lui demander de surveiller les changements de prix sur un site web. Dès qu'une baisse de prix est détectée, il peut automatiquement déclencher un workflow d'automatisation n8n pour vous envoyer une notification par e-mail.
* **Assistant de développement dédié :** Demandez-lui de vous aider à gérer des serveurs, exécuter des scripts et consulter des journaux. Vous pouvez simplement dire : "Vérifie la charge système pour moi", et il peut se connecter en SSH à votre serveur, exécuter la commande et vous retourner les résultats.
* **"Compagnon" matériel :** C'est un cas d'usage très intéressant. Vous pouvez faire contrôler par OpenClaw du matériel connecté à un Raspberry Pi. Par exemple, un développeur l'a utilisé pour contrôler un aspirateur robot avec un bras mécanique, ou même pour l'aider à analyser les données d'un simulateur de course et les afficher sur un écran LED. L'équipe officielle de Raspberry Pi l'a même utilisé pour construire un photomaton automatique pour un mariage, simplement par la conversation, sans écrire une seule ligne de code !

**Pourquoi installer openclaw sur un Raspberry Pi ?**

L'installer sur un Raspberry Pi présente deux avantages principaux :

* **Isolation de sécurité :** OpenClaw nécessite des permissions système élevées, ce qui présente un risque sur un ordinateur principal. Utiliser un Raspberry Pi comme appareil dédié, c'est comme lui donner un "bac à sable" ; même si quelque chose tourne mal, votre système principal ne sera pas affecté.
* **Disponibilité 24h/24 et 7j/7 :** Le Raspberry Pi a une consommation électrique extrêmement faible, ce qui lui permet de rester allumé en permanence, prêt à exécuter des tâches à tout moment.

----------------------------------------------------------------

Démarrage rapide d'OpenClaw
------------------------------

Si vous voulez expérimenter la puissance d'OpenClaw le plus rapidement possible, utilisez cette méthode. Elle installera automatiquement et lancera un assistant d'installation interactif.

1.  Ouvrez le terminal sur votre Raspberry Pi et exécutez directement la commande suivante. Cette commande télécharge le script d'installation depuis le site officiel et l'exécute :

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash
   
    .. note:: Étant donné que les nouvelles versions sont mises à jour rapidement, il est normal que vos étapes d'installation diffèrent légèrement.

2.  Le script téléchargera et installera automatiquement OpenClaw.

    .. image:: /pironman5/home_server/img/openclaw/install_open_claw.png


3.  Vous verrez ensuite une invite de sécurité vous demandant si vous faites confiance à OpenClaw. Une fois que vous êtes sûr qu'il est sûr et fiable, utilisez les touches fléchées pour naviguer vers "Yes" et appuyez sur Entrée.

    .. image:: /pironman5/home_server/img/openclaw/security_open_claw.png


4.  Sélectionnez Quick Start, puis appuyez sur Entrée.

    .. image:: /pironman5/home_server/img/openclaw/quickstart_open_claw.png

5.  Sélectionnez votre Model, puis appuyez sur Entrée. Ici, nous utilisons OpenAI comme exemple.

    .. image:: /pironman5/home_server/img/openclaw/model_provider_open_claw.png

6.  Sélectionnez OpenAI API Key.

    .. image:: /pironman5/home_server/img/openclaw/api_key_open_claw.png

7.  Collez votre clé API maintenant.

    .. image:: /pironman5/home_server/img/openclaw/paste_api_key_open_claw.png


8.  Allez sur |link_openai_platform| et connectez-vous. Sur la page **API keys**, cliquez sur **Create new secret key**.

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_create.png

9.  Remplissez les détails (Propriétaire, Nom, Projet, et permissions si nécessaire), puis cliquez sur **Create secret key**.

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_create_confirm.png

10. Une fois la clé créée, copiez-la immédiatement — vous ne pourrez plus la revoir. Si vous la perdez, vous devrez en générer une nouvelle.

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_copy.png

11. Collez la clé dans la configuration d'OpenCLaw.

    .. image:: /pironman5/home_server/img/openclaw/paste_api_key_enter_open_claw.png

12. Sélectionnez le Model que vous souhaitez utiliser. Dans cet exemple, nous utiliserons **Keep current**.

    .. image:: /pironman5/home_server/img/openclaw/model_config_open_claw.png

13. Vient ensuite la sélection des channels. Les channels font référence aux services de communication supportés par OpenClaw, tels que Telegram, WhatsApp, Discord, etc. Utilisez la touche fléchée vers le bas pour sélectionner l'option "Skip for now", puis appuyez sur Entrée.

    .. image:: /pironman5/home_server/img/openclaw/channel_open_claw.png

14. Ensuite, il vous sera demandé de configurer les skills immédiatement. Sélectionnez "Yes" et appuyez sur Entrée.

    .. image:: /pironman5/home_server/img/openclaw/config_skill_open_claw.png

15. Installez les skills dont vous avez besoin. Dans l'exemple suivant, nous sélectionnons l'option "Skip for now" (appuyez sur la barre d'espace pour sélectionner), puis appuyez sur Entrée.

    .. image:: /pironman5/home_server/img/openclaw/install_skill_open_claw.png


16. Ensuite, les Hooks ; nous allons cocher "command-logger" et "session-memory".

    .. image:: /pironman5/home_server/img/openclaw/hooks2_open_claw.png


17. L'installation est maintenant terminée. Vous pouvez démarrer OpenClaw en sélectionnant "Hatch in TUI" et en appuyant sur Entrée.

   .. image:: /pironman5/home_server/img/openclaw/hatch_open_claw.png


.. note:: 
   
   Vous pouvez démarrer OpenClaw en entrant la commande suivante :

    .. code-block:: bash

       openclaw tui

   Et vous pouvez appuyer deux fois sur ctrl+c pour quitter l'interface tui.




-----------------------------------------------------

.. end_using_openclaw

Faire en sorte qu'OpenClaw pilote le Pironman5
----------------------------------------------

Pour permettre à OpenClaw de piloter le Pironman5, nous devons installer le skill Pironman5.

1.  Assurez-vous d'avoir déjà installé le Pironman5. Si ce n'est pas le cas, veuillez vous référer à :ref:`install_pironman5_module_5`.

2.  Exécutez la commande suivante dans le terminal :

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-skill/ ~/.openclaw/skills/pironman5-skill/

3.  Vous pouvez maintenant piloter le Pironman5 dans ``openclaw tui``. Essayez d'envoyer des commandes dans la TUI, par exemple en essayant d'allumer les LED du boîtier, de changer leur couleur, ou de faire prendre une photo par la caméra. Vous pouvez même lui dire que vous avez un module DHT11 connecté au GPIO17 et lui demander de vous donner la température.

   .. note:: Si OpenClaw ne reconnaît toujours pas le skill que vous avez importé, rappelez-lui de faire un rsync.

---------------------------------------

.. start_using_openclaw_telegram

Pilotez votre système avec Telegram
---------------------------------------


**Aperçu**

Grâce à OpenClaw, vous pouvez utiliser des applications de messagerie populaires pour piloter votre système (ici, nous utilisons Telegram comme exemple). Vous pouvez même laisser OpenClaw vous aider à réaliser cette configuration.

Demandez simplement dans ``openclaw tui`` : *"Je veux te connecter à Telegram, que dois-je faire ?"*

Il vous guidera étape par étape, et vous pourrez suivre ses instructions pour terminer la configuration.


**Prérequis**

Avant de commencer, assurez-vous d'avoir :

- Un **compte Telegram**
- Un accès réseau à Telegram
- OpenClaw fonctionnant correctement (vérifiez avec ``openclaw status``)

**Étape 1 : Créer un bot Telegram**

1. **Trouvez @BotFather sur Telegram** (le créateur officiel de bots)
2. **Créez un nouveau bot** : Envoyez la commande ``/newbot``
3. **Suivez les instructions** :

   - Donnez un nom à votre bot (exemple : ``Mon Assistant OpenClaw``)
   - Définissez un nom d'utilisateur pour votre bot (doit se terminer par ``_bot``, ex. : ``mon_openclaw_bot``)

4. **En cas de succès, vous recevrez un message** contenant votre **Jeton de Bot (Bot Token)**, semblable à :

   .. code-block:: text

      1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

   .. warning:: Gardez ce jeton comme un mot de passe !

**Étape 2 : Configurer Telegram dans OpenClaw**

Dans ``openclaw tui``, dites directement :

> *"Je veux connecter mon bot Telegram à OpenClaw. Voici mon jeton de bot : <votre-jeton-ici>. Aide-moi à terminer la configuration s'il te plaît."*

OpenClaw va automatiquement :

- Installer les dépendances nécessaires (comme ``node-telegram-bot-api``)
- Créer le fichier de configuration de la passerelle Telegram
- Tester si la connexion est réussie


**Étape 3 : Tester la connexion**

1. Trouvez votre bot nouvellement créé sur Telegram
2. Envoyez la commande ``/start``
3. Le bot devrait répondre avec un code d'appairage, envoyez ce code à l'interface TUI d'OpenClaw (exemple : ``Code d'appairage : ZAN4XI34``)
4. Attendez que la configuration soit correctement effectuée
5. Essayez d'envoyer des commandes simples comme "bonjour"
6. Si tout est correctement configuré, vous devriez voir la réponse de votre bot

**Étape 4 : Profitez !**

Après avoir terminé cette configuration, vous pourrez :

* Contrôler votre Raspberry Pi à tout moment, n'importe où, via Telegram
* Exécuter des commandes à distance et vérifier l'état du système
* Contrôler des périphériques physiques en intégrant le GPIO (comme allumer des LED)
* Profiter d'une expérience interactive intelligente avec votre assistant IA


**Configuration de sécurité (Critique !)**

Pour empêcher des inconnus de contrôler votre système, assurez-vous de mettre en œuvre les mesures de sécurité suivantes :

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Mesure de sécurité
     - Méthode de configuration
     - Description
   * - Restreindre les utilisateurs
     - Définir ``allowedUsers`` dans la config
     - Autoriser uniquement des utilisateurs Telegram spécifiques
   * - Définir un mot de passe
     - Ajouter ``"password": "votre-mot-de-passe"`` dans la config
     - Exiger une vérification du mot de passe avant les commandes
   * - Restreindre les commandes
     - Créer une liste blanche de commandes
     - Autoriser uniquement des commandes prédéfinies spécifiques
   * - Journaux d'audit
     - Activer le hook ``command-logger``
     - Journaliser toutes les commandes exécutées via Telegram


**Rappelez-vous : La sécurité d'abord !** Restreignez toujours les utilisateurs et la portée des commandes de manière appropriée. Si vous rencontrez des problèmes spécifiques lors de la configuration, n'hésitez pas à demander de l'aide.

-------------------------------------

.. end_using_openclaw_telegram

.. start_using_openclaw_faq

Dépannage d'OpenClaw
-------------------------------------

Q. Pendant l'installation, j'obtiens l'erreur ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``. Que dois-je faire ?

   Vous pouvez ignorer cela pour l'instant, mais vous pourriez rencontrer des problèmes dans les étapes suivantes. Veuillez vous y référer une par une à ce moment-là.


Q. Quand j'exécute ``openclaw tui``, j'obtiens l'erreur ``-bash: openclaw: command not found``. Que dois-je faire ?

   Exécutez la commande suivante :

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   Vous devriez maintenant pouvoir démarrer l'interface tui avec ``openclaw tui``.



Q. Dans ``openclaw tui``, je rencontre l'erreur ``not connected to gateway — message not sent`` ou le message ``gateway disconnected: closed``.

   Cela signifie que votre service OpenClaw Gateway n'est pas démarré. Ouvrez un autre terminal et exécutez la commande suivante pour démarrer OpenClaw Gateway :

   .. code-block:: bash

      openclaw gateway

   Puis redémarrez ``openclaw tui``, et vous pourrez l'utiliser directement.


Q. Je veux configurer le service OpenClaw Gateway pour qu'il tourne en arrière-plan / démarre automatiquement au boot. Comment faire ?

   Normalement, votre service OpenClaw Gateway devrait démarrer automatiquement au boot. Si ce n'est pas le cas, vous pouvez le démarrer manuellement avec la commande suivante.

   1. Créez le répertoire ``~/.config/systemd/user`` :

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user


   2. Créez le fichier ``openclaw-gateway.service`` :

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


   3. Rechargez ensuite la configuration systemd :

   .. code-block:: bash

      systemctl --user daemon-reload

   4. Démarrez le service :

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   À ce stade, redémarrez ``openclaw tui``, et vous pourrez l'utiliser directement.

   5. Activez-le pour qu'il démarre au boot :

   .. code-block:: bash

      systemctl --user enable openclaw-gateway


Q. Mon OpenClaw ne peut pas interagir avec le système, que dois-je faire ?

   Une nouvelle installation d'OpenClaw peut ne pas avoir la permission d'interagir avec votre système Raspberry Pi par défaut ; il ne peut que discuter. Nous devons configurer manuellement les permissions.

   1.  Ouvrez le fichier de configuration d'OpenClaw :

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  Recherchez l'option ``Tools`` et modifiez les options ``Profile`` et ``exec`` comme suit.

      .. code-block:: json

         "tools": {
            "profile": "coding",
            "exec": {
               "secrity": "full"
            }
         },

   3.  Sauvegardez et quittez.

   4.  Entrez la commande suivante dans le terminal pour redémarrer OpenClaw Gateway :

      .. code-block:: bash

         openclaw gateway restart

   Maintenant, OpenClaw devrait avoir les permissions de lecture et d'écriture et être capable d'interagir avec votre système Raspberry Pi.

.. end_using_openclaw_faq