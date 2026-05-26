.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

FAQ
============


Quick Troubleshooting
-------------------------------

* OLED screen not working → :ref:`faq_oled_5`
* RGB LEDs not working → :ref:`faq_rgb_5`
* GPIO GPIO Fans not working → :ref:`faq_gpio_fans_5`
* CPU fan not spinning → :ref:`faq_pwm_fan_5`
* Dashboard shows no data → :ref:`faq_dashboard_5`
* NVMe SSD not detected → :ref:`faq_nvme_5`



1. Hardware
-------------------------------


.. _compatible_systems_5:

Compatible Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_com_os

Systems that passed testing on the Raspberry Pi 5:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

.. end_faq_com_os

Power Button
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_5`

.. start_faq_power_button

The power button extends the original Raspberry Pi 5 power button and behaves similarly.

* Briefly press: Power on / wake OLED / switch OLED pages.
* Hold for 2 seconds: Safe shutdown (requires |link_safe_shutdown|).
* Hold for 5 seconds: Force shutdown.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

.. end_faq_power_button


Airflow Direction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_airflow_direction

The airflow inside the Pironman 5 is designed to maximize cooling efficiency. Cool air enters through the GPIO opening and other vents, passes through the tower cooler, and is exhausted through the two side GPIO Fans.

For a detailed demonstration, refer to the following video:

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="../_static/video/airflow_direction.mp4"  type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>

.. end_faq_airflow_direction


Copper Pipe Ends on the Tower Cooler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_copper_pipe_ends

The flattened ends of the U-shaped copper heat pipes are part of the normal manufacturing process and are designed to allow the heat pipes to pass through the aluminum fins.

.. image:: img/tower_cooler1.png

.. end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_ai_hat

The Raspberry Pi AI HAT+ is not compatible with the Pironman 5.

.. image:: img/output3.png
    :width: 400

The Raspberry Pi AI Kit combines the Raspberry Pi M.2 HAT+ and the Hailo AI accelerator module.

.. image:: img/output2.jpg
    :width: 400

You can detach the Hailo AI accelerator module from the Raspberry Pi AI Kit and insert it directly into the NVMe PIP module of the Pironman 5.

.. image:: img/output4.png
    :width: 800

.. end_faq_ai_hat



2. Cooling and Fans
-------------------------------


.. _faq_pwm_fan_5:

CPU Fan Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_pwm_fan

The CPU fan on the Pironman 5 is controlled by the Raspberry Pi system. The CPU fan speed depends on the Raspberry Pi 5 CPU temperature.

Default CPU fan curve:

* < 50°C: Off (0%)
* 50°C+: Low speed (30%)
* 60°C+: Medium speed (50%)
* 67.5°C+: High speed (70%)
* 75°C+: Full speed (100%)

Check the current CPU temperature (example output: ``temp=48.7'C``):

.. code-block:: shell

   vcgencmd measure_temp

You can manually control the CPU fan using the following commands:

.. code-block:: shell

   pinctrl FAN_PWM op dl   # Enable fan (low active)
   pinctrl FAN_PWM op dh   # Disable fan (high active)
   pinctrl FAN_PWM a0      # Auto mode

You can also adjust the CPU fan temperature thresholds by editing:

.. code-block:: shell

   nano /boot/firmware/config.txt

Add:

.. code-block:: text

   dtparam=cooling_fan=on
   dtparam=fan_temp0=40000
   dtparam=fan_temp0_hyst=10000
   dtparam=fan_temp0_speed=125

This configuration starts the CPU fan at 40°C with PWM speed level 125.

After saving the file, reboot the Raspberry Pi for the changes to take effect.

.. end_faq_pwm_fan


.. _faq_gpio_fans_5:

GPIO GPIO Fans Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_gpio_fans

First, check whether the FAN jumper cap on the IO Expander board is installed correctly.

.. image:: hardware/img/io_board_fan_j9.png

Then set the GPIO Fans to ``Always On`` mode and check whether the fans start spinning.

.. code-block:: shell

   sudo pironman5 -gm 0

You can also connect the GPIO GPIO Fans directly to the Raspberry Pi ``5V`` and ``GND`` pins for testing.

If the fans spin normally when connected directly, the issue may be related to the IO Expander board. Please contact us for further support.

If the issue still persists, open the Dashboard **Log** page and check for error messages. You can also send us the following log file:

.. code-block:: shell

   cat /var/log/pironman5/pironman5.log

.. end_faq_gpio_fans

3. OLED and RGB
-------------------------------


.. _faq_oled_5:

OLED Screen Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_set_up_pironman5| replace:: :ref:`set_up_pironman5_5`
.. |link_compatible_systems| replace:: :ref:`compatible_systems_5`

.. start_faq_oled

If the OLED screen is not displaying or displaying incorrectly, follow these troubleshooting steps:

#. Ensure the FPC cable of the OLED screen is securely connected. It is recommended to reconnect the OLED screen and then power on the device.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_oled_screen.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. Confirm that the Raspberry Pi is running a supported operating system.

   See |link_compatible_systems|.

#. When the OLED screen is powered on for the first time, it may only display pixel blocks. You need to follow the instructions in |link_set_up_pironman5| to complete the configuration before it can display proper information.

#. Use the following command to check if the OLED I2C address ``0x3C`` is detected:

   .. code-block:: shell

      sudo i2cdetect -y 1

   * If the I2C address ``0x3C`` is detected, restart the Pironman 5 service:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * If the address is not detected, enable I2C:

     .. code-block:: shell

        sudo nano /boot/firmware/config.txt

     Add:

     .. code-block:: shell

        dtparam=i2c_arm=on

     Save the file and reboot the Raspberry Pi.

#. If the issue still persists, please send us the following log file:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_oled


.. _faq_rgb_5:

RGB LEDs Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. start_faq_rgb

#. The two pins on the IO Expander above J9 are used to connect the RGB LEDs to GPIO10. Ensure that the jumper cap on these two pins is properly installed.

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Confirm that the Raspberry Pi is running a supported operating system.

   See |link_compatible_systems|.

#. Run the following command to enable SPI:

   .. code-block:: shell

      sudo raspi-config

   Navigate to:

   ``3 Interfacing Options`` → ``I3 SPI`` → ``YES``

   Then reboot the Raspberry Pi.

#. If the issue still persists, please send us the following log file:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_rgb

.. _faq_customize_oled_5:

How to Customize the OLED Display?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_customize_oled

If you want to customize the OLED display, such as adding custom 2–4 digit image displays, you can modify the OLED page files in one of the following ways.

* **Method 1: Modify the Installed Files Directly**

  #. List the OLED page files:

     .. code-block:: shell

        ls /opt/pironman5/venv/lib/python3.13/site-packages/pm_auto/addons/oled/pages/

  #. Modify the desired Python files.

  #. Restart the service to apply the changes:

     .. code-block:: shell

        sudo systemctl restart pironman5.service


* **Method 2: Clone and Reinstall ``pm_auto``**

  #. Clone the ``pm_auto`` repository:

     .. code-block:: shell

        git clone -b 1.4.x https://github.com/sunfounder/pm_auto/

  #. After making changes, reinstall the modified package:

     .. code-block:: shell

        sudo /opt/pironman5/venv/bin/pip3 uninstall pm_auto -y && \
        sudo /opt/pironman5/venv/bin/pip3 install ~/pm_auto --no-build-isolation && \
        sudo chown -R pironman5:pironman5 /opt/pironman5

  #. Restart the service:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

* **Testing and Debugging**

  To view runtime logs:

  .. code-block:: shell

     journalctl -xefu pironman5.service

  You can also stop the service and run it manually for faster testing:

  .. code-block:: shell

     sudo systemctl stop pironman5.service
     sudo systemctl restart pironman5.service

.. end_faq_customize_oled

4. Dashboard and Software
-------------------------------


.. _faq_dashboard_5:

The Dashboard Shows No Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_dashboard

If the Dashboard shows no data, first open the Dashboard **Log** page and check whether there are any error messages related to ``influxdb``.

Common errors include:

* ``database not found``
* ``failed to connect to influxdb``
* ``connection refused``
* ``timeout``

You can try the following steps to resolve the issue.

#. Clear your browser cache, or reopen the Dashboard page using **Incognito / Private** mode.

#. Check whether the following services are running properly:

   .. code-block:: shell

      sudo systemctl status pironman5 --no-pager
      sudo systemctl status influxdb --no-pager

   Both services should display:

   .. code-block:: text

      active (running)

#. If either service is not running properly, restart them:

   .. code-block:: shell

      sudo systemctl restart influxdb
      sudo systemctl restart pironman5

   Then wait about 30 seconds and refresh the Dashboard page.

#. Check whether the ``pironman5`` database exists:

   .. code-block:: shell

      influx

   Then run:

   .. code-block:: text

      SHOW DATABASES;

   You should see:

   .. code-block:: text

      pironman5
      _internal

#. If the database is missing or corrupted, you can try clearing the historical data from the Dashboard using:

   ``Settings → Clear All Data``

#. If the issue still persists after trying all the above steps, we recommend reinstalling the Raspberry Pi OS and Pironman 5 software.

.. end_faq_dashboard


How to Disable the Web Dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard_5`

.. start_faq_disable_dashboard

Once you have completed the installation of the ``pironman5`` module, you will be able to access the |link_view_control_dashboard|.

If you do not need this feature and want to reduce CPU and RAM usage, you can disable the dashboard during installation by adding the ``--disable-dashboard`` flag.

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

If you have already installed ``pironman5``, you can remove the Dashboard module and ``influxdb``:

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

.. end_faq_disable_dashboard


How to Uninstall and Reinstall the Pironman 5 Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_reinstall_pironman5

#. Uninstall the current ``pironman5`` software:

   .. code-block:: shell

      cd ~/pironman5
      sudo python3 install.py --uninstall

#. Reboot the Raspberry Pi as prompted, then remove the ``pironman5`` directory:

   .. code-block:: shell

      cd ~/
      sudo rm -rf pironman5

#. Run the following command to reinstall the software for your Pironman 5 model:

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash

.. end_faq_reinstall_pironman5


How to Control Components Using the ``pironman5`` Command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_commands| replace:: :ref:`view_control_commands_5`

.. start_faq_pironman5_command

You can refer to the following tutorial to control the components of the Pironman 5 series using the ``pironman5`` command.

* |link_view_control_commands|

.. end_faq_pironman5_command



5. Boot and Storage
-------------------------------


PI5 Fails to Boot (Red LED)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_update_bootloader| replace:: :ref:`update_bootloader_5`

.. start_faq_pi5_boot_fail

This issue may be caused by a system update, changes to the boot order, or a corrupted bootloader. You can try the following steps to resolve the problem:

#. Check USB-HDMI Adapter Connection

   * Please carefully check whether the USB-HDMI adapter is securely connected to the PI5.
   * Try unplugging and reconnecting the USB-HDMI adapter.
   * Then reconnect the power supply and check if the PI5 boots successfully.

#. Test PI5 Outside the Case

   * If reconnecting the adapter does not solve the problem:
   * Remove the PI5 from the Pironman 5 series case.
   * Power the PI5 directly with the power adapter (without the case).
   * Check if it can boot normally.

#. Restore the Bootloader

   * If the PI5 still cannot boot, the bootloader may be corrupted. You can follow this guide: |link_update_bootloader| and choose whether to boot from SD card or NVMe/USB.
   * Insert the prepared SD card into the PI5, power it on, and wait at least 10 seconds. Once the recovery is complete, remove and reformat the SD card.
   * Then use Raspberry Pi Imager to flash the latest Raspberry Pi OS and try booting again.

.. end_faq_pi5_boot_fail


.. _faq_nvme_5:

NVMe PIP Module Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_install_the_os| replace:: :ref:`install_the_os_5`
.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_5`

.. start_faq_nvme_pip

#. Ensure the FPC cable connecting the NVMe PIP module to the Raspberry Pi 5 is securely attached.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. Confirm that your SSD is properly secured to the NVMe PIP module.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_ssd.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. Check the status of the NVMe PIP Module LEDs:

   * **PWR LED**: Should be lit.
   * **STA LED**: Should blink during normal operation.

   .. image:: img/nvme_pip_leds.png

   * If the **PWR LED** is on but the **STA LED** is not blinking, the NVMe SSD is not recognized.
   * If the **PWR LED** is off, short the ``Force Enable`` pins (J4).

     .. image:: img/nvme_pip_j4.png

#. Confirm that your NVMe SSD contains a valid operating system.

   See |link_install_the_os|.

#. If the SSD still fails to boot, try booting from a Micro SD card first, then configure NVMe boot:

   * |link_configure_boot_ssd|

#. If the issue still persists, please send us the following log file:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_nvme_pip


How to Change the Raspberry Pi Boot Order Using Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_boot_order_command

If you are already logged into your Raspberry Pi, you can change the boot order using commands.

* |link_configure_boot_ssd|

.. end_faq_boot_order_command


How to Modify the Boot Order with Raspberry Pi Imager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_boot_order_imager

In addition to modifying the ``BOOT_ORDER`` in the EEPROM configuration, you can also use Raspberry Pi Imager to change the boot order.

* |link_update_bootloader|

.. end_faq_boot_order_imager


How to Copy the System from the SD Card to an NVMe SSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_5`

.. start_faq_copy_sd_to_nvme

If you do not have an NVMe-to-USB adapter, you can first install the system onto a Micro SD card, then copy the system to the NVMe SSD after booting successfully.

* |link_copy_sd_to_nvme|

.. end_faq_copy_sd_to_nvme



6. Advanced Usage
-------------------------------


How to Remove the Protective Film
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_remove_film

Two acrylic panels are included in the package, both covered with yellow/transparent protective film on both sides to prevent scratches.

The protective film may be difficult to remove. Use a screwdriver to gently lift one corner, then carefully peel off the entire film.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. end_faq_remove_film