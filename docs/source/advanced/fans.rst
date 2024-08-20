.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Profitez d'un accès anticipé aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales** : Bénéficiez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et tirages au sort** : Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Ventilateurs
================

Ventilateur PWM
-------------------

Le ventilateur PWM du Pironman 5 est contrôlé par le système Raspberry Pi.

En ce qui concerne les solutions de refroidissement pour le Raspberry Pi 5, surtout en cas de forte charge, le design du Pironman 5 intègre un système de refroidissement intelligent. Il comporte un ventilateur PWM principal et deux ventilateurs RGB supplémentaires. La stratégie de refroidissement est étroitement liée au système de gestion thermique du Raspberry Pi 5.

Le fonctionnement du ventilateur PWM est basé sur la température du Raspberry Pi 5 :

* En dessous de 50°C, le ventilateur PWM reste éteint (vitesse à 0%).
* À 50°C, le ventilateur démarre à basse vitesse (vitesse à 30%).
* Lorsqu'il atteint 60°C, le ventilateur augmente à vitesse moyenne (vitesse à 50%).
* À 67,5°C, le ventilateur passe à une vitesse élevée (vitesse à 70%).
* À 75°C et au-delà, le ventilateur fonctionne à pleine vitesse (vitesse à 100%).

Cette relation température-vitesse s'applique également lorsque la température diminue, avec une hystérésis de 5°C. La vitesse du ventilateur diminue lorsque la température tombe 5°C en dessous de chacun de ces seuils.

* Commandes pour surveiller le ventilateur PWM. Pour vérifier l'état du ventilateur PWM :

  .. code-block:: shell
  
    cat /sys/class/thermal/cooling_device0/cur_state

* Pour voir la vitesse du ventilateur PWM :

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

Dans le Pironman 5, le ventilateur PWM est un composant essentiel pour maintenir des températures de fonctionnement optimales, en particulier lors de tâches intensives, garantissant ainsi que le Raspberry Pi 5 fonctionne de manière efficace et fiable.

Ventilateurs RGB
---------------------

.. image:: img/size_fan.png

* **Dimensions externes** : 40*40*10MM
* **Poids** : 13,5±5g/pc
* **Durée de vie** : 40 000 heures (température ambiante 25°C)
* **Débit d'air maximal** : 2,46 CFM
* **Pression d'air maximale** : 0,62 mm-H2O
* **Niveau sonore** : 22,31 dBA
* **Puissance nominale d'entrée** : 5V/0.1A
* **Vitesse nominale** : 3500±10% RPM
* **Température de fonctionnement** : -10℃~+70℃
* **Température de stockage** : -30℃~+85℃
