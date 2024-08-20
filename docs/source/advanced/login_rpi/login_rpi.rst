.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et tirages au sort** : Participez à des concours et des promotions de fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _login_rpi:

Connexion à l'OS Raspberry Pi
=====================================

Dans ce chapitre, vous apprendrez à vous connecter à votre Raspberry Pi. Que vous ayez un écran connecté ou que vous deviez y accéder à distance, cette section vous guidera pour ouvrir le terminal, que vous utiliserez dans les chapitres suivants pour entrer des commandes.

.. note::

    Si vous êtes déjà familiarisé avec les opérations sur Raspberry Pi, vous pouvez sauter ce chapitre.

Connexion avec un écran
---------------------------

Disposer d'un écran connecté à votre Raspberry Pi facilite l'interaction directe avec le système.

**Composants requis**

* Pironman 5
* Adaptateur secteur
* Carte Micro SD ou SSD NVMe avec l'OS Raspberry Pi pré-installé
* Adaptateur d'alimentation pour moniteur
* Câble HDMI
* Moniteur
* Souris
* Clavier

**Étapes**

#. Insérez la carte Micro SD dans le Pironman 5.

#. Connectez la souris et le clavier aux ports USB du Pironman 5.

#. Utilisez le câble HDMI pour connecter le moniteur au port HDMI du Pironman 5. Assurez-vous que le moniteur est connecté à une source d'alimentation et est allumé.

#. Allumez le Pironman 5 à l'aide de l'adaptateur secteur. Vous devriez bientôt voir le bureau de l'OS Raspberry Pi apparaître sur le moniteur.

   .. image:: img/bookwarm.png
      :width: 90%
      

#. Une fois le bureau visible, ouvrez le Terminal en cliquant sur l'icône du terminal ou en le recherchant dans le menu pour commencer à entrer des commandes.

Connexion à distance sans écran
------------------------------------

Si vous n'avez pas accès à un moniteur, vous pouvez toujours utiliser votre Raspberry Pi en vous connectant à distance.

Pour accéder à la ligne de commande, vous pouvez utiliser SSH pour vous connecter à la console Bash du Raspberry Pi, le shell Linux par défaut, qui permet de gérer l'appareil via des commandes.

Pour ceux qui préfèrent une interface graphique, l'utilisation d'une application de bureau à distance telle que VNC Viewer offre un moyen visuel de gérer les fichiers et les opérations à distance.

**Composants requis**

* Pironman 5 
* Adaptateur secteur
* Carte Micro SD ou SSD NVMe avec l'OS Raspberry Pi pré-installé

Étapes :

#. Insérez la carte Micro SD dans le Pironman 5.

#. Connectez le Pironman 5 à une source d'alimentation à l'aide de l'adaptateur secteur.

#. Pour des tutoriels détaillés sur la configuration de l'accès à distance en fonction du système d'exploitation de votre ordinateur, consultez les sections suivantes :

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop
