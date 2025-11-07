.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _set_up_umbrel_max:

Configuration sur Umbrel OS
======================================================================

Si vous avez installé Umbrel OS sur votre Raspberry Pi 5, vous devrez configurer le Pironman 5 MAX en utilisant la ligne de commande. Vous trouverez ci-dessous les instructions détaillées :

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
      git clone -b max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

#. Une fois l’installation terminée, entrez la commande suivante pour redémarrer votre Raspberry Pi.

   .. code-block:: shell

      sudo reboot

#. Au redémarrage, le service ``pironman5.service`` sera lancé automatiquement.  
   Voici les principales configurations du Pironman 5 MAX :
   
   * L’écran OLED affiche le CPU, la RAM, l’utilisation du disque, la température du CPU et l’adresse IP du Raspberry Pi.  
   * Quatre LED WS2812 RGB s’allumeront en bleu avec un effet de respiration.  
   * Les ventilateurs RGB sont configurés par défaut sur le mode **Toujours activé**. Pour des températures de déclenchement différentes, consultez :ref:`cc_control_fan_max`.

#. Vous pouvez utiliser l’outil ``systemctl`` pour ``start``, ``stop``, ``restart`` ou vérifier le ``status`` du service ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart`` : Utilisez cette commande pour appliquer les modifications apportées aux paramètres du Pironman 5 MAX.  
   * ``start/stop`` : Active ou désactive le service ``pironman5.service``.  
   * ``status`` : Vérifie l’état de fonctionnement du programme ``pironman5`` à l’aide de l’outil ``systemctl``.

.. note::

   À ce stade, vous avez configuré avec succès le Pironman 5 MAX et il est prêt à être utilisé.  
   Pour un contrôle avancé de ses composants, consultez :ref:`control_commands_dashboard_max`.



