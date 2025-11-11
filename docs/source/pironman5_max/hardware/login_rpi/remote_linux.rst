针对 Linux/Unix 用户
==========================

#. 找到并打开您 Linux/Unix 系统中的 **终端（Terminal）**。

#. 确保树莓派已连接至与电脑相同的网络。您可以通过输入 `ping <hostname>.local` 来确认，例如：

    .. code-block::

        ping raspberrypi.local

    如果树莓派已成功连接网络，您将看到其 IP 地址的响应。

    * 若终端显示类似 ``Ping request could not find host pi.local. Please check the name and try again.`` 的提示，请检查主机名是否输入正确。
    * 如果无法获取 IP 地址，请检查树莓派的网络或 WiFi 设置。

#. 输入命令 ``ssh <username>@<hostname>.local`` 或 ``ssh <username>@<IP address>`` 来发起 SSH 连接。例如：

    .. code-block::

        ssh pi@raspberrypi.local

#. 初次登录时，系统会显示一条安全提示信息。请输入 ``yes`` 继续连接。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入您之前设置的密码。请注意，出于安全考虑，输入密码时终端中不会显示任何字符。

    .. note::
        输入密码时不显示字符属于正常现象。请确保输入无误。

#. 登录成功后，即表示您已成功连接树莓派，可以继续进行下一步操作。
