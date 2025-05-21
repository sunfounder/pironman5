.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d’autres passionnés pour explorer plus en profondeur l’univers du Raspberry Pi, d’Arduino et de l’ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Résolvez les problèmes après-vente et défis techniques grâce à notre communauté et notre équipe.
    - **Apprendre et partager** : Échangez des conseils et tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des concours et offres spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès maintenant !

.. _remote_desktop_mini:

Accès au bureau à distance pour Raspberry Pi
==================================================

Si vous préférez une interface graphique (GUI) plutôt que la ligne de commande, le Raspberry Pi prend en charge l’accès à distance via le bureau. Ce guide vous montre comment configurer et utiliser VNC (Virtual Network Computing) pour un accès à distance.

Nous recommandons l'utilisation de `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ à cet effet.

**Activation du service VNC sur le Raspberry Pi**

Le service VNC est préinstallé dans Raspberry Pi OS, mais désactivé par défaut. Suivez ces étapes pour l’activer :

#. Saisissez la commande suivante dans le terminal du Raspberry Pi :

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Naviguez jusqu’à **Interfacing Options** à l’aide des flèches directionnelles, puis appuyez sur **Entrée**.

   .. image:: img/bookwarm_config_interface.png
      :width: 90%
      

#. Sélectionnez **VNC** parmi les options disponibles.

   .. image:: img/bookwarm_vnc.png
      :width: 90%
      

#. Utilisez les touches fléchées pour sélectionner **<Yes>** -> **<OK>** -> **<Finish>** afin de terminer l’activation du service VNC.

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%
      

**Connexion via VNC Viewer**

#. Téléchargez et installez `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ sur votre ordinateur personnel.

#. Une fois installé, lancez VNC Viewer. Saisissez le nom d’hôte ou l’adresse IP de votre Raspberry Pi, puis appuyez sur Entrée.

   .. image:: img/vnc_viewer1.png
      :width: 90%
      

#. Lorsqu’un mot de passe est requis, entrez le nom d’utilisateur et le mot de passe de votre Raspberry Pi, puis cliquez sur **OK**.

   .. image:: img/vnc_viewer2.png
      :width: 90%
      

#. Vous accédez désormais à l’interface du bureau de votre Raspberry Pi.

   .. image:: img/bookwarm.png
      :width: 90%

