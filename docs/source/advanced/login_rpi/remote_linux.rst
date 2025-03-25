For Linux/Unix 用户
==========================

#. 在你的Linux/Unix系统上找到并打开 **终端** 。

#. 确保你的Raspberry Pi连接到了同一个网络。通过输入 `ping <hostname>.local` 来验证。例如：

    .. code-block::

        ping raspberrypi.local

    如果Raspberry Pi连接到了网络，你应该能看到它的IP地址。

    * 如果终端显示 ``Ping请求无法找到主机pi.local。请检查名称并重试。`` ，请仔细检查你输入的主机名是否正确。
    * 如果仍然无法获取IP地址，请检查Raspberry Pi的网络或WiFi设置。

#. 输入 ``ssh <username>@<hostname>.local`` 或 ``ssh <username>@<IP address>`` 来发起SSH连接。例如：

    .. code-block::

        ssh pi@raspberrypi.local

#. 在首次登录时，会出现安全提示。输入 ``yes`` 以继续。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入你之前设置的密码。请注意，为了安全，密码在输入时不会显示。

    .. note::
        密码字符不在终端显示是正常现象。只需确保输入正确的密码。

#. 登录成功后，你的Raspberry Pi已连接，接下来可以进行下一步操作。
