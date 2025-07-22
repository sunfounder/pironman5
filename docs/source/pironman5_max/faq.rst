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

Does the Pironman 5 MAX support retro gaming systems?
------------------------------------------------------
Yes, it is compatible. However, most retro gaming systems are streamlined versions that cannot install and run additional software. This limitation may cause some components on the Pironman 5 MAX, such as the OLED display, the two RGB fans, and the 4 RGB LEDs, to not function properly because these components require the installation of Pironman 5 MAX's software packages.


.. note::

    The Batocera.linux system is now fully compatible with Pironman 5 MAX. Batocera.linux is an open-source and completely free retro-gaming distribution.

    * :ref:`max_install_batocera`
    * :ref:`max_set_up_batocera`


Reduce ``pironman5`` Logging in SYSLOG
-----------------------------------------------
To reduce the amount of logging output to SYSLOG, you can take the following steps:

First, disable HTTP request logging in ``influxd``:

.. code-block:: bash
   
   sudo nano /etc/influxdb/influxdb.conf 


Locate the ``http`` section and set ``log-enabled`` to ``false``.

.. code-block:: bash
   :emphasize-lines: 22

   ###
   ### [http]
   ###
   ### Controls how the HTTP endpoints are configured. These are the primary
   ### mechanism for getting data into and out of InfluxDB.
   ###

   [http]
   # Determines whether HTTP endpoint is enabled.
   # enabled = true

   # The bind address used by the HTTP service.
   # bind-address = ":8086"

   # Determines whether user authentication is enabled over HTTP/HTTPS.
   # auth-enabled = false

   # The default realm sent back when issuing a basic auth challenge.
   # realm = "InfluxDB"

   # Determines whether HTTP request logging is enabled.
   log-enabled = false

   # Determines whether the HTTP write request logs should be suppressed when the log is enabled.
   # suppress-write-log = false

   # When HTTP request logging is enabled, this option specifies the path where
   # log entries should be written. If unspecified, the default is to write to stderr, which
   # intermingles HTTP logs with internal InfluxDB logging.


After saving the file, restart the ``influxd`` service:

.. code-block:: bash

   sudo systemctl restart influxd.service

Then, reduce the logging level of the ``pironman5`` program to warning:

.. code-block:: bash
   
   sudo nano /etc/systemd/system/pironman5.service

In the ``Service`` section, set the ``debug-level`` to ``warning``:

.. code-block:: bash
   :emphasize-lines: 10

   # https://www.freedesktop.org/software/systemd/man/systemd.service.html
   [Unit]
   Description=pironman5 service
   # Need to start last to avoid gpio being occupied
   After=multi-user.target

   [Service]
   Type=forking
   # WorkingDirectory=/opt/pironman5
   ExecStart=/usr/local/bin/pironman5 start --background --debug-level=warning
   # ExecStop=/usr/local/bin/pironman5 stop
   # PrivateTmp=False

   [Install]
   WantedBy=multi-user.target

After saving, reload the systemd configuration and restart the ``pironman5`` service:

.. code-block:: bash

   sudo systemctl daemon-reload
   sudo systemctl restart pironman5.service






How to Control Components Using the ``pironman5`` Command
----------------------------------------------------------------------
You can refer to the following tutorial to control the components of the Pironman 5 MAX using the ``pironman5`` command.

* :ref:`max_view_control_commands`

How to Change the Raspberry Pi Boot Order Using Commands
-------------------------------------------------------------

If you are already logged into your Raspberry Pi, you can change the boot order using commands. Detailed instructions are as follows:

* :ref:`max_configure_boot_ssd`


How to Modify the Boot Order with Raspberry Pi Imager?
---------------------------------------------------------------

In addition to modifying the ``BOOT_ORDER`` in the EEPROM configuration, you can also use the **Raspberry Pi Imager** to change the boot order of your Raspberry Pi.

It is recommended to use a spare card for this step.

* :ref:`max_update_bootloader`

How to Copy the System from the SD Card to an NVMe SSD?
-------------------------------------------------------------

If you have an NVMe SSD but do not have an adapter to connect your NVMe to your computer, you can first install the system on your Micro SD card. Once the Pironman 5 MAX boots up successfully, you can copy the system from your Micro SD card to your NVMe SSD. Detailed instructions are as follows:


* :ref:`max_copy_sd_to_nvme_rpi`


NVMe PIP Module Not Working?
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



OLED Screen Not Working?
--------------------------

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



.. _max_openssh_powershell:

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



If I set up OMV, can I still use the Pironman5's function?
--------------------------------------------------------------------------------------------------------

Yes, OpenMediaVault is set up on the Raspberry Pi system. Please follow the steps of :ref:`max_set_up_pi_os` to continue the configuration.
