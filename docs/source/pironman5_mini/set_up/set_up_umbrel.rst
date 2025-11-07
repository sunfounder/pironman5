.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d'autres passionnés pour approfondir vos connaissances sur Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Obtenez de l’aide pour les problèmes techniques ou après-vente grâce à notre communauté et notre équipe.
    - **Apprendre et partager** : Échangez des astuces et tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et à des aperçus inédits.
    - **Réductions spéciales** : Bénéficiez d’offres exclusives sur nos produits les plus récents.
    - **Promotions et cadeaux festifs** : Participez à des jeux-concours et des offres spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _set_up_umbrel_mini:

Configuration sur Umbrel OS
======================================================================

Si vous avez installé Umbrel OS sur votre Raspberry Pi 5, vous devrez configurer le Pironman 5 Mini en utilisant la ligne de commande. Vous trouverez ci-dessous les instructions détaillées :

#. Connectez votre Raspberry Pi 5 au réseau à l’aide d’un câble Ethernet. Cette étape est essentielle pour garantir que le Raspberry Pi ait accès à Internet.

#. Dans votre navigateur, visitez : ``http://umbrel.local``.  
   Si la page ne s’ouvre pas, vérifiez dans votre routeur l’adresse IP de l’appareil Umbrel, par exemple : ``http://192.168.1.50``

   .. image:: img/umbrel_local.png

#. Créez votre compte Umbrel en définissant un nom d’utilisateur et un mot de passe.  
   Ce mot de passe sera utilisé pour les futurs accès à distance à Umbrel, veillez donc à bien le mémoriser.

   .. image:: img/umbrel_account.png

#. Cliquez sur **Next** pour terminer la configuration d’Umbrel et accéder à l’environnement de bureau.

   .. image:: img/umbrel_desktop.png

#. Ouvrez le Terminal. Depuis le bureau, cliquez sur l’icône **Settings**, puis sélectionnez **Advanced Settings** et cliquez sur **Open**.

   .. image:: img/umbrel_setting.png

#. Cliquez sur **Open Terminal**.

   .. image:: img/umbrel_open_terminal.png

#. Vous pouvez choisir d’ouvrir le terminal dans Umbrel OS ou à l’intérieur d’une application spécifique. Les deux options vous mèneront à l’interface du terminal.

   .. image:: img/umbrel_terminal.png

#. Procédez au téléchargement du code depuis GitHub et à l’installation du module ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b mini https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

#. Une fois l’installation terminée, entrez la commande suivante pour redémarrer votre Raspberry Pi.

   .. code-block:: shell

      sudo reboot

#. Au redémarrage, le service ``pironman5.service`` sera lancé automatiquement.  
   Voici les principales configurations du Pironman 5 Mini :
   
   * Quatre LED WS2812 RGB s’allumeront en bleu avec un effet de respiration.  
   * Les ventilateurs RGB sont configurés par défaut sur le mode **Toujours activé**. Pour des températures de déclenchement différentes, consultez :ref:`cc_control_fan_mini`.

#. Vous pouvez utiliser l’outil ``systemctl`` pour ``start``, ``stop``, ``restart`` ou vérifier le ``status`` du service ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart`` : Utilisez cette commande pour appliquer les modifications apportées aux paramètres du Pironman 5 Mini.  
   * ``start/stop`` : Active ou désactive le service ``pironman5.service``.  
   * ``status`` : Vérifie l’état de fonctionnement du programme ``pironman5`` à l’aide de l’outil ``systemctl``.

.. note::

   À ce stade, vous avez configuré avec succès le Pironman 5 Mini et il est prêt à être utilisé.  
   Pour un contrôle avancé de ses composants, consultez :ref:`control_commands_dashboard_mini`.

