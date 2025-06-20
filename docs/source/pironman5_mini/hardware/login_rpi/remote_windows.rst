针对 Windows 用户
=======================

对于 Windows 10 及以上版本用户，可通过以下步骤实现远程登录 Raspberry Pi：

#. 在 Windows 搜索栏中输入 ``powershell``，右键点击 ``Windows PowerShell``，选择“以管理员身份运行”。

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. 在 PowerShell 中输入以下命令，以获取 Raspberry Pi 的 IP 地址：

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%
      

   当 Raspberry Pi 成功连接至网络后，其 IP 地址将显示在终端中。

   * 如果终端提示 ``Ping request could not find host pi.local. Please check the name and try again.``，请确认您输入的主机名是否正确。
   * 如果仍无法获取 IP 地址，请检查 Raspberry Pi 的网络或 WiFi 设置。

#. 确认 IP 地址后，使用以下命令登录到您的 Raspberry Pi： ``ssh <用户名>@<主机名>.local`` 或 ``ssh <用户名>@<IP 地址>``。

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        若出现错误提示 ``The term 'ssh' is not recognized as the name of a cmdlet...``，说明系统未预装 SSH 工具。此时请参阅 :ref:`openssh_powershell_mini` 手动安装 OpenSSH，或使用第三方工具如 |link_putty|。

#. 首次登录时会出现安全提示信息，输入 ``yes`` 以继续连接：

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入您之前设置的密码。请注意，输入时密码不会显示，这是正常的安全机制。

    .. note::
        密码输入过程不显示字符属正常现象，请确保输入正确的密码。

#. 成功连接后，您即可开始远程操作 Raspberry Pi。

   .. image:: img/sp221221_140628.png
      :width: 90%

