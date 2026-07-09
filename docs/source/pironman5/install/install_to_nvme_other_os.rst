.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _install_to_nvme_home_bridge:

Installing the OS on an NVMe SSD
============================================

If you are using an NVMe SSD and have an adapter to connect the NVMe SSD to your computer for system installation, you can use the following tutorial for a quick installation.

   .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**Required Components**

* A Personal Computer
* A NVMe SSD
* A NVMe to USB Adapter
* Micro SD Card and Reader

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Install the OS to the microSD Card
------------------------------------------------

#. Insert the **NVMe SSD** into your computer using an adapter.

2. When **Raspberry Pi Imager** opens, you will see the **Device** page.  
   Select your **Raspberry Pi 5** model from the list.

   .. image:: img/imager_device.png
      :width: 90%

3. Go to the **OS** section, scroll down to the bottom of the page, and select your operating system.

   .. note::

      * For **Ubuntu**, click **Other general-purpose OS** → **Ubuntu**, then select  
        **Ubuntu Desktop 24.04 LTS (64-bit)** or **Ubuntu Server 24.04 LTS (64-bit)**.
      * For **Kali Linux**, **Home Assistant**, and **Homebridge**, click  
        **Other specific-purpose OS**, then select the corresponding system.

   .. warning::

      Whichever system you choose, be sure to select a **64-bit** version. On a **32-bit** system, some packages are only available for ``aarch64`` (64-bit), and certain features may fail to install or work properly.

   .. image:: img/imager_other_os.png
      :width: 90%

4. In the **Storage** section, select your **NVMe SSD**. 

   .. image:: img/nvme_storage.png
      :width: 90%

#. Click **NEXT**.

   .. note::

      * For systems that **cannot be configured in advance**, clicking **NEXT** will skip the **Customisation** step and go directly to **Writing**, where the OS is written to the microSD card.
      * For systems that **support pre-configuration**, follow the **Customisation** steps to configure options such as **Hostname**, **WiFi**, and **Enable SSH**.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. When the **“Write Successful”** popup appears, the image has been fully written and verified. You can now safely remove the microSD card and use it to boot your Raspberry Pi.
