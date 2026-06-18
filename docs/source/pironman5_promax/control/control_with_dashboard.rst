
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _promax_view_control_dashboard:

Visualiser et contrôler depuis le Tableau de Bord
===================================================

Une fois que vous avez installé avec succès le module ``pironman5``, le ``pironman5.service`` démarrera automatiquement au redémarrage.

Vous pouvez maintenant ouvrir la page de surveillance dans votre navigateur pour voir les informations sur votre Raspberry Pi, configurer les LEDs RGB, etc. Le lien de la page est : ``http://<ip>:34001``.

.. image:: img/dashboard_prm5promax.png
  :width: 90%

Cette page contient les sections **Tableau de bord**, **Historique**, **Journal** et **Paramètres**.

.. image:: img/dashboard_tab.png
  :width: 90%

Tableau de bord
-----------------------

Il y a plusieurs cartes pour visualiser l'état pertinent du Raspberry Pi, notamment :

* **Température** : Visualise la température du CPU et du GPU du Raspberry Pi.

  .. image:: img/dashboard_temp.png
    :align: center

* **Stockage** : Affiche la capacité de stockage d'un Raspberry Pi, montrant les différentes partitions de disque avec leur espace utilisé et disponible.

  .. image:: img/dashboard_storage.png
    :align: center

* **Mémoire** : Montre l'utilisation de la RAM du Raspberry Pi et son pourcentage.

  .. image:: img/dashboard_memory.png
    :align: center

* **Réseau** : Affiche le type de connexion réseau actuel, les vitesses de téléchargement et d'envoi.

  .. image:: img/dashboard_network.png
    :align: center

* **Processeur** : Illustre les performances du CPU du Raspberry Pi, y compris l'état de ses quatre cœurs, les fréquences de fonctionnement et le pourcentage d'utilisation du CPU.

  .. image:: img/dashboard_processor.png
    :align: center

Historique
--------------

La page Historique vous permet de visualiser les données historiques. Cochez les données que vous souhaitez voir dans la barre latérale gauche, puis sélectionnez la plage de temps pour voir les données de cette période, et vous pouvez également cliquer pour les télécharger.

.. image:: img/dashboard_history1.png
  :width: 90%

.. image:: img/dashboard_history2.png
  :width: 90%

Journal
------------

La page Journal est utilisée pour visualiser les journaux du service Pironman5 actuellement en cours d'exécution. Le service Pironman5 comprend plusieurs sous-services, chacun avec son propre journal. Sélectionnez le journal que vous souhaitez consulter, et vous pouvez voir les données du journal sur la droite. S'il est vide, cela peut signifier qu'il n'y a pas de contenu de journal.

* Chaque journal a une taille fixe de 10 Mo. Lorsqu'il dépasse cette taille, un deuxième journal est créé.
* Le nombre de journaux pour un même service est limité à 10. Si le nombre dépasse cette limite, le journal le plus ancien est automatiquement supprimé.
* Il y a des outils de filtrage au-dessus de la zone de journal à droite. Vous pouvez sélectionner le niveau de journal, filtrer par mots-clés, et utiliser plusieurs outils pratiques, incluant **Retour à la ligne**, **Défilement automatique** et **Mise à jour automatique**.
* Les journaux peuvent également être téléchargés localement.

.. image:: img/dashboard_log1.png
  :width: 90%

.. image:: img/dashboard_log2.png
  :width: 90%

Paramètres
-----------------

Il y a un menu de paramètres dans le **coin supérieur droit** de la page où vous pouvez personnaliser les réglages selon vos préférences. Après avoir effectué des modifications, les changements seront sauvegardés automatiquement. Si nécessaire, vous pouvez cliquer sur le bouton EFFACER en bas pour effacer les données historiques.

.. image:: img/dashboard_setting_darkmode.png
  :width: 600

* **Mode sombre** : Basculer entre les thèmes clair et sombre. L'option de thème est sauvegardée dans le cache du navigateur. Changer de navigateur ou vider le cache rétablira le thème clair par défaut.
* **Afficher les disques non montés** : Indique s'il faut afficher les disques non montés dans le tableau de bord.
* **Afficher tous les cœurs** : Indique s'il faut afficher tous les cœurs dans le tableau de bord.
* **Disposition des cartes** : Définit la disposition des cartes du tableau de bord.
* **Unité de température** : Définit l'unité de température affichée par le système.

**À propos de l'écran OLED**

.. image:: img/dashboard_setting_oled.png
  :width: 600

* **Activer OLED** : Active ou désactive l'OLED.
* **Rotation OLED** : Définit la rotation de l'OLED.
* **Délai de mise en veille OLED** : Définit le délai de mise en veille de l'OLED.
* **Page OLED** : Définit la page OLED à afficher : **Synthèse système**, **Métriques de performance**, **Utilisation du disque**, **Adresses IP**.

**À propos des LEDs RGB**

.. image:: img/dashboard_setting_rgb.png
  :width: 600

* **Activer RGB** : Active ou désactive les LEDs RGB.
* **Couleur RGB** : Définit la couleur des LEDs RGB.
* **Luminosité RGB** : Vous pouvez ajuster la luminosité des LEDs RGB avec un curseur.
* **Style RGB** : Choisit le mode d'affichage des LEDs RGB. Les options incluent **Uni**, **Respiration**, **Flux**, **Flux inversé**, **Arc-en-ciel**, **Arc-en-ciel inversé** et **Cycle de teinte**.
* **Vitesse RGB** : Définit la vitesse des changements des LEDs RGB.
* **Nombre de LEDs RGB** : Définit le nombre de LEDs RGB à contrôler.

**À propos des données**

.. image:: img/dashboard_setting_debug.png
  :width: 600

* **Niveau de débogage** : Définit le niveau de débogage. Les options incluent **Info**, **Avertissement**, **Erreur** et **Critique**.
* **Conservation de l'historique** : Définit le nombre de jours de conservation des données historiques.
* **Effacer toutes les données** : Efface toutes les données historiques.
* **Redémarrer** : Redémarre le système.
* **Éteindre** : Éteint le système.
* **Redémarrer le service** : Redémarre les services système.

**Ventilateur**

Ces ventilateurs se connectent à un port dédié pour Ventilateur du CPU 4 broches sur le Raspberry Pi 5. Leur stratégie de contrôle par défaut est un schéma d'ajustement de vitesse intelligent à plusieurs niveaux géré par le firmware, basé sur la température du CPU. Cela signifie que lorsque vous utilisez un Ventilateur du CPU officiel ou compatible et que vous le connectez correctement, le système ajustera automatiquement la vitesse du ventilateur en fonction des changements de température du CPU (commençant à fonctionner au-dessus de 50°C) sans aucune intervention manuelle de votre part.
