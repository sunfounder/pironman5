.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Convertisseur de bouton d’alimentation
============================================

Ce module permet de déporter le bouton d’alimentation du Raspberry Pi 5 vers l’extérieur.

.. image:: img/power_switch_conventor.jpeg

**Ajout du bouton d’alimentation**

* Le Raspberry Pi 5 dispose d’un cavalier **J2**, situé entre le connecteur de la pile RTC et le bord de la carte. Ce point de connexion permet d’ajouter un bouton d’alimentation personnalisé au Raspberry Pi 5 en y branchant un interrupteur momentanément fermé (NO). Une brève pression sur cet interrupteur reproduit le comportement du bouton d’alimentation intégré.

   .. image:: img/pi5_j2.jpg

* Sur le Pironman 5, un **convertisseur de bouton d’alimentation** prolonge le cavalier **J2** vers un bouton externe via deux broches pogo.

   .. image:: img/power_switch_convertor.png

* Le Raspberry Pi 5 peut désormais être allumé et éteint à l’aide du bouton d’alimentation externe.

   .. image:: img/pironman_button.JPG

**Cycle d’alimentation**

Lors de la première mise sous tension du Raspberry Pi 5, celui-ci démarre automatiquement sans avoir besoin d’appuyer sur le bouton.

Si vous utilisez l’environnement de bureau Raspberry Pi Desktop, une pression brève sur le bouton d’alimentation déclenche un arrêt propre. Un menu s’affiche avec des options d’arrêt, de redémarrage ou de déconnexion. Sélectionner une option ou appuyer de nouveau sur le bouton lancera l’arrêt.

.. image:: img/button_shutdown.png

**Arrêt**

    * Si vous utilisez le système **Raspberry Pi OS Desktop**, vous pouvez appuyer deux fois rapidement sur le bouton d’alimentation pour éteindre.
    * Si vous utilisez le système **Raspberry Pi OS Lite** sans interface graphique, appuyez une seule fois sur le bouton d’alimentation pour lancer l’arrêt.
    * Pour forcer un arrêt brutal, maintenez le bouton d’alimentation enfoncé.


**Mise sous tension**

    * Si la carte Raspberry Pi est éteinte mais toujours alimentée, une pression unique suffit pour rallumer l’appareil.

.. note::

    Si vous utilisez un système ne prenant pas en charge le bouton d’arrêt, maintenez le bouton enfoncé pendant 5 secondes pour forcer l’arrêt, puis appuyez une fois pour rallumer à partir de l’état éteint.

