.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _login_rpi:

Log in to the Raspberry Pi OS
=====================================

In this chapter, you will learn how to log in to the Raspberry Pi. Whether you have a screen attached or need to access it remotely, this section will guide you through opening the terminal, which you will use in later chapters to enter commands.

.. note::

    If you are already familiar with Raspberry Pi operations, you can skip this chapter.

Logging in with a Screen
---------------------------

Having a screen attached to your Raspberry Pi makes it easier to interact with the system directly.

**Required Components**

* Pironman 5 Mini
* Power Adapter
* Micro SD card or NVMe SSD with pre-installed Raspberry Pi OS
* Monitor Power Adapter
* HDMI cable
* Monitor
* Mouse
* Keyboard

**Steps**

#. Insert the Micro SD card into the Pironman 5 Mini.

#. Connect the Mouse and Keyboard to the USB ports of the Pironman 5 Mini.

#. Use the HDMI cable to connect the monitor to the HDMI port of the Pironman 5 Mini. Make sure the monitor is connected to a power source and is turned on.

#. Power up the Pironman 5 Mini using the power adapter. You should see the Raspberry Pi OS desktop appear on the monitor shortly.

   .. image:: img/bookwarm.png
      :width: 90%
      

#. Once the desktop is visible, open the Terminal by clicking on the terminal icon or searching for it in the menu to start entering commands.

Logging in Remotely Without a Screen
----------------------------------------------

If you do not have access to a monitor, you can still use your Raspberry Pi by logging in remotely.

For command-line access, you can use SSH to connect to the Raspberry Pi's Bash shell, the default Linux shell which allows for managing the device via commands.

For those who prefer a graphical interface, using a remote desktop application like VNC Viewer offers a visual way to manage files and operations remotely.

**Required Components**

* Pironman 5 Mini 
* Power Adapter
* Micro SD card or NVMe SSD with pre-installed Raspberry Pi OS

Steps:

#. Insert the Micro SD card into the Pironman 5 Mini.

#. Connect the Pironman 5 Mini to a power source using the power adapter.

#. For detailed tutorials on setting up remote access depending on your computer's operating system, see the following sections:

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


