.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes après-vente et surmontez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives**: Bénéficiez d'un accès anticipé aux nouvelles annonces de produits et à des aperçus exclusifs.
    - **Réductions spéciales**: Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours**: Participez à des tirages au sort et à des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _set_up_pironman5:

4. Configuration ou installation du logiciel
================================================

Maintenant que le système a été écrit sur la Micro SD ou le NVMe SSD, vous pouvez les insérer dans l'emplacement prévu du Pironman 5. Ensuite, appuyez sur le bouton d'alimentation pour allumer l'appareil.

Après avoir allumé l'appareil, vous verrez que les différentes LED d'alimentation sont allumées, mais l'écran OLED, les LED RGB et les ventilateurs RGB (les deux ventilateurs latéraux) ne fonctionneront pas encore, car ils doivent être configurés. Si vous constatez des problèmes d'affichage à l'écran, veuillez les ignorer pour l'instant ; ils seront résolus après la configuration.

Avant de procéder à la configuration, vous devez démarrer et vous connecter à votre Raspberry Pi. Si vous ne savez pas comment vous connecter, vous pouvez consulter le site officiel de Raspberry Pi: |link_rpi_get_start|.

Vous pouvez ensuite sélectionner le tutoriel de configuration en fonction de votre système.


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_umbrel



**À propos du bouton d'alimentation**

Le bouton d'alimentation fait ressortir le bouton d'alimentation du Raspberry Pi 5, et il fonctionne de la même manière que le bouton d'alimentation du Raspberry Pi 5.

* **Éteindre**

    * Si vous utilisez le système **Raspberry Pi OS Desktop**, vous pouvez appuyer deux fois rapidement sur le bouton d’alimentation pour éteindre.
    * Si vous utilisez le système **Raspberry Pi OS Lite** sans interface graphique, appuyez une seule fois sur le bouton d’alimentation pour lancer l’arrêt.
    * Pour forcer un arrêt brutal, maintenez le bouton d’alimentation enfoncé.

* **Allumer**

    * Si la carte Raspberry Pi est éteinte mais toujours alimentée, appuyez une seule fois pour allumer à partir d'un état d'arrêt.

* Si vous utilisez un système qui ne prend pas en charge un bouton d'arrêt, vous pouvez le maintenir enfoncé pendant 5 secondes pour forcer un arrêt brutal, puis appuyer une seule fois pour allumer à partir d'un état d'arrêt.

