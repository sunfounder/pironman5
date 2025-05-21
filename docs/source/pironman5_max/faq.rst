.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d’autres passionnés pour aller plus loin dans l’univers de Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Bénéficiez d’une assistance pour résoudre les problèmes techniques et après-vente grâce à notre communauté et notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en exclusivité aux annonces de nouveaux produits et à des aperçus.
    - **Réductions spéciales** : Profitez d’offres spéciales sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des concours et animations pendant les périodes festives.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

FAQ
============

Comment désactiver le tableau de bord Web ?
------------------------------------------------------

Une fois l’installation du module ``pironman5`` terminée, vous pouvez accéder au :ref:`max_view_control_dashboard`.

Si vous ne souhaitez pas utiliser cette fonctionnalité et souhaitez réduire la consommation CPU et RAM, vous pouvez désactiver le tableau de bord pendant l’installation avec l’option ``--disable-dashboard``.

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Si vous avez déjà installé ``pironman5``, vous pouvez désinstaller le module ``dashboard`` ainsi que ``influxdb``, puis redémarrer le service pour appliquer les changements :

.. code-block:: shell

   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

Le Pironman 5 est-il compatible avec les systèmes de jeux rétro ?
------------------------------------------------------------------------
Oui, il est compatible. Toutefois, la plupart des systèmes de jeux rétro sont des distributions allégées qui ne permettent pas l’installation de logiciels supplémentaires. Cela peut empêcher certains composants du Pironman 5, comme l’écran OLED, les deux ventilateurs RGB et les 4 LED RGB, de fonctionner correctement car ils nécessitent les paquets logiciels de Pironman 5.


.. note::

    Le système Batocera.linux est désormais entièrement compatible avec le Pironman 5. Il s’agit d’une distribution open source et gratuite dédiée au rétro-gaming.

    * :ref:`max_install_batocera`
    * :ref:`max_set_up_batocera`

Comment contrôler les composants avec la commande ``pironman5`` ?
----------------------------------------------------------------------
Vous pouvez consulter le tutoriel suivant pour contrôler les composants du Pironman 5 avec la commande ``pironman5`` :

* :ref:`max_view_control_commands`

Comment modifier l’ordre de démarrage du Raspberry Pi via commande ?
-----------------------------------------------------------------------

Si vous êtes déjà connecté à votre Raspberry Pi, vous pouvez modifier l’ordre de démarrage via ligne de commande. Voir les instructions détaillées :

* :ref:`max_configure_boot_ssd`


Comment modifier l’ordre de démarrage avec Raspberry Pi Imager ?
--------------------------------------------------------------------

En plus de modifier la variable ``BOOT_ORDER`` dans la configuration EEPROM, vous pouvez utiliser **Raspberry Pi Imager** pour définir l’ordre de démarrage.

Il est recommandé d’utiliser une carte Micro SD de rechange pour cette opération.

* :ref:`max_update_bootloader`

Comment copier le système de la carte SD vers un SSD NVMe ?
-----------------------------------------------------------------

Si vous avez un SSD NVMe mais pas d’adaptateur pour le connecter à votre ordinateur, vous pouvez d’abord installer le système sur la carte Micro SD. Une fois que le Pironman 5 démarre correctement, copiez le système de la carte SD vers le SSD NVMe. Suivez les instructions ci-dessous :


* :ref:`max_copy_sd_to_nvme_rpi`


L’écran OLED ne fonctionne pas ?
--------------------------------------

Si l’écran OLED n’affiche rien ou s’affiche de façon incorrecte, suivez ces étapes pour diagnostiquer le problème :

Vérifiez si le câble FPC de l’écran OLED est correctement connecté.

#. Utilisez la commande suivante pour consulter les journaux et détecter d’éventuelles erreurs :

   .. code-block:: shell

      cat /opt/pironman5/log

#. Vous pouvez aussi vérifier si l’adresse i2c 0x3C de l’écran est reconnue :

   .. code-block:: shell

        sudo i2cdetect -y 1

#. Si aucune anomalie n’est détectée, tentez de redémarrer le service pironman5 :


   .. code-block:: shell

        sudo systemctl restart pironman5.service

.. _max_openssh_powershell:

Installer OpenSSH via PowerShell
-----------------------------------

Lorsque vous tentez de vous connecter à votre Raspberry Pi via ``ssh <username>@<hostname>.local`` (ou ``ssh <username>@<IP address>``) et que vous voyez le message d’erreur suivant :

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


Cela signifie que votre système Windows est trop ancien et ne dispose pas de `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ préinstallé. Suivez les étapes ci-dessous pour l’installer manuellement.

#. Tapez ``powershell`` dans la barre de recherche de Windows, faites un clic droit sur ``Windows PowerShell`` et choisissez ``Run as administrator``.

   .. image:: img/powershell_ssh.png
      :width: 90%


#. Exécutez la commande suivante pour installer ``OpenSSH.Client`` :

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Une fois l’installation terminée, vous verrez un résultat semblable à celui-ci :

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Vérifiez l’installation avec la commande suivante :

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Vous verrez alors que ``OpenSSH.Client`` est installé avec succès :

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        Si cette information n’apparaît pas, cela signifie que votre version de Windows est trop ancienne. Nous vous recommandons d’utiliser un outil SSH tiers, comme |link_putty|.

#. Redémarrez PowerShell en tant qu’administrateur. Vous pourrez désormais vous connecter à votre Raspberry Pi avec la commande ``ssh``, qui vous demandera le mot de passe configuré précédemment.

   .. image:: img/powershell_login.png



Puis-je utiliser les fonctionnalités du Pironman 5 avec OMV ?
--------------------------------------------------------------------------------------------------------

Oui, OpenMediaVault est installé sur le système Raspberry Pi. Veuillez suivre les étapes décrites dans :ref:`max_set_up_pi_os` pour compléter la configuration.