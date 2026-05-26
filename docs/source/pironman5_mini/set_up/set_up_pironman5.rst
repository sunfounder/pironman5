.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_pironman5_mini:

4. Configuration ou installation du logiciel
================================================

Une fois le système écrit sur la carte Micro SD ou le SSD NVMe, insérez-le dans l’emplacement prévu du Raspberry Pi. Ensuite, appuyez sur le bouton d’alimentation pour démarrer l’appareil.

Après la mise sous tension, les différentes LED d’alimentation s’allumeront. Toutefois, les LED RGB et le ventilateur RGB ne fonctionneront pas encore, car ils nécessitent une configuration préalable. Si l’écran présente des artefacts ou du brouillage, ne vous en inquiétez pas : cela sera corrigé après configuration.

Avant toute configuration, vous devez démarrer et vous connecter à votre Raspberry Pi. Si vous ne savez pas comment procéder, vous pouvez consulter le site officiel du Raspberry Pi : |link_rpi_get_start|.

Vous pouvez ensuite choisir le tutoriel de configuration en fonction de votre système.


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_umbrel
    set_up_batocera

**À propos du bouton d’alimentation**

Le bouton d’alimentation reprend la fonctionnalité du bouton physique du Raspberry Pi 5 et agit de manière identique.

* **Arrêt**

    * Si vous utilisez le système **Raspberry Pi OS Desktop**, vous pouvez appuyer deux fois rapidement sur le bouton d’alimentation pour éteindre.
    * Si vous utilisez le système **Raspberry Pi OS Lite** sans interface graphique, appuyez une seule fois sur le bouton d’alimentation pour lancer l’arrêt.
    * Pour forcer un arrêt brutal, maintenez le bouton d’alimentation enfoncé.

* **Allumage**

    * Si la carte Raspberry Pi est éteinte mais toujours alimentée, une pression suffit pour la rallumer.

* Si votre système ne prend pas en charge le bouton d’arrêt, vous pouvez maintenir le bouton appuyé pendant 5 secondes pour forcer l’arrêt, puis effectuer une simple pression pour redémarrer l’appareil.



