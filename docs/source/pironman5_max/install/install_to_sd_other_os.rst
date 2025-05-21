.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d’autres passionnés pour approfondir vos connaissances et vos projets autour de Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes techniques et après-vente grâce à l’aide de notre équipe et de notre communauté.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Soyez parmi les premiers à découvrir nos nouveaux produits et leurs démonstrations.
    - **Réductions spéciales** : Bénéficiez d’offres exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des concours et animations spéciales pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _max_install_to_sd_home_bridge:

Installation du système d’exploitation sur une carte Micro SD
=================================================================

Si vous utilisez une carte Micro SD, vous pouvez suivre le tutoriel ci-dessous pour y installer le système.


**Composants requis**

* Un ordinateur personnel
* Une carte Micro SD et un lecteur

**Étapes**

#. Insérez la carte SD dans votre ordinateur ou ordinateur portable à l’aide d’un lecteur.

#. Dans le |link_rpi_imager|, cliquez sur **Raspberry Pi Device** et sélectionnez le modèle **Raspberry Pi 5** dans la liste déroulante.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. Cliquez sur l’onglet **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Faites défiler jusqu’en bas de la page et sélectionnez votre système d’exploitation.

   .. note::

      * Pour le système **Ubuntu**, cliquez sur **Other general-purpose OS** → **Ubuntu**, puis sélectionnez **Ubuntu Desktop 24.04 LTS (64 bit)** ou **Ubuntu Server 24.04 LTS (64 bit)**.
      * Pour les systèmes **Kali Linux**, **Home Assistant** et **Homebridge**, cliquez sur **Other specific-purpose OS**, puis choisissez le système correspondant.

   .. image:: img/os_other_os.png
      :width: 90%

#. Dans l’option **Storage**, sélectionnez le périphérique de stockage adéquat pour l’installation.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Cliquez sur **NEXT**.

   .. note::

      * Pour les systèmes ne permettant pas de configuration préalable, un message vous invitera à confirmer l'effacement des données. Si une sauvegarde a été effectuée, cliquez sur **Yes**.
      
      * Pour les systèmes permettant la configuration du nom d’hôte, du Wi-Fi et de l’accès SSH, une fenêtre s’ouvrira pour vous demander si vous souhaitez appliquer ces paramètres. Vous pouvez cliquer sur **Yes**, **No** ou revenir pour modifier les réglages.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Définissez un **hostname** pour votre Raspberry Pi. Il s’agit de son identifiant réseau. Vous pouvez y accéder via ``<hostname>.local`` ou ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png  

   * Créez un **Username** et un **Password** pour le compte administrateur. Un identifiant personnalisé est essentiel pour sécuriser votre Raspberry Pi, qui n’a pas de mot de passe par défaut.

     .. image:: img/os_set_username.png

   * Configurez le réseau sans fil en renseignant le **SSID** de votre Wi-Fi et son **Password**.

     .. note::

       Définissez le ``Wireless LAN country`` à l’aide du code alpha-2 à deux lettres défini par la norme `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondant à votre pays.

     .. image:: img/os_set_wifi.png

   * Pour accéder à distance à votre Raspberry Pi, activez le SSH dans l’onglet Services.

     * Pour **password authentication**, utilisez le nom d’utilisateur et le mot de passe définis dans l’onglet General.
     * Pour l’authentification par clé publique, sélectionnez « Autoriser uniquement l’authentification par clé publique ». Si une clé RSA est présente, elle sera utilisée. Sinon, cliquez sur « Exécuter SSH-keygen » pour générer une nouvelle paire de clés.

     .. image:: img/os_enable_ssh.png

   * Le menu **Options** permet de configurer le comportement d’Imager lors de l’écriture, notamment l’émission d’un son en fin de tâche, l’éjection automatique du support et l’activation de la télémétrie.

     .. image:: img/os_options.png

#. Une fois la configuration terminée, cliquez sur **Save** pour enregistrer vos réglages, puis sur **Yes** pour les appliquer lors de l’écriture de l’image.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Si la carte SD contient déjà des données, assurez-vous d’en effectuer une sauvegarde. Cliquez sur **Yes** si aucune sauvegarde n’est nécessaire.

   .. image:: img/os_continue.png
      :width: 90%


#. Lorsque la fenêtre « Write Successful » s’affiche, cela signifie que l’image a été correctement écrite et vérifiée. Vous êtes maintenant prêt(e) à démarrer votre Raspberry Pi depuis la carte Micro SD !
