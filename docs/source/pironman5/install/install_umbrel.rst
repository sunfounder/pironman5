.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives**: Bénéficiez d'un accès anticipé aux nouvelles annonces de produits et à des aperçus exclusifs.
    - **Réductions spéciales**: Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et concours**: Participez à des tirages au sort et à des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !


Installation de Umbrel OS
============================================

Umbrel est une plateforme/système d’exploitation open-source pour serveurs domestiques qui vous permet d’exécuter votre propre nœud Bitcoin, d’installer une variété d’applications auto-hébergées en un clic et de transformer votre matériel en votre cloud personnel. C’est un excellent moyen de débuter avec l’autocustodie et la confidentialité.

**Composants requis**

* Un ordinateur personnel  
* Un SSD NVMe  
* Un adaptateur NVMe vers USB  
* Une carte Micro SD et un lecteur


1. Mettre à jour le Bootloader
--------------------------------

Tout d’abord, il est nécessaire de mettre à jour le bootloader du Raspberry Pi 5 afin qu’il démarre à partir du NVMe avant d’essayer depuis l’USB, puis depuis la carte SD.

.. note::

    * À cette étape, il est recommandé d’utiliser une carte Micro SD de rechange. Écrivez d’abord le bootloader sur cette carte Micro SD, puis insérez-la immédiatement dans le Raspberry Pi pour activer le démarrage à partir d’un périphérique NVMe.  
    * Alternativement, vous pouvez écrire le bootloader directement sur votre périphérique NVMe, puis l’insérer dans le Raspberry Pi pour modifier la méthode de démarrage. Ensuite, connectez le SSD NVMe à un ordinateur pour installer le système d’exploitation et, une fois l’installation terminée, réinsérez-le dans le Raspberry Pi.

#. Insérez votre carte Micro SD ou SSD NVMe dans l’ordinateur ou l’ordinateur portable à l’aide d’un lecteur.

#. Dans |link_rpi_imager|, cliquez sur **Raspberry Pi Device** et sélectionnez le modèle **Raspberry Pi 5** dans le menu déroulant.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Dans l’onglet **Operating System**, faites défiler vers le bas et sélectionnez **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Sélectionnez **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Sélectionnez **NVMe/USB Boot** pour permettre au Raspberry Pi 5 de démarrer à partir du NVMe avant d’essayer l’USB puis la carte SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%
      
#. Dans l’option **Storage**, sélectionnez le périphérique de stockage approprié pour l’installation.

   .. note::

      Assurez-vous de sélectionner le bon périphérique de stockage. Pour éviter toute confusion, déconnectez les autres périphériques de stockage si plusieurs sont branchés.

   .. image:: img/os_choose_sd.png
      :width: 90%
      

#. Vous pouvez maintenant cliquer sur **NEXT**. Si le périphérique de stockage contient déjà des données, veillez à effectuer une sauvegarde afin d’éviter toute perte de données. Cliquez sur **Yes** pour continuer s’il n’est pas nécessaire de sauvegarder.

   .. image:: img/os_continue.png
      :width: 90%
      

#. Bientôt, un message vous indiquera que **NVMe/USB Boot** a été écrit sur votre périphérique de stockage.

   .. image:: img/nvme_boot_finish.png
      :width: 90%
      

#. Insérez votre carte Micro SD ou SSD NVMe dans le Raspberry Pi. Après avoir connecté l’adaptateur d’alimentation Type-C, le bootloader de la carte Micro SD ou du SSD NVMe sera écrit dans la mémoire EEPROM du Raspberry Pi.

   .. note::

      * Après la mise à jour, le Raspberry Pi démarrera d’abord depuis le disque NVMe, puis depuis l’USB et enfin depuis la carte Micro SD.  
      * Attendez une à deux minutes, puis éteignez le Raspberry Pi et retirez la carte Micro SD ou le SSD NVMe.

2. Installer le système d’exploitation sur le SSD NVMe
------------------------------------------------------------

**Étapes**

1. Téléchargez la dernière image d’Umbrel OS et extrayez-la. Vous pouvez également visiter la `page des versions d’Umbrel <https://github.com/getumbrel/umbrel/releases>`_ pour choisir une version spécifique.

   * :download:`Dernière image d’Umbrel OS <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

2. Dans |link_rpi_imager|, cliquez sur **Raspberry Pi Device** et sélectionnez **Raspberry Pi 5** dans le menu déroulant.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

3. Lancez le **Raspberry Pi Imager** et cliquez sur **CHOOSE OS**.

   .. image:: img/umbrel_choose_os.png
       :width: 600
       :align: center

4. Faites défiler jusqu’en bas et sélectionnez **Use custom**.

   .. image:: img/umbrel_use_custom.png
       :width: 600
       :align: center

5. Sélectionnez le fichier image d’Umbrel OS que vous avez téléchargé précédemment et cliquez sur **Open**.

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

6. Dans la section **Storage**, sélectionnez le SSD NVMe comme destination pour l’installation.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%

7. Cliquez sur **NEXT**, puis sélectionnez **NO**. Umbrel OS initialisera automatiquement son propre système et la configuration de l’utilisateur lors du premier démarrage. Il n’utilise pas le nom d’utilisateur ni le mot de passe définis dans le Raspberry Pi Imager.

   .. image:: img/umbrel_clear_setting.png
      :width: 90%

8. Si le SSD NVMe contient déjà des données, effectuez une sauvegarde avant de continuer afin d’éviter toute perte de données. Cliquez sur **Yes** pour continuer s’il n’est pas nécessaire de sauvegarder.

   .. image:: img/nvme_erase.png
      :width: 90%

9. Lorsque le message « Write Successful » apparaît, cela signifie que l’image a été complètement écrite et vérifiée. Votre SSD NVMe est maintenant prêt à démarrer le Raspberry Pi !

   .. image:: img/umbrel_finish.png
      :width: 90%

