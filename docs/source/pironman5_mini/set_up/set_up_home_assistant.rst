.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Seting Up on Home Assistant
============================================

Si vous avez installé le système Home Assistant, vous devrez ajouter les modules complémentaires nécessaires et les démarrer pour faire fonctionner le Pironman 5 Mini.

.. note::

    La méthode suivante s’applique uniquement aux systèmes avec Home Assistant installé de manière native. Elle ne s’applique pas aux systèmes Raspberry Pi avec Home Assistant installé en surcouche ni aux versions Docker de Home Assistant.

1. Connexion à Home Assistant
--------------------------------

* Après avoir démarré le Pironman 5 Mini, il est recommandé de brancher un câble Ethernet directement. Ensuite, ouvrez le navigateur de votre ordinateur et saisissez : ``homeassistant.local:8123`` pour accéder à Home Assistant.

  .. image:: img/home_login.png
   :width: 90%


* Sélectionnez **CREATE MY SMART HOME**, puis créez votre compte.

  .. image:: img/home_account.png
   :width: 90%

* Suivez les instructions pour définir votre emplacement et les autres paramètres. Une fois la configuration terminée, vous accéderez au tableau de bord de Home Assistant.

  .. image:: img/home_dashboard.png
   :width: 90%


2. Ajouter le dépôt des modules SunFounder
----------------------------------------------------

Les fonctionnalités du Pironman 5 Mini sont intégrées dans Home Assistant sous forme de modules complémentaires. Commencez par ajouter le dépôt **SunFounder**.

#. Ouvrez **Settings** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Cliquez sur le signe plus en bas à droite pour accéder à la boutique des modules complémentaires.

   .. image:: img/home_addon.png
      :width: 90%

#. Dans la boutique, cliquez sur le menu en haut à droite et sélectionnez **Repositories**.

   .. image:: img/home_add_res.png
      :width: 90%

#. Saisissez l’URL du dépôt **SunFounder** : ``https://github.com/sunfounder/home-assistant-addon``, puis cliquez sur **ADD**.

   .. image:: img/home_res_add.png
      :width: 90%

#. Une fois l’ajout effectué, fermez la fenêtre pop-up et actualisez la page. Vous verrez la liste des modules SunFounder.

   .. image:: img/home_addon_list.png
         :width: 90%

3. Installer le module **Pi Config Wizard**
------------------------------------------------------

Le module **Pi Config Wizard** permet d’activer les configurations nécessaires au fonctionnement du Pironman 5 Mini, comme I2C et SPI. Il peut être supprimé par la suite si inutile.

#. Trouvez **Pi Config Wizard** dans la liste des modules SunFounder et cliquez pour y accéder.

   .. image:: img/home_pi_config.png
      :width: 90%

#. Sur la page du **Pi Config Wizard**, cliquez sur **INSTALL** et attendez la fin de l’installation.

   .. image:: img/home_config_install.png
      :width: 90%

#. Une fois installé, allez à l’onglet **Log** pour vérifier s’il y a des erreurs.

   .. image:: img/home_log.png
      :width: 90%

#. S’il n’y a pas d’erreurs, retournez sur l’onglet **Info** et cliquez sur **START** pour démarrer le module.

   .. image:: img/home_start.png
      :width: 90%

#. Ouvrez ensuite l’interface WEB UI.

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. Dans l’interface Web, vous verrez une option pour monter la partition Boot. Cliquez sur **MOUNT**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Une fois le montage effectué, vous pourrez activer I2C, SPI et modifier le fichier config.txt. Cochez I2C et SPI, puis cliquez sur le bouton de redémarrage pour redémarrer le Raspberry Pi.

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. Après redémarrage, actualisez la page. Vous reviendrez à la page de montage de la partition. Cliquez de nouveau sur **MOUNT**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. En général, SPI sera activé, mais pas I2C car deux redémarrages sont nécessaires. Activez I2C à nouveau, puis redémarrez.

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. Après ce second redémarrage, retournez à la page **MOUNT**. I2C et SPI devraient maintenant être activés.

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * Si après actualisation vous n’êtes pas redirigé vers la page de montage, allez dans **Settings** -> **Add-ons** -> **Pi Config Wizard**.
    * Vérifiez que le module est bien démarré. Sinon, cliquez sur **START**.
    * Une fois démarré, cliquez sur **OPEN WEB UI**, puis sur **MOUNT** pour vérifier si I2C et SPI sont bien activés.



.. .. 这里要改PIRONMAN5 MINI的ADD ON 图


4. Installer le module **Pironman 5 Mini**
---------------------------------------------

L’installation du module **Pironman 5 Mini** peut maintenant commencer.

#. Ouvrez **Settings** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Cliquez sur le signe plus en bas à droite pour accéder à la boutique.

   .. image:: img/home_addon.png
      :width: 90%

#. Trouvez **Pironman 5 Mini** dans la liste **SunFounder** et cliquez dessus.

   .. image:: img/home_pironman5_mini_addon.png
      :width: 90%

#. Procédez à l’installation du module **Pironman 5 Mini**.

   .. image:: img/home_pironman5_mini_addon_install.png
      :width: 90%

#. Une fois installé, cliquez sur **START**. Quatre LED RGB WS2812 s’allumeront en bleu avec un effet de respiration.

   .. image:: img/home_pironman5_mini_addon_start.png
      :width: 90%

#. Cliquez ensuite sur **OPEN WEB UI** pour ouvrir l’interface web de Pironman 5 Mini. Vous pouvez aussi activer l’affichage dans la barre latérale pour y accéder plus rapidement.

   .. image:: img/home_pironman5_mini_webui.png
      :width: 90%

#. Vous pourrez alors consulter les informations de votre Raspberry Pi, configurer les LED RGB, contrôler le ventilateur, etc.

   .. image:: img/home_web.png
      :width: 90%


.. note::

   À ce stade, vous avez correctement configuré le Pironman 5 Mini, et il est prêt à être utilisé.

   Pour un contrôle avancé de ses composants, veuillez vous référer à :ref:`control_commands_dashboard_mini`.
