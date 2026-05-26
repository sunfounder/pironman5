.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Installation de Raspberry Pi OS
================================================================================

Vous pouvez choisir une méthode d’installation en fonction de la disponibilité d’une carte Micro SD ou d’un SSD NVMe.

**Utiliser uniquement une carte Micro SD**

  Si vous utilisez uniquement une carte Micro SD, vous pouvez simplement suivre la première méthode ci-dessous.

**Utiliser un SSD M.2 NVMe**

  * Si vous disposez d’un **boîtier adaptateur M.2 NVMe**, vous pouvez connecter votre SSD à votre ordinateur à l’aide de cet adaptateur et suivre la deuxième méthode pour installer le système d’exploitation.  

    .. image:: img/m2_nvme_adapter.png  
        :width: 300
        :align: center
  
  * Si vous ne disposez pas de l’adaptateur présenté ci-dessus, vous pouvez d’abord installer le système d’exploitation sur une carte Micro SD en utilisant la première méthode, puis utiliser la troisième méthode pour copier le système depuis la carte Micro SD vers votre SSD M.2 NVMe.

.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi