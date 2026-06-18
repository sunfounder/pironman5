.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_pironman5_max:

4. Configuration ou installation du logiciel
================================================

Une fois que le système est écrit sur la carte Micro SD ou le SSD NVMe, insérez-le dans l’emplacement prévu du Pironman 5 MAX. Appuyez ensuite sur le bouton d’alimentation pour allumer l’appareil.

Après la mise sous tension, vous verrez les différentes LED d’alimentation s’allumer. En revanche, l’écran OLED, les LED RGB et les Ventilateurs GPIO (les deux sur les côtés) ne fonctionneront pas encore, car une configuration est nécessaire. Si l’écran présente un affichage brouillé, ignorez-le pour l’instant ; cela sera corrigé une fois la configuration effectuée.

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



