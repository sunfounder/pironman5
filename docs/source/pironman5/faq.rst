.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-goûts.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et à des promotions spéciales pour les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

FAQ
=====

1. À propos des systèmes compatibles
---------------------------------------

Systèmes validés pour Raspberry Pi 5 :

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. À propos du bouton d'alimentation
--------------------------------------

Le bouton d'alimentation agit comme celui du Raspberry Pi 5 et offre les mêmes fonctions.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Arrêt**

  * Si vous utilisez le système **Bookworm Desktop** de Raspberry Pi, appuyez deux fois rapidement sur le bouton d'alimentation pour éteindre.
  * Si vous utilisez le système **Bookworm Lite**, appuyez une seule fois pour initier l'arrêt.
  * Pour forcer un arrêt brutal, maintenez le bouton d'alimentation enfoncé.

* **Mise sous tension**

  * Si la carte Raspberry Pi est éteinte mais toujours alimentée, appuyez une fois pour la rallumer.

* Si vous utilisez un système qui ne prend pas en charge un bouton d'arrêt, maintenez le bouton enfoncé pendant 5 secondes pour forcer un arrêt brutal, puis appuyez une fois pour rallumer.

3. À propos de la direction du flux d'air
--------------------------------------------

Le flux d'air dans le châssis Pironman 5 est conçu pour maximiser l'efficacité du refroidissement. L'air frais entre principalement par l'interface GPIO et d'autres petites ouvertures. Il passe ensuite par le Tool Cooler, équipé d'un ventilateur haute performance pour réguler la température interne, et est finalement expulsé par les deux ventilateurs RGB situés sur les panneaux latéraux.

Pour une démonstration détaillée, veuillez consulter la vidéo :

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="../_static/video/airflow_direction.mp4"  type="video/mp4">
            Votre navigateur ne prend pas en charge la balise vidéo.
        </video>
    </div>


4. À propos du refroidisseur tour
----------------------------------------------------------

#. Les caloducs en forme de U situés en haut du refroidisseur tour sont comprimés pour faciliter le passage des tubes en cuivre à travers les ailettes en aluminium. Il s'agit d'une étape normale du processus de fabrication des tubes en cuivre.

   .. image::  img/tower_cooler1.png

#. Précautions à prendre lors de l’installation d’un refroidisseur tour :

**Fixation des tampons** : Avant d’installer le refroidisseur tour, assurez-vous de fixer des tampons sur le Raspberry Pi afin d’éviter tout dommage ou rayure.

 .. image::  img/tower_cooler_thermal.png

**Orientation correcte** : Faites attention au sens de placement du refroidisseur tour. Alignez-le avec les trous de positionnement du Raspberry Pi avant d’appuyer sur les vis à ressort pour le fixer.

 .. image::  img/tower_cooler_place.jpg

**Retrait précautionneux** : Si le refroidisseur tour a été installé dans le mauvais sens ou si les tampons n’ont pas été appliqués, ne forcez pas son retrait.

- Pour retirer le refroidisseur tour en toute sécurité, suivez ces étapes :

  Utilisez une pince fine ou une pince à épiler pour saisir l’extrémité de l’écrou à ressort et poussez-le doucement vers le haut pour le détacher.

     .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/remove_tower_cooler.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>


5. À propos du Raspberry Pi AI HAT+
---------------------------------------

Le Raspberry Pi AI HAT+ n'est pas compatible avec le Pironman 5.

   .. image:: img/output3.png
        :width: 400

Le kit Raspberry Pi AI combine le Raspberry Pi M.2 HAT+ et le module accélérateur AI Hailo.

   .. image:: img/output2.jpg
        :width: 400

Vous pouvez détacher le module accélérateur AI Hailo du kit Raspberry Pi AI et l'insérer directement dans le module NVMe PIP du Pironman 5.

   .. image:: img/output4.png
        :width: 800

6. Le PI5 ne démarre pas (LED rouge) ?  
-------------------------------------------

Ce problème peut être causé par une mise à jour du système, des modifications de l’ordre de démarrage ou un chargeur de démarrage corrompu. Vous pouvez essayer les étapes suivantes pour résoudre le problème :

#. Vérifier la connexion de l’adaptateur USB-HDMI

   * Veuillez vérifier soigneusement si l’adaptateur USB-HDMI est correctement connecté au PI5.  
   * Essayez de débrancher puis de rebrancher l’adaptateur USB-HDMI.  
   * Reconnectez ensuite l’alimentation et vérifiez si le PI5 démarre correctement.

#. Tester le PI5 en dehors du boîtier

   * Si le fait de reconnecter l’adaptateur ne résout pas le problème :  
   * Retirez le PI5 du boîtier Pironman 5.  
   * Alimentez directement le PI5 avec l’adaptateur secteur (sans le boîtier).  
   * Vérifiez s’il peut démarrer normalement.

#. Restaurer le chargeur de démarrage

   * Si le PI5 ne démarre toujours pas, il se peut que le chargeur de démarrage soit corrompu. Vous pouvez suivre ce guide : :ref:`update_bootloader_5` et choisir de démarrer depuis la carte SD ou NVMe/USB.  
   * Insérez la carte SD préparée dans le PI5, mettez-le sous tension et attendez au moins 10 secondes. Une fois la récupération terminée, retirez et reformatez la carte SD.  
   * Ensuite, utilisez Raspberry Pi Imager pour flasher la dernière version de Raspberry Pi OS, réinsérez la carte et essayez de démarrer à nouveau.

.. 6. Le Pironman 5 est-il compatible avec les systèmes de rétro-gaming ?
.. -------------------------------------------------------------------------

.. Oui, il est compatible. Cependant, la plupart des systèmes de rétro-gaming sont des versions simplifiées qui ne peuvent pas installer et exécuter de logiciels supplémentaires. Cette limitation peut empêcher certains composants du Pironman 5, comme l'écran OLED, les deux ventilateurs RGB et les 4 LEDs RGB, de fonctionner correctement, car ils nécessitent l'installation des paquets logiciels de Pironman 5.

.. .. note::

..    Le système Batocera.linux est désormais entièrement compatible avec le Pironman 5. Batocera.linux est une distribution open-source et entièrement gratuite dédiée au rétro-gaming.

..    * :ref:`install_batocera`
..    * :ref:`set_up_batocera`

7. Écran OLED ne fonctionne pas ?
------------------------------------

Si l'écran OLED ne s'affiche pas ou affiche incorrectement, suivez ces étapes de dépannage :

#. Vérifiez que le câble FPC de l'écran OLED est correctement connecté. Il est recommandé de reconnecter l'écran OLED, puis d'allumer l'appareil.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_oled_screen.mp4" type="video/mp4">
               Votre navigateur ne prend pas en charge la balise vidéo.
           </video>
       </div>

#. Confirmez que le Raspberry Pi utilise un système d'exploitation compatible. Le Pironman 5 ne prend en charge que les systèmes suivants :

   .. image:: img/compitable_os.png  
      :width: 600  
      :align: center  

   Si vous avez installé un système non compatible, suivez le guide pour installer un système compatible : :ref:`install_the_os`.

#. Lors de la première activation de l'écran OLED, il peut afficher uniquement des blocs de pixels. Suivez les instructions dans :ref:`set_up_pironman5` pour compléter la configuration et permettre un affichage correct.

#. Utilisez la commande suivante pour vérifier si l'adresse I2C ``0x3C`` de l'OLED est détectée :

   .. code-block:: shell

      sudo i2cdetect -y 1

   * Si l'adresse I2C ``0x3C`` est détectée, redémarrez le service Pironman 5 avec cette commande :

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * Si l'adresse n'est pas détectée, activez l'I2C :

     * Modifiez le fichier de configuration avec cette commande :

       .. code-block:: shell

         sudo nano /boot/firmware/config.txt

     * Ajoutez la ligne suivante à la fin du fichier :

       .. code-block:: shell

         dtparam=i2c_arm=on

     * Enregistrez le fichier en appuyant sur ``Ctrl+X``, puis ``Y``, et quittez. Redémarrez le Pironman 5 et vérifiez si le problème est résolu.

Si le problème persiste après avoir effectué ces étapes, veuillez envoyer un e-mail à service@sunfounder.com. Nous vous répondrons dans les plus brefs délais.

8. Module NVMe PIP ne fonctionne pas ?
--------------------------------------------

1. Assurez-vous que le câble FPC reliant le module NVMe PIP au Raspberry Pi 5 est bien connecté.  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Votre navigateur ne prend pas en charge la balise vidéo.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Votre navigateur ne prend pas en charge la balise vidéo.
           </video>
       </div>

2. Vérifiez que votre SSD est correctement fixé au module NVMe PIP.  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_ssd.mp4" type="video/mp4">
               Votre navigateur ne prend pas en charge la balise vidéo.
           </video>
       </div>

3. Vérifiez l'état des voyants LED du module NVMe PIP :

   Une fois toutes les connexions vérifiées, allumez le Pironman 5 et observez les deux indicateurs sur le module NVMe PIP :  

   * **PWR LED** : Doit être allumé.  
   * **STA LED** : Doit clignoter pour indiquer un fonctionnement normal.  

   .. image:: img/nvme_pip_leds.png  

   * Si le **PWR LED** est allumé mais que le **STA LED** ne clignote pas, cela signifie que le NVMe SSD n'est pas reconnu par le Raspberry Pi.  
   * Si le **PWR LED** est éteint, reliez les broches "Force Enable" (J4) sur le module. Si le **PWR LED** s'allume, cela peut indiquer un câble FPC mal connecté ou une configuration système non prise en charge pour le NVMe.

     .. image:: img/nvme_pip_j4.png  

4. Vérifiez que votre NVMe SSD dispose d'un système d'exploitation correctement installé. Consultez : :ref:`install_the_os`.

5. Si le câblage est correct et que le système d'exploitation est installé, mais que le NVMe SSD ne démarre toujours pas, essayez de démarrer à partir d'une carte Micro SD pour vérifier la fonctionnalité des autres composants. Une fois confirmé, procédez à : :ref:`configure_boot_ssd`.

Si le problème persiste après avoir suivi ces étapes, veuillez envoyer un e-mail à service@sunfounder.com. Nous vous répondrons dans les plus brefs délais.

9. Les LEDs RGB ne fonctionnent pas ?
----------------------------------------

#. Les deux broches sur l'IO Expander au-dessus de J9 sont utilisées pour connecter les LEDs RGB à GPIO10. Assurez-vous que le cavalier sur ces deux broches est correctement en place.

   .. image:: img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Vérifiez que le Raspberry Pi utilise un système d'exploitation compatible. Le Pironman 5 prend uniquement en charge les versions suivantes :

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   Si vous avez installé un système non compatible, suivez le guide pour installer un système compatible : :ref:`install_the_os`.

#. Exécutez la commande ``sudo raspi-config`` pour ouvrir le menu de configuration. Allez dans **3 Interfacing Options** -> **I3 SPI** -> **YES**, puis cliquez sur **OK** et **Finish** pour activer SPI. Après avoir activé SPI, redémarrez le Pironman 5.

Si le problème persiste après avoir suivi ces étapes, veuillez envoyer un e-mail à service@sunfounder.com. Nous vous répondrons dans les plus brefs délais.

10. Le ventilateur CPU ne fonctionne pas ?
---------------------------------------------

Lorsque la température du CPU n'a pas atteint le seuil défini, le ventilateur CPU ne fonctionne pas.

**Contrôle de la vitesse du ventilateur basé sur la température**  

Le ventilateur PWM fonctionne de manière dynamique, ajustant sa vitesse en fonction de la température du Raspberry Pi 5 :  

* **En dessous de 50°C** : Le ventilateur reste éteint (0% de vitesse).  
* **À 50°C** : Le ventilateur fonctionne à faible vitesse (30% de vitesse).  
* **À 60°C** : Le ventilateur passe à une vitesse moyenne (50% de vitesse).  
* **À 67,5°C** : Le ventilateur accélère à une vitesse élevée (70% de vitesse).  
* **À 75°C et au-delà** : Le ventilateur fonctionne à pleine vitesse (100% de vitesse).  

Pour plus de détails, consultez : :ref:`Fans`.

11. Comment désactiver le tableau de bord web ?
--------------------------------------------------

Une fois l'installation du module ``pironman5`` terminée, vous pouvez accéder au :ref:`view_control_dashboard`.
      
Si vous n'avez pas besoin de cette fonctionnalité et souhaitez réduire l'utilisation du CPU et de la RAM, vous pouvez désactiver le tableau de bord lors de l'installation de ``pironman5`` en ajoutant l'option ``--disable-dashboard``.
      
.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard
      
Si vous avez déjà installé ``pironman 5``, vous pouvez supprimer le module ``dashboard`` et ``influxdb``, puis redémarrer pironman5 pour appliquer les changements :
      
.. code-block:: shell
      
   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

12. Comment contrôler les composants avec la commande ``pironman5`` ?
------------------------------------------------------------------------

Vous pouvez consulter le tutoriel suivant pour contrôler les composants du Pironman 5 en utilisant la commande ``pironman5`` :

* :ref:`view_control_commands`

13. Comment modifier l'ordre de démarrage du Raspberry Pi en utilisant des commandes ?
-----------------------------------------------------------------------------------------

Si vous êtes déjà connecté à votre Raspberry Pi, vous pouvez modifier l'ordre de démarrage en utilisant des commandes. Les instructions détaillées sont les suivantes :

* :ref:`configure_boot_ssd`

14. Comment modifier l'ordre de démarrage avec Raspberry Pi Imager ?
-----------------------------------------------------------------------

En plus de modifier le ``BOOT_ORDER`` dans la configuration EEPROM, vous pouvez également utiliser **Raspberry Pi Imager** pour changer l'ordre de démarrage de votre Raspberry Pi.

Il est recommandé d'utiliser une carte de secours pour cette étape.

* :ref:`update_bootloader_5`

15. Comment copier le système de la carte SD vers un NVMe SSD ?
-----------------------------------------------------------------

Si vous avez un NVMe SSD mais pas d'adaptateur pour connecter votre NVMe à votre ordinateur, vous pouvez d'abord installer le système sur votre carte Micro SD. Une fois que le Pironman 5 a démarré avec succès, vous pouvez copier le système de votre carte Micro SD vers votre NVMe SSD. Les instructions détaillées sont les suivantes :

* :ref:`copy_sd_to_nvme_rpi`

16. Comment retirer le film protecteur des plaques en acrylique ?
--------------------------------------------------------------------

Deux panneaux en acrylique sont inclus dans le paquet, chacun étant recouvert d'un film protecteur jaune ou transparent des deux côtés pour éviter les rayures. Ce film protecteur peut être un peu difficile à retirer. Utilisez un tournevis pour gratter doucement les coins, puis décollez soigneusement l'intégralité du film.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _openssh_powershell:

17. Comment installer OpenSSH via PowerShell ?
-------------------------------------------------

Lorsque vous utilisez la commande ``ssh <username>@<hostname>.local`` (ou ``ssh <username>@<IP address>``) pour vous connecter à votre Raspberry Pi, mais que le message d'erreur suivant apparaît :

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

Cela signifie que votre système d’exploitation est trop ancien et n’a pas `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ préinstallé. Suivez le tutoriel ci-dessous pour l’installer manuellement.

#. Tapez ``powershell`` dans la barre de recherche de votre bureau Windows, cliquez avec le bouton droit sur ``Windows PowerShell`` et sélectionnez ``Exécuter en tant qu'administrateur``.

   .. image:: img/powershell_ssh.png
      :width: 90%

#. Utilisez la commande suivante pour installer ``OpenSSH.Client`` :

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Après l'installation, la sortie suivante devrait apparaître :

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Vérifiez l'installation avec la commande suivante :

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Cela vous indique que ``OpenSSH.Client`` a été installé avec succès :

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

  .. warning:: 
        Si ce message n'apparaît pas, cela signifie que votre système Windows est encore trop ancien. Il est conseillé d'utiliser un outil SSH tiers comme |link_putty|.

#. Redémarrez PowerShell et exécutez-le de nouveau en tant qu'administrateur. Vous pourrez alors vous connecter à votre Raspberry Pi en utilisant la commande ``ssh``, et il vous sera demandé de saisir le mot de passe que vous avez configuré.

   .. image:: img/powershell_login.png

.. 18. Pourquoi l’écran OLED s’éteint-il automatiquement ?
.. ---------------------------------------------------------------------------------

.. Pour économiser de l’énergie et prolonger la durée de vie de l’écran, l’écran OLED s’éteint automatiquement après une période d’inactivité.  
.. Cela fait partie de la conception normale et n’affecte pas la fonctionnalité du produit.

.. Il suffit d’appuyer une fois sur le bouton de l’appareil pour rallumer l’écran OLED et reprendre l’affichage.

.. .. note::

..    Pour la configuration de l’écran OLED (comme activer/désactiver, temps de veille, rotation, etc.), veuillez vous référer à : :ref:`view_control_dashboard` ou :ref:`view_control_commands`.
