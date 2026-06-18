.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

FAQ
============


Dépannage rapide
-------------------------------

* Le bouton d'alimentation ne fonctionne pas → :ref:`faq_power_button_not_work_max`
* L'écran OLED ne fonctionne pas → :ref:`faq_oled_max`
* Les LED RGB ne fonctionnent pas → :ref:`faq_rgb_max`
* Les ventilateurs GPIO ne fonctionnent pas → :ref:`faq_gpio_fans_max`
* Le ventilateur CPU ne tourne pas → :ref:`faq_pwm_fan_max`
* Le tableau de bord n'affiche aucune donnée → :ref:`faq_dashboard_max`
* Le SSD NVMe n'est pas détecté → :ref:`faq_nvme_max`
* Le SSD NVMe est détecté mais provoque un redémarrage système → :ref:`faq_nvme_link_down_max`



1. Matériel
-------------------------------


.. _com_os_max:

Systèmes compatibles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os

Bouton d'alimentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button
   :end-before: end_faq_power_button


.. _faq_power_button_not_work_max:

Le bouton d'alimentation ne fonctionne pas ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button_not_work
   :end-before: end_faq_power_button_not_work


Extrémités des caloducs en cuivre du refroidisseur tour
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copper_pipe_ends
   :end-before: end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Raspberry Pi AI HAT+ n'est pas compatible avec le Pironman 5 MAX.

.. image:: img/output3.png
    :width: 400

Le kit Raspberry Pi AI combine le Raspberry Pi M.2 HAT+ et le module accélérateur IA Hailo.

.. image:: img/output2.jpg
    :width: 400

Vous pouvez détacher le module accélérateur IA Hailo du kit Raspberry Pi AI et l'insérer directement dans le module NVMe PIP du Pironman 5 MAX.

Puis-je utiliser la fonction d'interrupteur à vibration du Pironman5 Max ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

À partir de la version v1.3.6, le réveil de l'OLED utilise le bouton d'alimentation. Vous devez retirer le cavalier de l'interrupteur à vibration pour éviter d'occuper les broches GPIO du Raspberry Pi et prévenir d'éventuels conflits. Veuillez vérifier si ce cavalier est présent ; si ce n'est pas le cas, veuillez ignorer cet avis.

.. image:: /pironman5_max/img/remove_vib_jumper.jpg

2. Refroidissement et ventilateurs
-----------------------------------------------

.. _faq_pwm_fan_max:

Le ventilateur CPU ne tourne pas ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan


.. _faq_gpio_fans_max:

Les ventilateurs GPIO ne fonctionnent pas ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_gpio_fans
   :end-before: end_faq_gpio_fans


3. OLED et RGB
-------------------------------


.. _faq_oled_max:

L'écran OLED ne fonctionne pas ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_compatible_systems| replace:: :ref:`com_os_max`
.. |link_set_up_pironman5| replace:: :ref:`set_up_pironman5_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_oled
   :end-before: end_faq_oled

.. _faq_rgb_max:

Les LED RGB ne fonctionnent pas ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb


.. _faq_customize_oled_max:

Comment personnaliser l'affichage OLED ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_customize_oled
   :end-before: end_faq_customize_oled


4. Tableau de bord et logiciel
-------------------------------


.. _faq_dashboard_max:

Le tableau de bord n'affiche aucune donnée
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard

Comment désactiver le tableau de bord web
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_disable_dashboard
   :end-before: end_faq_disable_dashboard


Comment désinstaller et réinstaller le logiciel Pironman 5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_reinstall_pironman5
   :end-before: end_faq_reinstall_pironman5


Comment contrôler les composants avec la commande ``pironman5``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_commands| replace:: :ref:`max_view_control_commands`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command


5. Démarrage et stockage
-------------------------------

Si je configure OMV, puis-je toujours utiliser les fonctions du Pironman5 ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Oui, OpenMediaVault est configuré sur le système Raspberry Pi. Veuillez suivre les étapes de :ref:`set_up_os_max` pour continuer la configuration.


Le PI5 ne démarre pas (LED rouge) ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_update_bootloader| replace:: :ref:`update_bootloader_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pi5_boot_fail
   :end-before: end_faq_pi5_boot_fail

.. _faq_nvme_max:

Le module NVMe PIP ne fonctionne pas ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_install_the_os_dual| replace:: :ref:`install_the_os_max`

.. start_faq_nvme_pip_dual

#. Confirmez que votre SSD NVMe est compatible. Consultez la :ref:`liste des SSD NVMe compatibles <compitable_nvme_ssd_5>` pour des disques vérifiés, stables et compatibles.

#. Assurez-vous que le câble FPC reliant le module NVMe PIP au Raspberry Pi 5 est bien fixé.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(1)-11.mp4" type="video/mp4">
               Votre navigateur ne prend pas en charge la balise vidéo.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(2)-11.mp4" type="video/mp4">
               Votre navigateur ne prend pas en charge la balise vidéo.
           </video>
       </div>

#. Vérifiez que votre SSD est correctement fixé au module NVMe PIP.

#. Vérifiez l'état des LED du module NVMe PIP :

   Après avoir vérifié toutes les connexions, mettez l'appareil sous tension et observez les deux indicateurs sur le module NVMe PIP :

   * **LED PWR** : Doit être allumée.
   * **LED STA** : Doit clignoter pour indiquer un fonctionnement normal.

   .. image:: img/dual_nvme_pip_leds.png

   * Si la **LED PWR** est allumée mais que la **LED STA** ne clignote pas, cela indique que le SSD NVMe n'est pas reconnu par le Raspberry Pi.
   * Si la **LED PWR** est éteinte, court-circuitez les broches « Force Enable » sur le module. Si la **LED PWR** s'allume, cela peut indiquer un câble FPC mal connecté ou une configuration système non prise en charge pour le NVMe.

   .. image:: img/dual_nvme_pip_j4.png


#. Vérifiez que votre SSD NVMe dispose d'un système d'exploitation correctement installé. Reportez-vous à |link_install_the_os_dual|.

.. end_faq_nvme_pip_dual

#. Si le problème persiste, veuillez nous envoyer le fichier journal suivant :

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log


.. _faq_nvme_link_down_max:

Le SSD NVMe est détecté mais provoque un redémarrage du système en lecture/écriture ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_nvme_link_down
   :end-before: end_faq_nvme_link_down

Comment modifier l'ordre de démarrage du Raspberry Pi avec des commandes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_command
   :end-before: end_faq_boot_order_command


Comment modifier l'ordre de démarrage avec Raspberry Pi Imager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_imager
   :end-before: end_faq_boot_order_imager

Comment copier le système de la carte SD vers un SSD NVMe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copy_sd_to_nvme
   :end-before: end_faq_copy_sd_to_nvme

6. Utilisation avancée
-------------------------------

Comment retirer le film protecteur
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_remove_film
   :end-before: end_faq_remove_film
