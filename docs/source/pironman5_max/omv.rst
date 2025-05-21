.. _max_omv_5_max:


(Configuration optionnelle) Installation d’OpenMediaVault
============================================================

.. warning::

   OpenMediaVault **ne prend pas en charge** l'installation sur le bureau Raspberry Pi OS.

   Veillez à installer le bon système d'exploitation et à configurer le réseau correctement.
   La procédure décrite ici est cohérente avec :ref:`max_install_os_sd_rpi`, mais lors du choix de l’image, veuillez sélectionner Raspberry Pi OS Lite dans la section Raspberry Pi OS (autre).

   .. image:: img/omv/omv-install-1.png

OpenMediaVault (OMV) est un système d'exploitation open-source basé sur Debian Linux, destiné aux environnements domestiques et aux petites entreprises. Il vise à simplifier la gestion du stockage tout en offrant de nombreuses fonctionnalités de services réseau.

Veuillez suivre les étapes suivantes pour installer OpenMediaVault sur votre Raspberry Pi :

1. Connexion au Raspberry Pi via SSH
-----------------------------------------------------------

   Saisissez la commande suivante dans le terminal :

   .. code-block:: bash

      ssh pi@raspberrypi.local

   Si vous utilisez Windows, connectez-vous à votre Raspberry Pi avec PuTTY ou un autre client SSH.

2. Installation d’OpenMediaVault
--------------------------------------------

   Exécutez les commandes suivantes dans le terminal :

   .. code-block:: bash

      wget https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install  
      chmod +x install  
      sudo ./install -n

   Ce script téléchargera et lancera l'installation d’OpenMediaVault. Ne redémarrez pas le Raspberry Pi après l'installation.

3. Accès à OpenMediaVault
---------------------------------

   Dans votre navigateur, saisissez l’URL suivante :

   .. code-block:: bash

      http://raspberrypi.local

   .. note:: Si l'URL ci-dessus ne fonctionne pas, essayez avec l'adresse IP, par exemple http://192.168.1.100.

   Une page de connexion s'affichera. Connectez-vous avec les identifiants par défaut : nom d’utilisateur ``admin`` et mot de passe ``openmediavault``.

   .. image:: img/omv/omv-login.png

   Une fois connecté, l'interface principale d'OpenMediaVault apparaîtra.

   .. image:: img/omv/omv-main.png

   Vous avez désormais installé et accédé avec succès à OpenMediaVault. Vous pouvez commencer à configurer et à gérer votre stockage.



6. Configuration d’un RAID (optionnel)
-------------------------------------------

   Le RAID NVMe est une solution de stockage combinant plusieurs SSD NVMe à l’aide de la technologie RAID. Elle permet de maximiser les performances élevées du protocole NVMe tout en tirant parti de la redondance ou des améliorations de performance offertes par le RAID. Les modes les plus courants sont RAID 0, 1, 5 et 10. Avec deux SSD NVMe, les modes RAID 0 et RAID 1 sont les plus utilisés.

   * Le RAID 0 (entrelacement) répartit les données en bandes sur plusieurs disques pour augmenter la vitesse de lecture/écriture. Ce mode n’offre aucune redondance : en cas de panne d’un disque, toutes les données sont perdues.

   * Le RAID 1 (miroir) duplique les données sur plusieurs disques pour offrir une protection contre la perte de données. Les performances dépendent des vitesses individuelles des disques. Si un disque échoue, les autres peuvent continuer à fournir les données.

   .. note:: Pour les modes RAID 0 ou RAID 1, vous devez avoir au moins 2 disques montés. En RAID 0, la capacité totale correspond à la somme des capacités de tous les disques. En RAID 1, elle est limitée à la capacité du plus petit disque.

   1. Dans le menu ``System``, cliquez sur ``Plugins``, recherchez le plugin ``openmediavault-md`` et installez-le.

   .. image:: img/omv/omv-raid-1.png

   2. Dans le menu ``Storage``, cliquez sur ``Disks``, puis effacez les deux SSD.

   .. image:: img/omv/omv-raid-2.png

   3. Attention, cette action supprimera toutes les données présentes sur les disques. Assurez-vous d’avoir sauvegardé vos données importantes.

   .. image:: img/omv/omv-raid-3.png

   4. Pour le mode d’effacement, ``QUICK`` est suffisant.

   .. image:: img/omv/omv-raid-4.png

   5. Accédez à l’onglet ``Multiple Device``, puis cliquez sur ``Create``.

   .. image:: img/omv/omv-raid-5.png

   6. Dans l’option Level, choisissez Stripe (RAID 0) ou Mirror (RAID 1). Dans Devices, sélectionnez les disques précédemment effacés. Cliquez sur ``Save`` et patientez pendant la configuration du RAID.

   .. image:: img/omv/omv-raid-6.png

   .. note:: Si une erreur 500 (Internal Server Error) apparaît, essayez de redémarrer le système OMV.

   7. Appliquez la configuration en cliquant sur le bouton ``Apply``.

   .. image:: img/omv/omv-raid-7.png

   8. Attendez que l’état du RAID indique ``100%``.

   .. image:: img/omv/omv-raid-8.png

   9. Une fois la configuration terminée, vos disques fonctionnent désormais en RAID 0 ou RAID 1, et peuvent être utilisés comme un seul périphérique de stockage.

5. Configuration du stockage
--------------------------------

   Dans l’interface principale d’OpenMediaVault, cliquez sur ``Storage`` dans le menu de gauche. Ensuite, ouvrez l’onglet ``Disks`` pour visualiser tous les disques connectés au Raspberry Pi. Assurez-vous qu’un disque est connecté via NVMe PIP.

   .. image:: img/omv/omv-disk.png

   1. Dans la barre latérale, cliquez sur ``File System``. Créez puis montez un système de fichiers, en choisissant ``ext4`` comme type.

   .. image:: img/omv/omv-mount.png

   2. Sélectionnez le périphérique et cliquez sur ``Save``.

   .. note:: Si un RAID a été configuré, il apparaîtra dans la liste. Sélectionnez-le simplement et sauvegardez.

   .. image:: img/omv/omv-mount-2.png

   3. Une fenêtre s’ouvrira indiquant la création du système de fichiers. Patientez un instant.

   .. image:: img/omv/omv-mount-3.png

   4. Une fois terminé, accédez à l’interface ``Mount``, sélectionnez le système de fichiers nouvellement créé et montez-le.

   .. image:: img/omv/omv-mount-4.png

   .. note:: Si vous utilisez deux disques durs sans RAID, répétez les étapes ci-dessus pour monter également le second disque.

   5. Après le montage, cliquez sur ``Apply``. Vous pouvez désormais visualiser vos données via le système de fichiers.

   .. image:: img/omv/omv-mount-5.png

   OpenMediaVault est maintenant configuré et vos disques sont montés. Vous pouvez commencer à gérer votre stockage.


6. Création d’un dossier partagé
---------------------------------------

   1. Dans la page ``Storage``, ouvrez l’onglet ``Shared Folders`` et cliquez sur ``Create``.

   .. image:: img/omv/omv-share-1.png

   2. Dans la page ``Create Shared Folder``, entrez le nom du dossier, sélectionnez le disque, le chemin, et définissez les permissions. Cliquez ensuite sur ``Save``.

   .. image:: img/omv/omv-share-2.png

   3. Le dossier partagé s’affichera. Vérifiez qu’il est correct, puis appliquez les changements.

   .. image:: img/omv/omv-share-3.png

   Votre dossier partagé est désormais prêt à l’utilisation.


7. Création d’un nouvel utilisateur
---------------------------------------

   Pour accéder au dossier, créez un nouvel utilisateur comme suit :

   1. Dans la page ``User``, cliquez sur ``Create``.

   .. image:: img/omv/omv-user-1.png

   2. Saisissez un nom d’utilisateur et un mot de passe, puis cliquez sur ``Save``.

   .. image:: img/omv/omv-user-2.png

   L’utilisateur a été créé avec succès.


8. Définir les permissions pour le nouvel utilisateur
-------------------------------------------------------

   1. Dans la page ``Shared Folders``, sélectionnez le dossier partagé, puis cliquez sur ``Permissions``.

   .. image:: img/omv/omv-user-3.png

   2. Définissez les ``permissions`` appropriées, puis cliquez sur ``Save``.

   .. image:: img/omv/omv-user-4.png

   3. Cliquez sur ``Apply`` pour valider les modifications.

   .. image:: img/omv/omv-user-5.png

   Vous pouvez maintenant accéder au dossier partagé avec ce nouvel utilisateur.


9. Configuration du service SMB
---------------------------------------

   1. Dans la page ``Services``, ouvrez l’onglet ``SMB/CIFS`` > ``Setting``, activez l’option ``Enable``, puis cliquez sur ``Save``.

   .. image:: img/omv/omv-smb-1.png

   2. Cliquez sur ``Apply`` pour appliquer les modifications.

   .. image:: img/omv/omv-smb-2.png

   3. Accédez à l’onglet ``Shares`` et cliquez sur ``Create``.

   .. image:: img/omv/omv-smb-3.png

   4. Sélectionnez le chemin du dossier partagé, configurez les options selon vos besoins, puis cliquez sur ``Save``.

   .. image:: img/omv/omv-smb-4.png

   5. Cliquez sur ``Apply``.

   .. image:: img/omv/omv-smb-5.png

   Le service SMB est maintenant opérationnel. Vous pouvez accéder au dossier partagé via le protocole SMB.


10. Accéder au dossier partagé depuis Windows
----------------------------------------------------

   1. Ouvrez ``This PC``, puis cliquez sur ``Map network drive``.

   .. image:: img/omv/omv-network-location-1.png

   2. Dans la boîte de dialogue, entrez l’IP du Raspberry Pi dans le champ ``Folder``, par exemple ``\\192.168.1.100\``, ou bien son nom d’hôte, comme ``\\pi.local\``.

   .. image:: img/omv/omv-network-location-2.png

   3. Cliquez sur ``Parcourir``, sélectionnez le dossier, et entrez les identifiants utilisateur.

   .. image:: img/omv/omv-network-location-3.png

   4. Cochez "Se reconnecter à l’ouverture de session", puis cliquez sur ``Finish``.

   .. image:: img/omv/omv-network-location-4.png

   5. Le dossier partagé NAS est maintenant accessible.

   .. image:: img/omv/omv-network-location-5.png

10. Accéder au dossier partagé depuis macOS
-------------------------------------------------

   1. Dans le menu ``Go``, cliquez sur ``Connect to Server``.

   .. image:: img/omv/omv-mac-1.png

   2. Entrez l’adresse IP ou le nom d’hôte, par exemple ``smb://192.168.1.100`` ou ``smb://pi.local``.

   .. image:: img/omv/omv-mac-2.png

   3. Cliquez sur ``Connect``.

   .. image:: img/omv/omv-mac-3.png

   4. Saisissez le nom d’utilisateur et le mot de passe, puis cliquez de nouveau sur ``Connect``.

   .. image:: img/omv/omv-mac-4.png

   5. Le dossier partagé NAS est maintenant accessible.

   .. image:: img/omv/omv-mac-5.png
