适用于 Linux/Unix 用户
==========================

#. 在您的 Linux/Unix 系统中，找到并打开 **终端**（Terminal）。

#. 确保您的 Raspberry Pi 已连接至同一网络。您可以通过输入 `ping <hostname>.local` 进行验证，例如：

    .. code-block::

        ping raspberrypi.local

    如果 Raspberry Pi 已成功连接网络，您将看到其 IP 地址。

    * 若终端提示 ``Ping request could not find host pi.local. Please check the name and try again.``，请检查您输入的主机名是否正确。
    * 如果仍无法获取 IP 地址，请检查 Raspberry Pi 的网络或 WiFi 设置。

#. 在终端中输入 ``ssh <username>@<hostname>.local`` 或 ``ssh <username>@<IP address>`` 来启动 SSH 连接，例如：

    .. code-block::

        ssh pi@raspberrypi.local

#. 第一次登录时，您将看到安全提示信息。输入 ``yes`` 以继续连接。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入您之前设置的密码。出于安全考虑，输入过程中密码不会显示。

    .. note::
        密码在输入时不显示是正常现象，请确保输入正确的密码即可。

#. 登录成功后，即表示您的 Raspberry Pi 已连接，您可以继续进行下一步操作。
