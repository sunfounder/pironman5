.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 ! Rejoignez d'autres passionnés pour approfondir vos connaissances sur Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Obtenez de l'aide pour résoudre les problèmes après-vente et les difficultés techniques grâce à notre équipe et notre communauté.
    - **Apprendre et partager** : Échangez des conseils et tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Soyez informé en avant-première des nouvelles annonces produits.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des promotions et tirages au sort lors des événements spéciaux.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] pour nous rejoindre dès aujourd’hui !

.. _max_remote_desktop:

Accès au bureau à distance pour Raspberry Pi
==================================================

Pour ceux qui préfèrent une interface graphique (GUI) à l'accès en ligne de commande, le Raspberry Pi prend en charge la fonctionnalité de bureau à distance. Ce guide vous expliquera comment configurer et utiliser VNC (Virtual Network Computing) pour un accès distant.

Nous vous recommandons d’utiliser `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ à cet effet.

**Activer le service VNC sur le Raspberry Pi**

Le service VNC est préinstallé sur Raspberry Pi OS mais désactivé par défaut. Suivez les étapes ci-dessous pour l’activer :

#. Saisissez la commande suivante dans le terminal du Raspberry Pi :

    .. raw:: html

        <run></run>

    .. code-block::

        sudo raspi-config

#. Utilisez la flèche vers le bas pour accéder à **Interfacing Options**, puis appuyez sur **Entrée**.

   .. image:: img/bookwarm_config_interface.png
      :width: 90%


#. Sélectionnez **VNC** dans la liste.

   .. image:: img/bookwarm_vnc.png
      :width: 90%


#. Utilisez les flèches pour sélectionner **<Yes>** -> **<OK>** -> **<Finish>** afin d’activer le service VNC.

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%


**Connexion via VNC Viewer**

#. Téléchargez et installez `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ sur votre ordinateur personnel.

#. Une fois installé, lancez VNC Viewer. Saisissez le nom d'hôte ou l'adresse IP de votre Raspberry Pi, puis appuyez sur Entrée.

   .. image:: img/vnc_viewer1.png
      :width: 90%


#. Lorsque vous y êtes invité, saisissez le nom d’utilisateur et le mot de passe de votre Raspberry Pi, puis cliquez sur **OK**.

   .. image:: img/vnc_viewer2.png
      :width: 90%


#. Vous accéderez maintenant à l’interface de bureau de votre Raspberry Pi.

   .. image:: img/bookwarm.png
      :width: 90%

