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

1. About Compatible Systems
-------------------------------

Systems that passed the test on the Raspberry Pi 5:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. About Power Button
--------------------------

The power button brings out the power button of the Raspberry Pi 5, and it functions just like the power button of the Raspberry Pi 5.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Shutdown**

  * If you run Raspberry Pi **Bookworm Desktop** system, you can press the power button twice in quick succession to shutdown. 
  * If you run Raspberry Pi **Bookworm Lite** system, press the power button a single time to initiate a shutdown.
  * To force a hard shutdown, press and hold the power button.

* **Power on**

  * If the Raspberry Pi board is shut down, but still powered, single-press to power on from a shutdown state.

* If you are running a system that does not support a shutdown button, you can hold it for 5 seconds to force a hard shutdown, and single-press to power on from a shutdown state.

3. About the Raspberry Pi AI HAT+
----------------------------------------------------------

The Raspberry Pi AI HAT+ is not compatible with the Pironman 5.

   .. image::  img/output3.png
        :width: 400

The Raspberry Pi AI Kit combines the Raspberry Pi M.2 HAT+ and the Hailo AI accelerator module.

   .. image::  img/output2.jpg
        :width: 400

You can detach the Hailo AI accelerator module from the Raspberry Pi AI Kit and directly insert it into the NVMe PIP module of the Pironman 5 Mini.

   .. .. image::  img/output4.png
   ..      :width: 800

4. Does the Pironman 5 Mini support retro gaming systems?
--------------------------------------------------------------

Yes, it is compatible. However, most retro gaming systems are streamlined versions that cannot install and run additional software. This limitation may cause some components on the Pironman 5 Mini, such as the RGB fan, and the 4 RGB LEDs, to not function properly because these components require the installation of Pironman 5's software packages.


5. RGB LEDs Not Working?
--------------------------

#. The two pins on the IO Expander above J9 are used to connect the RGB LEDs to GPIO10. Ensure that the jumper cap on these two pins are properly in place.

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Verify that the Raspberry Pi is running a compatible operating system. The Pironman 5 only supports the following OS versions:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   If you have installed an unsupported OS, follow the guide to install a compatible operating system: :ref:`install_the_os_mini`.

#. Run the command ``sudo raspi-config`` to open the configuration menu. Navigate to **3 Interfacing Options** -> **I3 SPI** -> **YES**, then click **OK** and **Finish** to enable SPI. After enabling SPI, restart the Pironman 5.

If the problem persists after performing the above steps, please send an email to service@sunfounder.com. We will respond as soon as possible.

6. CPU fan not working?
----------------------------------------------

When the CPU temperature has not reached the set threshold, the CPU fan will not working.

**Fan Speed Control Based on Temperature**  

The PWM fan operates dynamically, adjusting its speed according to the Raspberry Pi 5's temperature:  

* **Below 50°C**: Fan remains off (0% speed).  
* **At 50°C**: Fan operates at low speed (30% speed).  
* **At 60°C**: Fan increases to medium speed (50% speed).  
* **At 67.5°C**: Fan ramps up to high speed (70% speed).  
* **At 75°C and above**: Fan operates at full speed (100% speed).  

For more detail please refer to : :ref:`fan_mini`

7. How to disable web dashboard?
------------------------------------------------------

Once you have completed the installation of the ``pironman5`` module, you will be able to access the :ref:`view_control_dashboard_mini`.
      
If you do not need this feature and want to reduce CPU and RAM usage, you can disable the dashboard during the installation of ``pironman5`` by adding the ``--disable-dashboard`` flag.
      
.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard
      
If you have already installed ``pironman 5``, you can remove the ``dashboard`` module and ``influxdb``, then restart pironman5 to apply the changes:
      
.. code-block:: shell
      
   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

8. How to Control Components Using the ``pironman5`` Command
----------------------------------------------------------------------
You can refer to the following tutorial to control the components of the Pironman 5 using the ``pironman5`` command.

* :ref:`view_control_commands_mini`

9. How to Change the Raspberry Pi Boot Order Using Commands
-------------------------------------------------------------

If you are already logged into your Raspberry Pi, you can change the boot order using commands. Detailed instructions are as follows:

* :ref:`configure_boot_ssd_mini`


10. How to Modify the Boot Order with Raspberry Pi Imager?
---------------------------------------------------------------

In addition to modifying the ``BOOT_ORDER`` in the EEPROM configuration, you can also use the **Raspberry Pi Imager** to change the boot order of your Raspberry Pi.

It is recommended to use a spare card for this step.

* :ref:`update_bootloader_mini`

11. How to Copy the System from the SD Card to an NVMe SSD?
-------------------------------------------------------------

If you have an NVMe SSD but do not have an adapter to connect your NVMe to your computer, you can first install the system on your Micro SD card. Once the Pironman 5 boots up successfully, you can copy the system from your Micro SD card to your NVMe SSD. Detailed instructions are as follows:


* :ref:`copy_sd_to_nvme_rpi_mini`

12. How to Remove the Protective Film from the Acrylic Plates
-----------------------------------------------------------------

Two acrylic panels are included in the package, both covered with yellow/transparent protective film on both sides to prevent scratches. The protective film may be a bit difficult to remove. Use a screwdriver to gently scrape at the corners, then carefully peel off the entire film.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center



.. _openssh_powershell_mini:

13. How to Install OpenSSH via Powershell?
----------------------------------------------

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
