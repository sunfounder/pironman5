.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _install_to_nvme_rpi_mini:

Installation du système d’exploitation sur un SSD NVMe
=========================================================

Si vous utilisez un SSD NVMe et disposez d’un adaptateur pour connecter le SSD NVMe à votre ordinateur afin d’installer le système, vous pouvez suivre le tutoriel ci-dessous pour une installation rapide.

**Composants requis**

* Un ordinateur personnel
* Un SSD NVMe
* Un adaptateur NVMe vers USB
* Une carte Micro SD et un lecteur de cartes


.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

.. start_update_bootloader

.. _update_bootloader_mini:


2. Mettre à jour le bootloader
--------------------------------

Commencez par mettre à jour le bootloader du Raspberry Pi 5 afin qu’il tente de démarrer **d’abord depuis le NVMe**, puis **l’USB**, et enfin **la carte SD**.

.. note::

    Il est recommandé d’utiliser une **carte Micro SD de rechange** pour cette étape.
    
    - Méthode 1 (recommandée) : Écrire le bootloader sur une carte Micro SD, l’insérer dans le Raspberry Pi, puis démarrer une fois pour appliquer le réglage.
    - Méthode 2 : Écrire le bootloader directement sur le SSD NVMe. Ensuite, connecter le NVMe à un ordinateur pour installer le système d’exploitation, puis le remettre dans le Raspberry Pi.

#. Insérez la **carte Micro SD de rechange ou le SSD NVMe** dans votre ordinateur à l’aide d’un lecteur de cartes ou d’un adaptateur.

#. Lorsque Raspberry Pi Imager s’ouvre, vous verrez la page **Device**. Sélectionnez votre modèle de **Raspberry Pi 5** dans la liste.

   .. image:: img/imager_device.png
      :width: 90%

#. Cliquez sur **OS**.

   * Faites défiler vers le bas et sélectionnez **Misc utility images**.

     .. image:: img/nvme_misc.png
        :width: 90%

   * Sélectionnez **Bootloader (Pi 5 family)**.

     .. image:: img/nvme_bootloader.png
        :width: 90%

   * Choisissez **NVMe/USB Boot** pour définir l’ordre de démarrage, puis cliquez sur **NEXT**.

     .. image:: img/nvme_boot.png
        :width: 90%


#. Dans **Storage**, sélectionnez la carte Micro SD ou le SSD NVMe approprié, puis cliquez sur **NEXT**.

   .. note::

      Assurez-vous que le bon périphérique est sélectionné. Déconnectez les autres périphériques de stockage si nécessaire.

   .. image:: img/imager_storage.png
      :width: 90%


#. Vérifiez les paramètres et cliquez sur **WRITE** pour démarrer l’opération.

   .. image:: img/nvme_write.png
      :width: 90%

#. Confirmez l’avertissement et autorisez Raspberry Pi Imager à effacer et écrire le bootloader.

   .. image:: img/imager_erase.png
      :width: 90%

#. Attendez que **Write complete!** apparaisse, puis retirez le périphérique de stockage en toute sécurité.

   .. image:: img/nvme_finish.png
      :width: 90%

#. Insérez la carte Micro SD dans le Raspberry Pi et allumez-le une fois afin d’appliquer la mise à jour du bootloader.

   .. image:: img/os_sd_to_pi.jpg
      :width: 70%

#. Attendez au moins **10 secondes** après que le Raspberry Pi a terminé le démarrage, puis éteignez-le et retirez la carte Micro SD ou le SSD NVMe.

Le Raspberry Pi 5 est maintenant prêt à démarrer depuis le **NVMe**.

.. end_update_bootloader

3. Installer le système d’exploitation sur le SSD NVMe
------------------------------------------------------------------

Vous pouvez maintenant installer le système d’exploitation sur votre SSD NVMe.

#. Insérez le **SSD NVMe** dans votre ordinateur à l’aide d’un adaptateur.

2. Lorsque Raspberry Pi Imager s’ouvre, vous verrez la page **Device**. Sélectionnez votre modèle de **Raspberry Pi 5** dans la liste.

   .. image:: img/imager_device.png
      :width: 90%

3. Accédez à la section **OS** et choisissez l’option recommandée **Raspberry Pi OS (64-bit)**.

   .. image:: img/imager_os.png
      :width: 90%

4. Dans la section **Storage**, sélectionnez votre **SSD NVMe**.

   .. image:: img/nvme_storage.png
      :width: 90%

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_os
   :end-before: end_install_os

