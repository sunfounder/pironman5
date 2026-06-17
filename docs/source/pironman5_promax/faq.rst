.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



FAQ
============


Quick Troubleshooting
-------------------------------

* Power button not working → :ref:`faq_power_button_not_work_promax`
* OLED screen not working → :ref:`faq_oled_promax`
* RGB LEDs not working → :ref:`faq_rgb_promax`
* Fan not working → :ref:`promax_fan_faq`
* Dashboard shows no data → :ref:`faq_dashboard_promax`
* NVMe SSD not detected → :ref:`faq_nvme_promax`
* NVMe SSD detected but causes system restart → :ref:`faq_nvme_link_down_promax`
* PI5 fails to boot → :ref:`faq_pi5_boot_fail_promax`



1. Hardware
-------------------------------


.. _com_os_promax:

Compatible Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os


.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_promax`

Power Button
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button
   :end-before: end_faq_power_button


.. _faq_power_button_not_work_promax:

Power Button Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button_not_work
   :end-before: end_faq_power_button_not_work


Copper Pipe Ends on the Tower Cooler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copper_pipe_ends
   :end-before: end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Raspberry Pi AI HAT+ is not compatible with the Pironman 5 Pro MAX.

.. image:: img/output3.png
    :width: 400

The Raspberry Pi AI Kit combines the Raspberry Pi M.2 HAT+ and the Hailo AI accelerator module.

.. image:: img/output2.jpg
    :width: 400

You can detach the Hailo AI accelerator module from the Raspberry Pi AI Kit and directly insert it into the NVMe PIP module of the Pironman 5 Pro MAX.


4.3-Inch Screen Is Black / Not Displaying?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The 4.3-inch DSI screen is plug-and-play — no additional driver installation is required.

.. note::

   The **ON/AUTO** jumper on the HDMI/USB board only controls the speaker audio output. It has **no effect** on the screen display.

If the screen is black or not displaying, check the following:

#. Ensure the DSI ribbon cable is connected to the correct DSI port on the Raspberry Pi 5.

#. Check that the ribbon cable is fully inserted, the clamp is pressed down firmly, and the contacts are facing the correct direction.

#. Run the following command to confirm whether the system detects the DSI screen:

   .. code-block:: shell

      sudo dmesg | grep -i dsi

   If the screen is detected, you should see output similar to ``DSI display found``. If there is no output, the screen is not being recognized — recheck the physical connection.


External HDMI Screen — Taskbar Only Appears on the 4.3-Inch Screen?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you connect an external HDMI monitor to the Pironman 5 Pro MAX, the desktop taskbar may stay on the built-in 4.3-inch DSI screen instead of moving to the external display. That is because the system defaults to the DSI screen as the primary display.

If you want to set the HDMI monitor as the primary screen at startup:

#. Create a startup script:

   .. code-block:: shell

      sudo nano /usr/local/bin/fix-primary-screen.sh

#. Add the following content to the script:

   .. code-block:: bash

      #!/bin/bash
      # Check if an external HDMI monitor is connected
      if wlr-randr | grep -q "HDMI-A-1"; then
          # Turn off the DSI screen first
          wlr-randr --output DSI-1 --off
          sleep 2
          # Re-enable DSI and place it to the right of HDMI
          wlr-randr --output DSI-1 --on --right-of HDMI-A-1
      fi

#. Make the script executable:

   .. code-block:: shell

      sudo chmod +x /usr/local/bin/fix-primary-screen.sh

#. Add the script to autostart. Edit the labwc autostart file:

   .. code-block:: shell

      nano ~/.config/labwc/autostart

   Add the following line (the ``&`` runs it in the background):

   .. code-block:: text

      /usr/local/bin/fix-primary-screen.sh &


2. Cooling and Fans
-------------------------------


.. _promax_fan_faq:

Fan Not Working / Cannot Be Controlled?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Pro MAX adopts the official Raspberry Pi PWM fan control solution. All three cooling fans are directly controlled by the Raspberry Pi system and do not rely on the pironman5 service (therefore, you will not see fan control options in the command-line tool or the Dashboard).

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan


Dashboard Does Not Show Fan Speed?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Pro MAX uses custom **5-pin** fans with the following pinout: **PWM / 5V / GND / RGB Data In / RGB Data Out**.

These fans do **not** have a tachometer (speed feedback) pin, so the system cannot read the actual RPM. The Dashboard not showing fan speed is expected and normal.

Fan speed is controlled by the Raspberry Pi's native PWM temperature curve:

* < 50°C: Off (0%)
* 50°C+: Low speed (30%)
* 60°C+: Medium speed (50%)
* 67.5°C+: High speed (70%)
* 75°C+: Full speed (100%)



3. OLED and RGB
-------------------------------


.. _faq_oled_promax:

OLED Screen Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_set_up_pironman5| replace:: :ref:`promax_set_up_pi_os`
.. |link_compatible_systems| replace:: :ref:`com_os_promax`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_oled
   :end-before: end_faq_oled


.. _faq_customize_oled_promax:

How to Customize the OLED Display?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_customize_oled
   :end-before: end_faq_customize_oled


.. _faq_rgb_promax:

RGB LEDs Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb


How to Wake Up the OLED Screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To save power and extend the screen's lifespan, the OLED screen will automatically turn off after a period of inactivity. This is part of the normal design and does not affect the product's functionality.

.. note::

   For OLED Screen configuration (such as turn ON/OFF, sleeptime, rotation, etc), please refer to :ref:`promax_view_control_dashboard` or :ref:`promax_view_control_commands`.



4. Dashboard and Software
-------------------------------


.. _faq_dashboard_promax:

The Dashboard Shows No Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard


.. |link_view_control_dashboard| replace:: :ref:`promax_view_control_dashboard`

How to Disable the Web Dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_disable_dashboard
   :end-before: end_faq_disable_dashboard


How to Uninstall and Reinstall the Pironman 5 Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_reinstall_pironman5
   :end-before: end_faq_reinstall_pironman5


.. |link_view_control_commands| replace:: :ref:`promax_view_control_commands`

How to Control Components Using the ``pironman5`` Command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command


.. _faq_piper_tts_32bit_promax:

``pip install piper-tts`` Fails with "Could Not Find a Version"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When installing ``sunfounder-voice-assistant`` on the Pironman 5 Pro MAX, you may encounter the following error:

.. code-block:: text

   ERROR: Could not find a version that satisfies the requirement piper-tts==1.3.0
   ERROR: No matching distribution found for piper-tts==1.3.0

This error occurs because ``piper-tts`` 1.3.0 only provides **64-bit** (``aarch64``) wheels. If your Raspberry Pi is running a **32-bit** operating system, pip cannot find a compatible package.

**Solution:** Install a 64-bit version of Raspberry Pi OS.

#. Check your current system architecture:

   .. code-block:: shell

      uname -m

   * ``aarch64`` → 64-bit (no issue)
   * ``armv7l`` → 32-bit (needs upgrade)

#. Use `Raspberry Pi Imager <https://www.raspberrypi.com/software/>`_ to flash a **64-bit** Raspberry Pi OS image onto your storage device.

#. After installing the 64-bit OS, reinstall the ``pironman5`` software and ``sunfounder-voice-assistant``.


5. Boot and Storage
-------------------------------


.. |link_update_bootloader| replace:: :ref:`update_bootloader_promax`

.. _faq_pi5_boot_fail_promax:

PI5 Fails to Boot (Red LED)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pi5_boot_fail
   :end-before: end_faq_pi5_boot_fail


.. _faq_nvme_promax:

NVMe PIP Module Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_install_the_os_dual| replace:: :ref:`install_the_os_promax`

.. include:: ../pironman5_max/faq.rst
   :start-after: start_faq_nvme_pip_dual
   :end-before: end_faq_nvme_pip_dual

#. If the wiring is correct and the OS is installed, but the NVMe SSD still fails to boot, try booting from a Micro SD card to verify the functionality of other components. Once confirmed, proceed to :ref:`configure_boot_ssd_promax`.

#. If the problem persists after performing the above steps, please send an email to service@sunfounder.com. We will respond as soon as possible.


.. _faq_nvme_link_down_promax:

NVMe SSD Detected but Causes System Restart on Read/Write?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_nvme_link_down
   :end-before: end_faq_nvme_link_down


.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_promax`

How to Change the Raspberry Pi Boot Order Using Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_command
   :end-before: end_faq_boot_order_command


How to Modify the Boot Order with Raspberry Pi Imager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_imager
   :end-before: end_faq_boot_order_imager


.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_promax`

How to Copy the System from the SD Card to an NVMe SSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copy_sd_to_nvme
   :end-before: end_faq_copy_sd_to_nvme



6. Advanced Usage
-------------------------------


How to Remove the Protective Film
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_remove_film
   :end-before: end_faq_remove_film


.. _promax_openssh_powershell:

How to Install OpenSSH via Powershell?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


If I Set Up OMV, Can I Still Use the Pironman5's Function?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, OpenMediaVault is set up on the Raspberry Pi system. Please follow the steps of :ref:`promax_set_up_pi_os` to continue the configuration.


Raspberry Pi Camera Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the camera is not working, 90% of the issues are related to the ribbon cable connection or the camera hardware itself.

First, use ``rpicam-hello --list-cameras`` to confirm whether the camera is detected. If it is successfully detected, you should see a message similar to the following:

.. code-block:: bash

   Available cameras
   -----------------
   0 : ov5647 [2592x1944] (/base/axi/pcie@1000120000/rp1/i2c@88000/ov5647@36)

If the camera is not detected, check whether the ribbon cable is reversed or not fully inserted. If the issue persists, try replacing the ribbon cable or the camera module for cross-testing.


Can I Install Home Assistant OS on the Pironman 5 Pro MAX?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Pironman 5 Pro MAX does not have its own dedicated Home Assistant add-on. However, you can use the **Pironman 5 MAX** add-on instead — follow the `SunFounder add-ons repository guide <https://docs.sunfounder.com/projects/pironman5/en/latest/pironman5_max/set_up/set_up_home_assistant.html#add-the-sunfounder-add-ons-repository>`_.

Be aware of the following limitations:

* **4.3-inch screen**: Home Assistant OS is a **lite** system without a desktop environment. The 4.3-inch screen built into the Pro MAX will not display anything.

* **NVMe PIP dual SSDs**: Home Assistant OS cannot read both NVMe SSDs on the Pro MAX's dual NVMe PIP module.

* **OLED screen and RGB LEDs**: These components work normally after installing the add-on — no additional configuration is required.

* **CPU fan**: The CPU fan requires manual configuration to work under Home Assistant OS. Add the following to ``/boot/firmware/config.txt``:

  .. code-block:: text

     dtparam=cooling_fan=on
     dtparam=fan_temp0=40000
     dtparam=fan_temp0_hyst=10000
     dtparam=fan_temp0_speed=125

  After saving and rebooting, the CPU fan will be controlled by the Raspberry Pi system based on CPU temperature. You can also control it manually via ``pinctrl`` commands — see :ref:`promax_fan_faq`.
