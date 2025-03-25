For Windows 用户
===========================

对于Windows 10或更高版本的用户，可以通过以下步骤实现远程登录到Raspberry Pi：

#. 在Windows搜索框中搜索 ``powershell`` ，右键点击 ``Windows PowerShell`` 并选择 ``以管理员身份运行`` 。

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. 通过在PowerShell中输入 ``ping -4 <hostname>.local`` 来确定Raspberry Pi的IP地址。

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%
      

   一旦Raspberry Pi连接到网络，它的IP地址将会显示出来。

   * 如果终端显示 ``Ping请求无法找到主机pi.local。请检查名称并重试。`` ，请检查您输入的主机名是否正确。
   * 如果仍然无法获取IP地址，请检查Raspberry Pi的网络或WiFi设置。

#. 一旦确认IP地址，使用 ``ssh <username>@<hostname>.local`` 或 ``ssh <username>@<IP address>`` 登录到Raspberry Pi。

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        如果出现错误提示 ``The term 'ssh' is not recognized as the name of a cmdlet...`` ，说明您的系统可能没有预安装SSH工具。在这种情况下，您需要按照 :ref:`openssh_powershell` 手动安装OpenSSH，或使用像 |link_putty| 这样的第三方工具。

#. 在首次登录时，会显示安全警告。输入 ``yes`` 以继续。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入您之前设置的密码。请注意，密码字符不会在屏幕上显示，这是标准的安全功能。

    .. note::
        输入密码时没有显示字符是正常的。确保输入正确的密码。

#. 连接成功后，您的Raspberry Pi即可进行远程操作。

   .. image:: img/sp221221_140628.png
      :width: 90%

