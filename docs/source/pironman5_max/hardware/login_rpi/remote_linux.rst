.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 ! Plongez dans l’univers du Raspberry Pi, de l’Arduino et de l’ESP32 aux côtés d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Assistance d’experts** : Bénéficiez de l’aide de notre équipe et de notre communauté pour résoudre les problèmes après-vente et les défis techniques.
    - **Apprentissage et partage** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Soyez parmi les premiers à découvrir nos nouveaux produits.
    - **Réductions spéciales** : Profitez d’offres exclusives sur nos dernières nouveautés.
    - **Promotions et cadeaux festifs** : Participez à des concours et événements spéciaux pendant les périodes de fête.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

Pour les utilisateurs de Linux/Unix
=======================================

#. Localisez et ouvrez le **Terminal** sur votre système Linux/Unix.

#. Assurez-vous que votre Raspberry Pi est connecté au même réseau. Vérifiez cela en tapant `ping <hostname>.local`. Par exemple :

    .. code-block::

        ping raspberrypi.local

    Si tout fonctionne, vous devriez voir l'adresse IP de votre Raspberry Pi s'afficher.

    * Si le terminal affiche un message du type ``Ping request could not find host pi.local. Please check the name and try again.``, vérifiez soigneusement le nom saisi.
    * Si vous n’arrivez pas à obtenir l’adresse IP, examinez les paramètres réseau ou Wi-Fi de votre Raspberry Pi.

#. Initiez une connexion SSH en tapant ``ssh <username>@<hostname>.local`` ou ``ssh <username>@<IP address>``. Par exemple :

    .. code-block::

        ssh pi@raspberrypi.local

#. Lors de votre première connexion, un message de sécurité apparaîtra. Tapez ``yes`` pour continuer.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Saisissez le mot de passe que vous avez défini précédemment. Pour des raisons de sécurité, aucun caractère ne s'affichera pendant la saisie.

    .. note::
        Il est normal que les caractères du mot de passe ne s’affichent pas dans le terminal. Assurez-vous simplement de taper le bon mot de passe.

#. Une fois connecté avec succès, votre Raspberry Pi est prêt à être utilisé. Vous pouvez passer à l’étape suivante.
