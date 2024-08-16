.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Set Up on Home Assistant
============================================

If you have installed the Home Assistant system, you will need to add the necessary add-ons to Home Assistant and start them to get the Pironman 5 working.

.. note::

    The following method is only applicable to systems with Home Assistant installed natively. It does not apply to Raspberry Pi systems with Home Assistant installed on top or to Docker versions of Home Assistant.

1. Log in to Home Assistant
-----------------------------

* After starting Pironman 5, it is recommended to plug in an Ethernet cable directly. This way, you can open your computer browser and enter: ``homeassistant.local:8123`` to access Home Assistant.

  .. image:: img/home_login.png
   :width: 90%


* Select **CREATE MY SMART HOME**, and then create your account.

  .. image:: img/home_account.png
   :width: 90%

* Follow the prompts to choose your location and other configurations. Once completed, you will enter the Home Assistant dashboard.

  .. image:: img/home_dashboard.png
   :width: 90%


2. Add the SunFounder Add-ons Repository
----------------------------------------------------

The functionality of Pironman 5 is installed on Home Assistant in the form of add-ons. First, you need to add the **SunFounder** add-ons repository.

#. Open **Settings** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Click the plus sign in the bottom right corner to enter the add-on store.

   .. image:: img/home_addon.png
      :width: 90%

#. In the add-on store, click the menu in the top right corner and select **Repositories**.

   .. image:: img/home_add_res.png
      :width: 90%

#. Enter the **SunFounder** add-ons repository URL: ``https://github.com/sunfounder/home-assistant-addon``, and click **ADD**.

   .. image:: img/home_res_add.png
      :width: 90%

#. After successfully adding, close the pop-up window and refresh the page. Find the SunFounder add-ons list.

   .. image:: img/home_addon_list.png
         :width: 90%

3. Install the **Pi Config Wizard** Add-on
------------------------------------------------------

The **Pi Config Wizard** can help enable the configurations needed for Pironman 5, such as I2C and SPI. If not needed afterward, it can be removed.

#. Find **Pi Config Wizard** in the SunFounder add-ons list and click to enter.

   .. image:: img/home_pi_config.png
      :width: 90%

#. On the **Pi Config Wizard** page, click **INSTALL**. Wait for the installation to complete.

   .. image:: img/home_config_install.png
      :width: 90%

#. After the installation is complete, switch to the **Log** page to confirm if there are any errors.

   .. image:: img/home_log.png
      :width: 90%

#. If there are no errors, return to the **Info** page and click **START** to start this add-on.

   .. image:: img/home_start.png
      :width: 90%

#. Now open the WEB UI.

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. In the Web UI, you will see an option to mount the Boot partition. Click **MOUNT** to mount the partition.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. After successful mounting, you will see options to set I2C, SPI, and edit the config.txt file. Check I2C and SPI to enable them. Once they show as enabled, click the reboot button at the bottom to restart the Raspberry Pi.

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. After the restart, refresh the page. You will return to the mount boot partition page again. Click **MOUNT** again.

   .. image:: img/home_mount_boot.png
      :width: 90%

#. Usually, you will see that SPI is enabled, but I2C is not because I2C requires two reboots. Enable I2C again, then restart the Raspberry Pi.

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. After the reboot, return to the **MOUNT** page again. You will see that both I2C and SPI are enabled.

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * If after refreshing the page, you do not enter the mount partition page, you can click **Settings** -> **Add-ons** -> **Pi Config Wizard** again.
    * Check if this add-on is started. If not, click **START**.
    * After starting, click **OPEN WEB UI**, then click **MOUNT** to confirm if I2C and SPI are enabled.

4. Install the **Pironman 5** Add-on
---------------------------------------------

Now officially start installing the **Pironman 5** add-on.

#. Open **Settings** -> **Add-ons**.

   .. image:: img/home_setting_addon.png
      :width: 90%

#. Click the plus sign in the bottom right corner to enter the add-on store.

   .. image:: img/home_addon.png
      :width: 90%

#. Find **Pironman 5** in the **SunFounder** add-ons list and click to enter.

   .. image:: img/home_pironman5_addon.png
      :width: 90%

#. Now install the Pironman 5 add-on.

   .. image:: img/home_install_pironman5.png
      :width: 90%

#. After installation is complete, click **START** to start this add-on. You will see the OLED screen display the Raspberry Pi CPU, temperature, and other related information. Four WS2812 RGB LEDs will light up in blue with a breathing mode.

   .. image:: img/home_start_pironman5.png
      :width: 90%

#. Now you can click **OPEN WEB UI** to open the Pironman 5 web page. You can also check the option to display the Web UI in the sidebar. This will allow you to see the Pironman 5 option in the left sidebar of Home Assistant, and click to open the Pironman 5 page.

   .. image:: img/home_web_ui.png
      :width: 90%

#. Now you can see the information about your Raspberry Pi, configure the RGB, and control the fan, etc.

   .. image:: img/home_web.png
      :width: 90%

.. note::

    For more information and usage of this Pironman 5 web page, please refer to: :ref:`view_control_dashboard`.
