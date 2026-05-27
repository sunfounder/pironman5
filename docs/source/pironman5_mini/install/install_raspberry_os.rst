.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Instalar Raspberry Pi OS
================================================================================

Puedes elegir un método de instalación según si dispones de una tarjeta Micro SD o de un SSD NVMe.

**Usar solo una tarjeta Micro SD**

  Si solo utilizas una tarjeta Micro SD, puedes seguir directamente el primer método que se describe a continuación.

**Usar un SSD M.2 NVMe**

  * Si tienes un **adaptador/carcasa para SSD M.2 NVMe**, puedes conectar tu SSD al ordenador mediante el adaptador y seguir el segundo método para instalar el sistema operativo.  

    .. image:: img/m2_nvme_adapter.png  
        :width: 300
        :align: center
  
  * Si no tienes el adaptador mostrado arriba, puedes instalar primero el sistema operativo en una tarjeta Micro SD usando el primer método y, a continuación, utilizar el tercer método para copiar el sistema desde la tarjeta Micro SD a tu SSD M.2 NVMe.  

.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi