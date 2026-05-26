.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Adaptateur USB HDMI
==========================================

.. image:: img/hdmi_adapter.jpeg

Cet adaptateur USB HDMI est spécialement conçu pour le Raspberry Pi 5. Sa fonction principale est de repositionner les connexions USB et HDMI pour qu'elles soient alignées avec le côté interface USB du Raspberry Pi, améliorant ainsi l'accessibilité et la gestion des câbles.

De plus, le port HDMI est converti en une interface HDMI Type A standard, offrant une plus grande compatibilité.

**Alimentation supplémentaire pour NVMe**

La carte dispose d'un connecteur d'alimentation 5V spécialement destiné à l'alimentation PIP du NVMe. Couplé à un connecteur d'extension, il peut être connecté à l'interface d'alimentation supplémentaire du NVMe pour fournir une puissance supplémentaire.

**Support de batterie 1220RTC**

Un support de batterie 1220RTC est intégré pour l'installation pratique d'une batterie RTC. Il se connecte à l'interface RTC du Raspberry Pi via un câble inversé SH1.0 2P.

Le support de batterie est compatible avec les batteries CR1220 et ML1220. Si vous utilisez une ML1220 (batterie au dioxyde de manganèse lithium), la charge peut être configurée directement sur le Raspberry Pi. Notez que la CR1220 n'est pas rechargeable.

**Activation de la charge d'entretien**

.. warning::

  Si vous utilisez une batterie CR1220, n'activez pas la charge d'entretien car cela pourrait causer des dommages irréparables à la batterie et risquer d'endommager la carte.

Par défaut, la fonction de charge d'entretien de la batterie est désactivée. Les fichiers ``sysfs`` indiquent la tension actuelle de charge d'entretien ainsi que les limites :

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Pour activer la charge d'entretien, ajoutez ``rtc_bbat_vchg`` à ``/boot/firmware/config.txt`` :

  * Ouvrez ``/boot/firmware/config.txt``.
  
    .. code-block:: shell
    
      sudo nano /boot/firmware/config.txt
      
  * Ajoutez ``rtc_bbat_vchg`` à ``/boot/firmware/config.txt``.
  
    .. code-block:: shell
    
      dtparam=rtc_bbat_vchg=3000000
  
Après redémarrage, le système affichera :

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

Cela confirme que la batterie est maintenant en charge d'entretien. Pour désactiver cette fonction, il suffit de supprimer la ligne ``dtparam`` du fichier ``config.txt``.
