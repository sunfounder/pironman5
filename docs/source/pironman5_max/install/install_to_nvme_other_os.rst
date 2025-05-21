.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d'autres passionnés pour approfondir vos connaissances et vos projets autour du Raspberry Pi, d’Arduino et d’ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Bénéficiez de l’aide de notre équipe et de notre communauté pour résoudre les problèmes techniques et après-vente.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et à des démonstrations inédites.
    - **Réductions spéciales** : Profitez d’offres exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des concours et événements spéciaux pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès maintenant !

.. _max_install_to_nvme_home_bridge:

Installation du système d’exploitation sur un SSD NVMe
==============================================================

Si vous utilisez un SSD NVMe et disposez d’un adaptateur pour le connecter à votre ordinateur, vous pouvez suivre ce tutoriel pour une installation rapide.

**Composants nécessaires**

* Un ordinateur personnel
* Un SSD NVMe
* Un adaptateur NVMe vers USB
* Une carte Micro SD et un lecteur

.. _max_update_bootloader:

1. Mettre à jour le bootloader
----------------------------------

Vous devez d’abord mettre à jour le bootloader du Raspberry Pi 5 pour qu’il démarre depuis le NVMe, avant de tenter via USB puis via la carte SD.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    Il est recommandé d’utiliser une carte Micro SD dédiée à cette étape. Commencez par y écrire le bootloader, puis insérez-la immédiatement dans le Raspberry Pi pour activer le démarrage depuis un périphérique NVMe.
    
    Vous pouvez aussi écrire le bootloader directement sur le SSD NVMe, puis l’insérer dans le Raspberry Pi pour modifier sa méthode de démarrage. Ensuite, connectez le SSD NVMe à un ordinateur pour y installer le système d’exploitation, et une fois terminé, réinsérez-le dans le Raspberry Pi.

#. Insérez votre carte Micro SD ou votre SSD NVMe dans l’ordinateur à l’aide d’un lecteur.

#. Dans le |link_rpi_imager|, cliquez sur **Raspberry Pi Device** et sélectionnez **Raspberry Pi 5** dans la liste déroulante.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%
      
#. Dans l’onglet **Operating System**, faites défiler vers le bas et sélectionnez **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Sélectionnez **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Choisissez **NVMe/USB Boot** pour permettre au Raspberry Pi 5 de démarrer depuis le NVMe, avant l’USB et la carte SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Dans l’option **Storage**, sélectionnez le périphérique de stockage approprié.

   .. note::

      Vérifiez bien que vous avez sélectionné le bon support. Pour éviter toute confusion, déconnectez les autres périphériques si nécessaire.

   .. image:: img/os_choose_sd.png
      :width: 90%

#. Cliquez ensuite sur **NEXT**. Si le support contient des données, sauvegardez-les avant de continuer. Cliquez sur **Yes** si aucune sauvegarde n’est requise.

   .. image:: img/os_continue.png
      :width: 90%


#. Un message vous confirmera ensuite que le mode **NVMe/USB Boot** a été correctement écrit sur le périphérique.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Insérez maintenant la carte Micro SD ou le SSD NVMe dans le Raspberry Pi. Une fois alimenté via un adaptateur USB-C, le bootloader sera écrit dans l’EEPROM du Raspberry Pi.

.. note::

   Le Raspberry Pi démarrera désormais depuis le NVMe, puis depuis l’USB, et enfin la carte SD si nécessaire.
    
   Éteignez le Raspberry Pi et retirez la carte Micro SD ou le SSD NVMe.


2. Installer le système sur le SSD NVMe
-----------------------------------------------

Vous pouvez maintenant procéder à l’installation du système d’exploitation sur votre SSD NVMe.

**Étapes**

#. Insérez votre carte SD dans l’ordinateur via un lecteur.

#. Dans le |link_rpi_imager|, cliquez sur **Raspberry Pi Device** et sélectionnez **Raspberry Pi 5**.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. Cliquez sur l’onglet **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Faites défiler jusqu’en bas de la page et sélectionnez le système souhaité.

   .. note::

      * Pour **Ubuntu**, cliquez sur **Other general-purpose OS** → **Ubuntu**, puis sélectionnez **Ubuntu Desktop 24.04 LTS (64 bit)** ou **Ubuntu Server 24.04 LTS (64 bit)**.
      * Pour **Kali Linux**, **Home Assistant** ou **Homebridge**, cliquez sur **Other specific-purpose OS** puis sélectionnez le système correspondant.

   .. image:: img/os_other_os.png
      :width: 90%

#. Dans l’option **Storage**, choisissez le support NVMe destiné à l’installation.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Cliquez sur **NEXT**.

   .. note::

      * Pour les systèmes qui ne peuvent pas être configurés à l’avance, vous serez invité à confirmer si vous souhaitez effacer les données. Si une sauvegarde a été faite, sélectionnez **Yes**.

      * Pour les systèmes configurables (nom d’hôte, Wi-Fi, SSH...), une fenêtre vous proposera d’appliquer vos réglages. Choisissez **Yes**, **No** ou retournez à l’édition.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Définissez un **hostname** pour votre Raspberry Pi. Il s’agit de l’identifiant réseau de votre appareil, accessible via ``<hostname>.local`` ou ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png

   * Créez un **nom d’utilisateur** et un **mot de passe** pour le compte administrateur. Ces identifiants sont essentiels pour sécuriser votre Raspberry Pi, qui n’a pas de mot de passe par défaut.

     .. image:: img/os_set_username.png

   * Configurez la connexion sans fil en saisissant le **SSID** et le **mot de passe** de votre réseau.

     .. note::

       Définissez le ``Wireless LAN country`` à l’aide du code alpha-2 de la norme `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondant à votre pays.

     .. image:: img/os_set_wifi.png

   * Pour accéder à distance au Raspberry Pi, activez SSH dans l’onglet Services.

     * Pour **password authentication**, utilisez les identifiants définis dans l’onglet General.
     * Pour l’authentification par clé publique, sélectionnez « Autoriser uniquement l’authentification par clé publique ». Si une clé RSA est disponible, elle sera utilisée. Sinon, cliquez sur « Exécuter SSH-keygen » pour générer une nouvelle paire de clés.

     .. image:: img/os_enable_ssh.png

   * Le menu **Options** permet de configurer le comportement d’Imager pendant l’écriture, notamment l’émission d’un son à la fin, l’éjection automatique du support, ou l’envoi de données anonymes.

     .. image:: img/os_options.png



#. Une fois vos réglages terminés, cliquez sur **Save** pour enregistrer la configuration, puis sur **Yes** pour les appliquer lors de l’écriture de l’image.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Si le SSD NVMe contient des données, veillez à effectuer une sauvegarde. Cliquez sur **Yes** si aucune sauvegarde n’est nécessaire.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Lorsque la fenêtre « Write Successful » s’affiche, cela signifie que l’image a été écrite et vérifiée avec succès. Vous pouvez maintenant démarrer votre Raspberry Pi depuis le SSD NVMe !
