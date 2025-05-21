Assemblage du module caméra 
===========================================

Procédez comme suit pour assembler le module caméra :

1. Retirez les deux panneaux latéraux en acrylique du boîtier.

   .. image:: img/IN_CMR/IN.CMR.1.png
      :width: 500
      :align: center

2. Déconnectez le câble 2 broches ainsi que la nappe FPC, comme illustré.

   .. image:: img/IN_CMR/IN.CMR.2.png
      :width: 500
      :align: center

3. Dévissez les quatre vis afin de retirer l’ensemble du module NVMe PIP et le convertisseur de l’interrupteur d’alimentation.

   .. image:: img/IN_CMR/IN.CMR.3.png
      :width: 500
      :align: center

4. Désassemblez le groupe de modules. Pour cela, retirez un rivet en poussant son axe central à l’aide d’un tournevis, puis en l’extrayant complètement.

   .. image:: img/IN_CMR/IN.CMR.4.png
      :width: 500
      :align: center

5. Connectez le module caméra à la nappe FPC.

   .. image:: img/IN_CMR/IN.CMR.5.png
      :width: 500
      :align: center

6. Faites passer le FPC à travers l’ouverture marquée "CAMERA" du boîtier.

   .. image:: img/IN_CMR/IN.CMR.6.png
      :width: 500
      :align: center

7. Continuez à insérer délicatement le FPC dans l’orifice "CAMERA" du boîtier.

   .. image:: img/IN_CMR/IN.CMR.7.png
      :width: 500
      :align: center

8. Connectez le FPC au Raspberry Pi. Cette étape exige une manipulation précise et minutieuse.

   .. image:: img/IN_CMR/IN.CMR.8.png
      :width: 500
      :align: center

9. Allumez l’appareil hôte et vérifiez que le module caméra est bien reconnu.

   * Commencez par connecter un écran au Raspberry Pi ou établissez une connexion via VNC.
   * Une fois l’affichage opérationnel, ouvrez un terminal et exécutez la commande suivante : ``raspistill -o test.jpg``
   * Si le module est bien fonctionnel, une photo sera prise et enregistrée sous ``test.jpg``.
   * Ouvrez le fichier ``test.jpg`` pour confirmer que l’image a bien été capturée.

10. Réinstallez le convertisseur de l’interrupteur d’alimentation dans le boîtier.

   .. image:: img/IN_CMR/IN.CMR.9.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.10.png
      :width: 500
      :align: center

11. Réinstallez le module NVMe PIP dans le boîtier.

   .. image:: img/IN_CMR/IN.CMR.11.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.12.png
      :width: 500
      :align: center

12. Replacez le couvercle supérieur du boîtier.

   .. image:: img/IN_CMR/IN.CMR.13.png
      :width: 500
      :align: center

