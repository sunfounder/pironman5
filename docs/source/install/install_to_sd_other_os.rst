.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux nouvelles annonces de produits et à des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_to_sd_home_bridge:

Installation du système d'exploitation sur une carte Micro SD
==================================================================

Si vous utilisez une carte Micro SD, vous pouvez suivre le tutoriel ci-dessous pour installer le système sur votre carte Micro SD.

**Composants requis**

* Un ordinateur personnel
* Une carte Micro SD et un lecteur


**Étapes**

#. Insérez votre carte SD dans votre ordinateur ou votre portable à l'aide d'un lecteur.

#. Dans l'outil |link_rpi_imager|, cliquez sur **Raspberry Pi Device** et sélectionnez le modèle **Raspberry Pi 5** dans la liste déroulante.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%
      

#. Cliquez sur l'onglet **Système d'exploitation**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Faites défiler jusqu'en bas de la page et sélectionnez votre système d'exploitation.

   .. note::

      * Pour le système **Ubuntu**, cliquez sur **Other general-purpose OS** -> **Ubuntu**, et sélectionnez soit **Ubuntu Desktop 24.04 LTS (64 bits)**, soit **Ubuntu Server 24.04 LTS (64 bits)**.
      * Pour les systèmes **Kali Linux**, **Home Assistant** et **Homebridge**, cliquez sur **Other specific-purpose OS**, puis sélectionnez le système correspondant.

   .. image:: img/os_other_os.png
      :width: 90%

#. Dans l'option **Stockage**, sélectionnez le périphérique de stockage approprié pour l'installation.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%
      

#. Cliquez sur **SUIVANT**.

   .. note::

      * Pour les systèmes qui ne peuvent pas être configurés à l'avance, après avoir cliqué sur **SUIVANT**, il vous sera demandé si vous souhaitez sauvegarder les données sur le périphérique. Si vous avez confirmé qu'une sauvegarde a été effectuée, sélectionnez **Oui**.

      * Pour les systèmes où le nom d'hôte, le WiFi et l'activation de SSH peuvent être configurés à l'avance, une fenêtre contextuelle apparaîtra, vous demandant si vous souhaitez appliquer les paramètres personnalisés du système d'exploitation. Vous pouvez choisir **Oui**, **Non**, ou revenir en arrière pour modifier d'autres paramètres.

   .. image:: img/os_enter_setting.png
      :width: 90%
      

   * Définissez un **nom d'hôte** pour votre Raspberry Pi. Le nom d'hôte est l'identifiant réseau de votre Raspberry Pi. Vous pouvez y accéder en utilisant ``<hostname>.local`` ou ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png  

   * Créez un **nom d'utilisateur** et un **mot de passe** pour le compte administrateur du Raspberry Pi. Établir un nom d'utilisateur et un mot de passe uniques est essentiel pour sécuriser votre Raspberry Pi, qui n'a pas de mot de passe par défaut.

     .. image:: img/os_set_username.png
         
   * Configurez le réseau sans fil en fournissant le **SSID** et le **mot de passe** de votre réseau.

     .. note::

       Réglez le ``pays du réseau sans fil`` sur le code alpha2 à deux lettres  `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondant à votre localisation.

     .. image:: img/os_set_wifi.png
         
   * Pour vous connecter à distance à votre Raspberry Pi, activez SSH dans l'onglet Services.

     * Pour l'**authentification par mot de passe**, utilisez le nom d'utilisateur et le mot de passe définis dans l'onglet Général.
     * Pour l'authentification par clé publique, choisissez "Autoriser uniquement l'authentification par clé publique". Si vous avez une clé RSA, elle sera utilisée. Sinon, cliquez sur "Exécuter SSH-keygen" pour générer une nouvelle paire de clés.

     .. image:: img/os_enable_ssh.png
         
   * Le menu **Options** vous permet de configurer le comportement de l'Imager pendant l'écriture, notamment jouer un son à la fin, éjecter les médias à la fin et activer la télémétrie.

     .. image:: img/os_options.png
           
#. Lorsque vous avez terminé d'entrer les paramètres de personnalisation du système d'exploitation, cliquez sur **Enregistrer** pour les sauvegarder. Ensuite, cliquez sur **Oui** pour les appliquer lors de l'écriture de l'image.

   .. image:: img/os_click_yes.png
      :width: 90%
      

#. Si la carte SD contient des données existantes, assurez-vous de les sauvegarder pour éviter toute perte de données. Procédez en cliquant sur **Oui** si aucune sauvegarde n'est nécessaire.

   .. image:: img/os_continue.png
      :width: 90%
      

#. Lorsque vous voyez le message "Écriture réussie", votre image a été entièrement écrite et vérifiée. Vous êtes maintenant prêt à démarrer un Raspberry Pi depuis la carte Micro SD !

