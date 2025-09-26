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

You can detach the Hailo AI accelerator module from the Raspberry Pi AI Kit and directly insert it into the NVMe PIP module of the Pironman 5 MAX.

   .. .. image::  img/output4.png
   ..      :width: 800

4. About the Copper Pipe Ends of Tower Cooler
----------------------------------------------------------

The U-shaped heat pipes at the top of the tower cooler are compressed to facilitate the copper pipes passing through the aluminum fins, which is part of the normal production process for copper pipes.

   .. image::  img/tower_cooler1.png

5. PI5 Fails to Boot (Red LED)?
-------------------------------------------

This issue may be caused by a system update, changes to the boot order, or a corrupted bootloader. You can try the following steps to resolve the problem:

#. Check USB-HDMI Adapter Connection

   * Please carefully check whether the USB-HDMI adapter is securely connected to the PI5.
   * Try unplugging and reconnecting the USB-HDMI adapter.
   * Then reconnect the power supply and check if the PI5 boots successfully.

#. Test PI5 Outside the Case

   * If reconnecting the adapter does not solve the problem:
   * Remove the PI5 from the Pironman 5 case.
   * Power the PI5 directly with the power adapter (without the case).
   * Check if it can boot normally.

#. Restore the Bootloader

   * If the PI5 still cannot boot, the bootloader may be corrupted. You can follow this guide: :ref:`update_bootloader_max` and choose whether to boot from SD card or NVMe/USB.
   * Insert the prepared SD card into the PI5, power it on, and wait at least 10 seconds. Once the recovery is complete, remove and reformat the SD card. 
   * Then, use Raspberry Pi Imager to flash the latest Raspberry Pi OS, insert the card back, and try booting again.

6. OLED Screen Not Working?
------------------------------

.. note:: The OLED screen may turn off automatically after a period of inactivity to save power. You can gently tap the case to trigger the vibration sensor and wake the screen.

If the OLED screen is not displaying or is displaying incorrectly, follow these troubleshooting steps:

1. **Check the OLED Screen Connection**

   Ensure that the FPC cable of the OLED screen is properly connected.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Oled-11.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>


2. **Check OS Compatibility**

   Make sure you are running a compatible operating system on your Raspberry Pi.

3. **Check I2C Address**

   Run the following command to check whether the OLED's I2C address (0x3C) is recognized:

   .. code-block:: shell

      sudo i2cdetect -y 1

   If the address is not detected, enable I2C using the following command:

   .. code-block:: shell

      sudo raspi-config

4. **Restart the pironman5 Service**

   Restart the `pironman5` service to see if it resolves the issue:

   .. code-block:: shell

      sudo systemctl restart pironman5.service

5. **Check the Log File**

   If the issue persists, check the log file for error messages and provide the information to customer support for further analysis:

   .. code-block:: shell

      cat /var/log/pironman5/pm_auto.oled.log

7. NVMe PIP Module Not Working?
---------------------------------------

1. Ensure the FPC cable connecting the NVMe PIP module to the Raspberry Pi 5 is securely attached.  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(1)-11.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(2)-11.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

2. Confirm that your SSD is properly secured to the NVMe PIP module.  

3. Check the status of the NVMe PIP Module's LEDs:

   After confirming all connections, power on the Pironman 5 MAX and observe the two indicators on the NVMe PIP Module:  

   * **PWR LED**: Should be lit.  
   * **STA LED**: Should blink to indicate normal operation.  

   .. image:: img/dual_nvme_pip_leds.png  

   * If the **PWR LED** is on but the **STA LED** is not blinking, it indicates the NVMe SSD is not recognized by the Raspberry Pi.  
   * If the **PWR LED** is off, short the "Force Enable" pins on the module. If the **PWR LED** lights up, it could indicate a loose FPC cable or unsupported system configuration for NVMe.

   .. image:: img/dual_nvme_pip_j4.png  

     
4. Confirm that your NVMe SSD has a properly installed operating system. Refer to: :ref:`max_install_the_os`.

5. If the wiring is correct and the OS is installed, but the NVMe SSD still fails to boot, try booting from a Micro SD card to verify the functionality of other components. Once confirmed, proceed to: :ref:`max_configure_boot_ssd`.

If the problem persists after performing the above steps, please send an email to service@sunfounder.com. We will respond as soon as possible.

8. RGB LEDs Not Working?
--------------------------

#. The two pins on the IO Expander above J9 are used to connect the RGB LEDs to GPIO10. Ensure that the jumper cap on these two pins are properly in place.

   .. image:: advanced/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Verify that the Raspberry Pi is running a compatible operating system. The Pironman 5 only supports the following OS versions:

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   If you have installed an unsupported OS, follow the guide to install a compatible operating system: :ref:`install_the_os`.

#. Run the command ``sudo raspi-config`` to open the configuration menu. Navigate to **3 Interfacing Options** -> **I3 SPI** -> **YES**, then click **OK** and **Finish** to enable SPI. After enabling SPI, restart the Pironman 5.

If the problem persists after performing the above steps, please send an email to service@sunfounder.com. We will respond as soon as possible.

9. CPU fan not working?
----------------------------------------------

When the CPU temperature has not reached the set threshold, the CPU fan will not working.

**Fan Speed Control Based on Temperature**  

The PWM fan operates dynamically, adjusting its speed according to the Raspberry Pi 5's temperature:  

* **Below 50°C**: Fan remains off (0% speed).  
* **At 50°C**: Fan operates at low speed (30% speed).  
* **At 60°C**: Fan increases to medium speed (50% speed).  
* **At 67.5°C**: Fan ramps up to high speed (70% speed).  
* **At 75°C and above**: Fan operates at full speed (100% speed).  

For more detail please refer to : :ref:`fan`

10. How to wake up the OLED screen?
---------------------------------------------------------------------------------

To save power and extend the screen’s lifespan, the OLED screen will automatically turn off after a period of inactivity. This is part of the normal design and does not affect the product’s functionality.

You can gently tap the case to trigger the vibration sensor and wake the screen.

.. note::

   For OLED Screen configuration (such as turn ON/OFF, sleeptime, rotation, etc), please refer to: :ref:`max_view_control_dashboard` or :ref:`max_view_control_commands`.

11. How to disable web dashboard?
------------------------------------------------------

Once you have completed the installation of the ``pironman5`` module, you will be able to access the :ref:`max_view_control_dashboard`.
      
If you do not need this feature and want to reduce CPU and RAM usage, you can disable the dashboard during the installation of ``pironman5`` by adding the ``--disable-dashboard`` flag.
      
.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard
      
If you have already installed ``pironman 5``, you can remove the ``dashboard`` module and ``influxdb``, then restart pironman5 to apply the changes:
      
.. code-block:: shell
      
   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

.. Does the Pironman 5 MAX support retro gaming systems?
.. ------------------------------------------------------
.. Yes, it is compatible. However, most retro gaming systems are streamlined versions that cannot install and run additional software. This limitation may cause some components on the Pironman 5 MAX, such as the OLED display, the two RGB fans, and the 4 RGB LEDs, to not function properly because these components require the installation of Pironman 5 MAX's software packages.


.. .. note::

..     The Batocera.linux system is now fully compatible with Pironman 5 MAX. Batocera.linux is an open-source and completely free retro-gaming distribution.

..     * :ref:`max_install_batocera`
..     * :ref:`max_set_up_batocera`

12. How to Control Components Using the ``pironman5`` Command
----------------------------------------------------------------------
You can refer to the following tutorial to control the components of the Pironman 5 MAX using the ``pironman5`` command.

* :ref:`max_view_control_commands`

13. How to Change the Raspberry Pi Boot Order Using Commands
-------------------------------------------------------------

If you are already logged into your Raspberry Pi, you can change the boot order using commands. Detailed instructions are as follows:

* :ref:`max_configure_boot_ssd`


14. How to Modify the Boot Order with Raspberry Pi Imager?
---------------------------------------------------------------

In addition to modifying the ``BOOT_ORDER`` in the EEPROM configuration, you can also use the **Raspberry Pi Imager** to change the boot order of your Raspberry Pi.

It is recommended to use a spare card for this step.

* :ref:`update_bootloader_max`

15. How to Copy the System from the SD Card to an NVMe SSD?
-------------------------------------------------------------

If you have an NVMe SSD but do not have an adapter to connect your NVMe to your computer, you can first install the system on your Micro SD card. Once the Pironman 5 MAX boots up successfully, you can copy the system from your Micro SD card to your NVMe SSD. Detailed instructions are as follows:


* :ref:`max_copy_sd_to_nvme_rpi`

16. How to Remove the Protective Film from the Acrylic Plates
-----------------------------------------------------------------

Two acrylic panels are included in the package, both covered with yellow/transparent protective film on both sides to prevent scratches. The protective film may be a bit difficult to remove. Use a screwdriver to gently scrape at the corners, then carefully peel off the entire film.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _max_openssh_powershell:

17. How to Install OpenSSH via Powershell?
--------------------------------------------------

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


18. If I set up OMV, can I still use the Pironman5's function?
--------------------------------------------------------------------------------------------------------

Yes, OpenMediaVault is set up on the Raspberry Pi system. Please follow the steps of :ref:`max_set_up_pi_os` to continue the configuration.
