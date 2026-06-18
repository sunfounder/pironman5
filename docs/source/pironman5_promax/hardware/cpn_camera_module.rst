
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _cpn_camera_module:

Module Caméra
====================================

**Description**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

Il s'agit d'un module caméra Raspberry Pi 5MP avec capteur OV5647. Il est prêt à l'emploi : connectez le câble nappe inclus au port CSI (Camera Serial Interface) de votre Raspberry Pi et vous êtes prêt à partir.

La carte est petite, environ 25 mm x 23 mm x 9 mm, et pèse 3 g, ce qui la rend idéale pour les applications mobiles ou autres applications critiques en termes de taille et de poids. Le module caméra a une résolution native de 5 mégapixels et dispose d'un objectif à mise au point fixe intégré qui capture des images fixes en 2592 x 1944 pixels, et prend également en charge la vidéo en 1080p30, 720p60 et 640x480p90.

.. note::

   Le module est uniquement capable de capturer des images et des vidéos, pas de son.

**Spécifications**

* **Résolution d'images fixes** : 2592×1944
* **Résolution vidéo prise en charge** : 1080p/30 fps, 720p/60fps et enregistrement vidéo 640 x480p 60/90
* **Ouverture (F)** : 1.8
* **Angle de vue** : 65 degrés
* **Dimensions** : 24 mm x 23,5 mm x 8 mm
* **Poids** : 3 g
* **Interface** : Connecteur CSI
* **Système d'exploitation pris en charge** : Raspberry OS (version récente recommandée)

Assembler le module caméra
-------------------------------------

Sur le module caméra ou le Raspberry Pi, vous trouverez un connecteur plat en plastique. Tirez soigneusement sur le commutateur de fixation noir jusqu'à ce qu'il soit partiellement sorti. Insérez le câble FFC dans le connecteur en plastique dans le sens indiqué et remettez le commutateur de fixation en place.

Si le câble FFC est installé correctement, il sera droit et ne se retirera pas lorsque vous tirez doucement dessus. Sinon, réinstallez-le à nouveau.

.. raw:: html

    <div style="text-align: center; margin: 16px 0;">
        <iframe width="560" height="315"
            src="https://www.youtube.com/embed/riUNPxS7sHs"
            title="Pironman 5 Pro MAX Camera Module Assembly"
            frameborder="0"
            allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen>
        </iframe>
    </div>

.. image:: img/connect_ffc.png

.. image:: img/1.10_camera.png
   :width: 700

.. attention::

   N'installez pas la caméra lorsque l'alimentation est allumée, cela pourrait endommager votre caméra.
