.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _install_the_os_ultra:

3. Installing the Operating System
=======================================

.. warning::

    * OpenMediaVault does not support installation on the Raspberry Pi OS desktop.
    * ⚠️ Only **Raspberry Pi OS Lite 64-bit** is supported — currently 13 (**Trixie**).

.. warning::

    * You need to install an OS that supports Raspberry Pi 5. Pironman 5 Ultra and the PiPower 5 module only support **64-bit** operating systems. Please use the latest Raspberry Pi Imager tool for system installation. The currently tested systems are:


.. list-table:: Tested Operating Systems
   :header-rows: 1
   :widths: 60 30

   * - Operating System
     - Compatibility
   * - Raspberry Pi OS (bookworm 64-bit desktop / lite)
     - Fully compatible
   * - Ubuntu
     - Fully compatible
   * - Kali Linux
     - Fully compatible

In this chapter, you will learn how to install the operating systems. All the installation steps depend on the |link_rpi_imager|, which you need to install first.

    .. toctree::
        :maxdepth: 1

        install_raspberry_os
        install_the_other_os
