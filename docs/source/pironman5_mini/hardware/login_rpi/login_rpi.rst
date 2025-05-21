.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d'autres passionnés pour explorer plus en profondeur l’univers du Raspberry Pi, d’Arduino et de l’ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Résolvez vos problèmes techniques ou après-vente grâce à l’aide de notre équipe et de notre communauté.
    - **Apprendre et partager** : Échangez des conseils et tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits.
    - **Réductions spéciales** : Bénéficiez d’offres exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des concours et promotions lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _login_rpi_mini:

Se connecter à Raspberry Pi OS
=====================================

Dans ce chapitre, vous apprendrez à vous connecter à votre Raspberry Pi. Que vous ayez un écran connecté ou que vous accédiez à distance, cette section vous guidera pour ouvrir le terminal, que vous utiliserez dans les chapitres suivants pour entrer des commandes.

.. note::

    Si vous êtes déjà à l’aise avec l’utilisation du Raspberry Pi, vous pouvez passer ce chapitre.

Connexion avec un écran
---------------------------

Un écran connecté au Raspberry Pi permet d’interagir directement avec le système.

**Composants nécessaires**

* Pironman 5 Mini  
* Adaptateur secteur  
* Carte Micro SD ou SSD NVMe avec Raspberry Pi OS préinstallé  
* Adaptateur secteur pour moniteur  
* Câble HDMI  
* Moniteur  
* Souris  
* Clavier  

**Étapes**

#. Insérez la carte Micro SD dans le Pironman 5 Mini.

#. Connectez la souris et le clavier aux ports USB du Pironman 5 Mini.

#. Utilisez le câble HDMI pour relier le moniteur au port HDMI du Pironman 5 Mini. Assurez-vous que le moniteur est branché et allumé.

#. Allumez le Pironman 5 Mini à l’aide de l’adaptateur secteur. Le bureau de Raspberry Pi OS devrait apparaître sur l’écran après quelques instants.

   .. image:: img/bookwarm.png
      :width: 90%
      

#. Une fois le bureau affiché, ouvrez le Terminal en cliquant sur l’icône correspondante ou en le recherchant dans le menu pour commencer à saisir des commandes.

Connexion à distance sans écran
----------------------------------------------

Si vous n’avez pas de moniteur, vous pouvez quand même utiliser votre Raspberry Pi à distance.

Pour une interface en ligne de commande, utilisez SSH pour vous connecter au shell Bash du Raspberry Pi, l’interpréteur de commandes par défaut sous Linux, permettant de gérer l’appareil via des instructions textuelles.

Pour ceux qui préfèrent une interface graphique, une application de bureau à distance comme VNC Viewer permet de gérer visuellement les fichiers et les opérations à distance.

**Composants nécessaires**

* Pironman 5 Mini  
* Adaptateur secteur  
* Carte Micro SD ou SSD NVMe avec Raspberry Pi OS préinstallé  

Étapes :

#. Insérez la carte Micro SD dans le Pironman 5 Mini.

#. Branchez le Pironman 5 Mini à une source d’alimentation via l’adaptateur secteur.

#. Pour des tutoriels détaillés sur la configuration de l’accès à distance selon le système d’exploitation de votre ordinateur, consultez les sections suivantes :

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


