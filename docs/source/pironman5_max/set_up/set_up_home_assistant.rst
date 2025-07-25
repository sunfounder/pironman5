.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d'autres passionnés pour approfondir vos connaissances et projets autour de Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes techniques et après-vente avec l’aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales** : Profitez d’offres exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et événements spéciaux pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

Configuration sous Home Assistant
============================================

Si vous avez installé le système Home Assistant, vous devrez ajouter les modules complémentaires nécessaires et les activer pour faire fonctionner le Pironman 5 MAX.

.. note::

    La méthode suivante s’applique uniquement aux systèmes avec Home Assistant installé en natif. Elle ne s’applique pas aux systèmes Raspberry Pi avec Home Assistant installé par-dessus un autre OS, ni aux versions Docker.

1. Connexion à Home Assistant
-----------------------------

* Après le démarrage du Pironman 5 MAX, il est recommandé de brancher un câble Ethernet. Vous pouvez ensuite ouvrir un navigateur sur votre ordinateur et accéder à : ``homeassistant.local:8123``.

  .. image:: img/home_login.png
   :width: 90%


* Cliquez sur **CREATE MY SMART HOME**, puis créez votre compte.

  .. image:: img/home_account.png
   :width: 90%

* Suivez les étapes pour choisir votre localisation et les paramètres. Une fois terminé, vous accéderez au tableau de bord de Home Assistant.

  .. image:: img/home_dashboard.png
   :width: 90%


2. Ajouter le dépôt de modules SunFounder
----------------------------------------------------

Les fonctionnalités de Pironman 5 MAX sont fournies sous forme de modules complémentaires dans Home Assistant. Commencez par ajouter le dépôt **SunFounder**.

#. Allez dans **Settings** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Cliquez sur le signe plus en bas à droite pour ouvrir le store des modules.

   .. image:: img/home_addon.png
      :width: 90%

#. Dans le store, cliquez sur le menu en haut à droite puis sélectionnez **Repositories**.

   .. image:: img/home_add_res.png
      :width: 90%

#. Saisissez l’URL du dépôt SunFounder : ``https://github.com/sunfounder/home-assistant-addon``, puis cliquez sur **ADD**.

   .. image:: img/home_res_add.png
      :width: 90%

#. Une fois le dépôt ajouté, fermez la fenêtre pop-up et actualisez la page. Recherchez la liste des modules SunFounder.

   .. image:: img/home_addon_list.png
         :width: 90%

3. Installer le module **Pi Config Wizard**
------------------------------------------------------

Le module **Pi Config Wizard** permet d’activer les fonctionnalités nécessaires comme I2C et SPI pour le fonctionnement du Pironman 5 MAX. Il peut être supprimé par la suite si non nécessaire.

#. Dans la liste SunFounder, cliquez sur **Pi Config Wizard**.

   .. image:: img/home_pi_config.png
      :width: 90%

#. Sur la page du module, cliquez sur **INSTALL** et attendez la fin de l’installation.

   .. image:: img/home_config_install.png
      :width: 90%

#. Une fois installé, passez à l’onglet **Log** pour vérifier l’absence d’erreurs.

   .. image:: img/home_log.png
      :width: 90%

#. S’il n’y a pas d’erreurs, revenez à l’onglet **Info** et cliquez sur **START** pour démarrer le module.

   .. image:: img/home_start.png
      :width: 90%

#. Cliquez ensuite sur OPEN WEB UI pour accéder à l’interface web.

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. Dans l’interface web, vous verrez une option pour monter la partition Boot. Cliquez sur **MOUNT**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Une fois montée, vous pourrez activer I2C et SPI, et modifier le fichier config.txt. Cochez I2C et SPI. Quand ils s’affichent comme activés, cliquez sur le bouton de redémarrage en bas.

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. Après redémarrage, actualisez la page. Vous reviendrez à l’écran de montage. Cliquez à nouveau sur **MOUNT**.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. En général, SPI sera activé mais pas I2C, car ce dernier nécessite deux redémarrages. Réactivez I2C puis redémarrez à nouveau.

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. Après le redémarrage, retournez sur la page **MOUNT**. Vous verrez que I2C et SPI sont tous deux activés.

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * Si la page de montage ne s’affiche pas après actualisation, allez dans **Settings** -> **Add-ons** -> **Pi Config Wizard**.
    * Vérifiez que le module est lancé. Sinon, cliquez sur **START**.
    * Une fois démarré, cliquez sur **OPEN WEB UI**, puis sur **MOUNT** pour vérifier que I2C et SPI sont bien activés.

4. Installer le module **Pironman 5 MAX**
---------------------------------------------

Il est temps d’installer officiellement le module **Pironman 5 MAX** .

#. Allez dans **Settings** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Cliquez sur le signe plus en bas à droite pour ouvrir le store.

   .. image:: img/home_addon.png
      :width: 90%

#. Trouvez **Pironman 5 MAX** dans la liste **SunFounder** et cliquez dessus.

   .. image:: img/home_pironman5_max_addon.png
      :width: 90%

#. Installez le module Pironman 5 MAX.

   .. image:: img/home_pironman5_max_addon_install.png
      :width: 90%

#. Une fois l’installation terminée, cliquez sur **START** pour lancer le module. L’écran OLED affichera les informations CPU, température, etc. Quatre LED WS2812 s’allumeront en bleu avec effet respirant.

   .. image:: img/home_pironman5_max_addon_start.png
      :width: 90%

#. Cliquez sur **OPEN WEB UI** pour accéder à la page web de Pironman 5 MAX. Vous pouvez également activer l’affichage de l’interface dans la barre latérale de Home Assistant.

   .. image:: img/home_pironman5_max_webui.png
      :width: 90%

#. Vous pourrez y visualiser les informations système, configurer les LED RGB, contrôler les ventilateurs, etc.

   .. image:: img/home_web.png
      :width: 90%

.. note::

    Pour plus d’informations sur l’utilisation de l’interface web de Pironman 5 MAX, veuillez consulter : :ref:`max_view_control_dashboard`.
