适用于 Mac OS X 用户
==========================

对于 Mac OS X 用户而言，SSH（安全外壳协议）是一种远程访问和控制树莓派的安全便捷方式。尤其在树莓派未连接显示器或需要远程操作时，SSH 显得尤为实用。通过 Mac 上的 Terminal（终端）应用，您可以建立这一安全连接。连接过程中，SSH 命令需包含树莓派的用户名和主机名。在首次连接时，系统会弹出安全提示，要求确认树莓派的身份信息。

#. 要连接树莓派，请输入以下 SSH 命令：

    .. code-block::

        ssh pi@raspberrypi.local

   .. image:: img/mac_vnc14.png

#. 首次登录时会弹出安全提示信息。请输入 **yes** 继续连接。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入树莓派的密码。请注意，输入时不会显示密码字符，这是出于安全考虑的正常现象。

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

