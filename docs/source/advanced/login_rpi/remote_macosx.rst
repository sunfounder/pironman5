适用于Mac OS X用户
==========================

对于Mac OS X用户，SSH（安全外壳）提供了一种安全且便捷的方法来远程访问和控制Raspberry Pi。这对于远程操作Raspberry Pi或当其未连接到显示器时特别有用。通过Mac上的终端应用程序，您可以建立这一安全连接。该过程涉及一个包含Raspberry Pi用户名和主机名的SSH命令。在首次连接时，系统会提示您确认Raspberry Pi的真实性。

#. 要连接到Raspberry Pi，输入以下SSH命令：

    .. code-block::

        ssh pi@raspberrypi.local

   .. image:: img/mac_vnc14.png

#. 在首次登录时，会出现安全消息。输入 **yes** 以继续。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入Raspberry Pi的密码。请注意，输入密码时，密码不会显示在屏幕上，这是标准的安全功能。

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
 
