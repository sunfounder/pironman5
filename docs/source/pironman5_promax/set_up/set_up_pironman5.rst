
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _promax_set_up_pironman5:

4. Configurer ou installer le logiciel
================================================

Maintenant que le système a été écrit sur la carte Micro SD ou le SSD NVMe, vous pouvez les insérer dans l'emplacement du Pironman 5 Pro MAX. Appuyez ensuite sur le bouton d'alimentation pour allumer l'appareil.

Après la mise sous tension, vous verrez les différentes LEDs d'alimentation s'allumer, mais l'écran OLED, les LEDs RGB et les Ventilateurs GPIO (les deux ventilateurs sur le côté) ne fonctionneront pas encore, car ils doivent être configurés. S'il y a un problème d'affichage avec l'écran, veuillez l'ignorer pour l'instant ; il sera résolu après la configuration.

Avant de configurer, vous devez démarrer et vous connecter à votre Raspberry Pi. Si vous ne savez pas comment vous connecter, vous pouvez visiter le site officiel de Raspberry Pi : |link_rpi_get_start|.

Vous pouvez ensuite sélectionner le tutoriel de configuration en fonction de votre système.

.. toctree::
    :maxdepth: 1

    set_up_rpi_os
    set_up_umbrel

.. set_up_batocera

.. set_up_home_assistant

**À propos du bouton d'alimentation**

Le bouton d'alimentation prolonge le bouton d'alimentation du Raspberry Pi 5 et fonctionne exactement comme le bouton d'alimentation du Raspberry Pi 5.

* **Arrêt**

    * Si vous exécutez le système **Raspberry Pi OS Desktop**, vous pouvez appuyer deux fois rapidement sur le bouton d'alimentation pour éteindre.
    * Si vous exécutez le système **Raspberry Pi OS Lite**, appuyez une seule fois sur le bouton d'alimentation pour initier un arrêt.
    * Pour forcer un arrêt brutal, maintenez le bouton d'alimentation enfoncé.

* **Mise sous tension**

    * Si la carte Raspberry Pi est éteinte, mais toujours alimentée, une seule pression permet de l'allumer à partir de l'état éteint.

* Si vous exécutez un système qui ne prend pas en charge un bouton d'arrêt, vous pouvez le maintenir enfoncé pendant 5 secondes pour forcer un arrêt brutal, et une seule pression pour l'allumer à partir de l'état éteint.
