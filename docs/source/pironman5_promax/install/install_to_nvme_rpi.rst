
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _install_to_nvme_rpi_promax:

Installation du système d'exploitation sur un SSD NVMe
=========================================================================

Si vous utilisez un SSD NVMe et disposez d'un adaptateur pour connecter le SSD NVMe à votre ordinateur afin d'installer le système, vous pouvez utiliser le tutoriel suivant pour une installation rapide.

**Composants requis**

* Un ordinateur personnel
* Un SSD NVMe
* Un adaptateur NVMe vers USB
* Une carte Micro SD et un lecteur de carte

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

.. start_update_bootloader

.. _update_bootloader_promax:

2. Mettre à jour le chargeur d'amorçage
----------------------------------------------------------

Tout d'abord, mettez à jour le chargeur d'amorçage du Raspberry Pi 5 pour qu'il tente de démarrer d'abord depuis **NVMe**, puis **USB**, et enfin la **carte SD**.

.. note::

    Il est recommandé d'utiliser une **carte Micro SD de rechange** pour cette étape.

    - Méthode 1 (Recommandée) : Écrire le chargeur d'amorçage sur une carte Micro SD, l'insérer dans le Raspberry Pi, et démarrer une fois pour appliquer le paramètre.
    - Méthode 2 : Écrire le chargeur d'amorçage directement sur le SSD NVMe. Ensuite, connectez le NVMe à un ordinateur pour installer le système d'exploitation, puis remettez-le dans le Raspberry Pi.

#. Insérez la **carte Micro SD de rechange ou le SSD NVMe** dans votre ordinateur à l'aide d'un lecteur de carte ou d'un adaptateur.

#. Lorsque Raspberry Pi Imager s'ouvre, vous verrez la page **Périphérique**. Sélectionnez votre modèle Raspberry Pi 5 dans la liste.

   .. image:: img/imager_device.png
      :width: 90%

#. Cliquez sur **Système d'exploitation**.

   * Descendez et sélectionnez **Images utilitaires diverses**.

     .. image:: img/nvme_misc.png
        :width: 90%

   * Sélectionnez **Chargeur d'amorçage (Famille Pi 5)**.

     .. image:: img/nvme_bootloader.png
        :width: 90%

   * Choisissez **Démarrage NVMe/USB** pour définir l'ordre de démarrage, puis cliquez sur **SUIVANT**.

     .. image:: img/nvme_boot.png
        :width: 90%

#. Dans **Stockage**, sélectionnez la bonne carte Micro SD ou le bon SSD NVMe, puis cliquez sur **SUIVANT**.

   .. note::

      Assurez-vous que le bon périphérique est sélectionné. Déconnectez les autres périphériques de stockage si nécessaire.

   .. image:: img/imager_storage.png
      :width: 90%

#. Vérifiez les paramètres et cliquez sur **ÉCRIRE** pour commencer.

   .. image:: img/nvme_write.png
      :width: 90%

#. Confirmez l'avertissement et permettez à Raspberry Pi Imager d'effacer et d'écrire le chargeur d'amorçage.

   .. image:: img/imager_erase.png
      :width: 90%

#. Attendez que **Écriture réussie !** apparaisse, puis retirez le périphérique de stockage en toute sécurité.

   .. image:: img/nvme_finish.png
      :width: 90%

#. Insérez la carte Micro SD dans le Raspberry Pi et allumez-le une fois pour appliquer la mise à jour du chargeur d'amorçage.

   .. image:: img/os_sd_to_pi.jpg
      :width: 70%

#. Attendez au moins **10 secondes** après la fin du démarrage du Raspberry Pi, puis éteignez-le et retirez la carte Micro SD ou le SSD NVMe.

Le Raspberry Pi 5 est maintenant prêt à démarrer depuis **NVMe**.

.. end_update_bootloader

3. Installer le système d'exploitation sur le SSD NVMe
-------------------------------------------------------------

Vous pouvez maintenant installer le système d'exploitation sur votre SSD NVMe.

#. Insérez le **SSD NVMe** dans votre ordinateur à l'aide d'un adaptateur.

2. Lorsque Raspberry Pi Imager s'ouvre, vous verrez la page **Périphérique**. Sélectionnez votre modèle Raspberry Pi 5 dans la liste.

   .. image:: img/imager_device.png
      :width: 90%

3. Allez dans la section **Système d'exploitation** et choisissez l'option recommandée **Raspberry Pi OS (64-bit)**.

   .. warning::

      Veillez à choisir une version **64 bits**. Si vous installez un système **32 bits**, certains paquets ne sont disponibles que pour ``aarch64`` (64 bits), et certaines fonctionnalités risquent de ne pas s’installer ou de ne pas fonctionner correctement.

   .. image:: img/imager_os.png
      :width: 90%

4. Dans la section **Stockage**, sélectionnez votre **SSD NVMe**.

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os
