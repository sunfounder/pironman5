.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

5. Control with Commands or Dashboard
=======================================================

Once you have successfully installed the ``pironman5`` module, the ``pironman5.service`` will automatically start upon reboot.

You can monitor and control the Pironman 5 via commands, or by accessing the dashboard through the webpage at ``http://<ip>:34001``.

.. note::

    * For the **Home Assistant** system, you can only monitor and control the Pironman 5 through the dashboard by opening the webpage at ``http://<ip>:34001``.
    * For the **Batocera.linux** system, you can only monitor and control the Pironman 5 via commands. It is important to note that any changes to the configuration require a restart of the service using ``pironman5 restart`` to take effect.


.. toctree::
    :maxdepth: 1

    control_with dashboard 
    control_with_commands