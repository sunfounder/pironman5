.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes après-vente et surmontez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des conseils et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives**: Bénéficiez d'un accès anticipé aux nouvelles annonces de produits et à des avant-premières.
    - **Réductions spéciales**: Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et tirages au sort**: Participez à des concours et à des promotions spéciales.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_to_nvme_rpi:

Installation du système d'exploitation sur un SSD NVMe
==================================================================

Si vous utilisez un SSD NVMe et disposez d'un adaptateur pour connecter le SSD NVMe à votre ordinateur pour installer le système, vous pouvez suivre le tutoriel suivant pour une installation rapide.

**Composants requis**

* Un ordinateur personnel
* Un SSD NVMe
* Un adaptateur NVMe vers USB
* Une carte Micro SD et un lecteur

.. _update_bootloader:

1. Mise à jour du Bootloader
----------------------------

Tout d'abord, vous devez mettre à jour le bootloader du Raspberry Pi 5 pour démarrer à partir du NVMe avant de tester l'USB, puis la carte SD.

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    À cette étape, il est recommandé d'utiliser une carte Micro SD de secours. Écrivez d'abord le bootloader sur cette carte Micro SD, puis insérez-la immédiatement dans le Raspberry Pi pour activer le démarrage à partir d'un périphérique NVMe.
    
    Alternativement, vous pouvez écrire le bootloader directement sur votre SSD NVMe, puis l'insérer dans le Raspberry Pi pour changer la méthode de démarrage. Ensuite, connectez le SSD NVMe à un ordinateur pour installer le système d'exploitation. Une fois l'installation terminée, réinsérez-le dans le Raspberry Pi.

#. Insérez votre carte Micro SD ou SSD NVMe de secours dans votre ordinateur ou votre portable à l'aide d'un lecteur.

#. Dans l'outil |link_rpi_imager|, cliquez sur **Appareil Raspberry Pi** et sélectionnez le modèle **Raspberry Pi 5** dans la liste déroulante.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Dans l'onglet **Système d'exploitation**, faites défiler vers le bas et sélectionnez **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Sélectionnez **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Sélectionnez **NVMe/USB Boot** pour permettre au Raspberry Pi 5 de démarrer à partir du NVMe avant de tester l'USB, puis la carte SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%
      


#. Dans l'option **Stockage**, sélectionnez le périphérique de stockage approprié pour l'installation.

   .. note::

      Assurez-vous de sélectionner le bon périphérique de stockage. Pour éviter toute confusion, déconnectez tout périphérique de stockage supplémentaire si plusieurs sont connectés.

   .. image:: img/os_choose_sd.png
      :width: 90%
      

#. Vous pouvez maintenant cliquer sur **SUIVANT**. Si le périphérique de stockage contient des données existantes, assurez-vous de les sauvegarder pour éviter toute perte de données. Cliquez sur **Oui** si aucune sauvegarde n'est nécessaire.

   .. image:: img/os_continue.png
      :width: 90%
      

#. Vous serez bientôt informé que le **NVMe/USB Boot** a été écrit sur votre périphérique de stockage.

   .. image:: img/nvme_boot_finish.png
      :width: 90%
      

#. Maintenant, vous pouvez insérer votre carte Micro SD ou SSD NVMe dans le Raspberry Pi. Après avoir alimenté le Raspberry Pi avec un adaptateur de type C, le bootloader de la carte Micro SD ou du SSD NVMe sera écrit dans l'EEPROM du Raspberry Pi.

.. note::

    Par la suite, le Raspberry Pi démarrera à partir du NVMe avant de tester l'USB, puis la carte SD. 
    
    Éteignez le Raspberry Pi et retirez la carte Micro SD ou le SSD NVMe.


2. Installation du système d'exploitation sur le SSD NVMe
---------------------------------------------------------

Vous pouvez maintenant installer le système d'exploitation sur votre SSD NVMe.

#. Dans l'outil |link_rpi_imager|, cliquez sur **Appareil Raspberry Pi** et sélectionnez le modèle **Raspberry Pi 5** dans la liste déroulante.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Sélectionnez **Système d'exploitation** et optez pour la version recommandée du système d'exploitation.

   .. image:: img/os_choose_os.png
      :width: 90%
      

#. Dans l'option **Stockage**, sélectionnez le périphérique de stockage approprié pour l'installation.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%
      

#. Cliquez sur **SUIVANT**, puis sur **MODIFIER LES PARAMÈTRES** pour personnaliser vos paramètres de système d'exploitation. 

   .. image:: img/os_enter_setting.png
      :width: 90%
      

   * Définissez un **nom d'hôte** pour votre Raspberry Pi. Le nom d'hôte est l'identifiant réseau de votre Raspberry Pi. Vous pouvez accéder à votre Pi en utilisant ``<hostname>.local`` ou ``<hostname>.lan``.
  
     .. image:: img/os_set_hostname.png
         
   * Créez un **nom d'utilisateur** et un **mot de passe** pour le compte administrateur du Raspberry Pi. L'établissement d'un nom d'utilisateur et d'un mot de passe uniques est essentiel pour sécuriser votre Raspberry Pi, qui n'a pas de mot de passe par défaut.

     .. image:: img/os_set_username.png
         
   * Configurez le réseau sans fil en fournissant le **SSID** et le **mot de passe** de votre réseau.

     .. note::

       Définissez le ``Wireless LAN country`` sur le code à deux lettres `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondant à votre localisation.

     .. image:: img/os_set_wifi.png
         
   * Pour vous connecter à distance à votre Raspberry Pi, activez SSH dans l'onglet Services.

     * Pour l'**authentification par mot de passe**, utilisez le nom d'utilisateur et le mot de passe de l'onglet Général.
     * Pour l'authentification par clé publique, choisissez "Allow public-key authentication only". Si vous avez une clé RSA, elle sera utilisée. Sinon, cliquez sur "Run SSH-keygen" pour générer une nouvelle paire de clés.

     .. image:: img/os_enable_ssh.png
         
   * Le menu **Options** vous permet de configurer le comportement d'Imager lors de l'écriture, y compris jouer un son à la fin, éjecter le média une fois terminé et activer la télémétrie.

     .. image:: img/os_options.png

#. Une fois que vous avez terminé de saisir les paramètres de personnalisation du système d'exploitation, cliquez sur **Enregistrer** pour les sauvegarder. Ensuite, cliquez sur **Oui** pour les appliquer lors de l'écriture de l'image.

   .. image:: img/os_click_yes.png
      :width: 90%
      

#. Si le SSD NVMe contient des données existantes, assurez-vous de les sauvegarder pour éviter toute perte de données. Cliquez sur **Oui** si aucune sauvegarde n'est nécessaire.

   .. image:: img/nvme_erase.png
      :width: 90%
      

#. Lorsque vous voyez le message "Écriture réussie", votre image a été entièrement écrite et vérifiée. Vous êtes maintenant prêt à démarrer un Raspberry Pi depuis le SSD NVMe !

   .. image:: img/nvme_install_finish.png
      :width: 90%
      
