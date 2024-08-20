.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-achat et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et tirages au sort** : Participez à des concours et des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _remote_desktop:

Accès au Bureau à Distance pour Raspberry Pi
==================================================

Pour ceux qui préfèrent une interface utilisateur graphique (GUI) plutôt qu'un accès en ligne de commande, le Raspberry Pi prend en charge la fonctionnalité de bureau à distance. Ce guide vous explique comment configurer et utiliser VNC (Virtual Network Computing) pour un accès à distance.

Nous vous recommandons d'utiliser `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ à cet effet.

**Activer le service VNC sur Raspberry Pi**

Le service VNC est pré-installé dans l'OS Raspberry Pi mais est désactivé par défaut. Suivez ces étapes pour l'activer :

#. Saisissez la commande suivante dans le terminal Raspberry Pi :

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Naviguez jusqu'aux **Options d'interface** à l'aide de la touche fléchée vers le bas, puis appuyez sur **Entrée**.

   .. image:: img/bookwarm_config_interface.png
      :width: 90%
      

#. Sélectionnez **VNC** dans les options.

   .. image:: img/bookwarm_vnc.png
      :width: 90%
      

#. Utilisez les touches fléchées pour choisir **<Oui>** -> **<OK>** -> **<Terminer>** et finaliser l'activation du service VNC.

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%
      

**Connexion via VNC Viewer**

#. Téléchargez et installez `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ sur votre ordinateur personnel.

#. Une fois installé, lancez VNC Viewer. Saisissez le nom d'hôte ou l'adresse IP de votre Raspberry Pi, puis appuyez sur Entrée.

   .. image:: img/vnc_viewer1.png
      :width: 90%
      

#. Lorsque cela vous est demandé, entrez le nom d'utilisateur et le mot de passe de votre Raspberry Pi, puis cliquez sur **OK**.

   .. image:: img/vnc_viewer2.png
      :width: 90%
      

#. Vous aurez alors accès à l'interface de bureau de votre Raspberry Pi.

   .. image:: img/bookwarm.png
      :width: 90%
      
