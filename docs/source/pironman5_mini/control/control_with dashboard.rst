
.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d’autres passionnés et explorez en profondeur le monde du Raspberry Pi, d’Arduino et de l’ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Résolvez vos problèmes techniques ou après-vente avec l’aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des conseils et tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Soyez les premiers informés des nouvelles annonces produits et aperçus.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des concours et offres spéciales lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès maintenant !

.. _view_control_dashboard_mini:

Visualiser et contrôler depuis le tableau de bord
=========================================================

Une fois le module ``pironman5`` installé avec succès, le service ``pironman5.service`` se lancera automatiquement au redémarrage.

Vous pouvez maintenant ouvrir la page de surveillance dans votre navigateur pour consulter les informations de votre Raspberry Pi, configurer les LED RGB, contrôler le ventilateur, etc. L'adresse de la page est : ``http://<ip>:34001``.

Cette interface comprend les onglets **Dashboard**, **Historique**, **Journal**, et une page **Paramètres**.

.. image:: img/dashboard_tab.png
  :width: 90%
  

Tableau de bord
-----------------------

Plusieurs cartes vous permettent de consulter les informations essentielles de votre Raspberry Pi, notamment :

* **Ventilateur** : Affiche la température du CPU et la vitesse du ventilateur PWM. **GPIO Fan State** indique l’état du ventilateur RGB. À la température actuelle, le ventilateur RGB est désactivé.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%
    

* **Stockage** : Montre la capacité de stockage du Raspberry Pi, avec le détail des partitions et de l’espace utilisé/disponible.

  .. image:: img/dashboard_storage.png
    :width: 90%
    

* **Mémoire** : Affiche l'utilisation de la RAM du Raspberry Pi, ainsi que le pourcentage utilisé.

  .. image:: img/dashboard_memory.png
    :width: 90%
    

* **Réseau** : Indique le type de connexion réseau, la vitesse d’envoi et de réception des données.

  .. image:: img/dashboard_network.png
    :width: 90%
    

* **Processeur** : Présente les performances du CPU, y compris l’état des quatre cœurs, les fréquences en cours et le pourcentage d’utilisation.

  .. image:: img/dashboard_processor.png
    :width: 90%
    

Historique
--------------

L’onglet Historique permet de consulter les données archivées. Cochez les données à afficher dans la barre latérale gauche, sélectionnez une période, puis cliquez pour les visualiser ou les télécharger.

.. image:: img/dashboard_history.png
  :width: 90%
  

Journal
------------

La page Journal affiche les journaux du service pironman5 en cours d’exécution. Ce service comporte plusieurs sous-services, chacun disposant de son propre journal. Sélectionnez celui que vous souhaitez consulter pour voir les données correspondantes à droite. Si l’espace est vide, cela signifie probablement qu’aucun journal n’est disponible.

* Chaque journal a une taille fixe de 10 Mo. Lorsqu’il est dépassé, un nouveau fichier est créé.
* Le nombre de journaux par service est limité à 10. Au-delà, les plus anciens sont automatiquement supprimés.
* Des outils de filtrage sont disponibles au-dessus de la zone des journaux : vous pouvez sélectionner le niveau de journalisation, filtrer par mots-clés et utiliser plusieurs options pratiques comme **Retour à la ligne automatique**, **Défilement automatique**, et **Mise à jour automatique**.
* Les journaux peuvent être téléchargés localement.

.. image:: img/dashboard_log.png
  :width: 90%
  

Paramètres
-----------------

Un menu Paramètres est accessible en haut à droite de la page.

.. note::

    Après toute modification, n’oubliez pas de cliquer sur le bouton **SAVE** en bas pour enregistrer vos paramètres.

.. image:: img/dashboard_settings.png
  :width: 90%
  

* **Dark Mode** : Basculez entre les thèmes clair et sombre. Le choix est mémorisé dans le cache du navigateur. Changer de navigateur ou vider le cache restaurera le thème par défaut (clair).
* **Temperature Unit** : Choisissez l’unité d’affichage des températures.
* **Fan Mode** : Définissez le mode de fonctionnement du ventilateur RGB. Chaque mode déclenche le ventilateur à une température différente :

    * **Quiet** : le ventilateur démarre à 70°C.
    * **Balanced** : le ventilateur démarre à 67,5°C.
    * **Cool** : le ventilateur démarre à 60°C.
    * **Performance** : le ventilateur démarre à 50°C.
    * **Always On** : le ventilateur reste toujours en marche.

    Par exemple, en mode **Performance**, le ventilateur s’active dès que le CPU atteint 50°C.

    Une fois les paramètres enregistrés, si la température du CPU dépasse 50°C, l’état **GPIO Fan State** passera à ON dans le tableau de bord et le ventilateur RGB commencera à tourner.

  .. image:: img/dashboard_rgbfan_on.png
    :width: 300
  

* **RGB Brightness** : Réglez la luminosité des LED RGB à l’aide d’un curseur.
* **RGB Color** : Définissez la couleur des LED RGB.
* **Style RGB** : Choisissez le mode d’animation des LED RGB. Les options incluent **Solid**, **Breathing**, **Flow**, **Flow_reverse**, **Rainbow**, **Rainbow Reverse** et **Hue Cycle**.

.. note::

  Si vous sélectionnez **Rainbow**, **Rainbow Reverse** ou **Hue Cycle** comme style RGB, la couleur ne pourra pas être définie manuellement.


* **Vitesse RGB** : Réglez la vitesse d’animation des effets RGB.