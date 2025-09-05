.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives**: Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales**: Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et concours**: Participez à des tirages au sort et à des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !


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

3. Ouvre ton navigateur et visite ton adresse Portainer : ``http://<your-rpi-ip-address>:9443`` .

.. note::

   Par défaut, tu verras un avertissement indiquant que le site utilise un certificat SSL/TLS auto-signé qui n’a pas été émis par une Autorité de Certification (CA) reconnue.  
   La plupart des navigateurs afficheront un tel avertissement.  
   Dans ce cas, tu peux l’ignorer sans risque, accepter et continuer.

   .. image:: img/home_server_app/private_save.png


4. Lors de la première connexion, tu devras définir un mot de passe administrateur.

   .. image:: img/home_server_app/ptn_new_admin.png

5. Après avoir enregistré le compte administrateur, tu accéderas à l’interface de Portainer. Depuis la barre de navigation à gauche, clique sur **Setting -> General**, trouve **App Templates**, et entre l’URL suivante dans le champ : ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

6. Clique sur **Save Application Settings**. La configuration prendra environ 10 secondes.


**Installer NextCloud**

1. Dans la barre de navigation de gauche, clique sur **Home -> local -> Templates -> Application**. Dans la barre de recherche en haut à droite, tape *nextcloud* et clique dessus.

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

2. Clique sur **Deploy the stack**, et attends que le déploiement soit terminé. Cela prend généralement environ deux minutes.

   .. image:: img/home_server_app/ptn_temp_deploy.png

Une fois terminé, NextCloud sera installé.


**Utiliser NextCloud**

1. Ouvre ton navigateur et visite ton adresse NextCloud : ``http://<your-rpi-ip-address>:32768`` .

.. note::

   De la même manière, tu verras un avertissement indiquant que le site utilise un certificat SSL/TLS auto-signé qui n’a pas été émis par une Autorité de Certification (CA) reconnue.  
   La plupart des navigateurs afficheront un tel avertissement.  
   Dans ce cas, tu peux l’ignorer sans risque, accepter et continuer.

   .. image:: img/home_server_app/private_save.png

2. Lors de la première connexion, tu devras définir un mot de passe administrateur.

   .. image:: img/home_server_app/nc_admin_install.png

3. Après l’enregistrement, tu peux commencer à utiliser NextCloud.

   .. image:: img/home_server_app/nc_dashboard.png
