.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _fan_mini:

Ventilateurs
=================

Refroidisseur actif
-------------------------

Le refroidisseur actif du Pironman 5 Mini est piloté directement par le système du Raspberry Pi.

.. image:: img/active_cooler.png

En matière de dissipation thermique pour le Raspberry Pi 5, notamment en situation de forte sollicitation, le Pironman 5 Mini intègre un système de refroidissement intelligent.  
Il se compose d’un refroidisseur actif principal (Active Cooler) et d’un Ventilateur GPIO complémentaire.  
La stratégie de refroidissement est étroitement liée au système de gestion thermique intégré du Raspberry Pi 5.

Le fonctionnement du refroidisseur actif est basé sur la température du Raspberry Pi 5 :

* En dessous de 50 °C, le refroidisseur reste éteint (0 % de vitesse).
* À 50 °C, le ventilateur démarre à basse vitesse (30 %).
* À 60 °C, il passe à une vitesse moyenne (50 %).
* À 67,5 °C, la vitesse augmente à un niveau élevé (70 %).
* À 75 °C et plus, le ventilateur tourne à pleine puissance (100 %).

Cette relation entre température et vitesse s’applique également à la baisse, avec une hystérésis de 5 °C. La vitesse du ventilateur diminue lorsque la température descend 5 °C sous chaque seuil défini.

* Commandes pour surveiller le refroidisseur actif. Pour vérifier son état :

  .. code-block:: shell
  
    cat /sys/class/thermal/cooling_device0/cur_state

* Pour consulter la vitesse de rotation du ventilateur :

  .. code-block:: shell

    cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input

Dans le Pironman 5 Mini, le refroidisseur actif joue un rôle essentiel pour maintenir une température de fonctionnement optimale, en particulier lors de tâches intensives, garantissant ainsi un fonctionnement efficace et stable du Raspberry Pi 5.

Ventilateur GPIO
-------------------

.. image:: img/size_fan.png

* **Dimensions externes** : 40×40×10 mm  
* **Poids** : 13,5 ± 5 g/pièce  
* **Durée de vie** : 40 000 heures (à température ambiante de 25 °C)  
* **Débit d’air maximal** : 2,46 CFM  
* **Pression statique maximale** : 0,62 mm H₂O  
* **Niveau sonore** : 22,31 dBA  
* **Puissance nominale** : 5 V / 0,1 A  
* **Vitesse nominale** : 3500 ± 10 % RPM  
* **Température de fonctionnement** : de -10 °C à +70 °C  
* **Température de stockage** : de -30 °C à +85 °C  
