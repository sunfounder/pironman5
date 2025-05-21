.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 ! Rejoignez d'autres passionnés pour approfondir vos connaissances sur le Raspberry Pi, l’Arduino et l’ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Résolvez les problèmes après-vente et relevez les défis techniques grâce à l’aide de notre équipe et de notre communauté.
    - **Apprendre & partager** : Échangez des conseils et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et à des démonstrations exclusives.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et à des offres spéciales pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _max_view_control_dashboard:

Vue et contrôle depuis le tableau de bord
===============================================

Une fois le module ``pironman5`` installé avec succès, le service ``pironman5.service`` démarrera automatiquement au redémarrage.

Vous pouvez désormais ouvrir la page de surveillance dans votre navigateur pour consulter les informations du Raspberry Pi, configurer les LED RGB, contrôler les ventilateurs, etc. Lien de la page : ``http://<ip>:34001``.

Cette interface comporte les onglets **Dashboard**, **Historique**, **Log** et **Settings**.

.. image:: img/dashboard_tab.png
  :width: 90%


Tableau de bord
-----------------------

Plusieurs cartes permettent de visualiser l’état du Raspberry Pi, dont :

* **Ventilateur** : Affiche la température du CPU et la vitesse du ventilateur PWM. **GPIO Fan State** indique l’état des deux ventilateurs RGB latéraux. À la température actuelle, ils sont éteints.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%


* **Stockage** : Montre la capacité de stockage du Raspberry Pi, les différentes partitions, l’espace utilisé et disponible.

  .. image:: img/dashboard_storage.png
    :width: 90%


* **Mémoire** : Affiche l’utilisation de la RAM du Raspberry Pi en valeur absolue et en pourcentage.

  .. image:: img/dashboard_memory.png
    :width: 90%


* **Réseau** : Affiche le type de connexion réseau actuel, ainsi que les vitesses de téléchargement et d’envoi.

  .. image:: img/dashboard_network.png
    :width: 90%


* **Processeur** : Affiche les performances du CPU, y compris l’état des 4 cœurs, les fréquences et l’utilisation du processeur.

  .. image:: img/dashboard_processor.png
    :width: 90%


Historique
--------------

L’onglet Historique permet de consulter les données enregistrées. Cochez les données souhaitées dans la barre latérale gauche, sélectionnez la plage temporelle, et vous pouvez également télécharger les résultats.

.. image:: img/dashboard_history1.png
  :width: 90%

.. image:: img/dashboard_history2.png
  :width: 90%

Journal
------------

L’onglet Journal permet de consulter les logs du service Pironman5 en cours d’exécution. Chaque sous-service a son propre journal. Sélectionnez celui que vous voulez consulter : s’il est vide, cela signifie qu’aucune donnée n’a encore été enregistrée.

* Chaque journal a une taille maximale de 10 Mo. Lorsqu’il est dépassé, un nouveau fichier est créé.
* Le nombre de journaux par service est limité à 10. Les plus anciens sont automatiquement supprimés.
* Des outils de filtrage sont disponibles : filtre par niveau de log, par mot-clé, **retour à la ligne automatique**, **défilement automatique**, et **mise à jour automatique**.
* Les journaux peuvent être téléchargés localement.

.. image:: img/dashboard_log1.png
  :width: 90%

.. image:: img/dashboard_log2.png
  :width: 90%


Paramètres
-----------------

Un menu Paramètres est disponible en haut à droite de la page pour personnaliser votre interface. Les modifications sont enregistrées automatiquement. Vous pouvez aussi cliquer sur le bouton CLEAR pour réinitialiser les données historiques.

.. image:: img/Dark_mode_and_Temperature.jpg
  :width: 600

* **Dark Mode** : Basculez entre les thèmes clair et sombre. Le choix est enregistré dans le cache du navigateur. Changer de navigateur ou vider le cache revient au thème par défaut.
* **Temperature Unit** : Définissez l’unité de température affichée.

**À propos de l’écran OLED**

.. image:: img/OLED_Sreens.jpg
  :width: 600

* **OLED Enable** : Activer ou désactiver l’écran OLED.
* **OLED Disk** : Choisir la partition à afficher sur l’OLED.
* **OLED Interface Réseau** :

  * **all** : Affiche en alternance l’IP Ethernet et Wi-Fi.
  * **eth0** : Affiche uniquement l’IP Ethernet.
  * **wlan0** : Affiche uniquement l’IP Wi-Fi.

* **OLED Rotation** : Définir l’orientation de l’écran OLED.

**À propos des LED RGB**

.. image:: img/RGB_LEDS.jpg
  :width: 600

* **RGB Enable** : Activer ou désactiver les LED RGB.
* **RGB Color** : Définir la couleur des LED RGB.
* **RGB Brightness** : Régler la luminosité via un curseur.
* **RGB Style** : Choisir un mode d’affichage parmi : **Solid**, **Breathing**, **Flow**, **Flow_reverse**, **Rainbow**, **Rainbow Reverse**, **Hue Cycle**.

  .. note::

     Si vous choisissez **Rainbow**, **Rainbow Reverse** ou **Hue Cycle**, la couleur ne pourra pas être personnalisée.

* **RGB Speed** : Définir la vitesse d’animation des LED RGB.

**À propos des ventilateurs RGB**

.. image:: img/RGB_FAN2.png
  :width: 600

* **GPIO Fan Mode** : Choisir le mode de fonctionnement des ventilateurs RGB latéraux, qui détermine à quelle température ils se déclenchent.

    * **Quiet** : Activation à 70°C.
    * **Balanced** : Activation à 67.5°C.
    * **Cool** : Activation à 60°C.
    * **Performance** : Activation à 50°C.
    * **Always On** : Toujours allumés.

Par exemple, en mode **Performance**, les ventilateurs se déclenchent à 50°C.

Après enregistrement, si la température du CPU dépasse 50°C, vous verrez **GPIO Fan State** passer à ON dans le tableau de bord, et les ventilateurs latéraux s’activeront.

.. image:: img/dashboard_rgbfan_on.png
  :width: 300

