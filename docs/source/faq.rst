FAQ
============

OLED Screen Not Working?
--------------------------

If the OLED Screen is not displaying or displaying incorrectly, you can follow these steps to troubleshoot the issue:

Check if the FPC cable of the OLED Screen is properly connected.

#. Use the following command to view the program's run logs and check for error messages.

    .. code-block:: shell

        cat /opt/pironman5/log

#. Alternatively, use the following command to check if the OLED's i2c address 0x3C is recognized:
    
    .. code-block:: shell
        
        sudo i2cdetect -y 1

#. If the first two steps don't reveal any issues, try restarting the pironman5 service to see if that resolves the problem.


    .. code-block:: shell

        sudo pironman5 restart

.. _openssh_powershell:

Install OpenSSH via Powershell
-----------------------------------

When you use ``ssh <username>@<hostname>.local`` (or ``ssh <username>@<IP address>``) to connect to your Raspberry Pi, but the following error message appears.

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


It means your computer system is too old and does not have `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ pre-installed, you need to follow the tutorial below to install it manually.

#. Type ``powershell`` in the search box of your Windows desktop, right click on the ``Windows PowerShell``, and select ``Run as administrator`` from the menu that appears.

    .. image:: img/powershell_ssh.png
        :align: center

#. Use the following command to install ``OpenSSH.Client``.

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. After installation, the following output will be returned.

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verify the installation by using the following command.

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. It now tells you that ``OpenSSH.Client`` has been successfully installed.

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        If the above prompt does not appear, it means that your Windows system is still too old, and you are advised to install a third-party SSH tool, like |link_putty|.

#. Now restart PowerShell and continue to run it as administrator. At this point you will be able to log in to your Raspberry Pi using the ``ssh`` command, where you will be prompted to enter the password you set up earlier.

    .. image:: img/powershell_login.png



