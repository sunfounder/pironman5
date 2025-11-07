.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 ! Plongez au cœur de l’univers Raspberry Pi, Arduino et ESP32 aux côtés d'autres passionnés.

    **Pourquoi rejoindre la communauté ?**

    - **Support d’experts** : Résolvez les problèmes après-vente et les défis techniques avec l’aide de notre équipe et des membres de la communauté.
    - **Apprentissage et partage** : Échangez des astuces et tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et à des démonstrations.
    - **Réductions spéciales** : Bénéficiez d’offres exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des jeux-concours et à des événements spéciaux.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _max_login_rpi:

Connexion à Raspberry Pi OS
=====================================

Dans ce chapitre, vous apprendrez à vous connecter à Raspberry Pi. Que vous disposiez d’un écran ou que vous deviez y accéder à distance, cette section vous guidera dans l’ouverture du terminal, que vous utiliserez dans les chapitres suivants pour saisir des commandes.

.. note::

    Si vous êtes déjà familiarisé avec l'utilisation de Raspberry Pi, vous pouvez passer ce chapitre.

Connexion avec écran
---------------------------

Un écran connecté à votre Raspberry Pi facilite l’interaction directe avec le système.

**Composants nécessaires**

* Pironman 5 MAX
* Adaptateur secteur
* Carte Micro SD ou SSD NVMe avec Raspberry Pi OS préinstallé
* Adaptateur d’alimentation de l’écran
* Câble HDMI
* Écran
* Souris
* Clavier

**Étapes**

#. Insérez la carte Micro SD dans le Pironman 5 MAX.

#. Connectez la souris et le clavier aux ports USB du Pironman 5 MAX.

#. Utilisez le câble HDMI pour connecter l’écran au port HDMI du Pironman 5 MAX. Assurez-vous que l’écran est alimenté et allumé.

#. Allumez le Pironman 5 MAX à l’aide de l’adaptateur secteur. Le bureau de Raspberry Pi OS devrait apparaître sur l’écran dans quelques instants.

   .. image:: img/bookwarm.png
      :width: 90%


#. Une fois le bureau visible, ouvrez le Terminal en cliquant sur l’icône correspondante ou en le recherchant dans le menu afin de commencer à entrer des commandes.

Connexion à distance sans écran
------------------------------------

Si vous ne disposez pas d’un écran, vous pouvez quand même utiliser votre Raspberry Pi en vous y connectant à distance.

Pour accéder à l’interface en ligne de commande, vous pouvez utiliser SSH afin de vous connecter au shell Bash de Raspberry Pi, le shell Linux par défaut permettant de gérer l’appareil via des commandes.

Pour ceux qui préfèrent une interface graphique, une application de bureau à distance comme VNC Viewer offre un moyen visuel de gérer les fichiers et opérations à distance.

**Composants nécessaires**

* Pironman 5 MAX
* Adaptateur secteur
* Carte Micro SD ou SSD NVMe avec Raspberry Pi OS préinstallé

**Étapes :**

#. Insérez la carte Micro SD dans le Pironman 5 MAX.

#. Connectez le Pironman 5 MAX à une source d’alimentation à l’aide de l’adaptateur secteur.

#. Pour des tutoriels détaillés sur la configuration de l’accès à distance selon le système d’exploitation de votre ordinateur, consultez les sections suivantes :

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


