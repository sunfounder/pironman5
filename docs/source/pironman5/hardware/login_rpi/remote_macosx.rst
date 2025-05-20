.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes post-achat et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives**: Profitez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales**: Bénéficiez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et tirages au sort**: Participez à des concours et des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Pour les utilisateurs de Mac OS X
=====================================

Pour les utilisateurs de Mac OS X, SSH (Secure Shell) offre une méthode sécurisée et pratique pour accéder à distance et contrôler un Raspberry Pi. Cela est particulièrement utile pour travailler à distance avec le Raspberry Pi ou lorsqu'il n'est pas connecté à un moniteur. En utilisant l'application Terminal sur un Mac, vous pouvez établir cette connexion sécurisée. Le processus implique une commande SSH intégrant le nom d'utilisateur et le nom d'hôte du Raspberry Pi. Lors de la première connexion, une invite de sécurité vous demandera de confirmer l'authenticité du Raspberry Pi.

#. Pour vous connecter au Raspberry Pi, tapez la commande SSH suivante :

    .. code-block::

        ssh pi@raspberrypi.local

   .. image:: img/mac_vnc14.png

#. Un message de sécurité apparaîtra lors de votre première connexion. Répondez par **yes** pour continuer.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Entrez le mot de passe du Raspberry Pi. Notez que le mot de passe ne s'affichera pas à l'écran pendant que vous tapez, ce qui est une fonctionnalité de sécurité standard.

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 

