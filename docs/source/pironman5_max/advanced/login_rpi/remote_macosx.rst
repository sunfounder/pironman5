.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 ! Rejoignez d'autres passionnés pour approfondir vos connaissances sur le Raspberry Pi, l’Arduino et l’ESP32.

    **Pourquoi nous rejoindre ?**

    - **Assistance d’experts** : Résolvez les problèmes après-vente et les difficultés techniques avec le soutien de notre équipe et de la communauté.
    - **Apprentissage et partage** : Échangez des conseils et des tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Soyez parmi les premiers informés des nouveautés produits et des aperçus en avant-première.
    - **Réductions spéciales** : Bénéficiez d’offres exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des jeux-concours et à des offres spéciales pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

Pour les utilisateurs de Mac OS X
========================================

Pour les utilisateurs de Mac OS X, SSH (Secure Shell) est une méthode sécurisée et pratique pour accéder à distance au Raspberry Pi et le contrôler. Cela s’avère particulièrement utile lorsque vous travaillez sans écran connecté. En utilisant l’application Terminal sur Mac, vous pouvez établir une connexion sécurisée. La procédure consiste à exécuter une commande SSH incluant le nom d’utilisateur et le nom d’hôte du Raspberry Pi. Lors de la première connexion, un message de sécurité vous demandera de confirmer l’authenticité du Raspberry Pi.

#. Pour vous connecter au Raspberry Pi, saisissez la commande SSH suivante :

    .. code-block::

        ssh pi@raspberrypi.local

   .. image:: img/mac_vnc14.png

#. Un message de sécurité s’affichera lors de la première connexion. Tapez **yes** pour continuer.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Saisissez ensuite le mot de passe de votre Raspberry Pi. Notez que pour des raisons de sécurité, aucun caractère ne s’affichera à l’écran pendant la saisie.

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

