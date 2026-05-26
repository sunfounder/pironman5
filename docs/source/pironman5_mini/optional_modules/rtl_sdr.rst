.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


RTL-SDR Blog V4  
==============================================

.. note::

    Les produits de la série Pironman 5 n’incluent pas le module suivant.  
    Vous devez en préparer un vous-même ou l’acheter sur notre site officiel :

    * `RTL-SDR Blog V4 <https://www.sunfounder.com/products/rtl-sdr-blog-v4>`_

Ce guide couvre une procédure d’installation fiable pour le RTL-SDR Blog V4, un récepteur radio défini par logiciel (SDR) USB populaire et abordable.  
La version V4 intègre un tuner R828D amélioré, un mode d’échantillonnage direct, une meilleure sensibilité, et un bias-tee intégré pour alimenter les antennes actives.  
Il fonctionne très bien pour recevoir la FM diffusée, les bandes aéronautiques, la radio amateur, l’ADS-B et de nombreux autres signaux sous Linux et Raspberry Pi.

Pour la documentation du fabricant d’origine, voir le guide officiel RTL-SDR Blog V4 : https://www.rtl-sdr.com/V4/

----

Installer le pilote pour RTL-SDR Blog V4  
------------------------------------------------

**0. Préparation**

.. code-block:: shell

   sudo apt update
   sudo apt install -y git cmake build-essential pkg-config libusb-1.0-0-dev sox

Note :  
    ``sox`` (qui fournit la commande ``play``) est inclus pour les tests audio directs.

**1. Nettoyage complet des anciennes bibliothèques et binaires (critique)**

.. code-block:: shell

   sudo apt purge -y 'librtlsdr*'
   sudo rm -rf /usr/lib/librtlsdr* /usr/include/rtl-sdr* \
               /usr/local/lib/librtlsdr* /usr/local/include/rtl-sdr* \
               /usr/local/include/rtl_* /usr/local/bin/rtl_*
   sudo ldconfig

Vérification A :

.. code-block:: shell

   ldconfig -p | grep rtlsdr || echo "OK: No librtlsdr found in system cache."

**2. Compiler et installer le pilote RTL-SDR Blog V4**

.. code-block:: shell

   cd ~
   git clone https://github.com/rtlsdrblog/rtl-sdr-blog.git
   cd rtl-sdr-blog
   mkdir build && cd build
   cmake .. -DINSTALL_UDEV_RULES=ON
   make
   sudo make install
   sudo cp ../rtl-sdr.rules /etc/udev/rules.d/
   sudo ldconfig

Vérification B :

.. code-block:: shell

   which rtl_test
   ldd "$(which rtl_test)" | grep rtlsdr   # Doit pointer vers /usr/local/lib/librtlsdr.so

**3. Désactiver le module noyau DVB et redémarrer**

.. code-block:: shell

   echo 'blacklist dvb_usb_rtl28xxu' | sudo tee /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf
   sudo reboot

Note :  
    Les commandes de rechargement immédiat (``udevadm control --reload-rules`` et ``udevadm trigger``)  
    sont optionnelles si vous prévoyez de redémarrer immédiatement.

**4. Vérifier le pilote après redémarrage**

.. code-block:: shell

   rtl_test -t

Attendu :  
    La sortie doit inclure ``RTL-SDR Blog V4 Detected`` sans messages ``[R82XX] PLL not locked!``.  
    La ligne ``Using device 0: Generic RTL2832U OEM`` est normale — il s’agit simplement du nom USB.

**6. Tester la réception FM depuis la ligne de commande**

.. code-block:: shell

   rtl_fm -f 97.1M -M wbfm -s 180000 -r 48000 -g 28 | play -t raw -r 48k -e s -b 16 -c 1 -

Astuces :

    * ``-g`` : Essayez entre 25–35 dB ; plus n’est pas toujours mieux.  
    * Réduisez ``-s`` à ~170k–180k pour diminuer le bruit.  
    * Ajustez légèrement la fréquence (par ex. ``97.1005M``) pour un réglage fin.  
    * Fermez tout autre logiciel SDR susceptible de monopoliser l’appareil.

----

Installer les logiciels radio courants  
-------------------------------------------------

Cette section présente quatre applications SDR largement utilisées, avec de courtes descriptions, des instructions d’installation et des conseils de configuration de base pour les systèmes basés sur Debian.

* :ref:`install_gqrx_mini`
* :ref:`install_sdrpp_mini`
* :ref:`install_rtl433_mini`
* :ref:`install_dump1090_mini`


----

.. _install_gqrx_mini:

GQRX  
^^^^^^^^^^^^

GQRX est une application SDR simple et conviviale avec une interface graphique. Elle prend en charge une large gamme d’appareils SDR et est idéale pour écouter la FM, l’AM, la BLU (SSB) et d’autres signaux avec un affichage en temps réel du spectre et de la cascade.

Vous pouvez également consulter le guide officiel d’installation pour Raspberry Pi ici : https://www.gqrx.dk/download/gqrx-sdr-for-the-raspberry-pi

**Option 1 – Installation rapide (recommandée pour la plupart des utilisateurs)**

Rapide, simple, et intégrée aux mises à jour système — mais peut ne pas être la dernière version.

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends gqrx-sdr

**Option 2 – Compilation depuis la source (optionnelle, dernières fonctionnalités)**

Garantit la dernière version et une personnalisation complète, mais prend plus de temps à compiler et nécessite davantage de dépendances.

.. code-block:: shell

   sudo apt update

   sudo apt-get install -y --no-install-recommends \
     cmake gnuradio-dev gr-osmosdr qt6-base-dev qt6-svg-dev \
     libasound2-dev libjack-jackd2-dev portaudio19-dev libpulse-dev

   git clone https://github.com/gqrx-sdr/gqrx.git
   cd gqrx
   mkdir build && cd build
   cmake ..
   make
   sudo make install

**Prévenir l’écrasement du pilote**

Lors de l’installation de GQRX, SDR++, gnuradio-dev ou gr-osmosdr, le système peut réinstaller une version obsolète de ``librtlsdr``.  
Après chaque installation, vérifiez :

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si cela ne pointe plus vers ``/usr/local/lib/librtlsdr.so``, exécutez :

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


Vous pouvez tester immédiatement (ou après un redémarrage pour un environnement propre) :

.. code-block:: shell

   rtl_test -t

Sortie attendue :

   * Contient RTL-SDR Blog V4 Detected.  
   * Aucun message [R82XX] PLL not locked!.

**Configuration au premier lancement**

* **Périphériques d’E/S** :

  * Appareil : ``RTL-SDR (V4)``.  
  * Débit d’entrée : ``1.8 MSPS`` (1800000).

* **Contrôles d’entrée** :

  * **Gain LNA** : Commencez autour de 25–35 dB, ajustez selon besoin.

* **Options du récepteur** :

  * Définir la correction de fréquence (PPM) issue de votre calibration.  
  * Mode : ``WFM (mono ou stéréo)`` pour la FM diffusée.

----

.. _install_sdrpp_mini:

SDR++ (SDRpp)  
^^^^^^^^^^^^^

SDR++ est un logiciel SDR moderne, rapide et multiplateforme qui prend en charge une variété d’appareils, y compris le RTL-SDR Blog V4. Il offre une interface claire et conviviale, une large prise en charge des modulations, un filtrage DSP avancé et des capacités d’enregistrement.

Vous pouvez consulter le manuel officiel ici : https://www.sdrpp.org/manual.pdf

**Installer depuis la source**

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends build-essential cmake git pkg-config \
     libfftw3-dev libvolk2-dev libglfw3-dev libglew-dev \
     libzstd-dev librtaudio-dev

   git clone https://github.com/AlexandreRouma/SDRPlusPlus
   cd SDRPlusPlus
   mkdir build && cd build
   cmake .. -DOPT_BUILD_RTL_SDR_SOURCE=ON
   make
   sudo make install

**Prévenir l’écrasement du pilote**

Lors de l’installation de GQRX, SDR++, gnuradio-dev ou gr-osmosdr, le système peut réinstaller une version obsolète de ``librtlsdr``.  
Après chaque installation, vérifiez :

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si cela ne pointe plus vers ``/usr/local/lib/librtlsdr.so``, exécutez :

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


Vous pouvez tester immédiatement (ou après un redémarrage pour un environnement propre) :

.. code-block:: shell

   rtl_test -t

Sortie attendue :

   * Contient RTL-SDR Blog V4 Detected.  
   * Aucun message [R82XX] PLL not locked!.

**Notes au premier lancement :**

Après l’installation, SDR++ apparaîtra dans le menu de votre bureau (généralement sous "Autre"), ou vous pouvez exécuter :

   .. code-block:: shell

      sdrpp

* **Appareil :** Sélectionnez **RTL-SDR (V4)** dans le menu **Source**.  
* **Débit d’échantillonnage :** 1.8 MSPS est typique ; réduisez si la charge CPU est élevée.  
* **Gain :** Désactivez l’AGC et définissez le gain manuel (commencez ~35 dB).  
* **Correction PPM :** Entrez la valeur de calibration issue de ``rtl_test -p``.  
* **Mode de démodulation :** Choisissez WFM pour la FM, SSB pour les bandes radioamateurs, etc.

----

.. _install_rtl433_mini:

rtl_433  
^^^^^^^^^^^^

rtl_433 est un outil en ligne de commande pour décoder les transmissions radio de dispositifs fonctionnant dans la bande ISM 433 MHz, tels que les stations météo, les capteurs de pression des pneus et les thermomètres sans fil.

**Installation :**

.. code-block:: shell

   sudo apt install -y rtl-433

**Prévenir l’écrasement du pilote**

Lors de l’installation de GQRX, SDR++, gnuradio-dev ou gr-osmosdr, le système peut réinstaller une version obsolète de ``librtlsdr``.  
Après chaque installation, vérifiez :

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si cela ne pointe plus vers ``/usr/local/lib/librtlsdr.so``, exécutez :

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


Vous pouvez tester immédiatement (ou après un redémarrage pour un environnement propre) :

.. code-block:: shell

   rtl_test -t

Sortie attendue :

   * Contient RTL-SDR Blog V4 Detected.  
   * Aucun message [R82XX] PLL not locked!.

**Utilisation de base :**

* Exécutez ``rtl_433`` pour détecter et décoder automatiquement les dispositifs courants en 433 MHz.  
* Utilisez ``rtl_433 -G`` pour lister tous les protocoles pris en charge.

----

.. _install_dump1090_mini:

dump1090-mutability  
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutability est un décodeur Mode S pour les données transpondeur ADS-B des avions. Il reçoit et décode les positions, vitesses et autres données de vol des avions, et peut fournir une carte en direct via un navigateur web.

**Installation :**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

**Prévenir l’écrasement du pilote**

Lors de l’installation de GQRX, SDR++, gnuradio-dev ou gr-osmosdr, le système peut réinstaller une version obsolète de ``librtlsdr``.  
Après chaque installation, vérifiez :

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si cela ne pointe plus vers ``/usr/local/lib/librtlsdr.so``, exécutez :

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


Vous pouvez tester immédiatement (ou après un redémarrage pour un environnement propre) :

.. code-block:: shell

   rtl_test -t

Sortie attendue :

   * Contient RTL-SDR Blog V4 Detected.  
   * Aucun message [R82XX] PLL not locked!.

**Utilisation de base :**

* Exécutez : ``dump1090 --interactive --net``.  
* Ouvrez ``http://<raspberrypi-ip>:8080`` dans votre navigateur pour visualiser le suivi en direct des avions.



