.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _max_set_up_batocera:

Set up on Batocera.linux
=========================================================

If you have installed the Batocera.linux OS, you can remotely log in to this system via SSH and then follow the steps below to complete the configuration.

#. Once the system boots up, use ssh to remotely connect to Pironman5. For Windows, you can open **Powershell**, and for Mac OS X and Linux, you can directly open **Terminal**.

   .. image:: img/batocera_powershell.png
      :width: 90%
      

#. The default hostname for the batocera system is ``batocera``, with the default username as ``root`` and the password as ``linux``. Therefore, you can log in by typing ``ssh root@batocera.local`` and entering the password ``linux``.

   .. image:: img/batocera_login.png
      :width: 90%

#. Execute the command: ``/etc/init.d/S92switch setup`` to enter the menu settings page.

   .. image:: img/batocera_configure.png  
      :width: 90%

#. Use the down arrow key to navigate to the end, select and activate the **Pironman5** services.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. After activating the pironman5 service, select **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Execute the command ``reboot`` to restart Pironman5.

   .. code-block:: shell

      reboot

#. Upon reboot, the ``pironman5.service`` will start automatically. Here are the primary configurations for Pironman 5 MAX:
   
   * The OLED screen displays CPU, RAM, Disk Usage, CPU Temperature, and the Raspberry Pi's IP Address.
   * Four WS2812 RGB LEDs will light up in blue with a breathing mode.
   * The GPIO Fans are set to **Balanced** mode by default. For information on adjusting activation temperatures, see :ref:`cc_control_fan_max`.

Now, you can connect the Pironman 5 MAX to a screen, game controllers, headphones, and more to immerse yourself in your gaming world.


.. note::

   At this point, you have successfully set up the Pironman 5 MAX, and it is ready to use.
   
   For advanced control of its components, please refer to :ref:`max_view_control_commands`.



