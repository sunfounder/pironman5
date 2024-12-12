.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez vos problèmes après-vente et relevez vos défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives**: Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales**: Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et tirages au sort**: Participez à des tirages au sort et à des promotions festives.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

FAQ
============

1. À propos des systèmes compatibles
---------------------------------------

Systèmes ayant réussi le test sur le Raspberry Pi 5 :

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. À propos du bouton d'alimentation
---------------------------------------

Le bouton d'alimentation reproduit les fonctionnalités du bouton d'alimentation du Raspberry Pi 5.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Extinction**

  * Si vous utilisez le système Raspberry Pi **Bookworm Desktop**, vous pouvez appuyer deux fois rapidement sur le bouton d'alimentation pour l'éteindre. 
  * Si vous utilisez le système Raspberry Pi **Bookworm Lite**, appuyez une seule fois sur le bouton pour lancer l'extinction.
  * Pour forcer une extinction brutale, maintenez le bouton d'alimentation enfoncé.

* **Allumage**

  * Si la carte Raspberry Pi est éteinte mais encore alimentée, une simple pression allumera le système.

* Si vous utilisez un système ne prenant pas en charge un bouton d'extinction, maintenez-le enfoncé pendant 5 secondes pour forcer une extinction brutale, et une simple pression allumera le système.

3. À propos du flux d'air
----------------------------

Le flux d'air dans le boîtier Pironman 5 est conçu pour maximiser l'efficacité du refroidissement. L'air frais entre principalement par l'interface GPIO et d'autres petites ouvertures, garantissant une prise uniforme. Il traverse ensuite le Tool Cooler, équipé d'un ventilateur haute performance pour réguler les températures internes, et est enfin expulsé par les deux ventilateurs RGB sur le panneau latéral.

Pour une démonstration détaillée, veuillez consulter la vidéo :

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="_static/video/airflow_direction.mp4"  type="video/mp4">
            Votre navigateur ne supporte pas la balise vidéo.
        </video>
    </div>

4. Le Pironman 5 prend-il en charge les systèmes de rétro-gaming ?
-------------------------------------------------------------------

Oui, il est compatible. Cependant, la plupart des systèmes de rétro-gaming sont des versions allégées qui ne permettent pas l'installation et l'exécution de logiciels supplémentaires. Cette limitation peut empêcher certains composants du Pironman 5, tels que l'écran OLED, les deux ventilateurs RGB et les 4 LED RGB, de fonctionner correctement, car ces composants nécessitent l'installation de packages logiciels spécifiques au Pironman 5.

.. note::

   Le système Batocera.linux est désormais entièrement compatible avec le Pironman 5. Batocera.linux est une distribution open-source et totalement gratuite dédiée au rétro-gaming.

   * :ref:`install_batocera`
   * :ref:`set_up_batocera`

5. Écran OLED ne fonctionne pas ?
-----------------------------------

Si l'écran OLED ne s'affiche pas ou s'affiche incorrectement, suivez ces étapes de dépannage :

#. Assurez-vous que le câble FPC de l'écran OLED est bien connecté. Il est recommandé de reconnecter l'écran OLED, puis d'allumer l'appareil.  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_oled_screen.mp4" type="video/mp4">
               Votre navigateur ne supporte pas la balise vidéo.
           </video>
       </div>

#. Vérifiez que le Raspberry Pi exécute un système d'exploitation compatible. Le Pironman 5 prend uniquement en charge les systèmes suivants :  

   .. image:: img/compitable_os.png  
      :width: 600  
      :align: center  

   Si vous avez installé un système non pris en charge, suivez le guide pour installer un système compatible : :ref:`install_the_os`.

#. Lors de la première mise sous tension de l'écran OLED, il peut n'afficher que des blocs de pixels. Vous devez suivre les instructions dans :ref:`set_up_pironman5` pour terminer la configuration avant qu'il puisse afficher les informations correctement.

#. Utilisez la commande suivante pour vérifier si l'adresse I2C ``0x3C`` de l'OLED est détectée :  

   .. code-block:: shell

      sudo i2cdetect -y 1

   * Si l'adresse I2C ``0x3C`` est détectée, redémarrez le service Pironman 5 avec cette commande :

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * Activez I2C si l'adresse n'est pas détectée :

     * Modifiez le fichier de configuration en exécutant :

       .. code-block:: shell

         sudo nano /boot/firmware/config.txt

     * Ajoutez la ligne suivante à la fin du fichier :

       .. code-block:: shell

         dtparam=i2c_arm=on

     * Enregistrez le fichier en appuyant sur ``Ctrl+X``, puis ``Y``, et quittez. Redémarrez le Pironman 5 et vérifiez si le problème est résolu.

Si le problème persiste après avoir effectué les étapes ci-dessus, veuillez envoyer un email à service@sunfounder.com. Nous répondrons dès que possible.

6. Le module NVMe PIP ne fonctionne pas ?
------------------------------------------

1. Assurez-vous que le câble FPC reliant le module NVMe PIP au Raspberry Pi 5 est solidement attaché.  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Votre navigateur ne supporte pas la balise vidéo.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Votre navigateur ne supporte pas la balise vidéo.
           </video>
       </div>

2. Vérifiez que votre SSD est correctement fixé au module NVMe PIP.  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_ssd.mp4" type="video/mp4">
               Votre navigateur ne supporte pas la balise vidéo.
           </video>
       </div>

3. Vérifiez l'état des LED du module NVMe PIP :

   Après avoir vérifié toutes les connexions, allumez le Pironman 5 et observez les deux indicateurs sur le module NVMe PIP :  

   * **LED PWR** : Doit être allumée.  
   * **LED STA** : Doit clignoter pour indiquer un fonctionnement normal.  

   .. image:: img/nvme_pip_leds.png  

   * Si la **LED PWR** est allumée mais que la **LED STA** ne clignote pas, cela indique que le SSD NVMe n'est pas reconnu par le Raspberry Pi.  
   * Si la **LED PWR** est éteinte, court-circuitez les broches "Force Enable" (J4) sur le module. Si la **LED PWR** s'allume, cela pourrait indiquer un câble FPC mal connecté ou une configuration système non prise en charge pour le NVMe.

     .. image:: img/nvme_pip_j4.png  

4. Vérifiez que votre SSD NVMe dispose d'un système d'exploitation correctement installé. Référez-vous à : :ref:`install_the_os`.

5. Si le câblage est correct et le système d'exploitation installé, mais que le SSD NVMe ne démarre toujours pas, essayez de démarrer à partir d'une carte Micro SD pour vérifier la fonctionnalité des autres composants. Une fois confirmé, passez à :ref:`configure_boot_ssd`.

Si le problème persiste après avoir effectué les étapes ci-dessus, veuillez envoyer un email à service@sunfounder.com. Nous répondrons dès que possible.

7. Les LED RGB ne fonctionnent pas ?
-------------------------------------

#. Les deux broches sur l'IO Expander au-dessus de J9 sont utilisées pour connecter les LED RGB au GPIO10. Assurez-vous que le cavalier sur ces deux broches est correctement en place.

   .. image:: advanced/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Vérifiez que le Raspberry Pi exécute un système d'exploitation compatible. Le Pironman 5 prend uniquement en charge les versions suivantes :

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Si vous avez installé un système d'exploitation non pris en charge, suivez le guide pour installer un système compatible : :ref:`install_the_os`.

#. Exécutez la commande ``sudo raspi-config`` pour ouvrir le menu de configuration. Accédez à **3 Interfacing Options** -> **I3 SPI** -> **YES**, puis cliquez sur **OK** et **Finish** pour activer SPI. Après l'activation de SPI, redémarrez le Pironman 5.

Si le problème persiste après avoir suivi ces étapes, veuillez envoyer un email à service@sunfounder.com. Nous répondrons dès que possible.

8. Comment désactiver le tableau de bord Web ?
-----------------------------------------------

Une fois le module ``pironman5`` installé, vous pourrez accéder au :ref:`view_control_dashboard`.

Si vous n'avez pas besoin de cette fonctionnalité et souhaitez réduire l'utilisation du processeur et de la RAM, vous pouvez désactiver le tableau de bord pendant l'installation de ``pironman5`` en ajoutant l'option ``--disable-dashboard``.

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Si ``pironman5`` est déjà installé, vous pouvez supprimer le module ``dashboard`` et ``influxdb``, puis redémarrer ``pironman5`` pour appliquer les modifications :

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

9. Comment contrôler les composants avec la commande ``pironman5``
-------------------------------------------------------------------

Vous pouvez vous référer au tutoriel suivant pour contrôler les composants du Pironman 5 en utilisant la commande ``pironman5``.

* :ref:`view_control_commands`

10. Comment changer l'ordre de démarrage du Raspberry Pi avec des commandes
----------------------------------------------------------------------------

Si vous êtes déjà connecté à votre Raspberry Pi, vous pouvez modifier l'ordre de démarrage en utilisant des commandes. Les instructions détaillées sont disponibles ici :

* :ref:`configure_boot_ssd`

11. Comment modifier l'ordre de démarrage avec Raspberry Pi Imager ?
-----------------------------------------------------------------------

En plus de modifier l'ordre de démarrage dans la configuration de l'EEPROM, vous pouvez également utiliser **Raspberry Pi Imager**.

Il est recommandé d'utiliser une carte de rechange pour cette étape.

* :ref:`update_bootloader`

12. Comment copier le système de la carte SD vers un SSD NVMe ?
----------------------------------------------------------------

Si vous avez un SSD NVMe mais pas d'adaptateur pour connecter votre NVMe à votre ordinateur, vous pouvez d'abord installer le système sur votre carte Micro SD. Une fois le Pironman 5 démarré avec succès, vous pouvez copier le système de la carte Micro SD vers le SSD NVMe. Instructions détaillées ici :

* :ref:`copy_sd_to_nvme_rpi`

13. Comment retirer le film protecteur des plaques en acrylique ?
-------------------------------------------------------------------

Deux panneaux en acrylique sont inclus dans le package, tous deux recouverts d'un film protecteur jaune/transparent des deux côtés pour éviter les rayures. Le film protecteur peut être difficile à retirer. Utilisez un tournevis pour gratter doucement les coins, puis retirez délicatement tout le film.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _openssh_powershell:

14. Comment installer OpenSSH via PowerShell ?
-----------------------------------------------

Lorsque vous utilisez ``ssh <username>@<hostname>.local`` (ou ``ssh <username>@<IP address>``) pour vous connecter à votre Raspberry Pi, mais que le message d'erreur suivant apparaît :

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

Cela signifie que votre système Windows est trop ancien et ne dispose pas de `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ préinstallé. Vous devez suivre le tutoriel ci-dessous pour l'installer manuellement.

#. Tapez ``powershell`` dans la barre de recherche de votre bureau Windows, faites un clic droit sur ``Windows PowerShell``, et sélectionnez ``Exécuter en tant qu'administrateur`` dans le menu qui apparaît.

   .. image:: img/powershell_ssh.png
      :width: 90%

#. Utilisez la commande suivante pour installer ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Après l'installation, le résultat suivant s'affichera :

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Vérifiez l'installation avec la commande suivante :

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Cela vous indiquera que ``OpenSSH.Client`` a été installé avec succès :

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        Si l'indication ci-dessus n'apparaît pas, cela signifie que votre système Windows est encore trop ancien. Nous vous conseillons d'installer un outil SSH tiers, comme |link_putty|.

#. Redémarrez PowerShell et exécutez-le à nouveau en tant qu'administrateur. Vous pourrez maintenant vous connecter à votre Raspberry Pi avec la commande ``ssh``, où il vous sera demandé d'entrer le mot de passe configuré précédemment.

   .. image:: img/powershell_login.png

