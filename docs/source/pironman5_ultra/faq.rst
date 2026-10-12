.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

FAQ
============


.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_ultra`
.. |link_set_up_pironman5| replace:: :ref:`set_up_pironman5_ultra`
.. |link_compatible_systems| replace:: :ref:`compatible_systems_ultra`
.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard_ultra`
.. |link_view_control_commands| replace:: :ref:`view_control_commands_ultra`
.. |link_update_bootloader| replace:: :ref:`update_bootloader_ultra`
.. |link_install_the_os| replace:: :ref:`install_the_os_ultra`
.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_ultra`
.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_ultra`

Quick Troubleshooting
-------------------------------

* Power button not working → :ref:`faq_power_button_not_work_ultra`
* OLED screen not working → :ref:`faq_oled_ultra`
* RGB lighting not working → :ref:`faq_rgb_ultra`
* Fans not working → :ref:`faq_fan_ultra`
* CPU fan not spinning → :ref:`faq_pwm_fan_ultra`
* Dashboard shows no data → :ref:`faq_dashboard_ultra`
* Battery not detected or not charging → :ref:`faq_battery_ultra`
* Device does not power off after shutdown → :ref:`faq_power_off_ultra`
* NVMe SSD not detected → :ref:`faq_nvme_ultra`
* NVMe SSD detected but causes system restart → :ref:`faq_nvme_link_down_ultra`


1. Hardware
-------------------------------


.. _compatible_systems_ultra:

Compatible Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os

.. note::

   Pironman 5 Ultra and the PiPower 5 module only support **64-bit operating systems**. 32-bit systems are not supported.

Power Button
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button
   :end-before: end_faq_power_button


.. _faq_power_button_not_work_ultra:

Power Button Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button_not_work
   :end-before: end_faq_power_button_not_work


.. _faq_battery_ultra:

Battery Not Detected or Not Charging?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Check that the battery connector is fully inserted into the PiPower 5 module and that the polarity is correct. Never force the connector in reversed.

#. Check the battery status with:

   .. code-block:: shell

      pipower5 -a

   Look at the **Battery** block. If ``percentage`` stays at ``0 %`` or ``voltage`` is ``0 mV``, the battery is not detected.

#. Make sure the PiPower 5 service is running:

   .. code-block:: shell

      sudo systemctl status pironman5.service

#. If the battery is detected but not charging, check the **Charge SEL** DIP switch setting and the power supply. The charge power is limited by the power supply capability. See :ref:`pipower5_ultra`.

#. If the battery is unable to supply the Raspberry Pi for a long time under high load, set the shutdown percentage to ``100%`` so the Raspberry Pi shuts down immediately when external power is lost.

#. If the issue still persists, please send us the following log file:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log


.. _faq_power_off_ultra:

Device Does Not Power Off After Raspberry Pi Shutdown?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PiPower 5 cuts the power only after the Raspberry Pi reports that it has shut down. If the device stays powered on after shutdown:

#. Make sure the ``SDSIG`` jumper on the PiPower 5 module is connected to ``PI3V3``.

#. Configure the Raspberry Pi shutdown behaviour as described in :ref:`safe_shutdown_ultra`.

#. Note that the **Default On** jumper keeps the device powered whenever external power is present. Cutting the output after shutdown still requires the two steps above.


2. Cooling and Fans
-------------------------------

.. _faq_pwm_fan_ultra:

CPU Fan Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan

.. note::

   The CPU turbo fan and the two front fans only have a control signal and no tachometer (speed) signal, so the system cannot read the fan speed. This is normal.


.. _faq_fan_ultra:

Fans Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Confirm whether the temperature has reached the activation threshold. The fans are controlled by the system according to temperature and will not spin below the corresponding threshold. To confirm that they work, set the fans to **Always On** in the Dashboard and check again. You can also check the current state with:

   .. code-block:: shell

      cat /sys/class/thermal/cooling_device0/cur_state

#. Make sure the service is running normally: ``sudo systemctl status pironman5.service``, and check the log ``cat /var/log/pironman5/pironman5.log`` for errors.

#. If the RGB lighting works but the fans do not spin, the RGB data path is fine and the problem is in the fan power or PWM control signal. Check the fan power wires (red +5V / black GND).

#. If the front fans do not spin, note that they are connected through the RGB module. Check that the adapter connector and the fan plugs are firmly seated.

#. Note that the fans have only a control signal and no speed signal, so the system cannot read the fan speed. This is normal and does not indicate a fault.


3. OLED and RGB
-------------------------------


.. _faq_oled_ultra:

OLED Screen Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_oled
   :end-before: end_faq_oled

.. _faq_rgb_ultra:

RGB Lighting Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb


.. _faq_customize_oled_ultra:

How to Customize the OLED Display?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_customize_oled
   :end-before: end_faq_customize_oled


4. Dashboard and Software
-------------------------------


.. _faq_dashboard_ultra:

The Dashboard Shows No Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard

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


How to Control Components Using the ``pironman5`` Command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command


5. Boot and Storage
-------------------------------

If I set up OMV, can I still use Pironman 5 Ultra's functions?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. OpenMediaVault is set up on the Raspberry Pi system. Please follow the steps of :ref:`set_up_pironman5_ultra` to continue the configuration.


PI5 Fails to Boot (Red LED)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pi5_boot_fail
   :end-before: end_faq_pi5_boot_fail

.. _faq_nvme_ultra:

NVMe SSD Not Detected?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Confirm that your NVMe SSD is compatible. Refer to the :ref:`compatible NVMe SSD list <compitable_nvme_ssd_ultra>` for verified, stable, and compatible drives.

#. Ensure the PCIe ribbon cable connecting the dual NVMe PIP module to the Raspberry Pi 5 is securely attached.

#. Confirm that your SSD is properly secured to the M.2 slot.

#. Check the status of the NVMe PIP module LEDs. After powering on the device, observe the indicators:

   * **PWR LED**: should be lit.
   * **STA LED**: should blink to indicate normal operation.

   .. image:: img/nvme_pip_leds.png

   * If the **PWR LED** is on but the **STA LED** is not blinking, the NVMe SSD is not recognized by the Raspberry Pi.
   * If the **PWR LED** is off, short the "Force Enable" pins on the module. If the **PWR LED** lights up, it could indicate a loose FPC cable or an unsupported system configuration for NVMe.

   .. image:: img/nvme_pip_j4.png

#. If the SSD is installed in the second slot, remember that the second M.2 slot and the Raspberry Pi standard PCIe interface are **either/or**. If a PCIe HAT is connected, the MUX switches to the PCIe interface and the second M.2 slot is not available. See :ref:`nvme_pip_ultra`.

#. Confirm that your NVMe SSD has a properly installed operating system. Refer to :ref:`install_the_os_ultra`.

#. If the issue still persists, please send us the following log file:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log


.. _faq_nvme_link_down_ultra:

NVMe SSD Detected but Causes System Restart on Read/Write?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_nvme_link_down
   :end-before: end_faq_nvme_link_down


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

How to Copy the System from the SD Card to an NVMe SSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copy_sd_to_nvme
   :end-before: end_faq_copy_sd_to_nvme

6. Advanced Usage
-------------------------------

Can I use the Raspberry Pi AI HAT+ with Pironman 5 Ultra?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. Unlike other models in the series, Pironman 5 Ultra provides a Raspberry Pi standard PCIe interface. Connect the AI HAT+ / AI HAT+ 2 to the PCIe interface and the **DET** pin switches the MUX automatically. See :ref:`nvme_pip_ultra` and :ref:`ai_hat_ultra`.

How to Remove the Protective Film
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_remove_film
   :end-before: end_faq_remove_film
