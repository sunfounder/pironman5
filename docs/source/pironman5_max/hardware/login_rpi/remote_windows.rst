适用于 Windows 用户
=======================

对于 Windows 10 及更高版本的用户，可以通过以下步骤远程登录树莓派：

#. 在 Windows 的搜索框中输入 ``powershell``，右键点击 ``Windows PowerShell``，选择“以管理员身份运行”。

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. 在 PowerShell 中输入以下命令，以获取树莓派的 IP 地址：

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%


   如果树莓派已连接网络，其 IP 地址将会显示出来。

   * 若终端显示 ``Ping request could not find host pi.local. Please check the name and try again.``，请检查输入的主机名是否正确。
   * 若仍无法获取 IP 地址，请检查树莓派的网络或 WiFi 设置。

#. 确认 IP 地址后，使用如下命令登录树莓派：

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        如果出现 ``The term 'ssh' is not recognized as the name of a cmdlet...`` 的报错，说明系统尚未安装 SSH 工具。此时请按照 :ref:`max_openssh_powershell` 手动安装 OpenSSH，或使用第三方工具，如 |link_putty|。

#. 初次登录时将弹出安全提示。请输入 ``yes`` 以继续连接。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入您此前设置的密码。注意：出于安全考虑，输入时不会显示任何字符。

    .. note::
        输入密码时看不到字符是正常现象，请确保输入正确。

#. 成功连接后，您就可以对树莓派进行远程操作了。

   .. image:: img/sp221221_140628.png
      :width: 90%

