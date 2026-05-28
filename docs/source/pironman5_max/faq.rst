.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

FAQ
============


Quick Troubleshooting
-------------------------------

* OLED screen not working → :ref:`faq_oled_max`
* RGB LEDs not working → :ref:`faq_rgb_max`
* GPIO GPIO Fans not working → :ref:`faq_gpio_fans_max`
* CPU fan not spinning → :ref:`faq_pwm_fan_max`
* Dashboard shows no data → :ref:`faq_dashboard_max`
* NVMe SSD not detected → :ref:`faq_nvme_max`



1. Hardware
-------------------------------


.. _com_os_max:

Compatible Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os

Power Button
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button
   :end-before: end_faq_power_button

Copper Pipe Ends on the Tower Cooler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copper_pipe_ends
   :end-before: end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_ai_hat
   :end-before: end_faq_ai_hat

Can I use the Pironman5 Max's vibration switch function?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From v1.3.6, OLED wake-up uses the power button. You must remove the vibration switch jumper to avoid occupying Raspberry Pi GPIO pins and prevent potential conflicts. Please check whether this jumper exists; if not, please ignore this notice.

.. image:: /pironman5_max/img/remove_vib_jumper.jpg

2. Cooling and Fans
-------------------------------

.. _faq_pwm_fan_max:

CPU Fan Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan


.. _faq_gpio_fans_max:

GPIO GPIO Fans Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_gpio_fans
   :end-before: end_faq_gpio_fans


3. OLED and RGB
-------------------------------


.. _faq_oled_max:

OLED Screen Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_compatible_systems| replace:: :ref:`com_os_max`
.. |link_set_up_pironman5| replace:: :ref:`set_up_pironman5_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_oled
   :end-before: end_faq_oled

.. _faq_rgb_max:

RGB LEDs Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb


.. _faq_customize_oled_max:

How to Customize the OLED Display?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_customize_oled
   :end-before: end_faq_customize_oled


4. Dashboard and Software
-------------------------------


.. _faq_dashboard_max:

The Dashboard Shows No Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard

How to Disable the Web Dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard`

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

.. |link_view_control_commands| replace:: :ref:`max_view_control_commands`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command


5. Boot and Storage
-------------------------------

If I set up OMV, can I still use the Pironman5's function?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, OpenMediaVault is set up on the Raspberry Pi system. Please follow the steps of :ref:`set_up_os_max` to continue the configuration.


PI5 Fails to Boot (Red LED)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_update_bootloader| replace:: :ref:`update_bootloader_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pi5_boot_fail
   :end-before: end_faq_pi5_boot_fail

.. _faq_nvme_max:

NVMe PIP Module Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Ensure the FPC cable connecting the NVMe PIP module to the Raspberry Pi 5 is securely attached.  

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

#. Confirm that your SSD is properly secured to the NVMe PIP module.  

#. Check the status of the NVMe PIP Module's LEDs:

   After confirming all connections, power on the Pironman 5 MAX and observe the two indicators on the NVMe PIP Module:  

   * **PWR LED**: Should be lit.  
   * **STA LED**: Should blink to indicate normal operation.  

   .. image:: img/dual_nvme_pip_leds.png  

   * If the **PWR LED** is on but the **STA LED** is not blinking, it indicates the NVMe SSD is not recognized by the Raspberry Pi.  
   * If the **PWR LED** is off, short the "Force Enable" pins on the module. If the **PWR LED** lights up, it could indicate a loose FPC cable or unsupported system configuration for NVMe.

   .. image:: img/dual_nvme_pip_j4.png  

     
#. Confirm that your NVMe SSD has a properly installed operating system. Refer to: :ref:`install_the_os_max`.

#. If the issue still persists, please send us the following log file:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log
   
How to Change the Raspberry Pi Boot Order Using Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_max`

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

.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_max`

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
