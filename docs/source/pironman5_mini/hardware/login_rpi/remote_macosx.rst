.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d’autres passionnés pour approfondir vos connaissances sur Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Résolvez les problèmes techniques et après-vente grâce à l’aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour faire progresser vos compétences.
    - **Aperçus exclusifs** : Profitez d’un accès anticipé aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales** : Bénéficiez de remises exclusives sur nos nouveautés.
    - **Promotions festives et cadeaux** : Participez à nos concours et offres promotionnelles pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

Pour les utilisateurs de macOS
=================================

Pour les utilisateurs de macOS, SSH (Secure Shell) offre une méthode sécurisée et pratique pour accéder à distance à un Raspberry Pi et le contrôler. C’est particulièrement utile lorsque le Raspberry Pi n’est pas connecté à un écran. Grâce à l’application Terminal sur Mac, vous pouvez établir cette connexion sécurisée. La commande SSH utilise le nom d’utilisateur et le nom d’hôte du Raspberry Pi. Lors de la première connexion, un message de sécurité vous demandera de confirmer l’authenticité de l’appareil.

#. Pour se connecter au Raspberry Pi, tapez la commande SSH suivante :

    .. code-block::

        ssh pi@raspberrypi.local

   .. image:: img/mac_vnc14.png

#. Un message de sécurité apparaîtra lors de la première connexion. Répondez **yes** pour continuer.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Saisissez ensuite le mot de passe du Raspberry Pi. Notez que, pour des raisons de sécurité, rien ne s’affichera à l’écran pendant la saisie.

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

