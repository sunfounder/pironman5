
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _install_os_sd_rpi_promax:

Installation du système d'exploitation
==============================================================

Avant d'utiliser votre Raspberry Pi, vous devez installer **Raspberry Pi OS** sur une carte microSD.
Ce guide explique comment faire cela en utilisant **Raspberry Pi Imager** de manière simple et adaptée aux débutants.

**Composants requis**

* Un ordinateur (Windows, macOS ou Linux)
* Une carte microSD (16 Go ou plus ; marques recommandées : SanDisk, Samsung)
* Un lecteur de carte microSD

-------------------

.. start_install_imager

1. Installer Raspberry Pi Imager
-------------------------------------------

.. |shared_link_rpi_imager| raw:: html

    <a href="https://www.raspberrypi.com/software/" target="_blank">Raspberry Pi Imager</a>

#. Visitez la page de téléchargement officielle de Raspberry Pi Imager : |shared_link_rpi_imager|. Téléchargez le programme d'installation correct pour votre système d'exploitation.

   .. image:: img/imager_download.png
      :width: 70%

#. Suivez les instructions d'installation (langue, chemin d'installation, confirmation). Après l'installation, lancez **Raspberry Pi Imager** depuis votre bureau ou votre menu d'applications.

   .. image:: img/imager_install.png
      :width: 90%

.. end_install_imager

-------------------

2. Installer le système d'exploitation sur la carte microSD
------------------------------------------------------------------------

1. Insérez votre carte microSD dans votre ordinateur à l'aide d'un lecteur de carte. Sauvegardez toutes les données importantes avant de continuer.

   .. image:: img/insert_sd.png
      :width: 90%

2. Lorsque Raspberry Pi Imager s'ouvre, vous verrez la page **Périphérique**. Sélectionnez votre modèle Raspberry Pi 5 dans la liste.

   .. image:: img/imager_device.png
      :width: 90%

3. Allez dans la section **Système d'exploitation** et choisissez l'option recommandée **Raspberry Pi OS (64-bit)**.

   .. warning::

      Veillez à choisir une version **64 bits**. Si vous installez un système **32 bits**, certains paquets ne sont disponibles que pour ``aarch64`` (64 bits), et certaines fonctionnalités risquent de ne pas s’installer ou de ne pas fonctionner correctement.

   .. image:: img/imager_os.png
      :width: 90%

4. Dans la section **Stockage**, sélectionnez votre carte microSD.

   .. image:: img/imager_storage.png
      :width: 90%

   .. start_install_os

5. Cliquez sur **Suivant** pour passer à l'étape de personnalisation.

   .. note::

      * Si vous allez connecter un moniteur, un clavier et une souris directement à votre Raspberry Pi, vous pouvez cliquer sur **IGNORER LA PERSONNALISATION**.
      * Si vous prévoyez de configurer le Raspberry Pi *headless* (accès à distance via Wi-Fi), vous devez compléter les paramètres de personnalisation.

   .. image:: img/imager_custom_skip.png
      :width: 90%

#. **Définir le nom d'hôte**

   * Donnez un nom d'hôte unique à votre Raspberry Pi.
   * Vous pourrez vous y connecter plus tard en utilisant ``nomhôte.local``.

   .. image:: img/imager_custom_hostname.png
      :width: 90%

#. **Définir la localisation**

   * Choisissez votre ville capitale.
   * Imager complétera automatiquement le fuseau horaire et la disposition du clavier en fonction de votre sélection, mais vous pouvez les ajuster si nécessaire. Sélectionnez Suivant.

   .. image:: img/imager_custom_local.png
      :width: 90%

#. **Définir le nom d'utilisateur et le mot de passe**

   Créez un compte utilisateur pour votre Raspberry Pi.

   .. image:: img/imager_custom_user.png
      :width: 90%

#. **Configurer le Wi-Fi**

   * Entrez votre **SSID** Wi-Fi (nom du réseau) et votre **mot de passe**.
   * Votre Raspberry Pi se connectera automatiquement au premier démarrage.

   .. image:: img/imager_custom_wifi.png
      :width: 90%

#. **Activer SSH (Optionnel mais recommandé)**

   * Activer SSH vous permet de vous connecter à distance depuis votre ordinateur.
   * Vous pouvez vous connecter en utilisant votre nom d'utilisateur/mot de passe ou configurer des clés SSH.

   .. image:: img/imager_custom_ssh.png
      :width: 90%

#. **Activer Raspberry Pi Connect (Optionnel)**

   Raspberry Pi Connect vous permet d'accéder au bureau de votre Raspberry Pi depuis un navigateur web.

   * Activez **Raspberry Pi Connect**, puis cliquez sur **OUVRIR RASPBERRY PI CONNECT**.

     .. image:: img/imager_custom_connect.png
        :width: 90%

   * Le site web de Raspberry Pi Connect s'ouvrira dans votre navigateur par défaut. Connectez-vous à votre compte Raspberry Pi ID, ou inscrivez-vous si vous n'en avez pas encore.

     .. image:: img/imager_custom_open.png
        :width: 90%

   * Sur la page **Nouvelle clé d'authentification**, créez votre clé d'authentification à usage unique.

      * Si votre compte Raspberry Pi ID ne fait partie d'aucune organisation, sélectionnez **Créer une clé d'authentification et lancer Raspberry Pi Imager**.
      * Si vous appartenez à une ou plusieurs organisations, choisissez-en une, puis créez la clé et lancez Imager.
      * Assurez-vous d'allumer votre Raspberry Pi et de le connecter à Internet avant l'expiration de la clé.

     .. image:: img/imager_custom_authkey.png
        :width: 90%

   * Votre navigateur peut demander l'autorisation d'ouvrir Raspberry Pi Imager — autorisez-le.

     * Imager s'ouvrira sur l'onglet Raspberry Pi Connect, montrant le jeton d'authentification.
     * Si le jeton ne se transfère pas automatiquement, ouvrez la section **Having trouble?** sur la page Raspberry Pi Connect, copiez le jeton et collez-le manuellement dans Imager.

     .. image:: img/imager_custom_connect_token.png
        :width: 90%

#. Vérifiez tous les paramètres et cliquez sur **ÉCRIRE**.

   .. image:: img/imager_writing.png
      :width: 90%

#. Si la carte contient déjà des données, Raspberry Pi Imager affichera un avertissement indiquant que toutes les données sur le périphérique seront effacées. Vérifiez que vous avez sélectionné le bon lecteur, puis cliquez sur **JE COMPRENDS, EFFACER ET ÉCRIRE** pour continuer.

   .. image:: img/imager_erase.png
      :width: 90%

#. Attendez la fin de l'écriture et de la vérification. Une fois terminé, Raspberry Pi Imager affichera **Écriture réussie !** ainsi qu'un résumé de vos choix. Le périphérique de stockage sera éjecté automatiquement pour que vous puissiez le retirer en toute sécurité.

   .. image:: img/imager_finish.png
        :width: 90%

   .. end_install_os

#. Retirez la carte microSD et insérez-la dans l'emplacement situé sous votre Raspberry Pi. Votre Raspberry Pi est maintenant prêt à démarrer avec le nouveau système d'exploitation !

   .. image:: img/os_sd_to_pi.jpg
        :width: 70%
