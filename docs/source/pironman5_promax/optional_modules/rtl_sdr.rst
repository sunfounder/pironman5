
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message




RTL-SDR Blog V4
==============================================

.. note::

    Les produits de la série Pironman 5 n'incluent pas les modules suivants.
    Vous devez en préparer un vous-même ou l'acheter sur notre site officiel :

    * `RTL-SDR Blog V4 <https://www.sunfounder.com/products/rtl-sdr-blog-v4>`_

Ce guide couvre une procédure d'installation fiable pour le RTL-SDR Blog V4, un récepteur radio logicielle (SDR) USB populaire et abordable.
La version V4 dispose d'un tuner R828D amélioré, d'un mode d'échantillonnage direct, d'une meilleure sensibilité et d'un bias-tee intégré pour alimenter les antennes actives.
Il fonctionne bien pour recevoir la FM de diffusion, la bande aérienne, la radio amateur, l'ADS-B et de nombreux autres signaux sur les systèmes Linux et Raspberry Pi.

Pour la documentation originale du fabricant, consultez le guide officiel du RTL-SDR Blog V4 : https://www.rtl-sdr.com/V4/

----

Installer le pilote pour RTL-SDR Blog V4
-------------------------------------------------------------

Sous Linux, la procédure est également simple : il suffit de supprimer les pilotes RTL-SDR existants et d'installer une version mise à jour.

**1. Supprimer l'ancien pilote**

.. code-block:: shell

   sudo apt purge ^librtlsdr
   sudo rm -rvf /usr/lib/librtlsdr* /usr/include/rtl-sdr* /usr/local/lib/librtlsdr* /usr/local/include/rtl-sdr* /usr/local/include/rtl_* /usr/local/bin/rtl_*

Vérification A :

.. code-block:: shell

   ldconfig -p | grep rtlsdr || echo "OK : aucun librtlsdr trouvé dans le cache système."

**2. Installer les derniers pilotes**

.. code-block:: shell

   sudo apt-get install libusb-1.0-0-dev git cmake pkg-config build-essential
   git clone https://github.com/osmocom/rtl-sdr
   cd rtl-sdr
   mkdir build
   cd build
   cmake ../ -DINSTALL_UDEV_RULES=ON
   make
   sudo make install
   sudo cp ../rtl-sdr.rules /etc/udev/rules.d/
   sudo ldconfig

Remarque :
    Si vous souhaitez également tester la réception FM en ligne de commande (voir ci-dessous),
    ``sox`` est nécessaire : il fournit la commande ``play``.

    .. code-block:: shell

       sudo apt install -y sox

Vérification B :

.. code-block:: shell

   which rtl_test
   ldd "$(which rtl_test)" | grep rtlsdr   # Doit pointer vers /usr/local/lib/librtlsdr.so

**3. Mettre les pilotes DVB-T TV sur liste noire**

.. code-block:: shell

   echo 'blacklist dvb_usb_rtl28xxu' | sudo tee --append /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf

**4. Redémarrer**

.. code-block:: shell

   sudo reboot

**5. Vérifier le pilote après redémarrage**

.. code-block:: shell

   rtl_test -t

Résultat attendu :
    La sortie doit inclure ``RTL-SDR Blog V4 Detected`` sans messages ``[R82XX] PLL not locked!``.
    La ligne ``Using device 0: Generic RTL2832U OEM`` est normale — c'est juste le nom USB.

**6. Tester la réception FM depuis la ligne de commande**

.. code-block:: shell

   rtl_fm -f 97.1M -M wbfm -s 180000 -r 48000 -g 28 | play -t raw -r 48k -e s -b 16 -c 1 -

Conseils :

    * ``-g`` : Essayez entre 25–35 dB ; plus n'est pas toujours mieux.
    * Réduisez ``-s`` à environ 170k–180k pour diminuer le bruit.
    * Ajustez légèrement la fréquence (par exemple ``97.1005M``) pour un réglage fin.
    * Fermez tout autre logiciel SDR qui pourrait utiliser le périphérique.

----

Installer les logiciels radio courants
------------------------------------------------------------

Cette section présente quatre applications SDR largement utilisées, avec de brèves descriptions, des instructions d'installation et des conseils de configuration de base pour les systèmes basés sur Debian.

* :ref:`install_gqrx_promax`
* :ref:`install_sdrpp_promax`
* :ref:`install_rtl433_promax`
* :ref:`install_dump1090_promax`

----

.. _install_gqrx_promax:

GQRX
^^^^^^^^^^^^

GQRX est une application récepteur SDR simple et conviviale avec une interface graphique. Il prend en charge une large gamme de périphériques SDR et est idéal pour écouter la FM, AM, BLU et d'autres signaux avec des affichages en temps réel du spectre et de la cascade.

Vous pouvez également consulter le guide d'installation officiel pour Raspberry Pi ici : https://www.gqrx.dk/download/gqrx-sdr-for-the-raspberry-pi

**Option 1 – Installation rapide (Recommandée pour la plupart des utilisateurs)**

Rapide, simple et s'intègre aux mises à jour système — mais peut ne pas être la dernière version.

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends gqrx-sdr

**Option 2 – Compiler depuis les sources (Optionnelle, dernières fonctionnalités)**

Garantit la dernière version et une personnalisation complète, mais prend plus de temps à compiler et nécessite plus de dépendances.

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

**Prévenir l'écrasement du pilote**

Lors de l'installation de GQRX, SDR++, gnuradio-dev ou gr-osmosdr, le système peut réinstaller une ``librtlsdr`` obsolète.
Après chaque installation, vérifiez :

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si elle ne pointe plus vers ``/usr/local/lib/librtlsdr.so``, exécutez :

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig

Vous pouvez tester immédiatement (ou après un redémarrage pour un environnement propre) :

.. code-block:: shell

   rtl_test -t

Résultat attendu :

   * Contient RTL-SDR Blog V4 Detected.
   * Pas de messages [R82XX] PLL not locked!.

**Configuration du premier démarrage**

* **Périphériques E/S** :

  * Périphérique : ``RTL-SDR (V4)``.
  * Taux d'entrée : ``1.8 MSPS`` (1800000).

* **Contrôles d'entrée** :

  * **Gain LNA** : Commencez autour de 25–35 dB, ajustez si nécessaire

* **Options du récepteur** :

  * Définissez la correction de fréquence (PPM) à partir de votre calibrage.
  * Mode : ``WFM (mono or stereo)`` pour la FM de diffusion.

----

.. _install_sdrpp_promax:

SDR++ (SDRpp)
^^^^^^^^^^^^^

SDR++ est un récepteur radio logicielle (SDR) moderne, rapide et multiplateforme qui prend en charge une variété de périphériques, y compris le RTL-SDR Blog V4. Il offre une interface propre et conviviale, une large prise en charge des modulations, un filtrage DSP avancé et des capacités d'enregistrement.

Vous pouvez consulter le manuel utilisateur officiel ici : https://www.sdrpp.org/manual.pdf

**Installer depuis les sources**

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

**Prévenir l'écrasement du pilote**

Lors de l'installation de GQRX, SDR++, gnuradio-dev ou gr-osmosdr, le système peut réinstaller une ``librtlsdr`` obsolète.
Après chaque installation, vérifiez :

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si elle ne pointe plus vers ``/usr/local/lib/librtlsdr.so``, exécutez :

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig

Vous pouvez tester immédiatement (ou après un redémarrage pour un environnement propre) :

.. code-block:: shell

   rtl_test -t

Résultat attendu :

   * Contient RTL-SDR Blog V4 Detected.
   * Pas de messages [R82XX] PLL not locked!.

**Notes sur le premier démarrage :**

Après l'installation, SDR++ apparaîtra dans votre menu de bureau (généralement sous « Autres »), ou vous pouvez exécuter :

   .. code-block:: shell

      sdrpp

* **Périphérique :** Sélectionnez **RTL-SDR (V4)** dans le menu **Source**.
* **Taux d'échantillonnage :** 1,8 MSPS est typique ; plus bas si la charge CPU est élevée.
* **Gain :** Désactivez l'AGC et définissez un gain manuel (commencez à environ 35 dB).
* **Correction PPM :** Entrez votre valeur de calibrage à partir de ``rtl_test -p``.
* **Mode de démodulation :** Choisissez WFM pour la FM de diffusion, BLU pour les bandes amateurs, etc.

----

.. _install_rtl433_promax:

rtl_433
^^^^^^^^^^^^

rtl_433 est un outil en ligne de commande pour décoder les transmissions radio des appareils fonctionnant dans la bande ISM 433 MHz, tels que les stations météo, les capteurs de pression des pneus et les thermomètres sans fil.

**Installer :**

.. code-block:: shell

   sudo apt install -y rtl-433

**Prévenir l'écrasement du pilote**

Lors de l'installation de GQRX, SDR++, gnuradio-dev ou gr-osmosdr, le système peut réinstaller une ``librtlsdr`` obsolète.
Après chaque installation, vérifiez :

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si elle ne pointe plus vers ``/usr/local/lib/librtlsdr.so``, exécutez :

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig

Vous pouvez tester immédiatement (ou après un redémarrage pour un environnement propre) :

.. code-block:: shell

   rtl_test -t

Résultat attendu :

   * Contient RTL-SDR Blog V4 Detected.
   * Pas de messages [R82XX] PLL not locked!.

**Utilisation de base :**

* Exécutez ``rtl_433`` pour détecter et décoder automatiquement les appareils 433 MHz courants.
* Utilisez ``rtl_433 -G`` pour lister tous les protocoles pris en charge.

----

.. _install_dump1090_promax:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutability est un décodeur Mode S pour les données des transpondeurs d'avions ADS-B. Il reçoit et décode les positions, vitesses et autres données de vol des avions, et peut servir une carte en direct via un navigateur web.

**Installer :**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

**Prévenir l'écrasement du pilote**

Lors de l'installation de GQRX, SDR++, gnuradio-dev ou gr-osmosdr, le système peut réinstaller une ``librtlsdr`` obsolète.
Après chaque installation, vérifiez :

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si elle ne pointe plus vers ``/usr/local/lib/librtlsdr.so``, exécutez :

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig

Vous pouvez tester immédiatement (ou après un redémarrage pour un environnement propre) :

.. code-block:: shell

   rtl_test -t

Résultat attendu :

   * Contient RTL-SDR Blog V4 Detected.
   * Pas de messages [R82XX] PLL not locked!.

**Utilisation de base :**

* Exécutez : ``dump1090 --interactive --net``.
* Ouvrez ``http://<adresse-ip-raspberrypi>:8080`` dans votre navigateur pour visualiser le suivi des avions en direct.
