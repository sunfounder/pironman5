针对 Linux/Unix 用户
==========================

#. 在您的 Linux/Unix 系统中找到并打开 **终端（Terminal）**。

#. 确保您的 Raspberry Pi 已连接至同一网络。可通过以下命令验证连接状态： `ping <hostname>.local`，例如：

    .. code-block::

        ping raspberrypi.local

    如果 Raspberry Pi 成功连接网络，您将看到其 IP 地址返回结果。

    * 如果终端显示类似 ``Ping request could not find host pi.local. Please check the name and try again.`` 的信息，请检查您输入的主机名是否正确。
    * 若无法获取 IP 地址，请检查 Raspberry Pi 的网络或 WiFi 设置。

#. 输入命令 ``ssh <username>@<hostname>.local`` 或 ``ssh <username>@<IP address>`` 来建立 SSH 连接。例如：

    .. code-block::

        ssh pi@raspberrypi.local

#. 首次登录时，系统会显示安全提示信息。请输入 ``yes`` 继续连接。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入您之前设置的密码。请注意，为了安全起见，输入密码时不会显示任何字符。

    .. note::
        密码输入过程中终端不会显示字符是正常现象，请确保输入正确的密码。

#. 成功登录后，您的 Raspberry Pi 已连接完毕，可以进入下一步操作。
