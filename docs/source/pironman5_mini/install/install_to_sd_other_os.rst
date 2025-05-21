.. note::

    Bonjour et bienvenue dans la communauté SunFounder dédiée aux passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez au cœur de l'univers Raspberry Pi, Arduino et ESP32 aux côtés d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l’aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Accédez en exclusivité aux annonces et aperçus de nouveaux produits.
    - **Réductions spéciales** : Profitez de promotions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des concours et offres spéciales pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès maintenant !

.. _install_to_sd_home_bridge_mini:

Installation du système d’exploitation sur une carte Micro SD
================================================================

Si vous utilisez une carte Micro SD, vous pouvez suivre le tutoriel ci-dessous pour y installer le système.


**Composants requis**

* Un ordinateur personnel
* Une carte Micro SD et un lecteur de carte

**Étapes**

#. Insérez votre carte SD dans votre ordinateur ou ordinateur portable à l’aide d’un lecteur.

#. Dans l’outil |link_rpi_imager|, cliquez sur **Raspberry Pi Device** et sélectionnez le modèle **Raspberry Pi 5** dans la liste déroulante.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%


#. Cliquez sur l’onglet **Système d’exploitation**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Faites défiler la page jusqu’en bas et sélectionnez votre système d’exploitation.

   .. note::

      * Pour le système **Ubuntu**, cliquez sur **Other general-purpose OS** -> **Ubuntu**, puis choisissez **Ubuntu Desktop 24.04 LTS (64 bits)** ou **Ubuntu Server 24.04 LTS (64 bits)**.
      * Pour **Kali Linux**, **Home Assistant** ou **Homebridge**, cliquez sur **Other specific-purpose OS** et sélectionnez le système correspondant.

   .. image:: img/os_other_os.png
      :width: 90%

#. Dans l’option **Stockage**, sélectionnez le périphérique approprié pour l’installation.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%


#. Cliquez sur **SUIVANT**.

   .. note::

      * Pour les systèmes non configurables à l’avance, après avoir cliqué sur **SUIVANT**, vous serez invité à confirmer la sauvegarde des données sur l’appareil. Si la sauvegarde est faite, sélectionnez **Oui**.

      * Pour les systèmes configurables (nom d’hôte, Wi-Fi, SSH), une fenêtre apparaîtra vous demandant si vous souhaitez appliquer les paramètres personnalisés. Choisissez **Oui**, **Non** ou revenez pour les modifier.

   .. image:: img/os_enter_setting.png
      :width: 90%


   * Définissez un **nom d’hôte** pour votre Raspberry Pi. Il s’agit de son identifiant réseau. Vous pourrez y accéder via ``<hostname>.local`` ou ``<hostname>.lan``.

     .. image:: img/os_set_hostname.png

   * Créez un **nom d’utilisateur** et un **mot de passe** pour le compte administrateur du Raspberry Pi. Il est essentiel de sécuriser votre appareil avec des identifiants personnalisés.

     .. image:: img/os_set_username.png

   * Configurez le réseau Wi-Fi en saisissant le **SSID** et le **mot de passe** de votre réseau.

     .. note::

       Définissez le ``Wireless LAN country`` en utilisant le code à deux lettres `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondant à votre pays.

     .. image:: img/os_set_wifi.png

   * Pour vous connecter à distance à votre Raspberry Pi, activez le SSH dans l’onglet Services.

     * Pour une **authentification par mot de passe**, utilisez les identifiants saisis précédemment.
     * Pour une authentification par clé publique, sélectionnez "Autoriser uniquement l'authentification par clé publique". Si vous possédez une clé RSA, elle sera utilisée, sinon cliquez sur "Exécuter SSH-keygen" pour en générer une.

     .. image:: img/os_enable_ssh.png

   * Le menu **Options** vous permet de définir le comportement d’Imager après l’écriture, comme jouer un son à la fin, éjecter le support ou activer la télémétrie.

     .. image:: img/os_options.png

#. Une fois la personnalisation terminée, cliquez sur **Enregistrer**, puis sur **Oui** pour appliquer les paramètres lors de l’écriture de l’image.

   .. image:: img/os_click_yes.png
      :width: 90%


#. Si la carte SD contient déjà des données, veillez à les sauvegarder pour éviter toute perte. Cliquez sur **Oui** si vous n’avez pas besoin de sauvegarde.

   .. image:: img/os_continue.png
      :width: 90%


#. Lorsque la fenêtre "Écriture réussie" apparaît, l’image a été écrite et vérifiée avec succès. Vous êtes maintenant prêt(e) à démarrer votre Raspberry Pi à partir de la carte Micro SD !
