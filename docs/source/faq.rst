.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Assistance experte** : Résolvez les problèmes après-vente et les défis techniques avec l’aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aperçus exclusifs.
    - **Réductions spéciales** : Bénéficiez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et des promotions spéciales.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

FAQ
=====

1. À propos des systèmes compatibles
--------------------------------------

Systèmes ayant passé les tests sur le Raspberry Pi 5 :

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. À propos du bouton d’alimentation
--------------------------------------

Le bouton d’alimentation est une extension de celui du Raspberry Pi 5 et fonctionne de manière identique.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Arrêt**

  * Si vous utilisez le système Raspberry Pi **Bookworm Desktop**, appuyez deux fois rapidement sur le bouton d’alimentation pour l’éteindre.
  * Si vous utilisez le système Raspberry Pi **Bookworm Lite**, appuyez une seule fois sur le bouton d’alimentation pour initier l’arrêt.
  * Pour forcer un arrêt complet, maintenez le bouton d’alimentation enfoncé.

* **Allumage**

  * Si la carte Raspberry Pi est éteinte mais toujours alimentée, appuyez une seule fois pour l’allumer.

* Si vous utilisez un système qui ne prend pas en charge le bouton d’arrêt, maintenez-le enfoncé pendant 5 secondes pour forcer un arrêt complet, puis appuyez une seule fois pour l’allumer.

3. À propos de la direction du flux d’air
-------------------------------------------

Le flux d’air dans le châssis du Pironman 5 est conçu avec soin pour maximiser l’efficacité du refroidissement. L’air frais entre principalement par l’interface GPIO et d’autres petites ouvertures, garantissant une prise d’air uniforme. Il traverse ensuite le Tool Cooler, équipé d’un ventilateur haute performance pour réguler la température interne, et est finalement expulsé par les deux ventilateurs RGB sur le panneau latéral.

Pour une démonstration détaillée, consultez la vidéo suivante :

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="_static/video/airflow_direction.mp4"  type="video/mp4">
            Votre navigateur ne prend pas en charge la balise vidéo.
        </video>
    </div>


4. À propos des embouts en cuivre du refroidisseur à tour
------------------------------------------------------------

Les caloducs en forme de U situés en haut du refroidisseur à tour sont comprimés pour permettre leur passage à travers les ailettes en aluminium, ce qui fait partie du processus de fabrication standard des caloducs en cuivre.

   .. image:: img/tower_cooler1.png

5. Le Pironman 5 prend-il en charge les systèmes de jeux rétro ?
------------------------------------------------------------------

Oui, il est compatible. Cependant, la plupart des systèmes de jeux rétro sont des versions simplifiées qui ne permettent pas l’installation et l’exécution de logiciels supplémentaires. Cette limitation peut empêcher certains composants du Pironman 5, tels que l’écran OLED, les deux ventilateurs RGB et les 4 LED RGB, de fonctionner correctement, car ces composants nécessitent l’installation des paquets logiciels du Pironman 5.

.. note::

   Le système Batocera.linux est désormais entièrement compatible avec le Pironman 5. Batocera.linux est une distribution de jeux rétro open-source et entièrement gratuite.

   * :ref:`install_batocera`
   * :ref:`set_up_batocera`

6. L’écran OLED ne fonctionne pas ?
---------------------------------------

Si l’écran OLED ne s’affiche pas ou affiche incorrectement, suivez ces étapes de dépannage :

#. Assurez-vous que le câble FPC de l’écran OLED est correctement connecté. Il est recommandé de reconnecter l’écran OLED, puis de rallumer l’appareil.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_oled_screen.mp4" type="video/mp4">
               Votre navigateur ne prend pas en charge la balise vidéo.
           </video>
       </div>

#. Confirmez que le Raspberry Pi exécute un système d’exploitation compatible. Le Pironman 5 ne prend en charge que les systèmes suivants :  

   .. image:: img/compitable_os.png  
      :width: 600  
      :align: center  

   Si vous avez installé un système non pris en charge, suivez le guide pour installer un système d’exploitation compatible : :ref:`install_the_os`.

#. Lorsque l’écran OLED est alimenté pour la première fois, il peut n’afficher que des blocs de pixels. Suivez les instructions dans :ref:`set_up_pironman5` pour compléter la configuration avant qu’il puisse afficher les informations correctement.

#. Utilisez la commande suivante pour vérifier si l’adresse I2C ``0x3C`` de l’OLED est détectée :  

   .. code-block:: shell

      sudo i2cdetect -y 1

   * Si l’adresse I2C ``0x3C`` est détectée, redémarrez le service Pironman 5 avec cette commande :

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * Activez l’I2C si l’adresse n’est pas détectée :

     * Modifiez le fichier de configuration en exécutant :

       .. code-block:: shell

         sudo nano /boot/firmware/config.txt

     * Ajoutez la ligne suivante à la fin du fichier :

       .. code-block:: shell

         dtparam=i2c_arm=on

     * Enregistrez le fichier en appuyant sur ``Ctrl+X``, puis ``Y``, et quittez. Redémarrez le Pironman 5 et vérifiez si le problème est résolu.

Si le problème persiste après avoir suivi les étapes ci-dessus, veuillez envoyer un e-mail à service@sunfounder.com. Nous répondrons dès que possible.

7. Le module NVMe PIP ne fonctionne pas ?
----------------------------------------------

1. Assurez-vous que le câble FPC connectant le module NVMe PIP au Raspberry Pi 5 est solidement attaché.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Votre navigateur ne prend pas en charge la balise vidéo.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Votre navigateur ne prend pas en charge la balise vidéo.
           </video>
       </div>

2. Vérifiez que votre SSD est correctement fixé au module NVMe PIP.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_ssd.mp4" type="video/mp4">
               Votre navigateur ne prend pas en charge la balise vidéo.
           </video>
       </div>

3. Vérifiez l’état des voyants LED du module NVMe PIP :

   Après avoir vérifié toutes les connexions, allumez le Pironman 5 et observez les deux voyants du module NVMe PIP :

   * **PWR LED** : Doit être allumé.  
   * **STA LED** : Doit clignoter pour indiquer un fonctionnement normal.  

   .. image:: img/nvme_pip_leds.png  

   * Si la **PWR LED** est allumée mais que la **STA LED** ne clignote pas, cela indique que le SSD NVMe n’est pas reconnu par le Raspberry Pi.  
   * Si la **PWR LED** est éteinte, court-circuitez les broches "Force Enable" (J4) sur le module. Si la **PWR LED** s’allume, cela peut indiquer un câble FPC mal connecté ou une configuration système non prise en charge pour NVMe.

     .. image:: img/nvme_pip_j4.png  

4. Confirmez que votre SSD NVMe a un système d’exploitation correctement installé. Consultez : :ref:`install_the_os`.

5. Si le câblage est correct et que l’OS est installé, mais que le SSD NVMe ne démarre toujours pas, essayez de démarrer à partir d’une carte Micro SD pour vérifier la fonctionnalité des autres composants. Une fois confirmé, procédez à : :ref:`configure_boot_ssd`.

Si le problème persiste après avoir suivi les étapes ci-dessus, veuillez envoyer un e-mail à service@sunfounder.com. Nous répondrons dès que possible.

8. Les LED RGB ne fonctionnent pas ?
----------------------------------------

#. Les deux broches sur l’expanseur IO au-dessus de J9 sont utilisées pour connecter les LED RGB au GPIO10. Assurez-vous que le cavalier est correctement en place sur ces deux broches.

   .. image:: advanced/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Vérifiez que le Raspberry Pi exécute un système d’exploitation compatible. Le Pironman 5 ne prend en charge que les versions OS suivantes :

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Si vous avez installé un OS non pris en charge, suivez le guide pour installer un système d’exploitation compatible : :ref:`install_the_os`.

#. Exécutez la commande ``sudo raspi-config`` pour ouvrir le menu de configuration. Naviguez vers **3 Interfacing Options** -> **I3 SPI** -> **YES**, puis cliquez sur **OK** et **Finish** pour activer le SPI. Après avoir activé le SPI, redémarrez le Pironman 5.

Si le problème persiste après avoir suivi les étapes ci-dessus, veuillez envoyer un e-mail à service@sunfounder.com. Nous répondrons dès que possible.

9. Le ventilateur du processeur ne fonctionne pas ?
---------------------------------------------------

Lorsque la température du processeur n’a pas atteint le seuil défini, le ventilateur du processeur ne fonctionnera pas.

**Contrôle de la vitesse du ventilateur basé sur la température**  

Le ventilateur PWM fonctionne dynamiquement, ajustant sa vitesse en fonction de la température du Raspberry Pi 5 :  

* **En dessous de 50°C** : Le ventilateur reste éteint (vitesse 0 %).  
* **À 50°C** : Le ventilateur fonctionne à faible vitesse (vitesse 30 %).  
* **À 60°C** : Le ventilateur passe à une vitesse moyenne (vitesse 50 %).  
* **À 67,5°C** : Le ventilateur augmente à haute vitesse (vitesse 70 %).  
* **À 75°C et plus** : Le ventilateur fonctionne à pleine vitesse (vitesse 100 %).  

Pour plus de détails, veuillez vous référer à : :ref:`Fans`.

10. Comment désactiver le tableau de bord web ?
--------------------------------------------------

Une fois que vous avez terminé l’installation du module ``pironman5``, vous pourrez accéder à :ref:`view_control_dashboard`.
      
Si vous n’avez pas besoin de cette fonctionnalité et souhaitez réduire l’utilisation du CPU et de la RAM, vous pouvez désactiver le tableau de bord lors de l’installation de ``pironman5`` en ajoutant l’option ``--disable-dashboard``.
      
.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard
      
Si vous avez déjà installé ``pironman5``, vous pouvez supprimer le module ``dashboard`` et ``influxdb``, puis redémarrer ``pironman5`` pour appliquer les changements :
      
.. code-block:: shell
      
   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

11. Comment contrôler les composants avec la commande ``pironman5`` ?
----------------------------------------------------------------------

Vous pouvez consulter le tutoriel suivant pour contrôler les composants du Pironman 5 en utilisant la commande ``pironman5`` :

* :ref:`view_control_commands`

12. Comment changer l’ordre de démarrage du Raspberry Pi à l’aide de commandes ?
---------------------------------------------------------------------------------

Si vous êtes déjà connecté à votre Raspberry Pi, vous pouvez modifier l’ordre de démarrage à l’aide de commandes. Les instructions détaillées sont les suivantes :

* :ref:`configure_boot_ssd`

13. Comment modifier l’ordre de démarrage avec Raspberry Pi Imager ?
---------------------------------------------------------------------

En plus de modifier le paramètre ``BOOT_ORDER`` dans la configuration EEPROM, vous pouvez également utiliser **Raspberry Pi Imager** pour changer l’ordre de démarrage de votre Raspberry Pi.

Il est recommandé d’utiliser une carte de rechange pour cette étape.

* :ref:`update_bootloader`

14. Comment copier le système de la carte SD vers un SSD NVMe ?
---------------------------------------------------------------

Si vous avez un SSD NVMe mais pas d’adaptateur pour le connecter à votre ordinateur, vous pouvez d’abord installer le système sur votre carte Micro SD. Une fois que le Pironman 5 démarre correctement, vous pouvez copier le système de votre carte Micro SD vers votre SSD NVMe. Les instructions détaillées sont les suivantes :

* :ref:`copy_sd_to_nvme_rpi`

15. Comment retirer le film protecteur des plaques en acrylique ?
---------------------------------------------------------------------

Deux plaques en acrylique sont incluses dans le colis, chacune recouverte d’un film protecteur jaune/transparent des deux côtés pour éviter les rayures. Le film protecteur peut être un peu difficile à retirer. Utilisez un tournevis pour gratter délicatement les coins, puis retirez soigneusement tout le film.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _openssh_powershell:

16. Comment installer OpenSSH via PowerShell ?
--------------------------------------------------

Lorsque vous utilisez la commande ``ssh <username>@<hostname>.local`` (ou ``ssh <username>@<IP address>``) pour vous connecter à votre Raspberry Pi, le message d’erreur suivant peut apparaître :

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

Cela signifie que votre système d’exploitation est trop ancien et n’a pas `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ préinstallé. Suivez le tutoriel ci-dessous pour l’installer manuellement.

#. Tapez ``powershell`` dans la barre de recherche de votre bureau Windows, faites un clic droit sur ``Windows PowerShell`` et sélectionnez ``Exécuter en tant qu’administrateur`` dans le menu contextuel.

   .. image:: img/powershell_ssh.png
      :width: 90%

#. Utilisez la commande suivante pour installer ``OpenSSH.Client`` :

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Une fois l’installation terminée, la sortie suivante sera affichée :

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Vérifiez l’installation à l’aide de la commande suivante :

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Le message suivant indique que ``OpenSSH.Client`` a été installé avec succès :

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        Si l’invite ci-dessus n’apparaît pas, cela signifie que votre système Windows est encore trop ancien. Nous vous conseillons d’installer un outil SSH tiers comme |link_putty|.

#. Redémarrez PowerShell et exécutez-le de nouveau en tant qu’administrateur. Vous pourrez alors vous connecter à votre Raspberry Pi en utilisant la commande ``ssh``, où il vous sera demandé d’entrer le mot de passe que vous avez défini précédemment.

   .. image:: img/powershell_login.png


17. Comment activer/désactiver l’écran OLED ?
-------------------------------------------------

Vous pouvez activer ou désactiver l’écran OLED via le tableau de bord ou la ligne de commande.

1. Activer/désactiver l’écran OLED depuis le tableau de bord.

   .. note::

    Avant d’utiliser le tableau de bord, vous devez l’avoir configuré sur Home Assistant. Veuillez vous référer à :ref:`view_control_dashboard`.

- Une fois la configuration terminée, suivez ces étapes pour activer, désactiver ou configurer votre écran OLED.

   .. image:: img/set_up_on_dashboard.jpg
      :width: 90%

2. Activer/désactiver l’écran OLED via la ligne de commande.

- Utilisez la commande suivante pour activer ou désactiver l’écran OLED :

.. code-block::

    sudo pironman5 -oe on/off

.. note::

    Il peut être nécessaire de redémarrer le service pironman5 pour que les modifications prennent effet. Utilisez la commande suivante pour redémarrer le service :

      .. code-block::

        sudo systemctl restart pironman5.service
