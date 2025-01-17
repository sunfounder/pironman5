.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _set_up_batocera:

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

#. Upon reboot, the ``pironman5.service`` will start automatically. Here are the primary configurations for Pironman 5:
   
   * The OLED screen displays CPU, RAM, Disk Usage, CPU Temperature, and the Raspberry Pi's IP Address.
   * Four WS2812 RGB LEDs will light up in blue with a breathing mode.
   
   .. note::
    
     RGB fans won't spin unless the temperature hits 60°C. For different activation temperatures, see :ref:`cc_control_fan`.

Now, you can connect the Pironman 5 to a screen, game controllers, headphones, and more to immerse yourself in your gaming world.
