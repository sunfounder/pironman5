针对 Mac OS X 用户
==========================

对于 Mac OS X 用户而言，SSH（安全外壳协议）是一种安全且便捷的方式，可用于远程访问和控制 Raspberry Pi。这种方式尤其适用于远程操作或设备未连接显示器时的使用场景。您可以通过 Mac 自带的 Terminal 应用程序建立与 Raspberry Pi 的安全连接。连接过程涉及输入包含用户名与主机名的 SSH 命令。首次连接时，系统将提示您确认 Raspberry Pi 的身份信息。

#. 在终端中输入以下 SSH 命令以连接 Raspberry Pi：

    .. code-block::

        ssh pi@raspberrypi.local

   .. image:: img/mac_vnc14.png

#. 首次登录时会出现一条安全提示信息，输入 **yes** 继续连接：

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入 Raspberry Pi 的登录密码。请注意，为了安全起见，输入密码时不会在屏幕上显示任何字符。

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

