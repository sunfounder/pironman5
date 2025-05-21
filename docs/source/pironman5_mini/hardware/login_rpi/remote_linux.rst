.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

For Linux/Unix Users
==========================

#. Locate and open the **Terminal** on your Linux/Unix system.

#. Ensure your Raspberry Pi is connected to the same network. Verify this by typing `ping <hostname>.local`. For example:

    .. code-block::

        ping raspberrypi.local

    You should see the Raspberry Pi's IP address if it's connected to the network.

    * If the terminal shows a message like ``Ping request could not find host pi.local. Please check the name and try again.``, double-check the hostname you've entered.
    * If you're unable to retrieve the IP address, inspect your network or WiFi settings on the Raspberry Pi.

#. Initiate an SSH connection by typing ``ssh <username>@<hostname>.local`` or ``ssh <username>@<IP address>``. For instance:

    .. code-block::

        ssh pi@raspberrypi.local

#. On your first login, you'll encounter a security message. Type ``yes`` to proceed.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Enter the password you previously set. Note that for security reasons, the password won't be visible as you type.

    .. note::
        It's normal for the password characters not to display in the terminal. Just ensure to enter the correct password.

#. Once you've successfully logged in, your Raspberry Pi is now connected, and you're ready to proceed to the next step.
