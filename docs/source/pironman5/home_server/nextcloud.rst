.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    * **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    * **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    * **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    * **Special Discounts**: Enjoy exclusive discounts on our newest products.
    * **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!




Setting up NextCloudPi
=======================================

NextCloud is an open-source private cloud storage solution, similar to Google Drive or Dropbox. It can be used to store files, share documents, sync photos, and manage calendars and contacts.  
Unlike public cloud services, NextCloud gives users complete control over their data, making it ideal for individuals and small teams who value privacy and data security.

The Pironman5 series powered by Raspberry Pi offers low power consumption, compact size, and reliable performance, which makes it an excellent choice for a home private cloud server. Combined with NextCloud, it can serve as a cost-effective NAS system.


**Preparation**

* MicroSD card (16GB+, Class 10 recommended)  
* Raspberry Pi official system Raspberry Pi OS (or Raspberry Pi OS Lite)  
* Stable network connection (wired Ethernet recommended)  
* External hard drive or USB stick (for expanded storage)  


**Install portainer**

Open the terminal and enter the following commands:

1. Install docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Install portainer

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. Open your browser and visit your portainer address: ``http://<your-rpi-ip-address>:9443`` .

.. note::

   By default, you will see a warning that the site is using a self-signed SSL/TLS certificate not issued by a known Certificate Authority (CA). Most web browsers will display a warning about such certificates.  
   In this case, you can safely ignore the warning, accept the risk, and continue.

   .. image:: img/home_server_app/private_save.png


4. On the first login, you will need to set an admin password.

   .. image:: img/home_server_app/ptn_new_admin.png

5. After registering the admin account, you will enter the Portainer interface. From the left navigation bar, click **Setting -> General**, find **App Templates**, and enter the following URL in the field: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

6. Click **Save Application Settings**. The setup will take around 10 seconds to complete.


**Install NextCloud**

1. From the left navigation bar, click **Home -> local -> Templates -> Application**. In the upper-right search bar, type *nextcloud* and click it.

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

2. Click **Deploy the stack**, and wait for the deployment to complete. This usually takes about two minutes.

   .. image:: img/home_server_app/ptn_temp_deploy.png

Once completed, NextCloud will be installed.


**Using NextCloud**

1. Open your browser and visit your NextCloud address: ``http://<your-rpi-ip-address>:32768`` .

.. note::

   Similarly, you will see a warning that the site is using a self-signed SSL/TLS certificate not issued by a known Certificate Authority (CA). Most web browsers will display a warning about such certificates.  
   In this case, you can safely ignore the warning, accept the risk, and continue.

   .. image:: img/home_server_app/private_save.png

2. On the first login, you will need to set an admin password.

   .. image:: img/home_server_app/nc_admin_install.png

3. After registration, you can start using NextCloud.

   .. image:: img/home_server_app/nc_dashboard.png
