.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Pi5 NVMe PIP
=================

The Pi5 NVMe PIP (PCIe Peripheral Board), as defined by the Raspberry Pi Foundation, is a PCIe adapter board designed specifically for NVMe solid-state drives. It supports four different sizes of NVMe SSDs: 2230, 2242, 2260, and 2280, all fitting into an M.2 M key slot.

.. image:: img/nvme_pip.jpeg

* The board connects through a 16P 0.5mm reverse FFC (Flexible Flat Cable) or a custom impedance-matched FPC (Flexible Printed Circuit) cable.
* **STA**: A Status LED indicator.
* **PWR**: A Power LED indicator.
* The onboard 3.3V power supply can support up to 3A output. However, since the Raspberry Pi PCIe interface is limited to providing 5V/1A output (equivalent to 5W), additional power for 3.3V/3A usage can be supplied through the J3 connector from a 5V source.

Configure PCIe
-----------------

**Enabling PCIe**

By default the PCIe connector is not enabled. 

* To enable it you should open the ``/boot/firmware/config.txt`` file.

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* Then add the following line to the file. 

  .. code-block:: shell
  
    # Enable the PCIe External connector.
    dtparam=pciex1
  
* A more memorable alias for ``pciex1`` exists, so you can alternatively add ``dtparam=nvme`` to the ``/boot/firmware/config.txt`` file.

  .. code-block:: shell
  
    dtparam=nvme

.. note::

    Enumeration of PCIe devices behind a switch is not currently supported.

**PCIe Gen 3.0**

* The connection is certified for Gen 2.0 speeds (5 GT/sec), but you can force it to Gen 3.0 (10 GT/sec) if you add the following lines to your ``/boot/firmware/config.txt``.

  .. code-block:: shell
  
    # Force Gen 3.0 speeds
    dtparam=pciex1_gen=3
  
  .. warning::
  
    The Raspberry Pi 5 is not certified for Gen 3.0 speeds, and connections to PCIe devices at these speeds may be unstable.

* You should then reboot your Raspberry Pi for these settings to take effect.

  .. code-block:: shell
  
    sudo reboot
  
About the Model
---------------------------

M.2 SSDs, known for their compact size, come in various types mainly differentiated by their keying (notch design on the connector) and the interface they use. Here are the primary types:

* **M.2 SATA SSDs**: These use the SATA interface, similar to 2.5-inch SATA SSDs but in the smaller M.2 form factor. They are limited by the SATA III maximum speeds of around 600 MB/s. These SSDs are compatible with M.2 slots keyed for B and M keys.
* **M.2 NVMe SSDs**: These SSDs use the NVMe protocol over PCIe lanes and are significantly faster than M.2 SATA SSDs. They are suitable for applications requiring high read/write speeds like gaming, video editing, and data-intensive tasks. These SSDs typically require M-keyed slots. These drives utilize the PCIe (Peripheral Component Interconnect Express) interface, with different versions like 3.0, 4.0, and 5.0. Each new version of PCIe effectively doubles the data transfer speed of its predecessor. However, the Raspberry Pi 5 uses a PCIe 3.0 interface, capable of delivering transfer speeds up to 3,500 MB/s. 

M.2 SSDs come in three key types: B key, M key, and B+M key. However, later on, the B+M key was introduced, combining the functionalities of the B key and M key. As a result, it replaced the standalone B key. Please refer to the image below.

.. image:: img/ssd_key.png


In general, M.2 SATA SSDs are B+M-keyed (can fit in sockets for B-keyed and M-keyed modules), while M.2 NVMe SSDs for PCIe 3.0 x4 lane are M-keyed.

.. image:: img/ssd_model2.png

About the Length
-----------------------

M.2 modules come in different sizes and can also be utilized for Wi-Fi, WWAN, Bluetooth, GPS, and NFC.

Pironman 5 supports four (PCIE2.0 / PCIE 3.0）NVMe M.2 SSD sizes based on their names: 2230, 2242, 2260, and 2280. The "22" is the width in millimeters (mm), and the two following numbers are the length. The longer the drive, the more NAND flash chips can be mounted; therefore, the more capacity.


.. image:: img/m2_ssd_size.png
  :width: 600

Booting from the SSD
-------------------------
After you install the SSD into the Pironman 5 and reboot, an NVMe disk connected through the PCIe should be visible. If you want to boot your Raspberry Pi from the SSD, you need to do some configurations and install an operating system on the SSD.

**1. Configure boot from the SSD**

* To enable boot support, you need to change the ``BOOT_ORDER`` in the bootloader configuration. Edit the EEPROM configuration by:

  .. code-block::
  
    sudo rpi-eeprom-config --edit
  
* Then, change the ``BOOT_ORDER`` line to be as below.

  .. code-block:: shell
  
    BOOT_ORDER=0xf416


**2. Install an Operating System on the SSD**

There are two ways to install an operating system on the SSD:

* **Copy the system from the Micro SD to the SSD**: This method is simpler, and your previous configurations can also be directly copied.
* **Install via Raspberry Pi Imager**: If your Raspberry Pi uses a desktop version of the operating system, you can use an imaging tool (like Raspberry Pi Imager) to burn the system to the SSD. This example uses Raspberry Pi OS bookworm, but other systems might require installing the imaging tool first. However, this method requires you to reinstall the prionman module, and other configurations need to be redone as well.

**Copying the System from the Micro SD Card to the SSD**

#. Connect a display or access the Raspberry Pi desktop through VNC Viewer. Then click **Raspberry Pi logo** -> **Accessories** -> **SD Card Copier**.

    .. image:: img/ssd_copy.png

#. Make sure to select the correct **Copy From** and **Copy To** devices. Be careful not to mix them up.

    .. image:: img/ssd_copy_from.png

#. After selection, click **Start**.

    .. image:: img/ssd_copy_start.png

#. You will be prompted that the content on the SSD will be erased. Make sure to back up your data before clicking Yes.

    .. image:: img/ssd_copy_erase.png

#. Wait for some time, and the copying will be completed.

**Installing the System with Raspberry Pi Imager**

#. If your MicroSD card has a desktop version of the system installed, you can use an imaging tool (like Raspberry Pi Imager) to burn the system to the SSD. This example uses Raspberry Pi OS bookworm, but other systems might require installing the imaging tool first.

    .. image:: img/ssd_imager.png

#. Select Pi 5.

    .. image:: img/ssd_pi5.png

#. Choose an operating system.
    
    .. image:: img/ssd_os.png

#. Select the NVMe SSD card.

#. After configuration, click Yes.


**3. Restart Pironman 5**

After restarting the Raspberry Pi, it will boot from the SSD.

  .. code-block:: shell

    sudo reboot

.. note::

    If you are using the **Raspberry Pi Imager** to install the system on the SSD, you will need to reconfigure the setup after the Raspberry Pi boots up by following the steps to :ref:`set_up_pironman`.
