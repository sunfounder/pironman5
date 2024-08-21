.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes post-achat et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives**: Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales**: Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et tirages au sort**: Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _view_control_dashboard:

Affichage et Contrôle depuis le Tableau de Bord
===================================================

Une fois que vous avez installé avec succès le module ``pironman5``, le service ``pironman5.service`` démarrera automatiquement au redémarrage.

Vous pouvez maintenant ouvrir la page de surveillance dans votre navigateur pour consulter les informations sur votre Raspberry Pi, configurer les LEDs RGB, contrôler le ventilateur, etc. Le lien vers la page est: ``http://<ip>:34001``.

Cette page comprend un **Tableau de Bord**, une section **Historique**, une section **Journal**, ainsi qu'une page **Paramètres**.

.. image:: img/dashboard_tab.png
  :width: 90%
  
  
Tableau de Bord
-----------------------

Plusieurs cartes vous permettent de consulter l'état pertinent de votre Raspberry Pi, y compris :

* **Ventilateur**: Affiche la température du CPU du Raspberry Pi et la vitesse du ventilateur PWM. **État du Ventilateur GPIO** indique l'état des deux ventilateurs RGB latéraux. À la température actuelle, les deux ventilateurs RGB sont éteints.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%
    

* **Stockage**: Affiche la capacité de stockage d'un Raspberry Pi, montrant les différentes partitions de disque avec leur espace utilisé et disponible.

  .. image:: img/dashboard_storage.png
    :width: 90%
    

* **Mémoire**: Montre l'utilisation et le pourcentage de la RAM du Raspberry Pi.

  .. image:: img/dashboard_memory.png
    :width: 90%
    

* **Réseau**: Affiche le type de connexion réseau actuel, ainsi que les vitesses de téléchargement et de téléversement.

  .. image:: img/dashboard_network.png
    :width: 90%
    

* **Processeur**: Illustre les performances du CPU du Raspberry Pi, y compris l'état de ses quatre cœurs, les fréquences de fonctionnement et le pourcentage d'utilisation du CPU.

  .. image:: img/dashboard_processor.png
    :width: 90%
    

Historique
--------------

La page Historique vous permet de consulter les données historiques. Sélectionnez les données que vous souhaitez consulter dans la barre latérale gauche, puis choisissez la période pour afficher les données correspondantes. Vous pouvez également cliquer pour les télécharger.

.. image:: img/dashboard_history.png
  :width: 90%
  

Journal
------------

La page Journal permet de consulter les journaux du service Pironman5 actuellement en cours d'exécution. Le service Pironman5 comprend plusieurs sous-services, chacun ayant son propre journal. Sélectionnez le journal que vous souhaitez consulter et les données du journal s'afficheront à droite. Si l'écran est vide, cela peut signifier qu'il n'y a pas de contenu de journal.

* Chaque journal a une taille fixe de 10 Mo. Lorsqu'il dépasse cette taille, un deuxième journal est créé.
* Le nombre de journaux pour un même service est limité à 10. Si ce nombre est dépassé, le plus ancien journal sera automatiquement supprimé.
* Des outils de filtre se trouvent au-dessus de la zone de journal à droite. Vous pouvez sélectionner le niveau du journal, filtrer par mots-clés, et utiliser plusieurs outils pratiques, notamment **Retour à la ligne**, **Défilement automatique** et **Mise à jour automatique**.
* Les journaux peuvent également être téléchargés localement.

.. image:: img/dashboard_log.png
  :width: 90%
  

Paramètres
-----------------

Il y a un menu de paramètres dans le coin supérieur droit de la page. 

.. note::
    
    Après modification, vous devez cliquer sur le bouton **SAUVEGARDER** en bas pour enregistrer les paramètres.

.. image:: img/dashboard_settings.png
  :width: 90%
  

* **Mode sombre**: Basculez entre les thèmes clair et sombre. L'option de thème est enregistrée dans le cache du navigateur. Changer de navigateur ou vider le cache réinitialisera le thème par défaut (clair).
* **Unité de température**: Définissez l'unité de température affichée par le système.
* **Mode ventilateur**: Vous pouvez définir le mode de fonctionnement des deux ventilateurs RGB. Ces modes déterminent les conditions dans lesquelles les ventilateurs RGB s'activent.

    * **Silencieux**: Les ventilateurs RGB s'activent à 70°C.
    * **Équilibré**: Les ventilateurs RGB s'activent à 67,5°C.
    * **Cool**: Les ventilateurs RGB s'activent à 60°C.
    * **Performance**: Les ventilateurs RGB s'activent à 50°C.
    * **Toujours activés**: Les ventilateurs RGB seront toujours activés.

    Par exemple, si vous définissez le mode sur **Performance**, les ventilateurs RGB s'activeront à 50°C.

    Après avoir enregistré les modifications, si la température du CPU dépasse 50°C, vous verrez l'**État du Ventilateur GPIO** passer à ON dans le Tableau de Bord, et les ventilateurs RGB latéraux commenceront à tourner.

  .. image:: img/dashboard_rgbfan_on.png
    :width: 300
    

* **Luminosité RGB**: Vous pouvez ajuster la luminosité des LEDs RGB à l'aide d'un curseur.
* **Couleur RGB**: Définissez la couleur des LEDs RGB.
* **Style RGB**: Choisissez le mode d'affichage des LEDs RGB. Les options incluent **Solide**, **Respiration**, **Flow**, **Flow_reverse**, **Arc-en-ciel**, **Arc-en-ciel inversé**, et **Cycle de teinte**.

.. note::

  Si vous définissez le **Style RGB** sur **Arc-en-ciel**, **Arc-en-ciel inversé** ou **Cycle de teinte**, vous ne pourrez pas définir la couleur.


* **Vitesse RGB**: Réglez la vitesse des changements des LEDs RGB.
