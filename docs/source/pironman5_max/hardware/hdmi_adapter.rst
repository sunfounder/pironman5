.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 ! Rejoignez d'autres passionnés pour approfondir vos connaissances sur le Raspberry Pi, l’Arduino et l’ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Résolvez les problèmes après-vente et relevez les défis techniques grâce à l’aide de notre équipe et de notre communauté.
    - **Apprendre et partager** : Échangez des conseils et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et à des présentations exclusives.
    - **Réductions spéciales** : Bénéficiez de remises exclusives sur nos nouveautés.
    - **Promotions festives et cadeaux** : Participez à des jeux-concours et à des offres spéciales lors d’événements saisonniers.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

Adaptateur USB HDMI
==========================================

.. image:: img/hdmi_adapter.jpeg

Cette carte adaptateur USB HDMI est spécialement conçue pour le Raspberry Pi 5. Sa fonction principale est de repositionner les connexions USB et HDMI du côté des interfaces USB du Raspberry Pi, ce qui améliore l’accessibilité et la gestion des câbles.

De plus, le port HDMI est converti en interface HDMI Type A standard, offrant une compatibilité plus large.

**Alimentation supplémentaire pour NVMe**

La carte est équipée d’un connecteur d’alimentation 5V dédié à l’alimentation du NVMe PIP. Associé à un connecteur d’extension, il permet de relier l’alimentation supplémentaire du module NVMe pour une alimentation renforcée.

**Support de batterie RTC 1220**

Un support pour batterie RTC 1220 est intégré, facilitant l’installation d’une batterie pour l’horloge temps réel. Il se connecte à l’interface RTC du Raspberry Pi via un câble inversé SH1.0 2P.

Le support est compatible avec les batteries CR1220 et ML1220. Si vous utilisez une ML1220 (batterie lithium-dioxyde de manganèse), la recharge peut être configurée directement sur le Raspberry Pi. À noter que la CR1220 n’est pas rechargeable.

**Activation de la charge d’entretien (Trickle Charging)**

.. warning::

  Si vous utilisez une batterie CR1220, n’activez pas la charge d’entretien car cela pourrait endommager irréversiblement la batterie et le circuit.

Par défaut, la fonction de charge d’entretien est désactivée. Les fichiers ``sysfs`` permettent de consulter la tension et les limites actuelles de charge :

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Pour activer la charge d’entretien, ajoutez ``rtc_bbat_vchg`` dans ``/boot/firmware/config.txt`` :

  * Ouvrez le fichier ``/boot/firmware/config.txt``.
  
    .. code-block:: shell
    
      sudo nano /boot/firmware/config.txt
      
 * Ajoutez ``rtc_bbat_vchg`` dans ``/boot/firmware/config.txt``.
  
    .. code-block:: shell
    
      dtparam=rtc_bbat_vchg=3000000
  
Après le redémarrage, le système affichera :

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Cela confirme que la batterie est désormais en charge d’entretien. Pour désactiver cette fonctionnalité, il suffit de supprimer la ligne ``dtparam`` du fichier ``config.txt``.

