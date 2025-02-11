Assemblage du module caméra
===========================================

Suivez ces étapes pour assembler le module caméra :

1. Retirez les deux panneaux en acrylique du boîtier.

   .. image:: img/IN_CMR/IN.CMR.1.png
      :width: 500
      :align: center

2. Déconnectez le câble à 2 broches et le FPC comme indiqué sur l'image.

   .. image:: img/IN_CMR/IN.CMR.2.png
      :width: 500
      :align: center

3. Dévissez les quatre vis pour retirer le groupe de modules NVMe PIP et le convertisseur d'interrupteur d'alimentation.

   .. image:: img/IN_CMR/IN.CMR.3.png
      :width: 500
      :align: center

4. Démontez le groupe de modules. Cela implique de retirer un rivet, ce qui doit être fait en poussant l'axe central du rivet avec un tournevis, puis en retirant entièrement le rivet.

   .. image:: img/IN_CMR/IN.CMR.4.png
      :width: 500
      :align: center

5. Connectez le module caméra au câble FPC.

   .. image:: img/IN_CMR/IN.CMR.5.png
      :width: 500
      :align: center

6. Insérez le FPC à travers le trou "CAMERA" du boîtier.

   .. image:: img/IN_CMR/IN.CMR.6.png
      :width: 500
      :align: center

7. Continuez à faire passer le FPC à travers le trou "CAMERA" du boîtier.

   .. image:: img/IN_CMR/IN.CMR.7.png
      :width: 500
      :align: center

8. Connectez le FPC au Raspberry Pi. Cette étape est très compacte et nécessite une manipulation soigneuse.

   .. image:: img/IN_CMR/IN.CMR.8.png
      :width: 500
      :align: center

9. Allumez l'hôte et vérifiez si le module caméra est correctement connecté.

   * Tout d'abord, connectez un écran au Raspberry Pi ou établissez une connexion VNC.
   * Une fois l'affichage configuré, ouvrez un terminal et exécutez la commande suivante : ``raspistill -o test.jpg``
   * Si le module caméra fonctionne correctement, cette commande prendra une photo et l'enregistrera sous ``test.jpg``.
   * Ouvrez ``test.jpg`` pour vérifier que l'image a bien été capturée.

10. Remontez le convertisseur d'interrupteur d'alimentation dans le boîtier.

   .. image:: img/IN_CMR/IN.CMR.9.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.10.png
      :width: 500
      :align: center

11. Remontez le NVMe PIP dans le boîtier.

   .. image:: img/IN_CMR/IN.CMR.11.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.12.png
      :width: 500
      :align: center

12. Remontez le couvercle du boîtier.

   .. image:: img/IN_CMR/IN.CMR.13.png
      :width: 500
      :align: center

