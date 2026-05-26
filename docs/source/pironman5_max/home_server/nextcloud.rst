.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Configuration de NextCloudPi
=======================================

NextCloud est une solution de stockage cloud privé open-source, similaire à Google Drive ou Dropbox.  
Elle peut être utilisée pour stocker des fichiers, partager des documents, synchroniser des photos et gérer des calendriers et des contacts.  
Contrairement aux services de cloud publics, NextCloud donne aux utilisateurs un contrôle total sur leurs données, ce qui en fait une solution idéale pour les particuliers et les petites équipes qui accordent de l’importance à la confidentialité et à la sécurité des données.

La série Pironman5, propulsée par Raspberry Pi, offre une faible consommation d’énergie, une taille compacte et des performances fiables, ce qui en fait un excellent choix pour un serveur cloud privé domestique. Combiné avec NextCloud, il peut servir de système NAS économique.


**Préparation**

* Carte MicroSD (16 Go+, Classe 10 recommandée)  
* Système officiel Raspberry Pi OS (ou Raspberry Pi OS Lite)  
* Connexion réseau stable (Ethernet filaire recommandé)  
* Disque dur externe ou clé USB (pour un stockage étendu)  


**Installer Portainer**

Ouvre le terminal et entre les commandes suivantes :

1. Installer Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Installer Portainer

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. Redémarre ton Raspberry Pi. (Puis effectue les étapes suivantes **IMMÉDIATEMENT**.)

4. Après le démarrage de ton Raspberry Pi, ouvre un navigateur web et visite ton adresse Portainer : ``https://<adresse-ip-de-ton-rpi>:9443`` .

5. Par défaut, tu verras un avertissement indiquant que le site utilise un certificat SSL/TLS auto-signé qui n’a pas été émis par une Autorité de Certification (CA) reconnue. La plupart des navigateurs afficheront un tel avertissement. Dans ce cas, tu peux ignorer l’avertissement sans risque, accepter le risque et continuer.

   .. image:: img/home_server_app/private_save.png

#. Lors de la première connexion, tu devras définir un mot de passe administrateur.

   .. image:: img/home_server_app/ptn_new_admin.png

#. Après l’enregistrement du compte administrateur, tu accéderas à l’interface de Portainer. Depuis la barre de navigation de gauche, clique sur **Settings (Paramètres) -> General (Général)**, trouve **App Templates (Modèles d’application)**, et entre l’URL suivante dans le champ : ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. Clique sur **Save Application Settings (Enregistrer les paramètres de l’application)**. La configuration prendra environ 10 secondes.


**Installer NextCloud**

1. Dans la barre de navigation de gauche, clique sur **Home (Accueil) -> local**

   .. image:: img/home_server_app/ptn_home_local.png

2. Rends-toi dans **Templates (Modèles) -> Application**. Dans la barre de recherche en haut à droite, tape *nextcloud* et clique dessus.

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

3. Clique sur **Deploy the stack (Déployer la pile)**, et attends que le déploiement se termine. Cela prend généralement environ deux minutes.

   .. image:: img/home_server_app/ptn_temp_deploy.png

4. Une fois terminé, NextCloud sera installé.

   .. image:: img/home_server_app/ptn_temp_nextcloud_deploy_finish.png


**Utiliser NextCloud**

1. Ouvre ton navigateur et visite ton adresse NextCloud : ``https://<adresse-ip-de-ton-rpi>:32768`` .

.. note::

   De la même manière, tu verras un avertissement indiquant que le site utilise un certificat SSL/TLS auto-signé qui n’a pas été émis par une Autorité de Certification (CA) reconnue. La plupart des navigateurs afficheront un tel avertissement.  
   Dans ce cas, tu peux ignorer l’avertissement sans risque, accepter le risque et continuer.

   .. image:: img/home_server_app/private_save.png

2. Lors de la première connexion, tu devras définir un mot de passe administrateur.

   .. image:: img/home_server_app/nc_admin_install.png

3. Après l’enregistrement, tu peux commencer à utiliser NextCloud.

   .. image:: img/home_server_app/nc_dashboard.png