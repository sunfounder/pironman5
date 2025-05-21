.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d'autres passionnés pour approfondir vos connaissances sur Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Résolvez les problèmes après-vente et les défis techniques avec l’aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces et démonstrations de nouveaux produits.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des concours et événements promotionnels pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _install_to_nvme_home_bridge_mini:

Installation du système d’exploitation sur un SSD NVMe
===========================================================

Si vous utilisez un SSD NVMe et que vous disposez d’un adaptateur pour le connecter à votre ordinateur, suivez ce tutoriel pour effectuer une installation rapide.

    .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**Composants nécessaires**

* Un ordinateur personnel
* Un SSD NVMe
* Un adaptateur NVMe vers USB
* Une carte Micro SD et un lecteur

.. _update_bootloader_mini:

1. Mettre à jour le bootloader
----------------------------------

Vous devez d’abord mettre à jour le bootloader du Raspberry Pi 5 pour permettre le démarrage depuis le NVMe avant l’USB puis la carte SD.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    Il est recommandé d’utiliser une carte Micro SD de rechange. Écrivez d’abord le bootloader sur cette carte, puis insérez-la immédiatement dans le Raspberry Pi pour activer le démarrage via un périphérique NVMe.
    
    En alternative, vous pouvez écrire le bootloader directement sur le SSD NVMe, puis l’insérer dans le Raspberry Pi pour modifier la méthode de démarrage. Ensuite, connectez le SSD à votre ordinateur pour y installer le système, puis réinsérez-le dans le Raspberry Pi.

#. Insérez votre carte Micro SD de rechange ou votre SSD NVMe dans votre ordinateur à l’aide d’un lecteur.

#. Dans |link_rpi_imager|, cliquez sur **Appareil Raspberry Pi** et sélectionnez **Raspberry Pi 5** dans le menu déroulant.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%
      
#. Dans l’onglet **Système d’exploitation**, faites défiler vers le bas et sélectionnez **Images utilitaires diverses**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Sélectionnez **Bootloader (famille Pi 5)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Choisissez **Démarrage NVMe/USB** pour permettre au Raspberry Pi 5 de démarrer d’abord via NVMe.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Dans **Stockage**, sélectionnez le périphérique approprié.

   .. note::

      Assurez-vous de sélectionner le bon support. Déconnectez les autres supports si plusieurs sont branchés pour éviter toute confusion.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Cliquez sur **SUIVANT**. Si le support contient des données, effectuez une sauvegarde. Cliquez sur **Oui** pour continuer sans sauvegarde.

   .. image:: img/os_continue.png
      :width: 90%


#. Vous verrez une notification confirmant que le **Démarrage NVMe/USB** a bien été écrit.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Insérez maintenant la carte Micro SD ou le SSD NVMe dans le Raspberry Pi. En l’alimentant via un câble USB-C, le bootloader sera écrit dans l’EEPROM.

.. note::

    Le Raspberry Pi démarrera désormais depuis le NVMe, puis l’USB, puis la carte SD.

    Éteignez ensuite le Raspberry Pi et retirez la carte Micro SD ou le SSD NVMe.


2. Installer le système sur le SSD NVMe
----------------------------------------------

Vous pouvez maintenant installer le système d’exploitation sur le SSD NVMe.

**Étapes**

#. Insérez votre carte SD dans l’ordinateur via un lecteur.

#. Dans |link_rpi_imager|, cliquez sur **Appareil Raspberry Pi**, puis sélectionnez **Raspberry Pi 5**.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. Cliquez sur l’onglet **Système d’exploitation**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Faites défiler jusqu’en bas de la page et sélectionnez votre système d’exploitation.

   .. note::

      * Pour **Ubuntu**, cliquez sur **Autres systèmes à usage général** -> **Ubuntu**, puis choisissez **Ubuntu Desktop 24.04 LTS (64 bit)** ou **Ubuntu Server 24.04 LTS (64 bit)**.
      * Pour **Kali Linux**, **Home Assistant** et **Homebridge**, allez dans **Autres systèmes à usage spécifique** et sélectionnez le système correspondant.

   .. image:: img/os_other_os.png
      :width: 90%

#. Dans **Stockage**, sélectionnez le SSD NVMe.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Cliquez sur **SUIVANT**.

   .. note::

      * Pour les systèmes non configurables à l’avance, une alerte apparaîtra pour confirmer l’effacement des données. Cliquez sur **Oui** si vous avez sauvegardé.

      * Pour les systèmes configurables (nom d’hôte, Wi-Fi, SSH), une fenêtre s’ouvrira vous permettant de les paramétrer. Cliquez sur **Oui**, **Non**, ou retournez modifier.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Définissez un **nom d’hôte** pour votre Raspberry Pi. Il sert d’identifiant réseau et permet d’y accéder via ``<hostname>.local`` ou ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png

   * Créez un **Nom d’utilisateur** et un **Mot de passe** pour le compte administrateur. Cela est essentiel pour sécuriser votre Raspberry Pi.

     .. image:: img/os_set_username.png

   * Configurez le réseau sans fil avec le **SSID** et le **Mot de passe**.

     .. note::

       Définissez le champ ``Wireless LAN country`` avec le code pays à deux lettres selon `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_.

     .. image:: img/os_set_wifi.png
         
   * Pour la connexion à distance, activez SSH dans l’onglet Services.

     * Pour l’authentification par mot de passe, utilisez les identifiants définis plus haut.
     * Pour l’authentification par clé publique, choisissez "Autoriser uniquement l’authentification par clé publique". Cliquez sur "Run SSH-keygen" pour générer une paire de clés si nécessaire.

     .. image:: img/os_enable_ssh.png

   * Le menu **Options** vous permet de configurer le comportement de l’outil pendant l’écriture (signal sonore, éjection automatique, etc.).

     .. image:: img/os_options.png



#. Une fois vos paramètres définis, cliquez sur **Enregistrer**, puis sur **Oui** pour les appliquer.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Si le SSD contient des données, sauvegardez-les. Cliquez sur **Oui** pour continuer.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Lorsque la fenêtre "Écriture réussie" s’affiche, l’image a été correctement écrite et vérifiée. Vous êtes maintenant prêt à démarrer votre Raspberry Pi depuis le SSD NVMe !
