.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Configuration de Plex
=======================================

Plex est une puissante plateforme de serveur multimédia qui vous permet d’organiser, de diffuser et d’accéder à vos films, séries TV, musiques et photos sur plusieurs appareils.  
En configurant Plex sur la série Pironman5 alimentée par Raspberry Pi, vous pouvez créer un centre multimédia domestique abordable et économe en énergie fonctionnant 24h/24 et 7j/7.  
La taille compacte, la faible consommation d’énergie et la flexibilité du Raspberry Pi en font un excellent choix pour héberger Plex, transformant votre Pi en un hub de divertissement personnel accessible depuis votre réseau domestique ou même à distance.


**Préparation**

* Carte MicroSD (16 Go+, Classe 10 recommandée)  
* Système officiel Raspberry Pi OS (ou Raspberry Pi OS Lite)  
* Connexion réseau stable (Ethernet filaire recommandé)  
* Disque dur externe ou clé USB (pour un stockage étendu)  


**Installer Portainer**

Ouvrez le terminal et entrez les commandes suivantes :

1. Installer Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Installer Portainer

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. Redémarre ton Raspberry Pi. (Puis effectue les étapes suivantes **IMMÉDIATEMENT**.)

4. Après le démarrage de ton Raspberry Pi, ouvre un navigateur web et visite ton adresse Portainer : ``http://<adresse-ip-de-ton-rpi>:9443`` .

5. Par défaut, tu pourras voir un avertissement indiquant que le site utilise un certificat SSL/TLS auto-signé qui n’a pas été émis par une Autorité de Certification (CA) reconnue. La plupart des navigateurs afficheront un tel avertissement. Dans ce cas, tu peux l’ignorer sans risque, accepter le risque et poursuivre.

   .. image:: img/home_server_app/private_save.png

#. Lors de ta première connexion, il te sera demandé de définir un mot de passe administrateur.

   .. image:: img/home_server_app/ptn_new_admin.png

#. Après avoir créé le compte administrateur, tu accéderas à l’interface de Portainer. Depuis la barre de navigation de gauche, va dans **Settings (Paramètres) -> General (Général)**, trouve **App Templates (Modèles d’application)**, et entre l’URL suivante dans le champ : ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. Clique sur **Save Application Settings (Enregistrer les paramètres de l’application)**. La configuration prendra environ 10 secondes.


**Installer Plex**

1. Dans la barre de navigation de gauche, clique sur **Home (Accueil) -> local**.

   .. image:: img/home_server_app/ptn_home_local.png

2. Rends-toi dans **Templates (Modèles) -> Application**. Dans la barre de recherche en haut à droite, tape *plex* et clique dessus.

   .. image:: img/home_server_app/ptn_temp_plex.png

#. Définis le mode réseau sur **host (hôte)**.

   .. image:: img/home_server_app/ptn_plex_network_host.png

#. Déplie **Show advanced options (Afficher les options avancées)**.

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

#. Dans la section **volume mapping (mappage de volume)**, configure les chemins de stockage pour tes fichiers multimédias et accorde à Plex les permissions de lecture/écriture. Les chemins par défaut sont ``/portainer/TV`` et ``/portainer/Movies``, tous deux avec l’accès en lecture/écriture activé.

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

#. Clique sur **Deploy (Déployer)** et attends que l’installation de Plex se termine.


**Configurer le Serveur Plex**

1. Ouvre ton navigateur et saisis : ``http://<ton_ip>:32400/web`` . Tu devrais maintenant voir l’interface de Plex.

   .. image:: img/home_server_app/plex_visit.png

2. Ignore l’offre d’abonnement premium.

3. Ensuite, tu verras l’écran de **Configuration du serveur (Server Setup)**. Tu peux cocher *Autoriser l’accès à mes médias en dehors de mon domicile (Allow me to access my media outside my home)*. Pour l’instant, il est recommandé de laisser cette option décochée et de la configurer plus tard si nécessaire.

   .. image:: img/home_server_app/plex_server_setup1.png

4. Il te sera ensuite demandé d’organiser tes médias. Tu peux choisir *Ignorer (Skip)* et ajouter des médias plus tard via les paramètres. Cependant, il est recommandé d’ajouter directement les chemins de stockage que tu as configurés dans le mappage de volume de Portainer afin que Plex puisse scanner et importer automatiquement tes médias.

   .. image:: img/home_server_app/plex_server_setup2.png

5. Sélectionne le type de ta bibliothèque de médias, donne un nom à ta bibliothèque et choisis la langue.

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6. Ajoute des dossiers. Localise les chemins de stockage des médias que tu as définis précédemment et clique sur **Ajouter la bibliothèque (Add Library)**.

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7. Clique sur **Terminer (Finish)**. Ton serveur Plex sur Raspberry Pi est maintenant entièrement configuré.

   .. image:: img/home_server_app/plex_server_setup3.png

8. Tu devrais maintenant voir tes fichiers multimédias affichés sur la page d’accueil du serveur Plex.

   .. image:: img/home_server_app/plex_index.png