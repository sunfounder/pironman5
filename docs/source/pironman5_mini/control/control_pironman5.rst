.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez dans l’univers du Raspberry Pi, d’Arduino et de l’ESP32 aux côtés d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l’aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces et avant-premières de nouveaux produits.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à nos concours et offres spéciales pendant les périodes festives.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

5. Contrôle via commandes ou tableau de bord
=======================================================

Une fois le module ``pironman5`` installé avec succès, le service ``pironman5.service`` se lance automatiquement au redémarrage.

Vous pouvez surveiller et contrôler le Pironman 5 Mini à l’aide de commandes ou en accédant au tableau de bord via la page web à l’adresse ``http://<ip>:34001``.

.. note::

    * Pour le système **Home Assistant**, la surveillance et le contrôle du Pironman 5 Mini se font uniquement via le tableau de bord, accessible à l’adresse ``http://<ip>:34001``.

    .. * Pour le système **Batocera.linux**, le contrôle et la surveillance se font uniquement par commandes. Il est important de noter que toute modification de configuration nécessite un redémarrage du service via ``pironman5 restart`` pour être prise en compte.


.. toctree::
    :maxdepth: 1

    control_with dashboard 
    control_with_commands