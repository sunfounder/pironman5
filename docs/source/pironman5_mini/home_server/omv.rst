.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!



.. _mini_omv_5_mini:


Setting Up OpenMediaVault
=====================================

.. warning::

   OpenMediaVault **does not** support installation on the Raspberry Pi OS desktop.

   ⚠️ **Only Raspberry Pi OS Lite versions 11 (Bullseye) and 12 (Bookworm) are supported.** 

   Please make sure you have installed the correct operating system and configured the network.
   The procedure here is consistent with :ref:`install_os_sd_rpi_mini`, but when selecting an image, please choose Raspberry Pi OS Lite from Raspberry Pi OS (other).

   .. image:: img/omv/omv-install-1.png

OpenMediaVault (abbreviated as OMV) is an open-source Network Attached Storage (NAS) operating system based on Debian Linux, designed for home users and small office environments, aiming to simplify storage management and provide rich network service features.

Please follow these steps to install OpenMediaVault on your Raspberry Pi:

1. Connect to Your Raspberry Pi Using SSH
-----------------------------------------------------------

   Enter the following command in the terminal:

   .. code-block:: bash

      ssh pi@raspberrypi.local

   If you are using Windows, use PuTTY or another SSH client to connect to your Raspberry Pi.

2. Install OpenMediaVault
----------------------------

   Enter the following command in the terminal:

   .. code-block:: bash

      wget https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install  
      chmod +x install  
      sudo ./install -n

   This will download and run the installation script for OpenMediaVault. Do not restart your Raspberry Pi after installation.

3. Access OpenMediaVault
-----------------------------

   Enter the following URL in your browser to access OpenMediaVault:

   .. code-block:: bash

      http://raspberrypi.local

   .. note:: If you cannot access the above URL, try using the IP address instead, for example, http://192.168.1.100.

   You will see a login page, log in using the default username and password. The default username is ``admin``, and the password is ``openmediavault``.

   .. image:: img/omv/omv-login.png

   After logging in, you will see the main interface of OpenMediaVault.

   .. image:: img/omv/omv-main.png

   Now that you have successfully installed and accessed OpenMediaVault, you can start configuring and managing your storage.


4. Set Up RAID (Optional)
---------------------------------------

   NVMe RAID is a storage solution that combines multiple NVMe Solid State Drives (SSDs) using RAID technology, aimed at maximizing the high-speed performance of the NVMe protocol and the redundancy/performance enhancement features of RAID. Common modes include RAID 0, 1, 5, 10, etc. For dual NVMe SSDs, RAID 0 and RAID 1 are the most commonly used modes.

   * RAID 0 is a striping technology that divides data into multiple stripes and distributes these stripes across multiple hard drives, thus achieving higher read/write speeds. RAID 0 does not provide redundancy protection, so if any one of the hard drives fails, all data will be lost.

   * RAID 1 is a mirroring technology that copies data across multiple hard drives, thus providing redundancy protection. The read/write speeds of RAID 1 depend on the speed of a single hard drive, as data needs to be read from multiple hard drives. If any one of the hard drives fails, the others can continue to provide data.

   .. note:: At least mount 2 disks for RAID 0 or RAID 1. In RAID 0, the capacity of the RAID volume will be the sum of the capacities of all disks. In RAID 1,the capacity of the RAID volume will be the same as the capacity of the smallest disk. 

   1. In the ``System`` menu click on the ``Plugins`` option, search for the ``openmediavault-md`` plugin, and install it.

   .. image:: img/omv/omv-raid-1.png

   2. In the ``Storage`` menu click on the ``Disks`` option, erase two SSDs.
   
   .. image:: img/omv/omv-raid-2.png

   3. Please note that this action will erase all data on the hard drives, make sure you have backed up all important data.

   .. image:: img/omv/omv-raid-3.png

   4. Erase mode select ``QUICK`` is sufficient.

   .. image:: img/omv/omv-raid-4.png

   5. Enter the ``Multiple Device`` tab, click ``Create``.

   .. image:: img/omv/omv-raid-5.png

   6. In the Level option, you can choose Stripe (RAID 0) or Mirror (RAID 1). In the Devices option, select the hard drives you just erased. Click ``Save`` and wait for the RAID configuration to complete.

   .. image:: img/omv/omv-raid-6.png

   .. note:: If an error report (500 - Internal Server Error) pops up, try restarting the OMV system.

   7. Apply the configuration by clicking on the ``Apply`` button.

   .. image:: img/omv/omv-raid-7.png

   8. After the RAID configuration is complete, you have to wait the state of the RAID to be ``100%``.

   .. image:: img/omv/omv-raid-8.png

   9. After the RAID configuration is complete, your hard drives are now in a RAID 0 or RAID 1 configuration, and you can use them as a single storage device.

5. Configure Storage
-----------------------

   In the main interface of OpenMediaVault, click on the ``Storage`` option in the left-side menu. In the ``Storage`` page, click on the ``Disks`` tab. On the ``Disks`` page, you will see all the disks on your Raspberry Pi. Ensure your NVMe PIP has a connected hard drive.

   .. image:: img/omv/omv-disk.png

   1. In the sidebar, click the ``File System`` option. Then create and mount a file system. Choose ``ext4`` as the file system type.

   .. image:: img/omv/omv-mount.png

   2. Select Device, and save. 
   
   .. note:: If you have set up the RAID, you will see the RAID device in the list. Just select it and save.

   .. image:: img/omv/omv-mount-2.png

   3. A window will appear, informing you that the file system is being created, please wait a moment.

   .. image:: img/omv/omv-mount-3.png

   4. Once done, you will enter the ``Mount`` interface, select the file system you just created, and mount it to your Raspberry Pi.

   .. image:: img/omv/omv-mount-4.png

   .. note:: If you are using dual hard drives (and not RAID), you should repeat the above steps to also mount the second hard drive to your Raspberry Pi.

   5. After mounting, please Apply, and then you can see the data on your hard drives in the file system.

   .. image:: img/omv/omv-mount-5.png

   At this point, you have successfully configured OpenMediaVault and mounted your hard drives. You can now use OpenMediaVault to manage your storage.


6. Create a Shared Folder
---------------------------------------

   1. In the ``Storage`` page, go to the ``Shared Folders`` tab. And click the ``Create`` button.

   .. image:: img/omv/omv-share-1.png

   2. In the ``Create Shared Folder`` page, enter the name of the shared folder, select the hard drive you want to share, the path of the shared folder, and set the permissions of the shared folder. Then click the ``Save`` button.

   .. image:: img/omv/omv-share-2.png

   3. Now you can see the shared folder you just created. Confirm it is correct, then apply.

   .. image:: img/omv/omv-share-3.png

   You have now successfully created a shared folder. 


7. Create a New User
---------------------------------------

   To access the folder, we need to create a new user, please follow these steps:

   1. In the ``User`` page, click the ``Create`` button.

   .. image:: img/omv/omv-user-1.png

   2. In the ``Create User`` page, enter the new user's username and password, then click the ``Save`` button.

   .. image:: img/omv/omv-user-2.png

   You have now successfully created a new user.


8. Set Permissions for the New User
---------------------------------------

   1. In the ``Shared Folders`` page, click on the shared folder you just created. Then click the ``Permissions`` button.

   .. image:: img/omv/omv-user-3.png

   2. In the ``Permissions`` page, set the permissions. Then click the ``Save`` button.

   .. image:: img/omv/omv-user-4.png

   3. After completing, click the ``Apply`` button.

   .. image:: img/omv/omv-user-5.png

   You can now use this new user to access your shared folder.


9. Configure the SMB Service
---------------------------------------

   1. In the ``Services`` page, find the ``SMB/CIFS`` > ``Setting`` tab. And check the ``Enable`` option. Then click the ``Save`` button.

   .. image:: img/omv/omv-smb-1.png

   2. Apply the changes by clicking the ``Apply`` button.

   .. image:: img/omv/omv-smb-2.png

   3. Enter the ``Shares`` page, click the ``Create`` button.

   .. image:: img/omv/omv-smb-3.png

   4. In the ``Create Share`` page, select the path of the shared folder. Then click the ``Save`` button. Incidentally, there are many options on this page that you can configure as needed.

   .. image:: img/omv/omv-smb-4.png

   5. Click ``Apply``.

   .. image:: img/omv/omv-smb-5.png

   You have now successfully configured the SMB service. You can now use the SMB protocol to access your shared folder.


10. Access the Shared Folder on Windows
---------------------------------------

   1. Open ``This PC``, then click ``Map network drive``.

   .. image:: img/omv/omv-network-location-1.png

   2. In the pop-up dialog box, enter the IP of the Raspberry Pi in the ``Folder`` field, for example, ``\\192.168.1.100\``, or the Raspberry Pi's hostname, for example, ``\\pi.local\``.

   .. image:: img/omv/omv-network-location-2.png

   3. Click the browse button, then select the shared folder you want to access. During this process, you will need to enter the username and password you created earlier.

   .. image:: img/omv/omv-network-location-3.png

   4. Check "Reconnect at sign-in", and click the ``Finish`` button.

   .. image:: img/omv/omv-network-location-4.png
   
   5. You can now access the NAS shared folder.

   .. image:: img/omv/omv-network-location-5.png

10. Access the Shared Folder on Mac
-------------------------------------

   1. In the ``Go`` menu, click ``Connect to Server``.

   .. image:: img/omv/omv-mac-1.png

   2. In the pop-up dialog box, enter the IP of the Raspberry Pi, such as ``smb://192.168.1.100``, or the Raspberry Pi's hostname, such as ``smb://pi.local``.

   .. image:: img/omv/omv-mac-2.png

   3. Click the ``Connect`` button.

   .. image:: img/omv/omv-mac-3.png

   4. In the pop-up dialog box, enter the username and password you created earlier. Click the ``Connect`` button.

   .. image:: img/omv/omv-mac-4.png

   5. You can now access the NAS shared folder.

   .. image:: img/omv/omv-mac-5.png
