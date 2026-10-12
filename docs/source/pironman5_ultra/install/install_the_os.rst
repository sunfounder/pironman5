.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _install_the_os_ultra:

3. Installing the Operating System
=======================================

.. note::

    You need to install an OS that supports Raspberry Pi 5. Pironman 5 Ultra and the PiPower 5 module only support **64-bit** operating systems. Please use the latest Raspberry Pi Imager tool for system installation. The currently tested systems are:

   .. image:: img/compitable_os.png
        :width: 500
        :align: center

.. warning::

    **32-bit systems are not supported.** Please use a 64-bit system, such as Raspberry Pi OS 64-bit or Ubuntu 64-bit.

.. note::

    If you need to use OpenMediaVault as a storage / disk management tool, install a system **without a desktop**. Raspberry Pi OS Lite is recommended.

In this chapter, you will learn how to install the operating systems. All the installation steps depend on the |link_rpi_imager|, which you need to install first.

    .. toctree::
        :maxdepth: 1

        install_raspberry_os
        install_the_other_os
        install_umbrel
        install_batocera
