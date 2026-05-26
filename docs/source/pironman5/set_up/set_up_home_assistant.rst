.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Configuration sur Home Assistant
============================================

Si vous avez installé le système Home Assistant, vous devrez ajouter les add-ons nécessaires à Home Assistant et les démarrer pour que Pironman 5 fonctionne.

.. note::

    La méthode suivante ne s'applique qu'aux systèmes avec Home Assistant installé nativement. Elle ne s'applique pas aux systèmes Raspberry Pi avec Home Assistant installé par-dessus ou aux versions Docker de Home Assistant.

1. Connexion à Home Assistant
---------------------------------

* Après avoir démarré Pironman 5, il est recommandé de brancher directement un câble Ethernet. Vous pouvez ensuite ouvrir le navigateur de votre ordinateur et entrer: ``homeassistant.local:8123`` pour accéder à Home Assistant.

  .. image:: img/home_login.png
      :width: 90%


* Sélectionnez **CREATE MY SMART HOME**, puis créez votre compte.

  .. image:: img/home_account.png
      :width: 90%

* Suivez les instructions pour choisir votre emplacement et d'autres configurations. Une fois terminé, vous accéderez au tableau de bord de Home Assistant.

  .. image:: img/home_dashboard.png
      :width: 90%


2. Ajouter le dépôt d'add-ons SunFounder
----------------------------------------------------

Les fonctionnalités de Pironman 5 sont installées sur Home Assistant sous forme d'add-ons. Vous devez d'abord ajouter le dépôt d'add-ons **SunFounder**.

#. Ouvrez **Paramètres** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Cliquez sur le signe plus en bas à droite pour entrer dans la boutique des add-ons.

   .. image:: img/home_addon.png
      :width: 90%

#. Dans la boutique des add-ons, cliquez sur le menu en haut à droite et sélectionnez **Dépôts**.

   .. image:: img/home_add_res.png
      :width: 90%

#. Entrez l'URL du dépôt d'add-ons **SunFounder**: ``https://github.com/sunfounder/home-assistant-addon``, puis cliquez sur **ADD**.

   .. image:: img/home_res_add.png
      :width: 90%

#. Après avoir ajouté avec succès, fermez la fenêtre contextuelle et rafraîchissez la page. Trouvez la liste des add-ons SunFounder.

   .. image:: img/home_addon_list.png
      :width: 90%

3. Installer l'add-on **Pi Config Wizard**
------------------------------------------------------

Le **Pi Config Wizard** permet d'activer les configurations nécessaires pour Pironman 5, telles que l'I2C et le SPI. Si vous n'en avez plus besoin par la suite, vous pouvez le supprimer.

#. Trouvez **Pi Config Wizard** dans la liste des add-ons SunFounder et cliquez pour entrer.

   .. image:: img/home_pi_config.png
      :width: 90%

#. Sur la page **Pi Config Wizard**, cliquez sur **INSTALLER**. Attendez la fin de l'installation.

   .. image:: img/home_config_install.png
      :width: 90%

#. Une fois l'installation terminée, passez à l'onglet **Journal** pour vérifier s'il y a des erreurs.

   .. image:: img/home_log.png
      :width: 90%

#. S'il n'y a pas d'erreurs, revenez à la page **Info** et cliquez sur **START** pour démarrer cet add-on.

   .. image:: img/home_start.png
      :width: 90%

#. Maintenant, ouvrez l'interface Web.

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. Dans l'interface Web, vous verrez une option pour monter la partition Boot. Cliquez sur **MOUNT** pour monter la partition.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Après un montage réussi, vous verrez des options pour configurer I2C, SPI et éditer le fichier config.txt. Cochez I2C et SPI pour les activer. Une fois qu'ils apparaissent comme activés, cliquez sur le bouton de redémarrage en bas pour redémarrer le Raspberry Pi.

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. Après le redémarrage, actualisez la page. Vous reviendrez à la page de montage de la partition Boot. Cliquez à nouveau sur **MOUNT**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Généralement, vous verrez que SPI est activé, mais pas I2C, car I2C nécessite deux redémarrages. Activez à nouveau I2C, puis redémarrez le Raspberry Pi.

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. Après le redémarrage, retournez sur la page **MOUNT**. Vous verrez que l'I2C et le SPI sont tous deux activés.

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * Si après avoir actualisé la page, vous ne revenez pas sur la page de montage de la partition, vous pouvez cliquer sur **Paramètres** -> **Add-ons** -> **Pi Config Wizard** à nouveau.
    * Vérifiez si cet add-on est démarré. Si ce n'est pas le cas, cliquez sur **START**.
    * Après avoir démarré, cliquez sur **OPEN WEB UI**, puis sur **MOUNT** pour vérifier si I2C et SPI sont activés.

4. Installer l'add-on **Pironman 5**
---------------------------------------------

Passons maintenant à l'installation officielle de l'add-on **Pironman 5**.

#. Ouvrez **Paramètres** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Cliquez sur le signe plus en bas à droite pour entrer dans la boutique des add-ons.

   .. image:: img/home_addon.png
      :width: 90%

#. Trouvez **Pironman 5** dans la liste des add-ons **SunFounder** et cliquez pour entrer.

   .. image:: img/home_pironman5_addon.png
      :width: 90%

#. Installez maintenant l'add-on Pironman 5.

   .. image:: img/home_install_pironman5.png
      :width: 90%

#. Une fois l'installation terminée, cliquez sur **START** pour démarrer cet add-on. Vous verrez l'écran OLED afficher les informations sur le CPU du Raspberry Pi, la température et d'autres informations connexes. Quatre LED RGB WS2812 s'allumeront en bleu avec un mode respiration.

   .. image:: img/home_start_pironman5.png
      :width: 90%

#. Maintenant, vous pouvez cliquer sur **OPEN WEB UI** pour ouvrir la page Web de Pironman 5. Vous pouvez également cocher l'option pour afficher l'interface Web dans la barre latérale. Cela vous permettra de voir l'option Pironman 5 dans la barre latérale gauche de Home Assistant et de cliquer pour ouvrir la page de Pironman 5.

   .. image:: img/home_web_ui.png
      :width: 90%

#. Vous pouvez maintenant voir les informations concernant votre Raspberry Pi, configurer le RGB et contrôler le ventilateur, etc.

   .. image:: img/home_web_new.png
      :width: 90%

.. note::

   À ce stade, vous avez correctement configuré le Pironman 5, et il est prêt à être utilisé.

   Pour un contrôle avancé de ses composants, veuillez vous référer à :ref:`control_commands_dashboard_5`.
