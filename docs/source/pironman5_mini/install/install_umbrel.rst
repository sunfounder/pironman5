.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Installation d’Umbrel OS
============================================

Umbrel est une plateforme / un système d’exploitation open source de serveur domestique auto-hébergé qui vous permet d’exécuter votre propre nœud Bitcoin, d’installer une variété d’applications auto-hébergées en un clic — et de transformer votre matériel en cloud personnel à domicile. C’est une excellente façon de débuter avec l’auto-garde et la protection de la vie privée.

**Composants requis**

* Un ordinateur personnel
* Un SSD NVMe
* Un adaptateur NVMe vers USB
* Une carte Micro SD et un lecteur de cartes

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installer le système d’exploitation sur le SSD NVMe
-----------------------------------------------------------

Vous êtes maintenant prêt à installer le système d’exploitation sur votre **SSD NVMe**.  
Suivez simplement les étapes ci-dessous avec attention — ce guide est destiné aux débutants et est facile à suivre.

.. |link_umbrel_release| raw:: html

    <a href="https://github.com/getumbrel/umbrel/releases" target="_blank">Versions d’Umbrel OS</a>

#. Téléchargez la dernière image **Umbrel OS** et extrayez le fichier. Si vous souhaitez utiliser une version spécifique, vous pouvez également consulter la page |link_umbrel_release|.

   * :download:`Dernière image Umbrel OS <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

#. Insérez le **SSD NVMe** dans votre ordinateur à l’aide d’un **adaptateur NVMe vers USB**.

#. Ouvrez **Raspberry Pi Imager**. Sur l’écran **Device**, sélectionnez votre modèle de **Raspberry Pi 5** dans la liste.

   .. image:: img/imager_device.png
      :width: 90%

#. Accédez à la section **OS**, faites défiler jusqu’en bas, puis sélectionnez **Use custom**.

   .. image:: img/imager_use_custom.png
      :width: 90%

#. Sélectionnez le **fichier image Umbrel OS** que vous avez téléchargé et extrait précédemment, puis cliquez sur **Open**.

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

#. Cliquez sur **Next** pour continuer.

   .. image:: img/imager_custom_next.png
      :width: 90%

#. Dans la section **Storage**, sélectionnez votre **SSD NVMe**. Assurez-vous de choisir le SSD NVMe et non un autre disque de votre ordinateur.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Vérifiez attentivement tous les paramètres, puis cliquez sur **WRITE**.

   .. image:: img/imager_write_umbrel.png
      :width: 90%

#. Si le SSD NVMe contient déjà des données, Raspberry Pi Imager vous avertira que toutes les données seront effacées. Vérifiez une dernière fois que le bon disque est sélectionné, puis cliquez sur **I UNDERSTAND, ERASE AND WRITE**.

   .. image:: img/imager_erase.png
      :width: 90%

#. Lorsque le message **« Write Complete »** apparaît, l’image a été écrite et vérifiée avec succès.

   .. image:: img/imager_umbrel_finish.png
      :width: 90%

