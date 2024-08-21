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

Comment désactiver le tableau de bord web ?
------------------------------------------------------

Une fois l'installation du module ``pironman5`` terminée, vous pourrez accéder à :ref:`view_control_dashboard`.

Si vous n'avez pas besoin de cette fonctionnalité et souhaitez réduire l'utilisation du CPU et de la RAM, vous pouvez désactiver le tableau de bord lors de l'installation de ``pironman5`` en ajoutant le drapeau ``--disable-dashboard``.

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Si vous avez déjà installé ``pironman 5``, vous pouvez retirer le module ``dashboard`` et ``influxdb``, puis redémarrer pironman5 pour appliquer les modifications :

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5


Le Pironman 5 prend-il en charge les systèmes de jeux rétro ?
----------------------------------------------------------------

Oui, il est compatible. Cependant, la plupart des systèmes de jeux rétro sont des versions simplifiées qui ne permettent pas d'installer et d'exécuter de logiciels supplémentaires. Cette limitation peut empêcher certains composants du Pironman 5, comme l'écran OLED, les deux ventilateurs RGB et les 4 LED RGB, de fonctionner correctement, car ces composants nécessitent l'installation des packages logiciels du Pironman 5.


.. note::

    Le système Batocera.linux est désormais entièrement compatible avec le Pironman 5. Batocera.linux est une distribution rétro-gaming open-source et entièrement gratuite.

    * :ref:`install_batocera`
    * :ref:`set_up_batocera`

Comment contrôler les composants à l'aide de la commande ``pironman5``
---------------------------------------------------------------------------
Vous pouvez consulter le tutoriel suivant pour contrôler les composants du Pironman 5 à l'aide de la commande ``pironman5``.

* :ref:`view_control_commands`

Comment changer l'ordre de démarrage du Raspberry Pi à l'aide des commandes
------------------------------------------------------------------------------

Si vous êtes déjà connecté à votre Raspberry Pi, vous pouvez modifier l'ordre de démarrage à l'aide de commandes. Les instructions détaillées sont les suivantes :

* :ref:`configure_boot_ssd`


Comment modifier l'ordre de démarrage avec Raspberry Pi Imager ?
------------------------------------------------------------------

En plus de modifier le ``BOOT_ORDER`` dans la configuration de l'EEPROM, vous pouvez également utiliser le **Raspberry Pi Imager** pour changer l'ordre de démarrage de votre Raspberry Pi.

Il est recommandé d'utiliser une carte de rechange pour cette étape.

* :ref:`update_bootloader`

Comment copier le système de la carte SD vers un SSD NVMe ?
--------------------------------------------------------------------

Si vous avez un SSD NVMe mais pas d'adaptateur pour connecter votre NVMe à votre ordinateur, vous pouvez d'abord installer le système sur votre carte Micro SD. Une fois que le Pironman 5 a démarré avec succès, vous pouvez copier le système de votre carte Micro SD vers votre SSD NVMe. Les instructions détaillées sont les suivantes :

* :ref:`copy_sd_to_nvme_rpi`


L'écran OLED ne fonctionne pas ?
--------------------------------------

Si l'écran OLED ne s'affiche pas ou s'affiche de manière incorrecte, vous pouvez suivre ces étapes pour résoudre le problème :

Vérifiez si le câble FPC de l'écran OLED est correctement connecté.

#. Utilisez la commande suivante pour consulter les journaux d'exécution du programme et vérifier les messages d'erreur.

   .. code-block:: shell

      cat /opt/pironman5/log

#. Vous pouvez également utiliser la commande suivante pour vérifier si l'adresse i2c de l'OLED, 0x3C, est reconnue :
    
   .. code-block:: shell
        
        sudo i2cdetect -y 1

#. Si les deux premières étapes ne révèlent aucun problème, essayez de redémarrer le service pironman5 pour voir si cela résout le problème.


   .. code-block:: shell

        sudo systemctl restart pironman5.service

.. _openssh_powershell:

Installer OpenSSH via Powershell
------------------------------------

Lorsque vous utilisez ``ssh <username>@<hostname>.local`` (ou ``ssh <username>@<IP address>``) pour vous connecter à votre Raspberry Pi, mais que le message d'erreur suivant apparaît.

    .. code-block::

        ssh: Le terme 'ssh' n'est pas reconnu en tant que nom d'une cmdlet, fonction, fichier de script ou programme exécutable. Vérifiez l'orthographe du nom, ou si un chemin a été inclus, vérifiez que le chemin est correct et réessayez.


Cela signifie que votre système d'exploitation est trop ancien et ne dispose pas de `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ pré-installé, vous devez suivre le tutoriel ci-dessous pour l'installer manuellement.

#. Tapez ``powershell`` dans la barre de recherche de votre bureau Windows, faites un clic droit sur ``Windows PowerShell``, et sélectionnez ``Exécuter en tant qu'administrateur`` dans le menu qui apparaît.

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. Utilisez la commande suivante pour installer ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Après l'installation, le résultat suivant sera renvoyé.

   .. code-block::

        Path          :
        Online       : True
        RestartNeeded: False

#. Vérifiez l'installation en utilisant la commande suivante.

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Il vous indique maintenant que ``OpenSSH.Client`` a été installé avec succès.

   .. code-block::

        Name : OpenSSH.Client~~~~0.0.1.0
        State: Installed

        Name : OpenSSH.Server~~~~0.0.1.0
        State: NotPresent

    .. warning:: 
        Si l'invite ci-dessus n'apparaît pas, cela signifie que votre système Windows est encore trop ancien, et il est recommandé d'installer un outil SSH tiers, comme |link_putty|.

#. Maintenant, redémarrez PowerShell et continuez à l'exécuter en tant qu'administrateur. À ce stade, vous pourrez vous connecter à votre Raspberry Pi en utilisant la commande ``ssh``, où il vous sera demandé de saisir le mot de passe que vous avez défini précédemment.

   .. image:: img/powershell_login.png
