.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

FAQ
============


Dépannage rapide
-------------------------------

* Le bouton d'alimentation ne fonctionne pas → :ref:`faq_power_button_not_work_promax`
* L'écran OLED ne fonctionne pas → :ref:`faq_oled_promax`
* Les LEDs RGB ne fonctionnent pas → :ref:`faq_rgb_promax`
* Le ventilateur ne fonctionne pas → :ref:`promax_fan_faq`
* Le tableau de bord n'affiche aucune donnée → :ref:`faq_dashboard_promax`
* SSD NVMe non détecté → :ref:`faq_nvme_promax`
* SSD NVMe détecté mais provoque un redémarrage du système → :ref:`faq_nvme_link_down_promax`
* Le PI5 ne démarre pas → :ref:`faq_pi5_boot_fail_promax`



1. Matériel
-------------------------------


.. _com_os_promax:

Systèmes compatibles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os


.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_promax`

Bouton d'alimentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button
   :end-before: end_faq_power_button


.. _faq_power_button_not_work_promax:

Le bouton d'alimentation ne fonctionne pas ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button_not_work
   :end-before: end_faq_power_button_not_work


Extrémités des tubes en cuivre du refroidisseur tour
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copper_pipe_ends
   :end-before: end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Raspberry Pi AI HAT+ n'est pas compatible avec le Pironman 5 Pro MAX.

.. image:: img/output3.png
    :width: 400

Le Raspberry Pi AI Kit combine le Raspberry Pi M.2 HAT+ et le module accélérateur AI Hailo.

.. image:: img/output2.jpg
    :width: 400

Vous pouvez détacher le module accélérateur AI Hailo du Raspberry Pi AI Kit et l'insérer directement dans le HAT du Pironman 5 Pro MAX.



2. Refroidissement et ventilateurs
-----------------------------------


.. _promax_fan_faq:

Le ventilateur ne fonctionne pas ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan



3. OLED et RGB
-------------------------------


.. _faq_oled_promax:

L'écran OLED ne fonctionne pas ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_compatible_systems| replace:: :ref:`com_os_promax`
.. |link_set_up_pironman5| replace:: :ref:`promax_set_up_pironman5`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_oled
   :end-before: end_faq_oled


.. _faq_rgb_promax:

Les LEDs RGB ne fonctionnent pas ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb



4. Tableau de bord et logiciel
-------------------------------


.. _faq_dashboard_promax:

Le tableau de bord n'affiche aucune donnée
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard


Comment désactiver le tableau de bord web
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_dashboard| replace:: :ref:`promax_view_control_dashboard`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_disable_dashboard
   :end-before: end_faq_disable_dashboard


Comment désinstaller et réinstaller le logiciel Pironman 5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_reinstall_pironman5
   :end-before: end_faq_reinstall_pironman5


.. |link_view_control_commands| replace:: :ref:`promax_view_control_commands`

Comment contrôler les composants en utilisant la commande ``pironman5``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command



5. Démarrage et stockage
-------------------------------


.. _faq_pi5_boot_fail_promax:

Le PI5 ne démarre pas (LED rouge) ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ce problème peut être causé par une mise à jour du système, une modification de l'ordre de démarrage ou un chargeur d'amorçage corrompu. Vous pouvez essayer les étapes suivantes pour résoudre le problème :

#. Rebranchez l'alimentation et vérifiez si le PI5 démarre correctement.

#. Testez le PI5 à l'extérieur du boîtier

   * Retirez le PI5 du boîtier Pironman 5 Pro MAX.
   * Alimentez le PI5 directement avec l'adaptateur secteur (sans le boîtier).
   * Vérifiez s'il peut démarrer normalement.

#. Restaurez le chargeur d'amorçage

   * Si le PI5 ne démarre toujours pas, le chargeur d'amorçage peut être corrompu. Vous pouvez suivre ce guide : :ref:`update_bootloader_promax` et choisir de démarrer depuis la carte SD ou NVMe/USB.
   * Insérez la carte SD préparée dans le PI5, allumez-le et attendez au moins 10 secondes. Une fois la restauration terminée, retirez et reformatez la carte SD.
   * Ensuite, utilisez Raspberry Pi Imager pour flasher la dernière version de Raspberry Pi OS et essayez de démarrer à nouveau.


.. _faq_nvme_promax:

Le module NVMe PIP ne fonctionne pas ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_install_the_os_promax| replace:: :ref:`install_the_os_promax`

#. Confirmez que votre SSD NVMe est compatible. Référez-vous à la :ref:`liste des SSD NVMe compatibles <compitable_nvme_ssd_5>` pour les disques vérifiés, stables et compatibles.

#. Assurez-vous que le câble FPC connectant le module NVMe PIP au Raspberry Pi 5 est solidement fixé.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Votre navigateur ne prend pas en charge la balise vidéo.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Votre navigateur ne prend pas en charge la balise vidéo.
           </video>
       </div>

#. Confirmez que votre SSD est correctement fixé au module NVMe PIP.

#. Vérifiez l'état des LEDs du module NVMe PIP :

   Après avoir confirmé toutes les connexions, allumez l'appareil et observez les deux indicateurs sur le module NVMe PIP :

   * **PWR LED** : Doit être allumée.
   * **STA LED** : Doit clignoter pour indiquer un fonctionnement normal.

   .. image:: img/nvme_pip_leds.png

   * Si la **PWR LED** est allumée mais que la **STA LED** ne clignote pas, le SSD NVMe n'est pas reconnu par le Raspberry Pi.
   * Si la **PWR LED** est éteinte, court-circuitez les broches ``Force Enable`` (J4). Si la **PWR LED** s'allume après le court-circuit, le problème peut provenir d'un câble FPC desserré ou d'une configuration système non prise en charge pour NVMe.

     .. image:: img/nvme_pip_j4.png

#. Confirmez que votre SSD NVMe a un système d'exploitation correctement installé. Référez-vous à |link_install_the_os_promax|.

#. Si le problème persiste, veuillez nous envoyer le fichier journal suivant :

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log


.. _faq_nvme_link_down_promax:

SSD NVMe détecté mais provoque un redémarrage du système en lecture/écriture ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_nvme_link_down
   :end-before: end_faq_nvme_link_down


Comment modifier l'ordre de démarrage du Raspberry Pi en utilisant des commandes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_command
   :end-before: end_faq_boot_order_command


Comment modifier l'ordre de démarrage avec Raspberry Pi Imager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_update_bootloader| replace:: :ref:`update_bootloader_promax`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_imager
   :end-before: end_faq_boot_order_imager



6. Utilisation avancée
-------------------------------


Comment retirer le film protecteur
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_remove_film
   :end-before: end_faq_remove_film
