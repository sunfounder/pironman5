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



L'écran 4,3 pouces est noir / ne s'affiche pas ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'écran DSI 4,3 pouces est plug-and-play — aucune installation de pilote supplémentaire n'est nécessaire.

.. note::

   Le cavalier **ON/AUTO** de la carte HDMI/USB ne contrôle que la sortie audio des haut-parleurs. Il n'a **aucun effet** sur l'affichage de l'écran.

Si l'écran est noir ou ne s'affiche pas, vérifiez les points suivants :

#. Assurez-vous que le câble ruban DSI est connecté au bon port DSI du Raspberry Pi 5.

#. Vérifiez que le câble ruban est complètement inséré, que le verrou est bien enfoncé et que les contacts sont orientés dans le bon sens.

#. Exécutez la commande suivante pour confirmer si le système détecte l'écran DSI :

   .. code-block:: shell

      sudo dmesg | grep -i dsi

   Si l'écran est détecté, vous devriez voir une sortie semblable à ``DSI display found``. Si aucune sortie n'apparaît, l'écran n'est pas reconnu — revérifiez la connexion physique.


Écran HDMI externe — la barre des tâches n'apparaît que sur l'écran 4,3 pouces ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lorsque vous connectez un moniteur HDMI externe au Pironman 5 Pro MAX, la barre des tâches du bureau peut rester sur l'écran DSI 4,3 pouces intégré au lieu de passer sur l'écran externe. Cela vient du fait que le système utilise l'écran DSI comme écran principal par défaut.

Si vous souhaitez définir le moniteur HDMI comme écran principal au démarrage :

#. Créez un script de démarrage :

   .. code-block:: shell

      sudo nano /usr/local/bin/fix-primary-screen.sh

#. Ajoutez le contenu suivant au script :

   .. code-block:: bash

      #!/bin/bash
      # Check if an external HDMI monitor is connected
      if wlr-randr | grep -q "HDMI-A-1"; then
          # Turn off the DSI screen first
          wlr-randr --output DSI-1 --off
          sleep 2
          # Re-enable DSI and place it to the right of HDMI
          wlr-randr --output DSI-1 --on --right-of HDMI-A-1
      fi

#. Rendez le script exécutable :

   .. code-block:: shell

      sudo chmod +x /usr/local/bin/fix-primary-screen.sh

#. Ajoutez le script au démarrage automatique. Modifiez le fichier d'autostart de labwc :

   .. code-block:: shell

      nano ~/.config/labwc/autostart

   Ajoutez la ligne suivante (le ``&`` l'exécute en arrière-plan) :

   .. code-block:: text

      /usr/local/bin/fix-primary-screen.sh &

2. Refroidissement et ventilateurs
-----------------------------------


.. _promax_fan_faq:

Le ventilateur ne fonctionne pas ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan



Le tableau de bord n'affiche pas la vitesse du ventilateur ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Pro MAX utilise des ventilateurs personnalisés **5 broches** avec le brochage suivant : **PWM / 5V / GND / RGB Data In / RGB Data Out**.

Ces ventilateurs n'ont **pas** de broche tachymètre (retour de vitesse), le système ne peut donc pas lire le régime réel. Le fait que le tableau de bord n'affiche pas la vitesse du ventilateur est normal et attendu.

La vitesse du ventilateur est contrôlée par la courbe de température PWM native du Raspberry Pi :

* < 50 °C : arrêt (0 %)
* 50 °C et plus : vitesse basse (30 %)
* 60 °C et plus : vitesse moyenne (50 %)
* 67,5 °C et plus : vitesse élevée (70 %)
* 75 °C et plus : vitesse maximale (100 %)

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


.. _faq_customize_oled_promax:

Comment personnaliser l'écran OLED ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_customize_oled
   :end-before: end_faq_customize_oled

.. _faq_rgb_promax:

Les LEDs RGB ne fonctionnent pas ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb



Comment réveiller l'écran OLED
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pour économiser l'énergie et prolonger la durée de vie de l'écran, l'écran OLED s'éteint automatiquement après une période d'inactivité. Cela fait partie de la conception normale et n'affecte pas les fonctionnalités du produit.

.. note::

   Pour la configuration de l'écran OLED (allumer/éteindre, durée de veille, rotation, etc.), reportez-vous à :ref:`promax_view_control_dashboard` ou :ref:`promax_view_control_commands`.

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



.. _faq_piper_tts_32bit_promax:

``pip install piper-tts`` échoue avec "Could Not Find a Version" ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lors de l'installation de ``sunfounder-voice-assistant`` sur le Pironman 5 Pro MAX, vous pouvez rencontrer l'erreur suivante :

.. code-block:: text

   ERROR: Could not find a version that satisfies the requirement piper-tts==1.3.0
   ERROR: No matching distribution found for piper-tts==1.3.0

Cette erreur se produit car ``piper-tts`` 1.3.0 ne fournit que des wheels **64 bits** (``aarch64``). Si votre Raspberry Pi exécute un système d'exploitation **32 bits**, pip ne trouve pas de paquet compatible.

**Solution :** installez une version 64 bits de Raspberry Pi OS.

#. Vérifiez l'architecture actuelle de votre système :

   .. code-block:: shell

      uname -m

   * ``aarch64`` → 64 bits (aucun problème)
   * ``armv7l`` → 32 bits (mise à niveau nécessaire)

#. Utilisez `Raspberry Pi Imager <https://www.raspberrypi.com/software/>`_ pour flasher une image **64 bits** de Raspberry Pi OS sur votre support de stockage.

#. Après avoir installé l'OS 64 bits, réinstallez le logiciel ``pironman5`` et ``sunfounder-voice-assistant``.

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



Comment copier le système de la carte SD vers un SSD NVMe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copy_sd_to_nvme
   :end-before: end_faq_copy_sd_to_nvme

6. Utilisation avancée
-------------------------------


Comment retirer le film protecteur
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_remove_film
   :end-before: end_faq_remove_film

.. _promax_openssh_powershell:

Comment installer OpenSSH via PowerShell ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lorsque vous utilisez ``ssh <username>@<hostname>.local`` (ou ``ssh <username>@<IP address>``) pour vous connecter à votre Raspberry Pi, mais que le message d'erreur suivant apparaît.

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


Cela signifie que votre système d'exploitation est trop ancien et n'a pas `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ préinstallé ; vous devez suivre le tutoriel ci-dessous pour l'installer manuellement.

#. Tapez ``powershell`` dans la zone de recherche de votre bureau Windows, faites un clic droit sur ``Windows PowerShell`` et sélectionnez ``Exécuter en tant qu'administrateur`` dans le menu qui apparaît.

   .. image:: img/powershell_ssh.png
      :width: 90%


#. Utilisez la commande suivante pour installer ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Après l'installation, la sortie suivante s'affiche.

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Vérifiez l'installation à l'aide de la commande suivante.

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Le système indique maintenant que ``OpenSSH.Client`` a été installé avec succès.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        Si l'invite ci-dessus n'apparaît pas, cela signifie que votre système Windows est encore trop ancien ; il est recommandé d'installer un outil SSH tiers, comme |link_putty|.

#. Redémarrez maintenant PowerShell et continuez à l'exécuter en tant qu'administrateur. Vous pourrez alors vous connecter à votre Raspberry Pi avec la commande ``ssh``, où vous serez invité à saisir le mot de passe défini précédemment.

   .. image:: img/powershell_login.png


Si je configure OMV, puis-je toujours utiliser les fonctions du Pironman5 ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Oui, OpenMediaVault est installé sur le système Raspberry Pi. Veuillez suivre les étapes de :ref:`promax_set_up_pi_os` pour poursuivre la configuration.


La caméra du Raspberry Pi ne fonctionne pas ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lorsque la caméra ne fonctionne pas, 90 % des problèmes sont liés à la connexion du câble ruban ou au matériel de la caméra lui-même.

Tout d'abord, utilisez ``rpicam-hello --list-cameras`` pour confirmer si la caméra est détectée. Si elle est détectée, vous devriez voir un message semblable à ceci :

.. code-block:: bash

   Available cameras
   -----------------
   0 : ov5647 [2592x1944] (/base/axi/pcie@1000120000/rp1/i2c@88000/ov5647@36)

Si la caméra n'est pas détectée, vérifiez si le câble ruban est inversé ou mal inséré. Si le problème persiste, essayez de remplacer le câble ruban ou le module caméra pour un test croisé.


Puis-je installer Home Assistant OS sur le Pironman 5 Pro MAX ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Pironman 5 Pro MAX ne dispose pas de son propre module complémentaire Home Assistant dédié. Cependant, vous pouvez utiliser le module complémentaire **Pironman 5 MAX** à la place — suivez le `guide du dépôt des modules complémentaires SunFounder <https://docs.sunfounder.com/projects/pironman5/en/latest/pironman5_max/set_up/set_up_home_assistant.html#add-the-sunfounder-add-ons-repository>`_.

Soyez conscient des limitations suivantes :

* **Écran 4,3 pouces** : Home Assistant OS est un système **lite** sans environnement de bureau. L'écran 4,3 pouces intégré au Pro MAX n'affichera rien.

* **Deux SSD NVMe du module NVMe PIP** : Home Assistant OS ne peut pas lire les deux SSD NVMe du module NVMe PIP double du Pro MAX.

* **Écran OLED et LEDs RGB** : ces composants fonctionnent normalement après l'installation du module complémentaire — aucune configuration supplémentaire n'est nécessaire.

* **Ventilateur CPU** : le ventilateur CPU nécessite une configuration manuelle pour fonctionner sous Home Assistant OS. Ajoutez ce qui suit dans ``/boot/firmware/config.txt`` :

  .. code-block:: text

     dtparam=cooling_fan=on
     dtparam=fan_temp0=40000
     dtparam=fan_temp0_hyst=10000
     dtparam=fan_temp0_speed=125

  Après avoir enregistré et redémarré, le ventilateur CPU sera contrôlé par le système Raspberry Pi en fonction de la température du CPU. Vous pouvez également le contrôler manuellement via les commandes ``pinctrl`` — voir :ref:`promax_fan_faq`.
