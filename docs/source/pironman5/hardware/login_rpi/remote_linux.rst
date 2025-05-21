.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes post-achat et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives**: Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales**: Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et tirages au sort**: Participez à des concours et des promotions lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Pour les utilisateurs de Linux/Unix
=======================================

#. Localisez et ouvrez le **Terminal** sur votre système Linux/Unix.

#. Assurez-vous que votre Raspberry Pi est connecté au même réseau. Vérifiez cela en tapant `ping <hostname>.local`. Par exemple :

    .. code-block::

        ping raspberrypi.local

    Vous devriez voir l'adresse IP de votre Raspberry Pi s'il est connecté au réseau.

    * Si le terminal affiche un message tel que ``Ping request could not find host pi.local. Please check the name and try again.``, vérifiez le nom d'hôte que vous avez entré.
    * Si vous ne parvenez pas à obtenir l'adresse IP, examinez vos paramètres réseau ou WiFi sur le Raspberry Pi.

#. Initiez une connexion SSH en tapant ``ssh <username>@<hostname>.local`` ou ``ssh <username>@<IP address>``. Par exemple :

    .. code-block::

        ssh pi@raspberrypi.local

#. Lors de votre première connexion, vous verrez un message de sécurité. Tapez ``yes`` pour continuer.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Entrez le mot de passe que vous avez précédemment défini. Notez que pour des raisons de sécurité, le mot de passe ne sera pas visible pendant que vous le tapez.

    .. note::
        Il est normal que les caractères du mot de passe ne s'affichent pas dans le terminal. Assurez-vous simplement de saisir correctement le mot de passe.



#. Une fois connecté avec succès, votre Raspberry Pi est désormais connecté, et vous êtes prêt à passer à l'étape suivante.

