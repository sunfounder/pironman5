.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-goûts.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et à des promotions spéciales pour les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_os_sd_rpi_mini:

Installation du système d’exploitation
===============================================

Avant d’utiliser votre Raspberry Pi, vous devez installer **Raspberry Pi OS** sur une carte microSD.  
Ce guide explique comment procéder à l’aide de **Raspberry Pi Imager**, de manière simple et adaptée aux débutants.

**Composants requis**

* Un ordinateur (Windows, macOS ou Linux)
* Une carte microSD (16 Go ou plus ; marques recommandées : SanDisk, Samsung)
* Un lecteur de carte microSD

-------------------

.. start_install_imager

1. Installer Raspberry Pi Imager
-------------------------------------------

.. |shared_link_rpi_imager| raw:: html

    <a href="https://www.raspberrypi.com/software/" target="_blank">Raspberry Pi Imager</a>   

#. Rendez-vous sur la page officielle de téléchargement de Raspberry Pi Imager : |shared_link_rpi_imager|. Téléchargez l’installateur correspondant à votre système d’exploitation.

   .. image:: img/imager_download.png
      :width: 70%

#. Suivez les instructions d’installation (langue, chemin d’installation, confirmation). Une fois l’installation terminée, lancez **Raspberry Pi Imager** depuis votre bureau ou le menu des applications.

   .. image:: img/imager_install.png
      :width: 90%

.. end_install_imager

-------------------

2. Installer le système d’exploitation sur la carte microSD
----------------------------------------------------------------

1. Insérez votre carte microSD dans votre ordinateur à l’aide d’un lecteur de cartes. Sauvegardez toutes les données importantes avant de continuer.

   .. image:: img/insert_sd.png
      :width: 90%

2. Lorsque Raspberry Pi Imager s’ouvre, vous verrez la page **Device**. Sélectionnez votre modèle de **Raspberry Pi 5** dans la liste.

   .. image:: img/imager_device.png
      :width: 90%

3. Allez dans la section **OS** et choisissez l’option recommandée **Raspberry Pi OS (64-bit)**.

   .. image:: img/imager_os.png
      :width: 90%

4. Dans la section **Storage**, sélectionnez votre carte microSD.

   .. image:: img/imager_storage.png
      :width: 90%

   .. start_install_os

5. Cliquez sur **Next** pour passer à l’étape de personnalisation.

   .. note::

      * Si vous comptez connecter directement un écran, un clavier et une souris à votre Raspberry Pi, vous pouvez cliquer sur **SKIP CUSTOMISATION**.  
      * Si vous prévoyez de configurer le Raspberry Pi en mode *headless* (accès distant via Wi-Fi), vous devez impérativement compléter les paramètres de personnalisation.

   .. image:: img/imager_custom_skip.png
      :width: 90%

#. **Définir le nom d’hôte (Hostname)**

   * Attribuez un nom d’hôte unique à votre Raspberry Pi.  
   * Vous pourrez vous y connecter ultérieurement en utilisant ``hostname.local``.

   .. image:: img/imager_custom_hostname.png
      :width: 90%

#. **Définir la localisation**

   * Choisissez votre ville principale.
   * Imager complétera automatiquement le fuseau horaire et la disposition du clavier en fonction de votre sélection, que vous pourrez ajuster si nécessaire. Sélectionnez **Next**.
   
   .. image:: img/imager_custom_local.png
      :width: 90%

#. **Définir le nom d’utilisateur et le mot de passe**

   Créez un compte utilisateur pour votre Raspberry Pi.
   
   .. image:: img/imager_custom_user.png
      :width: 90%

#. **Configurer le Wi-Fi**

   * Saisissez le **SSID** (nom du réseau) et le **mot de passe** de votre Wi-Fi.  
   * Votre Raspberry Pi se connectera automatiquement lors du premier démarrage.
   
   .. image:: img/imager_custom_wifi.png
      :width: 90%

#. **Activer SSH (optionnel mais recommandé)**

   * L’activation de SSH vous permet de vous connecter à distance depuis votre ordinateur.  
   * Vous pouvez vous connecter à l’aide de votre nom d’utilisateur/mot de passe ou configurer des clés SSH.
   
   .. image:: img/imager_custom_ssh.png
      :width: 90%

#. **Activer Raspberry Pi Connect (optionnel)**


   Raspberry Pi Connect vous permet d’accéder au bureau de votre Raspberry Pi depuis un navigateur web.
   
   * Activez **Raspberry Pi Connect**, puis cliquez sur **OPEN RASPBERRY PI CONNECT**.
   
     .. image:: img/imager_custom_connect.png
        :width: 90%

   * Le site web de Raspberry Pi Connect s’ouvrira dans votre navigateur par défaut. Connectez-vous à votre compte Raspberry Pi ID, ou créez-en un si vous n’en avez pas encore.

     .. image:: img/imager_custom_open.png
        :width: 90%

   * Sur la page **New auth key**, créez votre clé d’authentification à usage unique. 
      
      * Si votre compte Raspberry Pi ID ne fait partie d’aucune organisation, sélectionnez **Create auth key and launch Raspberry Pi Imager**.
      * Si vous appartenez à une ou plusieurs organisations, choisissez-en une, puis créez la clé et lancez Imager.
      * Assurez-vous d’allumer votre Raspberry Pi et de le connecter à Internet avant l’expiration de la clé.
   
     .. image:: img/imager_custom_authkey.png
        :width: 90%
   
   * Votre navigateur peut vous demander d’ouvrir Raspberry Pi Imager — autorisez cette action.

     * Imager s’ouvrira sur l’onglet Raspberry Pi Connect, affichant le jeton d’authentification.
     * Si le jeton ne se transfère pas automatiquement, ouvrez la section **Having trouble?** sur la page Raspberry Pi Connect, copiez le jeton et collez-le manuellement dans Imager.

     .. image:: img/imager_custom_connect_token.png
        :width: 90%

#. Vérifiez tous les paramètres et cliquez sur **WRITE**.

   .. image:: img/imager_writing.png
      :width: 90%

#. Si la carte contient déjà des données, Raspberry Pi Imager affichera un avertissement indiquant que toutes les données du périphérique seront effacées. Vérifiez attentivement que vous avez sélectionné le bon lecteur, puis cliquez sur **I UNDERSTAND, ERASE AND WRITE** pour continuer.

   .. image:: img/imager_erase.png
      :width: 90%

#. Attendez la fin de l’écriture et de la vérification. Une fois l’opération terminée, Raspberry Pi Imager affichera **Write complete!** ainsi qu’un récapitulatif de vos choix. Le périphérique de stockage sera automatiquement éjecté afin que vous puissiez le retirer en toute sécurité.


   .. image:: img/imager_finish.png
        :width: 90%

   .. end_install_os

#. Retirez la carte microSD et insérez-la dans l’emplacement situé sous votre Raspberry Pi. Votre Raspberry Pi est maintenant prêt à démarrer avec le nouveau système d’exploitation !

   .. image:: img/os_sd_to_pi.jpg
        :width: 70%

   
