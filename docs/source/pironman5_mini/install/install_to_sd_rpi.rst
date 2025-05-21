.. note:: 

    Bonjour et bienvenue dans la communauté SunFounder des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez au cœur de l’univers Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l’aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez astuces et tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits.
    - **Réductions spéciales** : Profitez d’offres exclusives sur nos derniers produits.
    - **Promotions et concours festifs** : Participez à des concours et événements promotionnels.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _install_os_sd_rpi_mini:

Installation du système d’exploitation sur une carte Micro SD
=================================================================
.. If you are using a Micro SD card, you can follow the tutorial below to install the system onto your Micro SD card.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Composants requis**

* Un ordinateur personnel
* Une carte Micro SD et un lecteur

**Étapes**

#. Insérez votre carte SD dans votre ordinateur ou votre ordinateur portable via un lecteur de carte.

#. Dans le |link_rpi_imager|, cliquez sur **Raspberry Pi Device** et sélectionnez le modèle **Raspberry Pi 5** dans la liste déroulante.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Sélectionnez **Système d'exploitation** et optez pour la version recommandée.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Cliquez sur **Choisir le support de stockage** et sélectionnez le périphérique de stockage approprié pour l’installation.

   .. image:: img/os_choose_sd.png
      :width: 90%

#. Cliquez sur **SUIVANT** puis sur **MODIFIER LES PARAMÈTRES** pour personnaliser les réglages du système.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Définissez un **nom d’hôte** pour votre Raspberry Pi. Il s’agit de l’identifiant réseau de votre Raspberry Pi. Vous pouvez y accéder via ``<hostname>.local`` ou ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png


   * Créez un **nom d’utilisateur** et un **mot de passe** pour le compte administrateur du Raspberry Pi. Un identifiant personnalisé est essentiel pour la sécurité de votre appareil.

     .. image:: img/os_set_username.png

   * Configurez le réseau sans fil en renseignant le **SSID** et le **mot de passe** de votre réseau.

     .. note::

       Définissez le ``Wireless LAN country`` en utilisant le code à deux lettres `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondant à votre pays.

     .. image:: img/os_set_wifi.png


   * Pour se connecter à distance à votre Raspberry Pi, activez SSH dans l’onglet Services.

     * Pour une **authentification par mot de passe**, utilisez les identifiants définis dans l’onglet Général.
     * Pour une authentification par clé publique, sélectionnez « Autoriser uniquement l'authentification par clé publique ». Si une clé RSA est disponible, elle sera utilisée. Sinon, cliquez sur « Générer une clé SSH » pour en créer une.

     .. image:: img/os_enable_ssh.png

   * Le menu **Options** permet de configurer le comportement d’Imager lors de l’écriture : lecture d’un son en fin de processus, éjection automatique du support ou activation de la télémétrie.

     .. image:: img/os_options.png

#. Une fois la personnalisation terminée, cliquez sur **Enregistrer** pour sauvegarder vos réglages. Cliquez ensuite sur **Oui** pour les appliquer à l’écriture de l’image.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Si la carte SD contient déjà des données, assurez-vous de les sauvegarder pour éviter toute perte. Cliquez sur **Oui** pour continuer si aucune sauvegarde n’est nécessaire.

   .. image:: img/os_continue.png
      :width: 90%


#. Lorsque la fenêtre "Écriture réussie" s'affiche, cela signifie que l’image a été entièrement écrite et vérifiée. Votre Raspberry Pi est désormais prêt à démarrer depuis la carte Micro SD !

   .. image:: img/os_finish.png
      :width: 90%
