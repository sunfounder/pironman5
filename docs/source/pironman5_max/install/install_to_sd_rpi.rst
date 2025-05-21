.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d'autres passionnés pour explorer plus en profondeur l'univers de Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Bénéficiez de l'aide de notre communauté et de notre équipe pour résoudre les problèmes techniques et après-vente.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives** : Soyez informé(e) en avant-première des annonces et aperçus de nouveaux produits.
    - **Réductions spéciales** : Profitez d'offres exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des jeux-concours et des événements spéciaux pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _max_install_os_sd_rpi:

Installation du système d’exploitation sur une carte Micro SD
=================================================================
Si vous utilisez une carte Micro SD, vous pouvez suivre le tutoriel ci-dessous pour y installer le système.

.. .. raw:: html

..     <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Composants requis**

* Un ordinateur personnel
* Une carte Micro SD et un lecteur

**Étapes**

#. Insérez votre carte SD dans l’ordinateur à l’aide d’un lecteur.

#. Dans le |link_rpi_imager|, cliquez sur **Raspberry Pi Device** et sélectionnez le modèle **Raspberry Pi 5** dans la liste déroulante.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. Sélectionnez **Operating System**, puis choisissez la version recommandée du système d’exploitation.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Cliquez sur **Choose Storage** et sélectionnez le support de stockage adéquat pour l’installation.

   .. image:: img/os_choose_sd.png
      :width: 90%

#. Cliquez sur **NEXT**, puis sur **EDIT SETTINGS** pour personnaliser les paramètres du système.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Définissez un **hostname** pour votre Raspberry Pi. Il s'agit de l'identifiant réseau de votre appareil. Vous pourrez y accéder via ``<hostname>.local`` ou ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png


   * Créez un **Username** et un **Password** pour le compte administrateur. Un identifiant unique est essentiel pour la sécurité de votre Raspberry Pi, qui n’a pas de mot de passe par défaut.

     .. image:: img/os_set_username.png

   * Configurez le réseau sans fil en saisissant le **SSID** de votre Wi-Fi ainsi que son **Password**.

     .. note::

       Définissez le ``Wireless LAN country`` à l’aide du code alpha-2 à deux lettres conforme à la norme `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondant à votre localisation.

     .. image:: img/os_set_wifi.png


   * Pour accéder à distance à votre Raspberry Pi, activez SSH dans l’onglet Services.

     * Pour **password authentication**, utilisez les identifiants définis dans l’onglet General.
     * Pour l’authentification par clé publique, sélectionnez « Autoriser uniquement l’authentification par clé publique ». Si vous disposez d’une clé RSA, elle sera utilisée. Sinon, cliquez sur « Exécuter SSH-keygen » pour générer une nouvelle paire de clés.

     .. image:: img/os_enable_ssh.png

   * Le menu **Options** vous permet de définir le comportement d’Imager pendant l’écriture : émettre un son à la fin, éjecter le support automatiquement, activer la télémétrie, etc.

     .. image:: img/os_options.png

#. Une fois les paramètres personnalisés, cliquez sur **Save** pour les enregistrer, puis sur **Yes** pour les appliquer lors de l’écriture de l’image.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Si la carte SD contient déjà des données, veillez à les sauvegarder. Cliquez sur **Yes** pour continuer si aucune sauvegarde n’est nécessaire.

   .. image:: img/os_continue.png
      :width: 90%


#. Lorsque la fenêtre « Write Successful » s’affiche, l’image a été écrite et vérifiée avec succès. Vous êtes maintenant prêt(e) à démarrer votre Raspberry Pi depuis la carte Micro SD !

   .. image:: img/os_finish.png
      :width: 90%
