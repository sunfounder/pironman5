.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

FAQ
============

How to disable web dashboard?
------------------------------------------------------

Once you have completed the installation of the ``pironman5`` module, you will be able to access the :ref:`view_control_dashboard`.
      
If you do not need this feature and want to reduce CPU and RAM usage, you can disable the dashboard during the installation of ``pironman5`` by adding the ``--disable-dashboard`` flag.
      
.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard
      
If you have already installed ``pironman 5``, you can remove the ``dashboard`` module and ``influxdb``, then restart pironman5 to apply the changes:
      
.. code-block:: shell
      
   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

Does the Pironman 5 support retro gaming systems?
------------------------------------------------------
Yes, it is compatible. However, most retro gaming systems are streamlined versions that cannot install and run additional software. This limitation may cause some components on the Pironman 5, such as the OLED display, the two RGB fans, and the 4 RGB LEDs, to not function properly because these components require the installation of Pironman 5's software packages.


.. note::

    The Batocera.linux system is now fully compatible with Pironman 5. Batocera.linux is an open-source and completely free retro-gaming distribution.

    * :ref:`install_batocera`
    * :ref:`set_up_batocera`

How to Control Components Using the ``pironman5`` Command
----------------------------------------------------------------------
You can refer to the following tutorial to control the components of the Pironman 5 using the ``pironman5`` command.

* :ref:`view_control_commands`

How to Change the Raspberry Pi Boot Order Using Commands
-------------------------------------------------------------

If you are already logged into your Raspberry Pi, you can change the boot order using commands. Detailed instructions are as follows:

* :ref:`configure_boot_ssd`


How to Modify the Boot Order with Raspberry Pi Imager?
---------------------------------------------------------------

In addition to modifying the ``BOOT_ORDER`` in the EEPROM configuration, you can also use the **Raspberry Pi Imager** to change the boot order of your Raspberry Pi.

It is recommended to use a spare card for this step.

* :ref:`update_bootloader`

How to Copy the System from the SD Card to an NVMe SSD?
-------------------------------------------------------------

If you have an NVMe SSD but do not have an adapter to connect your NVMe to your computer, you can first install the system on your Micro SD card. Once the Pironman 5 boots up successfully, you can copy the system from your Micro SD card to your NVMe SSD. Detailed instructions are as follows:


* :ref:`copy_sd_to_nvme_rpi`


OLED Screen Not Working?
--------------------------

If the OLED Screen is not displaying or displaying incorrectly, you can follow these steps to troubleshoot the issue:

Check if the FPC cable of the OLED Screen is properly connected.

#. Use the following command to view the program's run logs and check for error messages.

   .. code-block:: shell

      cat /opt/pironman5/log

#. Alternatively, use the following command to check if the OLED's i2c address 0x3C is recognized:
    
   .. code-block:: shell
        
        sudo i2cdetect -y 1

#. If the first two steps don't reveal any issues, try restarting the pironman5 service to see if that resolves the problem.


   .. code-block:: shell

        sudo systemctl restart pironman5.service

.. _openssh_powershell:

Install OpenSSH via Powershell
-----------------------------------

When you use ``ssh <username>@<hostname>.local`` (or ``ssh <username>@<IP address>``) to connect to your Raspberry Pi, but the following error message appears.

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


It means your computer system is too old and does not have `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ pre-installed, you need to follow the tutorial below to install it manually.

#. Type ``powershell`` in the search box of your Windows desktop, right click on the ``Windows PowerShell``, and select ``Run as administrator`` from the menu that appears.

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. Use the following command to install ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. After installation, the following output will be returned.

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verify the installation by using the following command.

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. It now tells you that ``OpenSSH.Client`` has been successfully installed.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        If the above prompt does not appear, it means that your Windows system is still too old, and you are advised to install a third-party SSH tool, like |link_putty|.

#. Now restart PowerShell and continue to run it as administrator. At this point you will be able to log in to your Raspberry Pi using the ``ssh`` command, where you will be prompted to enter the password you set up earlier.

   .. image:: img/powershell_login.png



