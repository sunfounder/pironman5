.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 ! Plongez-vous dans l’univers du Raspberry Pi, d’Arduino et d’ESP32 aux côtés d’autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques avec l’aide de notre équipe et de notre communauté.
    - **Apprendre & Partager** : Échangez astuces et tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des aperçus privilégiés.
    - **Réductions spéciales** : Profitez d’offres exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des campagnes promotionnelles.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _set_up_pironman5:

4. Configuration ou installation du logiciel
================================================

Une fois le système écrit sur la carte Micro SD ou le SSD NVMe, insérez-le dans l’emplacement prévu du Pironman 5. Appuyez ensuite sur le bouton d’alimentation pour démarrer l’appareil.

Après l’allumage, les différentes LED d’alimentation s’allument. En revanche, l’écran OLED, les LED RGB et les ventilateurs RGB (les deux ventilateurs latéraux) ne fonctionneront pas encore, car ils doivent être configurés. Si vous constatez des anomalies d’affichage à l’écran, ne vous en inquiétez pas : elles seront résolues après la configuration.

Avant toute configuration, vous devez démarrer votre Raspberry Pi et vous y connecter. Si vous ne savez pas comment faire, consultez le site officiel de Raspberry Pi : |link_rpi_get_start|.

Vous pouvez ensuite sélectionner le tutoriel de configuration correspondant à votre système.


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_batocera


**À propos du bouton d’alimentation**

Le bouton d’alimentation reproduit fidèlement le comportement du bouton physique du Raspberry Pi 5.

* **Extinction**

    * Si vous utilisez le système **Bookworm Desktop** de Raspberry Pi, appuyez deux fois rapidement pour éteindre l’appareil.
    * Si vous utilisez le système **Bookworm Lite**, une seule pression déclenche l’arrêt.
    * Pour forcer un arrêt brutal, maintenez le bouton enfoncé.

* **Allumage**

    * Si la carte Raspberry Pi est éteinte mais toujours alimentée, une simple pression suffit pour la rallumer.

* Si vous utilisez un système ne prenant pas en charge la gestion du bouton d’arrêt, maintenez le bouton enfoncé pendant 5 secondes pour forcer l’arrêt, puis appuyez une fois pour allumer.

