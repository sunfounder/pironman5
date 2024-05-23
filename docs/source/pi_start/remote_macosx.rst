For Mac OS X Users
==========================

For Mac OS X users, SSH (Secure Shell) offers a secure and convenient method to remotely access and control a Raspberry Pi. This is particularly handy for working with the Raspberry Pi remotely or when it's not connected to a monitor. Using the Terminal application on a Mac, you can establish this secure connection. The process involves an SSH command incorporating the Raspberry Pi's username and hostname. During the initial connection, a security prompt will ask for confirmation of the Raspberry Pi's authenticity.

#. To connect to the Raspberry Pi, type the following SSH command:

    .. code-block::

        ssh pi@raspberrypi.local

    .. image:: img/mac_vnc14.png

#. A security message will appear during your first login. Respond with **yes** to proceed.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Input the password for the Raspberry Pi. Be aware that the password won’t display on the screen as you type, which is a standard security feature.

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 

