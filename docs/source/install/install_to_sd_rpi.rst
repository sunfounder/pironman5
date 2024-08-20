.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux nouvelles annonces de produits et à des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_os_sd_rpi:

Installation du système d'exploitation sur une carte Micro SD
=================================================================
Si vous utilisez une carte Micro SD, vous pouvez suivre le tutoriel ci-dessous pour installer le système sur votre carte Micro SD.

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Composants requis**

* Un ordinateur personnel
* Une carte Micro SD et un lecteur

**Étapes**

#. Insérez votre carte SD dans votre ordinateur ou portable à l'aide d'un lecteur.

#. Dans l'outil |link_rpi_imager|, cliquez sur **Raspberry Pi Device** et sélectionnez le modèle **Raspberry Pi 5** dans la liste déroulante.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Sélectionnez **Système d'exploitation** et choisissez la version recommandée du système d'exploitation.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Cliquez sur **Choisir Stockage** et sélectionnez le périphérique de stockage approprié pour l'installation.

   .. image:: img/os_choose_sd.png
      :width: 90%

#. Cliquez sur **SUIVANT** puis sur **MODIFIER LES PARAMÈTRES** pour personnaliser les réglages de votre système d'exploitation.

   .. image:: img/os_enter_setting.png
      :width: 90%

   * Définissez un **nom d'hôte** pour votre Raspberry Pi. Le nom d'hôte est l'identifiant réseau de votre Raspberry Pi. Vous pouvez y accéder en utilisant ``<hostname>.local`` ou ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png

   * Créez un **nom d'utilisateur** et un **mot de passe** pour le compte administrateur du Raspberry Pi. Établir un nom d'utilisateur et un mot de passe uniques est essentiel pour sécuriser votre Raspberry Pi, qui n'a pas de mot de passe par défaut.

     .. image:: img/os_set_username.png

   * Configurez le réseau sans fil en fournissant le **SSID** et le **mot de passe** de votre réseau.

     .. note::

       Réglez le ``pays du réseau sans fil`` sur le code alpha-2 `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondant à votre localisation.

     .. image:: img/os_set_wifi.png

   * Pour vous connecter à distance à votre Raspberry Pi, activez SSH dans l'onglet Services.

     * Pour l'**authentification par mot de passe**, utilisez le nom d'utilisateur et le mot de passe définis dans l'onglet Général.
     * Pour l'authentification par clé publique, choisissez "Autoriser uniquement l'authentification par clé publique". Si vous avez une clé RSA, elle sera utilisée. Sinon, cliquez sur "Exécuter SSH-keygen" pour générer une nouvelle paire de clés.

     .. image:: img/os_enable_ssh.png

   * Le menu **Options** vous permet de configurer le comportement de l'Imager pendant l'écriture, notamment jouer un son à la fin, éjecter les médias à la fin et activer la télémétrie.

     .. image:: img/os_options.png

#. Lorsque vous avez terminé d'entrer les paramètres de personnalisation du système d'exploitation, cliquez sur **Enregistrer** pour sauvegarder vos paramètres. Ensuite, cliquez sur **Oui** pour les appliquer lors de l'écriture de l'image.

   .. image:: img/os_click_yes.png
      :width: 90%

#. Si la carte SD contient des données existantes, assurez-vous de les sauvegarder pour éviter toute perte de données. Procédez en cliquant sur **Oui** si aucune sauvegarde n'est nécessaire.

   .. image:: img/os_continue.png
      :width: 90%

#. Lorsque vous voyez le message "Écriture réussie", votre image a été entièrement écrite et vérifiée. Vous êtes maintenant prêt à démarrer un Raspberry Pi depuis la carte Micro SD !

   .. image:: img/os_finish.png
      :width: 90%
