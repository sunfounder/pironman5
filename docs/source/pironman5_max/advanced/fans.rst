.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 ! Rejoignez d'autres passionnés pour approfondir vos connaissances sur le Raspberry Pi, l’Arduino et l’ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Résolvez les problèmes après-vente et relevez les défis techniques grâce à notre équipe et à la communauté.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Soyez informé(e) en avant-première des nouveaux produits et bénéficiez d’aperçus privilégiés.
    - **Réductions spéciales** : Profitez d’offres exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des concours et à des événements promotionnels pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

Ventilateurs
==============

Ventilateur PWM
---------------------

Le ventilateur PWM du Pironman 5 est contrôlé directement par le système du Raspberry Pi.

En ce qui concerne le refroidissement du Raspberry Pi 5, notamment en cas de forte charge, le Pironman 5 intègre un système de refroidissement intelligent. Il comprend un ventilateur PWM principal et deux ventilateurs RGB supplémentaires. Cette stratégie de refroidissement est étroitement liée au système de gestion thermique du Raspberry Pi 5.

Le fonctionnement du ventilateur PWM est basé sur la température du Raspberry Pi 5 :

* En dessous de 50°C, le ventilateur reste éteint (0 % de vitesse).
* À 50°C, il démarre à faible vitesse (30 %).
* À 60°C, la vitesse passe à un niveau moyen (50 %).
* À 67,5°C, la vitesse augmente à un niveau élevé (70 %).
* À 75°C et au-delà, le ventilateur fonctionne à pleine vitesse (100 %).

Cette correspondance température/vitesse s’applique également en cas de baisse de température, avec une hystérésis de 5°C. Le ventilateur réduit sa vitesse lorsque la température descend de 5°C en dessous de chaque seuil défini.

* Commandes pour surveiller le ventilateur PWM. Pour vérifier l’état du ventilateur :

  .. code-block:: shell
  
    cat /sys/class/thermal/cooling_device0/cur_state

* Pour afficher la vitesse du ventilateur :

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

Dans le Pironman 5, le ventilateur PWM est un élément essentiel pour maintenir une température de fonctionnement optimale, en particulier lors de tâches intensives, garantissant ainsi des performances stables et efficaces du Raspberry Pi 5.

Ventilateurs RGB
-------------------

.. image:: img/size_fan.png

* **Dimensions externes** : 40×40×10 mm  
* **Poids** : 13,5 ± 5 g/unité  
* **Durée de vie** : 30 000 heures (à température ambiante de 25°C)  
* **Débit d’air maximal** : 2,46 CFM  
* **Pression statique maximale** : 0,62 mm-H2O  
* **Niveau sonore** : 22,31 dBA  
* **Puissance d’entrée nominale** : 5V / 0,15A  
* **Vitesse nominale** : 3500 ±10 % RPM  
* **Température de fonctionnement** : -10℃ à +60℃  
* **Température de stockage** : -20℃ à +70℃

