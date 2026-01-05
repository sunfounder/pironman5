Installing Umbrel OS
============================================

Umbrel is an open-source, self-hosted home-server platform/OS that lets you run your own Bitcoin node, install a variety of one-click self-hosted apps — and turn your hardware into your personal home cloud. It’s an excellent way to start with self-custody and privacy.

**Required Components**

* A Personal Computer
* A NVMe SSD
* A NVMe to USB Adapter
* Micro SD Card and Reader

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Install the OS on the NVMe SSD
-----------------------------------

Now you are ready to install the operating system onto your **NVMe SSD**.  
Just follow the steps below carefully — this guide is written for beginners and is easy to follow.

.. |link_umbrel_release| raw:: html

    <a href="https://github.com/getumbrel/umbrel/releases" target="_blank">Umbrel OS Releases</a>

#. Download the latest **Umbrel OS** image and extract the file. If you want to use a specific version, you can also visit the |link_umbrel_release| page.

   * :download:`Latest Umbrel OS Image <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

#. Insert the **NVMe SSD** into your computer using an **NVMe to USB adapter**.

#. Open **Raspberry Pi Imager**. On the **Device** screen, select your **Raspberry Pi 5** model from the list.

   .. image:: img/imager_device.png
      :width: 90%

#. Go to the **OS** section, scroll to the bottom, and select **Use custom**.

   .. image:: img/imager_use_custom.png
      :width: 90%

#. Select the **Umbrel OS image file** you downloaded and extracted earlier, then click **Open**.

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

#. Click **Next** to continue.

   .. image:: img/imager_custom_next.png
      :width: 90%

#. In the **Storage** section, select your **NVMe SSD**. Make sure you choose the NVMe SSD and not another drive on your computer.

   .. image:: img/nvme_storage.png
      :width: 90%

#. Review all settings carefully, then click **WRITE**.

   .. image:: img/imager_write_umbrel.png
      :width: 90%

#. If the NVMe SSD already contains data, Raspberry Pi Imager will warn you that all data will be erased. Double-check that the correct drive is selected, then click **I UNDERSTAND, ERASE AND WRITE**.

   .. image:: img/imager_erase.png
      :width: 90%

#. When the **“Write Complete”** message appears, the image has been written and verified successfully. 

   .. image:: img/imager_umbrel_finish.png
      :width: 90%

