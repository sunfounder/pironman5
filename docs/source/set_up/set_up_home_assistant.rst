.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 ! Plongez-vous dans l’univers du Raspberry Pi, d’Arduino et d’ESP32 aux côtés d’autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et surmontez les défis techniques grâce à l’assistance de notre équipe et de notre communauté.
    - **Apprendre & Partager** : Échangez astuces et tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Profitez d’un accès anticipé aux annonces de nouveaux produits et à des aperçus privilégiés.
    - **Réductions spéciales** : Bénéficiez d’offres exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des campagnes promotionnelles.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

Configuration sur Home Assistant
============================================

Si vous avez installé le système Home Assistant, vous devrez ajouter les modules complémentaires nécessaires et les activer pour faire fonctionner le Pironman 5.

.. note::

    Cette méthode s’applique uniquement aux systèmes où Home Assistant est installé nativement. Elle ne convient pas aux Raspberry Pi avec Home Assistant installé en surcouche, ni aux versions Docker de Home Assistant.

1. Connexion à Home Assistant
---------------------------------

* Après avoir démarré le Pironman 5, il est recommandé de brancher un câble Ethernet directement. Ouvrez ensuite le navigateur de votre ordinateur et saisissez : ``homeassistant.local:8123`` pour accéder à Home Assistant.

  .. image:: img/home_login.png
      :width: 90%


* Sélectionnez **CREATE MY SMART HOME**, puis créez votre compte.

  .. image:: img/home_account.png
      :width: 90%

* Suivez les instructions pour choisir votre emplacement et effectuer les autres configurations. Une fois terminées, vous accéderez au tableau de bord Home Assistant.

  .. image:: img/home_dashboard.png
      :width: 90%


2. Ajouter le dépôt des add-ons SunFounder
----------------------------------------------------

Les fonctionnalités de Pironman 5 sont fournies sous forme de modules complémentaires (add-ons) dans Home Assistant. Commencez par ajouter le dépôt **SunFounder**.

#. Ouvrez **Paramètres** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Cliquez sur le signe plus en bas à droite pour accéder à la boutique des add-ons.

   .. image:: img/home_addon.png
      :width: 90%

#. Dans la boutique, cliquez sur le menu en haut à droite et sélectionnez **Dépôts**.

   .. image:: img/home_add_res.png
      :width: 90%

#. Saisissez l’URL du dépôt **SunFounder** : ``https://github.com/sunfounder/home-assistant-addon``, puis cliquez sur **ADD**.

   .. image:: img/home_res_add.png
      :width: 90%

#. Une fois le dépôt ajouté, fermez la fenêtre contextuelle et actualisez la page. Vous verrez la liste des add-ons SunFounder.

   .. image:: img/home_addon_list.png
      :width: 90%

3. Installer l’add-on **Pi Config Wizard**
------------------------------------------------------

Le **Pi Config Wizard** vous permet d’activer les options nécessaires au fonctionnement du Pironman 5, comme I2C et SPI. Si vous n’en avez plus besoin par la suite, vous pouvez le désinstaller.

#. Recherchez **Pi Config Wizard** dans la liste des add-ons SunFounder et cliquez dessus.

   .. image:: img/home_pi_config.png
      :width: 90%

#. Sur la page de l’add-on, cliquez sur **INSTALLER** et attendez la fin de l’installation.

   .. image:: img/home_config_install.png
      :width: 90%

#. Une fois l’installation terminée, accédez à l’onglet **Journal** pour vérifier s’il y a des erreurs.

   .. image:: img/home_log.png
      :width: 90%

#. S’il n’y a pas d’erreurs, retournez à l’onglet **Info** et cliquez sur **START** pour démarrer l’add-on.

   .. image:: img/home_start.png
      :width: 90%

#. Ouvrez maintenant l’interface Web.

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. Dans l’interface Web, vous trouverez une option pour monter la partition Boot. Cliquez sur **MOUNT** pour la monter.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Une fois le montage réussi, vous pourrez activer I2C, SPI et modifier le fichier config.txt. Cochez les options I2C et SPI pour les activer. Une fois activés, cliquez sur le bouton de redémarrage en bas de page pour redémarrer le Raspberry Pi.

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. Après le redémarrage, actualisez la page. Vous reviendrez sur l’écran de montage de la partition Boot. Cliquez de nouveau sur **MOUNT**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. En général, SPI est activé, mais I2C ne l’est pas encore car il nécessite deux redémarrages. Activez à nouveau I2C, puis redémarrez le Raspberry Pi.

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. Après le second redémarrage, retournez à la page **MOUNT**. Vous devriez voir que I2C et SPI sont tous deux activés.

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * Si, après actualisation, vous ne revenez pas à la page de montage, accédez de nouveau à **Paramètres** -> **Add-ons** -> **Pi Config Wizard**.
    * Vérifiez si l’add-on est bien démarré. Sinon, cliquez sur **START**.
    * Une fois démarré, cliquez sur **OPEN WEB UI**, puis sur **MOUNT** pour vérifier l’activation d’I2C et de SPI.

4. Installer l’add-on **Pironman 5**
---------------------------------------------

Passons maintenant à l’installation de l’add-on **Pironman 5**.

#. Ouvrez **Paramètres** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Cliquez sur le signe plus en bas à droite pour accéder à la boutique.

   .. image:: img/home_addon.png
      :width: 90%

#. Recherchez **Pironman 5** dans la liste des add-ons **SunFounder**, puis cliquez dessus.

   .. image:: img/home_pironman5_addon.png
      :width: 90%

#. Installez l’add-on Pironman 5.

   .. image:: img/home_install_pironman5.png
      :width: 90%

#. Une fois l’installation terminée, cliquez sur **START** pour le lancer. L’écran OLED affichera alors des informations telles que l’utilisation CPU, la température et d’autres données système. Quatre LED RGB WS2812 s’allumeront en bleu avec un effet de respiration.

   .. image:: img/home_start_pironman5.png
      :width: 90%

#. Cliquez sur **OPEN WEB UI** pour ouvrir l’interface Web du Pironman 5. Vous pouvez aussi cocher l’option pour afficher cette interface dans la barre latérale de Home Assistant, afin d’y accéder rapidement.

   .. image:: img/home_web_ui.png
      :width: 90%

#. Vous pourrez ensuite consulter les informations de votre Raspberry Pi, configurer les LED RGB, contrôler le ventilateur, etc.

   .. image:: img/home_web_new.png
      :width: 90%

.. note::

    Pour en savoir plus sur l’interface Web du Pironman 5 et ses fonctionnalités, veuillez consulter : :ref:`view_control_dashboard`.

