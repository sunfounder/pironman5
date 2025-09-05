.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    * **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    * **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    * **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    * **Special Discounts**: Enjoy exclusive discounts on our newest products.
    * **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!



Setting up Plex
=======================================

Plex is a powerful media server platform that allows you to organize, stream, and access your movies, TV shows, music, and photos across multiple devices. By setting up Plex on the Pironman5 series powered by Raspberry Pi, you can create an affordable and energy-efficient home media center that runs 24/7. The Raspberry Pi’s compact size, low power consumption, and flexibility make it an excellent choice for hosting Plex, turning your Pi into a personal entertainment hub accessible from your home network or even remotely.


**Preparation**

* MicroSD card (16GB+, Class 10 recommended)  
* Raspberry Pi official system Raspberry Pi OS (or Raspberry Pi OS Lite)  
* Stable network connection (wired Ethernet recommended)  
* External hard drive or USB stick (for expanded storage)  


**Install Portainer**

Open the terminal and enter the following commands:

1. Install Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Install Portainer

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. Open your browser and visit your Portainer address: ``http://<your-rpi-ip-address>:9443`` .

.. note::

   By default, you may see a warning that the site is using a self-signed SSL/TLS certificate not issued by a known Certificate Authority (CA). Most web browsers will display such a warning.  
   In this case, you can safely ignore it, accept the risk, and proceed.

   .. image:: img/home_server_app/private_save.png


4. On your first login, you will be asked to set an administrator password.

   .. image:: img/home_server_app/ptn_new_admin.png

5. After creating the admin account, you will enter the Portainer interface. From the left navigation bar, go to **Setting -> General**, find **App Templates**, and enter the following URL into the field:  
   ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

6. Click **Save Application Settings**. The setup will take about 10 seconds to complete.


**Install Plex**

1. From the left navigation bar, click **Home -> local -> Templates -> Application**. In the top-right search bar, type *plex* and select it.

   .. image:: img/home_server_app/ptn_temp_plex.png

2. Set the network mode to **host**.

   .. image:: img/home_server_app/ptn_plex_network_host.png

3. Expand **Show advanced options**.

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

4. In the **volume mapping** section, configure the storage paths for your media files and grant Plex read/write permissions. The default paths are ``/portainer/TV`` and ``/portainer/Movies``, both with read/write access enabled.

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

5. Click **Deploy** and wait for Plex to finish installing.


**Configure Plex Server**

1. Open your browser and enter: ``http://<your_ip>:32400/`` . You should now see the Plex interface.

   .. image:: img/home_server_app/plex_visit.png

2. Skip the premium subscription offer.

3. Next, you will see the **Server Setup** screen. You can check *Allow me to access my media outside my home*. For now, it is recommended to leave this unchecked and configure it later if needed.

   .. image:: img/home_server_app/plex_server_setup1.png

4. You will then be prompted to organize your media. You may choose *Skip* and add media later through the settings. However, it is recommended to directly add the storage paths you configured in Portainer’s volume mapping so that Plex can automatically scan and import your media.

   .. image:: img/home_server_app/plex_server_setup2.png

5. Select your media library type, give your library a name, and choose the language.

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6. Add folders. Locate the media storage paths you set earlier and click **Add Library**.

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7. Click **Finish**. Your Raspberry Pi Plex server is now fully configured.

   .. image:: img/home_server_app/plex_server_setup3.png

8. You should now see your media files displayed on the Plex server homepage.

   .. image:: img/home_server_app/plex_index.png
