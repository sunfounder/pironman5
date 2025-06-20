适用于 Windows 用户
===========================

对于 Windows 10 或更高版本的用户，可通过以下步骤远程登录至 Raspberry Pi：

#. 在 Windows 搜索框中输入 ``powershell``，右键点击 ``Windows PowerShell`` 并选择“以管理员身份运行”。

   .. image:: img/powershell_ssh.png
      :width: 90%


#. 在 PowerShell 中输入以下命令，确定 Raspberry Pi 的 IP 地址：

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%


   当 Raspberry Pi 成功连接至网络后，其 IP 地址将会显示。

   * 如果终端提示 ``Ping request could not find host pi.local. Please check the name and try again.``，请确认输入的主机名是否正确。
   * 若仍无法获取 IP 地址，请检查 Raspberry Pi 的网络或 WiFi 设置。

#. 确认 IP 地址后，使用 ``ssh <用户名>@<主机名>.local`` 或 ``ssh <用户名>@<IP 地址>`` 登录到您的 Raspberry Pi。

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        如果出现 ``The term 'ssh' is not recognized as the name of a cmdlet...`` 的错误提示，说明系统尚未安装 SSH 工具。此时您可以根据 :ref:`openssh_powershell` 手动安装 OpenSSH，或使用第三方工具，如 |link_putty|。

#. 第一次登录时将显示安全提示信息，输入 ``yes`` 以继续连接。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入您先前设置的密码。请注意，输入过程中密码不会显示在屏幕上，这是标准的安全机制。

    .. note::
        输入密码时不显示字符属于正常现象，请确保输入正确即可。

#. 连接成功后，您就可以对 Raspberry Pi 进行远程操作了。

   .. image:: img/sp221221_140628.png
      :width: 90%

