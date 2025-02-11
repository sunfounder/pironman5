.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-goûts.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et à des promotions spéciales pour les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _view_control_dashboard:

Afficher et contrôler depuis le tableau de bord
=================================================

Une fois que vous avez installé le module ``pironman5`` avec succès, le service ``pironman5.service`` démarrera automatiquement au redémarrage.

Vous pouvez maintenant ouvrir la page de surveillance dans votre navigateur pour consulter les informations sur votre Raspberry Pi, configurer les LEDs RGB et contrôler le ventilateur. Le lien de la page est : ``http://<ip>:34001``.

Cette page comprend **Tableau de bord**, **Historique**, **Journal** et une page de **Paramètres**.

.. image:: img/dashboard_tab_new.jpg


Tableau de bord
-------------------------

Plusieurs cartes sont disponibles pour consulter l'état pertinent de votre Raspberry Pi, notamment :

* **Ventilateur** : Consultez la température du CPU du Raspberry Pi et la vitesse du ventilateur PWM. **GPIO Fan State** indique l'état des deux ventilateurs RGB latéraux. À la température actuelle, les deux ventilateurs RGB sont arrêtés.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%
    
* **Stockage** : Affiche la capacité de stockage d'un Raspberry Pi, montrant les différentes partitions de disque avec l'espace utilisé et disponible.

  .. image:: img/dashboard_storage.png
    :width: 90%
    
* **Mémoire** : Affiche l'utilisation de la RAM du Raspberry Pi ainsi que le pourcentage utilisé.

  .. image:: img/dashboard_memory.png
    :width: 90%
    
* **Réseau** : Affiche le type de connexion réseau actuel, ainsi que les vitesses de téléchargement et de téléversement.

  .. image:: img/dashboard_network.png
    :width: 90%
    
* **Processeur** : Illustre les performances du CPU du Raspberry Pi, y compris l'état de ses quatre cœurs, les fréquences d'opération et le pourcentage d'utilisation du CPU.

  .. image:: img/dashboard_processor.png
    :width: 90%
    

Historique
--------------

La page Historique vous permet de visualiser des données historiques. Sélectionnez les données que vous souhaitez consulter dans la barre latérale gauche, puis choisissez la plage de temps pour voir les données correspondantes. Vous pouvez également cliquer pour les télécharger.

.. image:: img/dashboard_history1.png
  :width: 90%
  
.. image:: img/dashboard_history2.png
  :width: 90%

Journal
----------

La page Journal est utilisée pour consulter les journaux du service Pironman5 en cours d'exécution. Le service Pironman5 comprend plusieurs sous-services, chacun ayant son propre journal. Sélectionnez le journal que vous souhaitez consulter, et vous pourrez voir les données correspondantes sur la droite. Si aucun contenu n'apparaît, cela peut signifier qu'il n'y a pas de journal disponible.

* Chaque journal a une taille fixe de 10 Mo. Lorsqu'il dépasse cette taille, un deuxième journal est créé.
* Le nombre de journaux pour un même service est limité à 10. Si ce nombre est dépassé, le journal le plus ancien est automatiquement supprimé. Vous pouvez également supprimer les journaux manuellement.
* Des outils de filtrage sont disponibles au-dessus de la zone de journal sur la droite. Vous pouvez sélectionner le niveau de journalisation, filtrer par mots-clés et utiliser plusieurs outils pratiques, notamment **Retour à la ligne**, **Défilement automatique** et **Mise à jour automatique**.
* Les journaux peuvent également être téléchargés localement.

.. image:: img/dashboard_log1.png
  :width: 90%
  
.. image:: img/dashboard_log2.png
  :width: 90%

Paramètres
------------

Dans le coin supérieur droit de la page, vous trouverez un menu de paramètres où vous pourrez personnaliser les réglages selon vos préférences. Après avoir effectué des modifications, elles seront enregistrées automatiquement. Si nécessaire, vous pouvez cliquer sur le bouton EFFACER en bas pour supprimer les données historiques.

.. image:: img/Dark_mode_and_Temperature.jpg
  :width: 600

* **Mode sombre** : Basculez entre les thèmes clair et sombre. L'option de thème est enregistrée dans le cache du navigateur. Changer de navigateur ou effacer le cache rétablira le thème clair par défaut.
* **Unité de température** : Définissez l'unité de température affichée par le système.

**À propos de l'écran OLED**

.. image:: img/OLED_Sreens.jpg
  :width: 600

* **Activer l'OLED** : Déterminez si l'écran OLED doit être activé.
* **Disque OLED** : Configurez le disque OLED.
* **Interface réseau OLED** :

  * **all** : Alterne entre l'affichage de l'adresse IP Ethernet et Wi-Fi.
  * **eth0** : Affiche uniquement l'adresse IP Ethernet.
  * **wlan0** : Affiche uniquement l'adresse IP Wi-Fi.

* **Rotation de l'OLED** : Configurez la rotation de l'écran OLED.

**À propos des LEDs RGB**

.. image:: img/RGB_LEDS.jpg
  :width: 600

* **Activer les RGB** : Déterminez si les LEDs RGB doivent être activées.
* **Couleur RGB** : Configurez la couleur des LEDs RGB.
* **Luminosité RGB** : Ajustez la luminosité des LEDs RGB à l'aide d'un curseur.
* **Style RGB** : Choisissez le mode d'affichage des LEDs RGB. Les options incluent **Solid**, **Breathing**, **Flow**, **Flow_reverse**, **Rainbow**, **Rainbow Reverse**, et **Hue Cycle**.

  .. note::

     Si vous définissez le **Style RGB** sur **Rainbow**, **Rainbow Reverse**, ou **Hue Cycle**, vous ne pourrez pas configurer la couleur.

* **Vitesse RGB** : Définissez la vitesse des changements des LEDs RGB.

**À propos des ventilateurs RGB**

.. image:: img/RGB_fans.png
  :width: 600

* **LED du ventilateur** : Configurez les LEDs du ventilateur en mode ON, OFF ou FOLLOW.
* **Mode ventilateur** : Configurez le mode de fonctionnement des deux ventilateurs RGB. Ces modes déterminent les conditions dans lesquelles les ventilateurs s'activent.

    * **Silencieux** : Les ventilateurs RGB s'activent à 70°C.
    * **Équilibré** : Les ventilateurs RGB s'activent à 67.5°C.
    * **Froid** : Les ventilateurs RGB s'activent à 60°C.
    * **Performance** : Les ventilateurs RGB s'activent à 50°C.
    * **Toujours activé** : Les ventilateurs RGB restent toujours activés.

Par exemple, si le mode **Performance** est activé, les ventilateurs RGB s'activent à 50°C.

Après avoir enregistré les réglages, si la température du CPU dépasse 50°C, vous verrez l'état **GPIO Fan State** passer à ON dans le tableau de bord, et les ventilateurs RGB latéraux commenceront à tourner.

.. image:: img/dashboard_rgbfan_on.png
  :width: 300
