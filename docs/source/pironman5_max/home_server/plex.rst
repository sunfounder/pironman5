.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives**: Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales**: Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et concours**: Participez à des tirages au sort et à des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !



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

3. Ouvrez votre navigateur et visitez votre adresse Portainer : ``http://<your-rpi-ip-address>:9443`` .

.. note::

   Par défaut, il se peut que vous voyiez un avertissement indiquant que le site utilise un certificat SSL/TLS auto-signé qui n’a pas été délivré par une Autorité de Certification (CA) reconnue.  
   La plupart des navigateurs afficheront un tel avertissement.  
   Dans ce cas, vous pouvez l’ignorer en toute sécurité, accepter le risque et continuer.

   .. image:: img/home_server_app/private_save.png


4. Lors de votre première connexion, il vous sera demandé de définir un mot de passe administrateur.

   .. image:: img/home_server_app/ptn_new_admin.png

5. Après avoir créé le compte administrateur, vous accéderez à l’interface Portainer. Dans la barre de navigation de gauche, allez dans **Setting -> General**, trouvez **App Templates**, et saisissez l’URL suivante dans le champ :  
   ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

6. Cliquez sur **Save Application Settings**. La configuration prendra environ 10 secondes.


**Installer Plex**

1. Dans la barre de navigation de gauche, cliquez sur **Home -> local -> Templates -> Application**. Dans la barre de recherche en haut à droite, tapez *plex* et sélectionnez-le.

   .. image:: img/home_server_app/ptn_temp_plex.png

2. Réglez le mode réseau sur **host**.

   .. image:: img/home_server_app/ptn_plex_network_host.png

3. Développez **Show advanced options**.

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

4. Dans la section **volume mapping**, configurez les chemins de stockage de vos fichiers multimédias et accordez à Plex les permissions de lecture/écriture.  
   Les chemins par défaut sont ``/portainer/TV`` et ``/portainer/Movies``, tous deux avec l’accès lecture/écriture activé.

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

5. Cliquez sur **Deploy** et attendez que l’installation de Plex soit terminée.


**Configurer le serveur Plex**

1. Ouvrez votre navigateur et entrez : ``http://<your_ip>:32400/`` . Vous devriez maintenant voir l’interface Plex.

   .. image:: img/home_server_app/plex_visit.png

2. Ignorez l’offre d’abonnement premium.

3. Ensuite, vous verrez l’écran **Server Setup**. Vous pouvez cocher *Allow me to access my media outside my home*.  
   Pour l’instant, il est recommandé de laisser cette option décochée et de la configurer plus tard si nécessaire.

   .. image:: img/home_server_app/plex_server_setup1.png

4. Vous serez ensuite invité à organiser vos médias. Vous pouvez choisir *Skip* et ajouter vos médias plus tard via les paramètres.  
   Cependant, il est recommandé d’ajouter directement les chemins de stockage que vous avez configurés dans le mappage de volumes de Portainer afin que Plex puisse analyser et importer automatiquement vos médias.

   .. image:: img/home_server_app/plex_server_setup2.png

5. Sélectionnez le type de bibliothèque multimédia, donnez un nom à votre bibliothèque et choisissez la langue.

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6. Ajoutez des dossiers. Localisez les chemins de stockage des médias que vous avez configurés précédemment et cliquez sur **Add Library**.

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7. Cliquez sur **Finish**. Votre serveur Plex sur Raspberry Pi est maintenant entièrement configuré.

   .. image:: img/home_server_app/plex_server_setup3.png

8. Vous devriez maintenant voir vos fichiers multimédias affichés sur la page d’accueil du serveur Plex.

   .. image:: img/home_server_app/plex_index.png
