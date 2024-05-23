3. Installing the Operating System
=======================================

In this chapter, you will learn how to install the operating system.

.. note::

    You need to install an OS that supports Raspberry Pi 5. Please use the latest Raspberry Pi Imager tool for system installation. The currently tested systems are:

    * **Raspberry Pi OS (bookworm 64 desktop / lite)**: Perfectly compatible
    * **Ubuntu Desktop 23.10**: No SPI, causing LED to not light up
    * **Kali**: No I2C, causing OLED screen to not light up
    * **Home Assistant**: Cannot enable I2C and SPI

**1. Installing the OS to Micro SD Card**

If you are using a Micro SD card, you can follow the tutorial below to install the system onto your Micro SD card.

.. toctree::
    :maxdepth: 1

    install_to_sd


**2. Installing the OS to NVMe SSD**

If you are using an NVMe SSD and have an adapter to connect the NVMe SSD to your computer for system installation, you can use the following tutorial for a quick installation.

.. toctree::
    :maxdepth: 1

    install_to_nvme

**3. Copy the OS from the Micro SD card to the NVMe SSD**

If you have an NVMe SSD but do not have an adapter to connect your NVMe to your computer, you can first install the system on your Micro SD card. Once the Pironman 5 boots up successfully, you can copy the system from your Micro SD card to your NVMe SSD. Detailed instructions are as follows:

You will need to follow these steps:

1. Install the system on your Micro SD card.

* :ref:`install_os_sd`

2. Boot up and log in to the Raspberry Pi.

* :ref:`set_up_rpi`

3. Set up booting from the NVMe SSD, then copy the system from the Micro SD card to the NVMe SSD, or use the Imager in the Raspberry Pi system to install the system directly to the NVMe SSD.

* :ref:`boot_from_ssd`

