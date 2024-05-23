.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _set_up_rpi:

4. Setting Up Your Raspberry Pi
=====================================

In this chapter, you will learn how to log in to the Raspberry Pi. If you have a screen, connect it to display the Raspberry Pi desktop.

If you do not have a screen, you will need to log in to the Raspberry Pi remotely. You can also use VNC Viewer to access the Raspberry Pi desktop.

.. note::

    If you are already familiar with Raspberry Pi operations, you can skip this chapter.



Setting Up with a Screen
---------------------------

Having a screen simplifies the process of working with your Raspberry Pi.

**Required Components**

* Pironman 5
* Power Adapter
* Micro SD card
* Screen Power Adapter
* HDMI cable
* Screen
* Mouse
* Keyboard

Steps:

#. Insert the Micro SD card with Raspberry Pi OS installed into the Pironman 5.

#. Connect the Mouse and Keyboard to the Pironman 5.

#. Use the HDMI cable to connect the screen to the Pironman 5's HDMI port. Ensure the screen is plugged into a power source and turned on.

#. Power the Pironman 5 using the power adapter. The Raspberry Pi OS desktop should appear on the screen after a few seconds.

    .. image:: img/bookwarm.png
        :align: center

#. Now you can open the Terminal to enter commands.


Setting Up Without a Screen
------------------------------

If you don't have a monitor, remote login is a viable option.

Using SSH, you can access the Raspberry Pi's Bash shell, which is the default Linux shell. Bash offers a command-line interface for performing various tasks.

For those preferring a graphical user interface (GUI), the remote desktop feature is a convenient alternative for managing files and operations.


**Required Components**

* Pironman 5 
* Power Adapter
* Micro SD card

Steps:

#. Insert the Micro SD card with Raspberry Pi OS installed into the Pironman 5.

#. Power the Pironman 5 using the power adapter. 

#. For detailed setup tutorials based on your operating system, refer to the following sections:

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop

