.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d’autres passionnés pour approfondir vos connaissances sur Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes techniques et après-vente avec l’aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Soyez informé(e) en avant-première des annonces et démonstrations de nouveaux produits.
    - **Réductions spéciales** : Profitez d’offres exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des jeux-concours et promotions pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _max_set_up_pironman5:

4. Configuration ou installation du logiciel
================================================

Une fois que le système est écrit sur la carte Micro SD ou le SSD NVMe, insérez-le dans l’emplacement prévu du Pironman 5 MAX. Appuyez ensuite sur le bouton d’alimentation pour allumer l’appareil.

Après la mise sous tension, vous verrez les différentes LED d’alimentation s’allumer. En revanche, l’écran OLED, les LED RGB et les ventilateurs RGB (les deux sur les côtés) ne fonctionneront pas encore, car une configuration est nécessaire. Si l’écran présente un affichage brouillé, ignorez-le pour l’instant ; cela sera corrigé une fois la configuration effectuée.

Avant de configurer, vous devez démarrer et vous connecter à votre Raspberry Pi. Si vous ne savez pas comment procéder, vous pouvez consulter le site officiel Raspberry Pi : |link_rpi_get_start|.

Vous pouvez ensuite sélectionner le tutoriel de configuration adapté à votre système.


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_umbrel

.. set_up_batocera


**À propos du bouton d’alimentation**

Le bouton d’alimentation est relié au bouton de mise sous tension du Raspberry Pi 5 et fonctionne de la même manière.

* **Extinction**

    * Si vous utilisez le système **Raspberry Pi OS Desktop**, vous pouvez appuyer deux fois rapidement sur le bouton d’alimentation pour éteindre.
    * Si vous utilisez le système **Raspberry Pi OS Lite** sans interface graphique, appuyez une seule fois sur le bouton d’alimentation pour lancer l’arrêt.
    * Pour forcer un arrêt brutal, maintenez le bouton d’alimentation enfoncé.

* **Allumage**

    * Si le Raspberry Pi est éteint mais toujours alimenté, appuyez une fois sur le bouton pour le rallumer.

* Si votre système ne prend pas en charge l’extinction via le bouton, maintenez-le enfoncé pendant 5 secondes pour forcer l’arrêt, puis une pression unique pour rallumer.



