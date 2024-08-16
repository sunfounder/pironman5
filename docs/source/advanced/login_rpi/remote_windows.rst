.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

For Windows Users
=======================

For Windows 10 or higher users, remote login to a Raspberry Pi can be achieved through the following steps:

#. Search for ``powershell`` in your Windows search box. Right-click on ``Windows PowerShell`` and select ``Run as administrator``.

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. Determine your Raspberry Pi's IP address by typing ``ping -4 <hostname>.local`` in PowerShell.

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%
      

   The Raspberry Pi's IP address will be displayed once it's connected to the network.

   * If the terminal displays ``Ping request could not find host pi.local. Please check the name and try again.``, verify the hostname you've entered is correct.
   * If the IP address still isn't retrievable, check your network or WiFi settings on the Raspberry Pi.

#. Once the IP address is confirmed, log in to your Raspberry Pi using ``ssh <username>@<hostname>.local`` or ``ssh <username>@<IP address>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        If an error appears stating ``The term 'ssh' is not recognized as the name of a cmdlet...``, your system may not have SSH tools pre-installed. In this case, you need to manually install OpenSSH following :ref:`openssh_powershell`, or use a third-party tool like |link_putty|.

#. A security message will appear on your first login. Enter ``yes`` to proceed.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Enter the password you previously set. Note that the password characters won't be displayed on the screen, which is a standard security feature.

    .. note::
        The absence of visible characters when typing the password is normal. Ensure you input the correct password.

#. Once connected, your Raspberry Pi is ready for remote operations.

   .. image:: img/sp221221_140628.png
      :width: 90%
      
