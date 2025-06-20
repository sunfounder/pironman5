适用于 Mac OS X 用户
==========================

对于 Mac OS X 用户来说，SSH（安全外壳协议）是一种安全且便捷的方式，可用于远程访问和控制 Raspberry Pi。无论是在无显示器的场景下，还是需要远程操作时，SSH 都非常实用。借助 Mac 系统中的终端（Terminal）应用，您可以与 Raspberry Pi 建立安全连接。此过程通过包含 Raspberry Pi 用户名与主机名的 SSH 命令实现。在首次连接时，系统会提示您确认连接设备的身份。

#. 要连接到 Raspberry Pi，请输入以下 SSH 命令：

    .. code-block::

        ssh pi@raspberrypi.local

   .. image:: img/mac_vnc14.png

#. 首次登录时将出现安全提示信息，输入 **yes** 继续连接。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入 Raspberry Pi 的登录密码。请注意，出于安全考虑，输入时屏幕不会显示任何字符。

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

