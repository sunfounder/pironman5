.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes post-achat et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives**: Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales**: Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et tirages au sort**: Participez à des concours et à des promotions lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Pour les utilisateurs de Windows
==================================

Pour les utilisateurs de Windows 10 ou supérieur, la connexion à distance à un Raspberry Pi peut être réalisée en suivant les étapes suivantes :

#. Recherchez ``powershell`` dans la barre de recherche Windows. Faites un clic droit sur ``Windows PowerShell`` et sélectionnez ``Exécuter en tant qu'administrateur``.

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. Déterminez l'adresse IP de votre Raspberry Pi en tapant ``ping -4 <hostname>.local`` dans PowerShell.

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%
      

   L'adresse IP du Raspberry Pi sera affichée une fois qu'il sera connecté au réseau.

   * Si le terminal affiche ``Ping request could not find host pi.local. Please check the name and try again.``, vérifiez que le nom d'hôte que vous avez saisi est correct.
   * Si l'adresse IP ne peut toujours pas être récupérée, vérifiez les paramètres de votre réseau ou de votre WiFi sur le Raspberry Pi.

#. Une fois l'adresse IP confirmée, connectez-vous à votre Raspberry Pi en utilisant ``ssh <username>@<hostname>.local`` ou ``ssh <username>@<IP address>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Si une erreur apparaît indiquant ``The term 'ssh' is not recognized as the name of a cmdlet...``, il est possible que votre système n'ait pas les outils SSH pré-installés. Dans ce cas, vous devrez installer manuellement OpenSSH en suivant :ref:`openssh_powershell`, ou utiliser un outil tiers tel que |link_putty|.

#. Un message de sécurité apparaîtra lors de votre première connexion. Saisissez ``yes`` pour continuer.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Entrez le mot de passe que vous avez précédemment défini. Notez que les caractères du mot de passe ne seront pas affichés à l'écran, ce qui est une fonctionnalité de sécurité standard.

    .. note::
        L'absence de caractères visibles lors de la saisie du mot de passe est normale. Assurez-vous de bien entrer le mot de passe correct.

#. Une fois connecté, votre Raspberry Pi est prêt pour les opérations à distance.

   .. image:: img/sp221221_140628.png
      :width: 90%
      
