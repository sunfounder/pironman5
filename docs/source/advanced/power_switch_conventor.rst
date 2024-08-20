.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et tirages au sort** : Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Convertisseur de Bouton d'Alimentation
==========================================

Il s'agit d'un module qui permet d'étendre le bouton d'alimentation du Raspberry Pi 5 vers l'extérieur.

.. image:: img/power_switch_conventor.jpeg

**Ajout du bouton d'alimentation**

* Le Raspberry Pi 5 est équipé d'un cavalier **J2**, situé entre le connecteur de la batterie RTC et le bord de la carte. Cette extension permet d'ajouter un bouton d'alimentation personnalisé au Raspberry Pi 5 en connectant un interrupteur momentané normalement ouvert (NO) sur les deux pastilles. Appuyer brièvement sur cet interrupteur reproduit la fonctionnalité du bouton d'alimentation intégré.

   .. image:: img/pi5_j2.jpg

* Sur le Pironman 5, il y a un **convertisseur de bouton d'alimentation** qui étend le cavalier **J2** vers un bouton d'alimentation externe à l'aide de deux broches Pogo.

   .. image:: img/power_switch_convertor.png

* Désormais, le Raspberry Pi 5 peut être alimenté ou éteint en utilisant le bouton d'alimentation.

   .. image:: img/pironman_button.JPG

**Cycle d'alimentation**

Lors de la mise sous tension initiale de votre Raspberry Pi 5, il s'allumera automatiquement et démarrera dans le système d'exploitation sans avoir besoin d'appuyer sur le bouton.

Si vous utilisez le bureau Raspberry Pi, une brève pression sur le bouton d'alimentation lance un processus d'arrêt propre. Un menu apparaîtra, offrant des options pour éteindre, redémarrer ou se déconnecter. Sélectionner une option ou appuyer de nouveau sur le bouton d'alimentation déclenchera un arrêt propre.

.. image:: img/button_shutdown.png

**Arrêt**

    * Si vous utilisez le système **Bookworm Desktop** de Raspberry Pi, vous pouvez appuyer deux fois rapidement sur le bouton d'alimentation pour éteindre.
    * Si vous utilisez le système **Bookworm Lite** de Raspberry Pi sans bureau, appuyez une seule fois sur le bouton d'alimentation pour lancer l'arrêt.
    * Pour forcer un arrêt brutal, maintenez le bouton d'alimentation enfoncé.

**Mise sous tension**

    * Si la carte Raspberry Pi est éteinte mais toujours sous tension, une simple pression permettra de rallumer la carte depuis l'état d'arrêt.

.. note::

    Si vous utilisez un système qui ne prend pas en charge le bouton d'arrêt, vous pouvez le maintenir enfoncé pendant 5 secondes pour forcer un arrêt brutal, puis appuyer une seule fois pour rallumer la carte depuis l'état d'arrêt.
