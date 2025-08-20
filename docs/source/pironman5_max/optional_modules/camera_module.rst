.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives**: Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales**: Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et tirages au sort**: Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !



Module Caméra  
===========================================

.. note::

    La série Pironman 5 n’inclut pas de module caméra.  
    Vous devrez en préparer un vous-même ou l’acheter sur notre site officiel :

    * `Module Caméra <https://www.sunfounder.com/products/ov5647-camera-module>`_

Dans cette section, vous apprendrez à :

* Désassembler le Pironman 5.  
* Installer le module caméra sur le Raspberry Pi 5.  
* Réassembler le boîtier.  
* Tester le module caméra en capturant des photos et en enregistrant des vidéos.

À la fin de cette section, vous aurez un module caméra entièrement installé et fonctionnel, prêt pour vos projets.

Assembler le module caméra  
------------------------------------

Suivez ces étapes pour assembler le module caméra :

1. Retirez les deux panneaux acryliques du boîtier.

   .. image:: img/IN.CMR.1.png
      :align: center

2. Débranchez le câble 2 broches et le FPC comme indiqué sur l’image.

   .. image:: img/IN.CMR.2.png
      :align: center

3. Dévissez les quatre vis pour retirer le groupe de modules NVMe PIP et Convertisseur d’alimentation.

   .. image:: img/IN.CMR.3.png
      :align: center

4. Désassemblez le groupe de modules. Cela implique de retirer un rivet, ce qui doit être fait en poussant l’axe central du rivet avec un tournevis, puis en retirant complètement le rivet.

   .. image:: img/IN.CMR.4.png
      :align: center

5. Connectez le module caméra au câble FPC.

   .. image:: img/IN.CMR.5.png
      :align: center

6. Passez le FPC par le trou **CAMERA** du boîtier.

   .. image:: img/IN.CMR.6.png
      :align: center

7. Continuez à passer le FPC par le trou **CAMERA** du boîtier.

   .. image:: img/IN.CMR.7.png
      :align: center

8. Connectez le FPC au Raspberry Pi. Cette étape est très compacte et nécessite une manipulation soigneuse.

   .. image:: img/IN.CMR.8.png
      :align: center

9. Allumez le Raspberry Pi 5 et vérifiez si le module caméra est correctement connecté.

   * Tout d’abord, connectez un écran au Raspberry Pi ou établissez une connexion VNC.  
   * Après le démarrage du système, exécutez la commande suivante pour vérifier si la caméra fonctionne : ``libcamera-hello``  
   * Si vous voyez une fenêtre d’aperçu, la caméra fonctionne correctement.

10. Réinstallez le convertisseur d’alimentation dans le boîtier.

   .. image:: img/IN.CMR.9.png
      :align: center

   .. image:: img/IN.CMR.10.png
      :align: center

11. Réinstallez le NVMe PIP dans le boîtier.

   .. image:: img/IN.CMR.11.png
      :align: center

   .. image:: img/IN.CMR.12.png
      :align: center

12. Réinstallez le couvercle du boîtier.

   .. image:: img/IN.CMR.13.png
      :align: center

Utiliser le module caméra  
---------------------------

**Tester la caméra**

Raspberry Pi OS (Bookworm et versions ultérieures) utilise la pile **libcamera**.  
Après le démarrage du système, exécutez la commande suivante pour vérifier si la caméra fonctionne :

.. code-block:: bash

    libcamera-hello

Si vous voyez une fenêtre d’aperçu, la caméra fonctionne correctement.

**Prendre une photo**

.. code-block:: bash

    libcamera-jpeg -o test.jpg

Cela capturera une image fixe et l’enregistrera sous le nom ``test.jpg``.

**Enregistrer une vidéo**

.. code-block:: bash

    libcamera-vid -t 10000 -o test.h264

* ``-t 10000`` signifie enregistrer pendant 10 secondes.  
* ``-o test.h264`` enregistre la sortie en vidéo H.264.

Pour convertir la vidéo au format MP4 :

.. code-block:: bash

    ffmpeg -i test.h264 -c copy test.mp4

**Exemple en Python**

Vous pouvez également contrôler la caméra avec Python en utilisant la bibliothèque ``picamera2``.

Installez les dépendances :

.. code-block:: bash

    sudo apt install python3-picamera2 -y

Créez un fichier Python :

.. code-block:: bash

    nano camera_test.py

Puis collez le code suivant :

.. code-block:: python

    from picamera2 import Picamera2
    import time

    picam2 = Picamera2()
    picam2.start()
    time.sleep(2)
    picam2.capture_file("image.jpg")

Enregistrez et quittez nano en appuyant sur ``CTRL+O``, puis ``ENTRÉE``, et ``CTRL+X``.

Exécutez le script :

.. code-block:: bash

    python3 camera_test.py
