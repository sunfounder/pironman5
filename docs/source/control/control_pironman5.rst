.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes post-achat et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives**: Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales**: Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et tirages au sort**: Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

5. Contrôle par Commandes ou Tableau de Bord
=======================================================

Une fois le module ``pironman5`` installé avec succès, le service ``pironman5.service`` démarrera automatiquement lors du redémarrage.

Vous pouvez surveiller et contrôler le Pironman 5 via des commandes, ou en accédant au tableau de bord via la page web à l'adresse ``http://<ip>:34001``.

.. note::

    * Pour le système **Home Assistant**, vous pouvez uniquement surveiller et contrôler le Pironman 5 via le tableau de bord en ouvrant la page web à l'adresse ``http://<ip>:34001``.
    * Pour le système **Batocera.linux**, vous pouvez uniquement surveiller et contrôler le Pironman 5 via des commandes. Il est important de noter que toute modification de la configuration nécessite un redémarrage du service à l'aide de la commande ``pironman5 restart`` pour être prise en compte.


.. toctree::
    :maxdepth: 1

    control_with dashboard 
    control_with_commands