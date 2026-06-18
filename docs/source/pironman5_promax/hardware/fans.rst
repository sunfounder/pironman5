
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



Ventilateurs
==============

Ventilateur du CPU
----------------------------

Il y a 3 Ventilateurs du CPU sur le Pironman 5 Pro MAX.

Le Ventilateur du CPU sur le Pironman 5 Pro MAX est contrôlé par le système Raspberry Pi.

En ce qui concerne les solutions de refroidissement pour le Raspberry Pi 5, surtout sous charge élevée, la conception du Pironman 5 Pro MAX intègre un système de refroidissement intelligent. Il comporte un Ventilateur du CPU principal et deux Ventilateurs GPIO supplémentaires. La stratégie de refroidissement est étroitement intégrée au système de gestion thermique du Raspberry Pi 5.

Le fonctionnement du Ventilateur du CPU est basé sur la température du Raspberry Pi 5 :

* En dessous de 50°C, le Ventilateur du CPU reste éteint (vitesse 0%).
* À 50°C, le ventilateur démarre à basse vitesse (vitesse 30%).
* En atteignant 60°C, le ventilateur augmente à vitesse moyenne (vitesse 50%).
* À 67,5°C, le ventilateur monte à haute vitesse (vitesse 70%).
* À 75°C et plus, le ventilateur fonctionne à pleine vitesse (vitesse 100%).

Cette relation température-vitesse s'applique également lorsque la température diminue, avec un hystérésis de 5°C. La vitesse du ventilateur diminue lorsque la température chute de 5°C en dessous de chacun de ces seuils.

* Commandes pour surveiller le Ventilateur du CPU. Pour vérifier l'état du Ventilateur du CPU :

  .. code-block:: shell

    cat /sys/class/thermal/cooling_device0/cur_state

* Pour voir la vitesse du Ventilateur du CPU :

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

Dans le Pironman 5 Pro MAX, le Ventilateur du CPU est un composant critique pour maintenir des températures de fonctionnement optimales, particulièrement pendant les tâches intensives, garantissant que le Raspberry Pi 5 fonctionne efficacement et de manière fiable.

**Spécifications du ventilateur**

.. image:: img/size_fan.png

* **Dimensions externes** : 40*40*10 mm
* **Puissance d'entrée nominale** : 5V/0,106A
* **Vitesse nominale** : 4000 tr/min
* **Poids** : 13,5±5 g/pièce
* **Durée de vie** : 30 000 heures (température ambiante 25°C)
* **Bruit acoustique** : 22,31 dBA
* **Débit d'air maximal** : 2,46 CFM
* **Pression d'air maximale** : 0,62 mm-H2O
* **Température de fonctionnement** : -10°C à +60°C
* **Température de stockage** : -20°C à +70°C

**Définition des broches**

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Broche
     - Couleur
     - Description
   * - 1
     - Bleu
     - Signal PWM pour contrôler la vitesse du ventilateur
   * - 2
     - Rouge
     - Alimentation 5V
   * - 3
     - Noir
     - Masse
   * - 4
     - Jaune
     - Données d'entrée de la LED RGB interne
   * - 5
     - Vert
     - Données de sortie de la LED RGB interne

Refroidisseur tour
----------------------------

Sur le Pro MAX, le refroidisseur tour est une solution de refroidissement haute performance conçue pour maintenir votre Raspberry Pi 5 à des températures optimales pendant les tâches exigeantes. Il dispose d'un grand dissipateur thermique en aluminium et d'un ventilateur qui peut être contrôlé via PWM pour ajuster les performances de refroidissement selon les besoins. Le refroidisseur tour est compatible avec le Raspberry Pi 5 et peut être facilement installé à l'aide des vis et du support de montage inclus.

.. image:: img/size_tower_cooler.png

**Avertissement**

Ne touchez pas les pales, ne laissez pas les fils d'alimentation s'enrouler autour du ventilateur, et ne tirez pas sur les fils d'alimentation avec force pour éviter d'endommager le ventilateur.

Ne pas utiliser dans des environnements contenant des gaz inflammables ou tout danger.

Lorsque le ventilateur fonctionne, veuillez ne pas essayer de bloquer le ventilateur pendant une longue période. Si vous le faites, le ventilateur grillera en raison de la chaleur élevée générée par l'arrêt continu.

Lors de l'assemblage du ventilateur, veuillez prêter une attention particulière au bruit généré par la résonance ou les vibrations.

Ne laissez pas tomber le refroidisseur tour Icecube de hauteur, car cela pourrait affecter l'équilibre des pales du ventilateur.
