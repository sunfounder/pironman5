.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d’autres passionnés pour approfondir vos connaissances sur Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes techniques et après-vente grâce à l’aide de notre équipe et de la communauté.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour faire évoluer vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des démonstrations inédites.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des concours et événements promotionnels lors des fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _max_install_to_nvme_rpi:

Installation du système d’exploitation sur un SSD NVMe
=============================================================
Si vous utilisez un SSD NVMe et disposez d’un adaptateur pour le connecter à votre ordinateur, vous pouvez suivre ce tutoriel pour une installation rapide.

**Composants requis**

* Un ordinateur personnel
* Un SSD NVMe
* Un adaptateur NVMe vers USB
* Une carte Micro SD et un lecteur

.. _max_update_bootloader:

1. Mettre à jour le bootloader
--------------------------------

Vous devez d’abord mettre à jour le bootloader du Raspberry Pi 5 afin qu’il démarre depuis un SSD NVMe avant d’essayer les ports USB, puis la carte SD.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    Il est recommandé d’utiliser une carte Micro SD de rechange à cette étape. Écrivez d’abord le bootloader sur cette carte, puis insérez-la immédiatement dans le Raspberry Pi pour activer le démarrage depuis un périphérique NVMe.
    
    Vous pouvez également écrire le bootloader directement sur le SSD NVMe, puis l’insérer dans le Raspberry Pi pour modifier l’ordre de démarrage. Ensuite, connectez le SSD à un ordinateur pour y installer le système d’exploitation, puis réinsérez-le dans le Raspberry Pi une fois l’installation terminée.

#. Insérez votre carte Micro SD ou votre SSD NVMe dans l’ordinateur à l’aide d’un lecteur.

#. Dans le |link_rpi_imager|, cliquez sur **Raspberry Pi Device** et sélectionnez le modèle **Raspberry Pi 5** dans la liste déroulante.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Dans l’onglet **Operating System**, faites défiler vers le bas et sélectionnez **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Sélectionnez **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%


#. Choisissez **NVMe/USB Boot** pour permettre au Raspberry Pi 5 de démarrer depuis un NVMe avant d’essayer l’USB puis la carte SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Dans l’onglet **Storage**, sélectionnez le bon périphérique de stockage pour l’installation.

   .. note::

      Vérifiez que vous avez sélectionné le bon périphérique. Pour éviter toute erreur, débranchez les autres supports de stockage s’il y en a plusieurs connectés.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Cliquez sur **NEXT**. Si le périphérique contient déjà des données, assurez-vous de les sauvegarder. Cliquez sur **Yes** pour continuer sans sauvegarde.

   .. image:: img/os_continue.png
      :width: 90%


#. Un message vous indiquera que **NVMe/USB Boot** a bien été écrit sur le support.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Insérez maintenant la carte Micro SD ou le SSD NVMe dans votre Raspberry Pi. Une fois alimenté via un câble USB-C, le bootloader sera écrit dans l’EEPROM du Raspberry Pi.

.. note::

    Le Raspberry Pi démarrera désormais depuis le NVMe, puis l’USB, puis la carte SD.
    
    Éteignez le Raspberry Pi et retirez la carte Micro SD ou le SSD NVMe.


2. Installer le système sur le SSD NVMe
--------------------------------------------

Vous pouvez maintenant installer le système d’exploitation sur votre SSD NVMe.


#. Dans le |link_rpi_imager|, cliquez sur **Raspberry Pi Device** et sélectionnez le modèle **Raspberry Pi 5**.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Sélectionnez **Operating System**, puis choisissez la version recommandée du système d’exploitation.

   .. image:: img/os_choose_os.png
      :width: 90%


#. Dans l’option **Storage**, sélectionnez le SSD NVMe pour l’installation.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Cliquez sur **NEXT**, puis sur **EDIT SETTINGS** pour personnaliser les paramètres de votre OS.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Définissez un **hostname** pour votre Raspberry Pi. Il s’agit de l’identifiant réseau de votre appareil. Vous pourrez y accéder via ``<hostname>.local`` ou ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png
         
   * Créez un **nom d’utilisateur** et un **mot de passe** pour le compte administrateur. Ces identifiants sont essentiels pour sécuriser votre Raspberry Pi, qui ne possède pas de mot de passe par défaut.

     .. image:: img/os_set_username.png
         
   * Configurez le Wi-Fi en renseignant le **SSID** de votre réseau ainsi que le **mot de passe**.

     .. note::

       Définissez le ``Wireless LAN country`` à l’aide du code alpha-2 à deux lettres de la norme `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondant à votre localisation.

     .. image:: img/os_set_wifi.png
         
   * Pour permettre un accès à distance à votre Raspberry Pi, activez SSH dans l’onglet Services.

     * Pour **password authentication**, utilisez les identifiants définis dans l’onglet General.
     * Pour l’authentification par clé publique, sélectionnez « Autoriser uniquement l’authentification par clé publique ». Si vous disposez d’une clé RSA, elle sera utilisée. Sinon, cliquez sur « Exécuter SSH-keygen » pour générer une paire de clés.

     .. image:: img/os_enable_ssh.png
         
   * Le menu **Options** vous permet de configurer le comportement d’Imager lors de l’écriture, comme la lecture d’un son à la fin, l’éjection automatique du support ou l’activation de la télémétrie.

     .. image:: img/os_options.png

#. Une fois la configuration terminée, cliquez sur **Save** pour enregistrer vos réglages, puis sur **Yes** pour les appliquer à l’écriture de l’image.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Si le SSD NVMe contient déjà des données, assurez-vous d’effectuer une sauvegarde. Cliquez sur **Yes** si aucune sauvegarde n’est nécessaire.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Lorsque le message "Write Successful" s’affiche, l’image a été correctement écrite et vérifiée. Votre Raspberry Pi est désormais prêt à démarrer depuis le SSD NVMe !

   .. image:: img/nvme_install_finish.png
      :width: 90%

