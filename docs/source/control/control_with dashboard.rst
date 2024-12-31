.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Assistance experte** : Résolvez les problèmes après-vente et les défis techniques avec l’aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aperçus exclusifs.
    - **Réductions spéciales** : Bénéficiez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et des promotions spéciales.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _view_control_dashboard:

Afficher et contrôler depuis le tableau de bord
=====================================================

Une fois que vous avez installé avec succès le module ``pironman5``, le service ``pironman5.service`` démarrera automatiquement après le redémarrage.

Vous pouvez désormais ouvrir la page de surveillance dans votre navigateur pour consulter les informations sur votre Raspberry Pi, configurer les LED RGB et contrôler le ventilateur, entre autres. Le lien de la page est : ``http://<ip>:34001``.

Cette page contient les sections **Tableau de bord**, **Historique**, **Journal** et **Paramètres**.

.. image:: img/dashboard_tab_new.jpg

  
Tableau de bord
------------------

Plusieurs cartes sont disponibles pour visualiser l’état du Raspberry Pi, notamment :

* **Ventilateur** : Affiche la température du processeur du Raspberry Pi et la vitesse du ventilateur PWM. **GPIO Fan State** indique l’état des deux ventilateurs RGB latéraux. À la température actuelle, les deux ventilateurs RGB sont éteints.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%

* **Stockage** : Montre la capacité de stockage du Raspberry Pi, affichant les différentes partitions et leurs espaces utilisés et disponibles.

  .. image:: img/dashboard_storage.png
    :width: 90%

* **Mémoire** : Indique l’utilisation de la RAM du Raspberry Pi et son pourcentage.

  .. image:: img/dashboard_memory.png
    :width: 90%

* **Réseau** : Affiche le type de connexion réseau actuel, ainsi que les vitesses de téléchargement et de téléversement.

  .. image:: img/dashboard_network.png
    :width: 90%

* **Processeur** : Illustre les performances du processeur du Raspberry Pi, y compris l’état de ses quatre cœurs, les fréquences de fonctionnement et le pourcentage d’utilisation du CPU.

  .. image:: img/dashboard_processor.png
    :width: 90%


Historique
-------------

La page Historique vous permet de consulter les données historiques. Sélectionnez les données à afficher dans la barre latérale gauche, choisissez la période souhaitée, et téléchargez les données si nécessaire.

.. image:: img/dashboard_history1.png
  :width: 90%

.. image:: img/dashboard_history2.png
  :width: 90%

Journal
----------

La page Journal est utilisée pour consulter les journaux du service Pironman5 en cours d’exécution. Le service Pironman5 inclut plusieurs sous-services, chacun ayant son propre journal. Sélectionnez le journal que vous souhaitez consulter pour afficher les données correspondantes. Si l’écran est vide, cela signifie qu’il n’y a pas de contenu de journal.

* Chaque journal a une taille fixe de 10 Mo. Lorsqu’il dépasse cette taille, un deuxième journal est créé.
* Le nombre de journaux pour un même service est limité à 10. Si ce nombre est dépassé, le plus ancien journal sera automatiquement supprimé.
* Des outils de filtrage sont disponibles au-dessus de la zone de journal, vous permettant de sélectionner le niveau de journalisation, de filtrer par mots-clés et d’utiliser des outils pratiques tels que **Enroulement des lignes**, **Défilement automatique** et **Mise à jour automatique**.
* Les journaux peuvent également être téléchargés localement.

.. image:: img/dashboard_log1.png
  :width: 90%

.. image:: img/dashboard_log2.png
  :width: 90%

Paramètres
-------------

Un menu des paramètres se trouve dans le coin supérieur droit de la page, vous permettant de personnaliser les réglages selon vos préférences. Les modifications sont enregistrées automatiquement. Si nécessaire, vous pouvez cliquer sur le bouton CLEAR en bas pour effacer les données historiques.

.. image:: img/Dark_mode_and_Temperature.jpg
  :width: 600

* **Mode sombre** : Basculez entre les thèmes clair et sombre. Cette option est enregistrée dans le cache du navigateur. Le changement de navigateur ou la suppression du cache réinitialisera le thème par défaut clair.
* **Unité de température** : Définissez l’unité de température affichée par le système.

**À propos de l’écran OLED**

.. image:: img/OLED_Sreens.jpg
  :width: 600

* **Activation de l’OLED** : Permet d’activer ou de désactiver l’OLED.
* **Disque OLED** : Configurez le disque OLED.
* **Interface réseau OLED** : 

  * **all** : Alterne entre l’adresse IP Ethernet et Wi-Fi.
  * **eth0** : Affiche uniquement l’adresse IP Ethernet.
  * **wlan0** : Affiche uniquement l’adresse IP Wi-Fi.

* **Rotation de l’OLED** : Définissez l’angle de rotation de l’OLED.

**À propos des LED RGB**

.. image:: img/RGB_LEDS.jpg
  :width: 600

* **Activation des RGB** : Activez ou désactivez les LED RGB.
* **Couleur des RGB** : Configurez la couleur des LED RGB.
* **Luminosité des RGB** : Ajustez la luminosité des LED RGB à l’aide d’un curseur.
* **Style des RGB** : Choisissez le mode d’affichage des LED RGB. Les options incluent **Fixe**, **Respiration**, **Flux**, **Flux inversé**, **Arc-en-ciel**, **Arc-en-ciel inversé**, et **Cycle de teinte**.

  .. note::

     Si vous sélectionnez **Arc-en-ciel**, **Arc-en-ciel inversé**, ou **Cycle de teinte**, vous ne pourrez pas configurer la couleur.

* **Vitesse des RGB** : Définissez la vitesse des changements de couleur des LED RGB.

**À propos des ventilateurs RGB**

.. image:: img/RGB_fans.png
  :width: 600

* **LED du ventilateur** : Configurez la LED du ventilateur sur ON, OFF ou FOLLOW.
* **Mode du ventilateur** : Définissez le mode de fonctionnement des deux ventilateurs RGB. Ces modes déterminent les conditions d’activation des ventilateurs RGB.

    * **Silencieux** : Les ventilateurs s’activent à 70°C.
    * **Équilibré** : Les ventilateurs s’activent à 67,5°C.
    * **Cool** : Les ventilateurs s’activent à 60°C.
    * **Performance** : Les ventilateurs s’activent à 50°C.
    * **Toujours actif** : Les ventilateurs fonctionnent en permanence.

Par exemple, si le mode **Performance** est défini, les ventilateurs RGB s’activent à 50°C.

Après enregistrement, si la température du CPU dépasse 50°C, l’état **GPIO Fan State** passera à ON dans le tableau de bord, et les ventilateurs RGB latéraux commenceront à tourner.

.. image:: img/dashboard_rgbfan_on.png
  :width: 300
