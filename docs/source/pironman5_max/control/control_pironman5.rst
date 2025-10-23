.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 ! Rejoignez d'autres passionnés pour approfondir vos connaissances sur le Raspberry Pi, l’Arduino et l’ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Résolvez les problèmes après-vente et relevez les défis techniques grâce à notre équipe et à la communauté.
    - **Apprendre & partager** : Échangez des astuces et des tutoriels pour renforcer vos compétences.
    - **Aperçus exclusifs** : Soyez informé(e) en avant-première des annonces de nouveaux produits et bénéficiez d’aperçus exclusifs.
    - **Réductions spéciales** : Profitez d’offres exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et à des promotions festives.

    👉 Prêt(e) à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _control_commands_dashboard_max:

5. Contrôle par commandes ou tableau de bord
=======================================================

Une fois le module ``pironman5`` installé avec succès, le service ``pironman5.service`` démarrera automatiquement après chaque redémarrage.

Vous pouvez surveiller et contrôler le Pironman 5 soit par commandes, soit via le tableau de bord accessible depuis l’interface web à l’adresse ``http://<ip>:34001``.

.. note::

    * Pour le système **Home Assistant**, vous pouvez uniquement surveiller et contrôler le Pironman 5 via le tableau de bord en ouvrant la page ``http://<ip>:34001``.
    * Pour le système **Batocera.linux**, vous ne pouvez surveiller et contrôler le Pironman 5 que par commandes. Il est important de noter que toute modification de la configuration nécessite un redémarrage du service avec ``pironman5 restart`` pour être prise en compte.


.. toctree::
    :maxdepth: 1

    control_with dashboard 
    control_with_commands