.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Installare Raspberry Pi OS
================================================================================

Puoi scegliere il metodo di installazione in base alla disponibilità di una scheda Micro SD o di un SSD NVMe.

**Utilizzando solo una scheda Micro SD**

  Se utilizzi esclusivamente una scheda Micro SD, puoi semplicemente seguire il primo metodo riportato di seguito.

**Utilizzando un SSD M.2 NVMe**

  * Se disponi di un **adattatore enclosure per SSD M.2 NVMe**, puoi collegare l’SSD al computer tramite l’adattatore e seguire il secondo metodo per installare il sistema operativo.  

    .. image:: img/m2_nvme_adapter.png  
        :width: 300
        :align: center
  
  * Se non disponi dell’adattatore mostrato sopra, puoi prima installare il sistema operativo su una scheda Micro SD utilizzando il primo metodo, quindi usare il terzo metodo per copiare il sistema dalla scheda Micro SD al tuo SSD M.2 NVMe.  

.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi