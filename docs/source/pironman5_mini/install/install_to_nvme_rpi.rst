.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez dans l’univers du Raspberry Pi, de l’Arduino et de l’ESP32 avec d’autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Résolvez les problèmes après-vente et techniques avec l’aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits.
    - **Réductions spéciales** : Bénéficiez de remises exclusives sur nos nouveautés.
    - **Promotions festives et concours** : Participez à des jeux-concours et événements spéciaux.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _install_to_nvme_rpi_mini:

Installation du système d’exploitation sur un SSD NVMe
===============================================================

Si vous utilisez un SSD NVMe et que vous disposez d’un adaptateur pour le connecter à votre ordinateur, vous pouvez suivre ce tutoriel pour une installation rapide.

**Matériel nécessaire**

* Un ordinateur
* Un SSD NVMe
* Un adaptateur NVMe vers USB
* Une carte Micro SD et un lecteur

.. _update_bootloader_mini:

1. Mettre à jour le bootloader
--------------------------------

Vous devez d’abord mettre à jour le bootloader du Raspberry Pi 5 pour lui permettre de démarrer depuis le SSD NVMe avant de tester l’USB, puis la carte SD.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/tCKTgAeWIjc?start=47&end=95&si=xbmsWGBvCWefX01T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


.. note::

    Il est recommandé d’utiliser une carte Micro SD de secours pour cette étape. Écrivez d’abord le bootloader sur cette carte, puis insérez-la immédiatement dans le Raspberry Pi pour activer le démarrage depuis un périphérique NVMe.
    
    Alternativement, vous pouvez écrire le bootloader directement sur le SSD NVMe, l’insérer ensuite dans le Raspberry Pi pour modifier la méthode de démarrage. Puis, connectez le SSD à un ordinateur pour y installer le système, et réinsérez-le dans le Raspberry Pi après l’installation.

#. Insérez la carte Micro SD ou le SSD NVMe dans votre ordinateur via un lecteur.

#. Dans |link_rpi_imager|, cliquez sur **Appareil Raspberry Pi** et sélectionnez **Raspberry Pi 5** dans la liste.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Dans l’onglet **Système d’exploitation**, faites défiler jusqu’à **Images utilitaires diverses**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Sélectionnez **Bootloader (famille Pi 5)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Choisissez **Démarrage NVMe/USB** pour activer le démarrage via NVMe avant l’USB et la carte SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%



#. Dans **Stockage**, sélectionnez le périphérique approprié.

   .. note::

      Assurez-vous de choisir le bon périphérique. Déconnectez les autres supports de stockage pour éviter toute confusion.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Cliquez sur **SUIVANT**. Si le support contient des données, sauvegardez-les. Cliquez sur **Oui** si aucune sauvegarde n’est nécessaire.

   .. image:: img/os_continue.png
      :width: 90%


#. Un message vous indiquera que **NVMe/USB Boot** a bien été écrit.

   .. image:: img/nvme_boot_finish.png
      :width: 90%


#. Insérez maintenant la carte Micro SD ou le SSD NVMe dans le Raspberry Pi. Branchez l’alimentation via un câble Type C : le bootloader sera écrit dans la mémoire EEPROM du Raspberry Pi.

.. note::

    Par la suite, le Raspberry Pi démarrera depuis le SSD NVMe, puis l’USB, puis la carte SD.
    
    Éteignez le Raspberry Pi et retirez la carte Micro SD ou le SSD NVMe.


2. Installer l’OS sur le SSD NVMe
-----------------------------------

Vous pouvez désormais installer le système d’exploitation sur votre SSD NVMe.


#. Dans |link_rpi_imager|, cliquez sur **Appareil Raspberry Pi** et sélectionnez **Raspberry Pi 5**.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Sélectionnez **Système d’exploitation** et choisissez la version recommandée.

   .. image:: img/os_choose_os.png
      :width: 90%


#. Dans **Stockage**, sélectionnez le SSD NVMe.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Cliquez sur **SUIVANT**, puis sur **MODIFIER LES PARAMÈTRES** pour personnaliser le système.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Définissez un **nom d’hôte** pour votre Raspberry Pi. Ce nom identifie votre Raspberry Pi sur le réseau. Vous pouvez y accéder via ``<hostname>.local`` ou ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png
         
   * Créez un **nom d’utilisateur** et un **mot de passe** pour le compte administrateur. Ceci est crucial pour la sécurité du Raspberry Pi, qui n’a pas de mot de passe par défaut.

     .. image:: img/os_set_username.png
         
   * Configurez le Wi-Fi en saisissant le **SSID** et le **mot de passe** de votre réseau.

     .. note::

       Définissez le paramètre ``Wireless LAN country`` en utilisant le code à deux lettres `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondant à votre pays.

     .. image:: img/os_set_wifi.png
         
   * Pour activer l’accès à distance, cochez **Activer SSH** dans l’onglet Services.

     * Pour une **authentification par mot de passe**, utilisez les identifiants définis dans l’onglet Général.
     * Pour une authentification par **clé publique**, cochez "Autoriser uniquement l’authentification par clé publique". Si aucune clé RSA n’est présente, cliquez sur "Run SSH-keygen" pour générer une paire de clés.

     .. image:: img/os_enable_ssh.png

   * Le menu **Options** permet de régler le comportement d’Imager : son en fin d’écriture, éjection automatique, télémétrie, etc.

     .. image:: img/os_options.png

#. Une fois les paramètres personnalisés, cliquez sur **Enregistrer**, puis sur **Oui** pour les appliquer.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Si le SSD contient des données, sauvegardez-les. Cliquez sur **Oui** pour continuer sans sauvegarde.

   .. image:: img/nvme_erase.png
      :width: 90%


#. Une fois le message "Écriture réussie" affiché, votre image a bien été écrite et vérifiée. Vous êtes prêt(e) à démarrer votre Raspberry Pi depuis le SSD NVMe !

   .. image:: img/nvme_install_finish.png
      :width: 90%