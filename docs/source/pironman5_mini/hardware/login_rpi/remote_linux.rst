.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d’autres passionnés pour approfondir vos connaissances sur Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Résolvez vos problèmes techniques et après-vente avec l’aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez astuces et tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces et aperçus de nouveaux produits.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des concours et offres spéciales à l’occasion des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

Pour les utilisateurs de Linux/Unix
=======================================

#. Localisez et ouvrez le **Terminal** sur votre système Linux/Unix.

#. Assurez-vous que votre Raspberry Pi est connecté au même réseau. Vérifiez cela en tapant `ping <hostname>.local`. Par exemple :

    .. code-block::

        ping raspberrypi.local

    Vous devriez voir l’adresse IP du Raspberry Pi s’afficher s’il est bien connecté au réseau.

    * Si le terminal affiche un message tel que ``Ping request could not find host pi.local. Please check the name and try again.``, revérifiez le nom d’hôte saisi.
    * Si vous ne parvenez pas à obtenir l’adresse IP, examinez les paramètres réseau ou Wi-Fi de votre Raspberry Pi.

#. Lancez une connexion SSH en tapant ``ssh <username>@<hostname>.local`` ou ``ssh <username>@<IP address>``. Par exemple :

    .. code-block::

        ssh pi@raspberrypi.local

#. Lors de la première connexion, un message de sécurité s’affichera. Tapez ``yes`` pour continuer.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Saisissez ensuite le mot de passe que vous avez défini. Pour des raisons de sécurité, rien ne s’affichera à l’écran pendant la saisie.

    .. note::
        Il est normal que les caractères du mot de passe ne s’affichent pas dans le terminal. Assurez-vous simplement de taper le bon mot de passe.

#. Une fois connecté avec succès, votre Raspberry Pi est opérationnel et vous pouvez passer à l’étape suivante.
