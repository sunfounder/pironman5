在 Home Assistant 上设置
============================================

如果你已经在 Raspberry Pi 上安装了 Home Assistant 系统，你需要添加必要的插件，并启动它们以使 Pironman 5 正常工作。

.. note::

    以下方法仅适用于原生安装了 Home Assistant 的系统，不适用于在 Raspberry Pi 上安装了 Home Assistant 或 Docker 版本的系统。

1. 登录 Home Assistant
-----------------------------

* 启动 Pironman 5 后，建议直接插入网线。这样，你可以打开计算机浏览器并输入： ``homeassistant.local:8123`` 来访问 Home Assistant。

  .. image:: img/home_login.png
   :width: 90%


* 选择 **CREATE MY SMART HOME**，然后创建你的账户。

  .. image:: img/home_account.png
   :width: 90%

* 按照提示选择你的所在位置及其他配置。完成后，你将进入 Home Assistant 控制面板。

  .. image:: img/home_dashboard.png
   :width: 90%


2. 添加 SunFounder 插件库
----------------------------------------------------

Pironman 5 的功能以插件形式安装在 Home Assistant 中。首先，你需要添加 **SunFounder** 插件库。

#. 打开 **Settings** -> **Add-ons**。

   .. image:: img/home_setting_addon.png
      :width: 90%

#. 点击右下角的加号，进入插件商店。

   .. image:: img/home_addon.png
      :width: 90%

#. 在插件商店中，点击右上角的菜单，选择 **Repositories**。

   .. image:: img/home_add_res.png
      :width: 90%

#. 输入 **SunFounder** 插件库的 URL: ``https://github.com/sunfounder/home-assistant-addon`` ，然后点击 **ADD**。

   .. image:: img/home_res_add.png
      :width: 90%

#. 添加成功后，关闭弹窗并刷新页面，找到 SunFounder 插件列表。

   .. image:: img/home_addon_list.png
         :width: 90%

3. 安装 **Pi Config Wizard** 插件
------------------------------------------------------

**Pi Config Wizard** 可以帮助启用 Pironman 5 所需的配置，如 I2C 和 SPI。如果之后不需要，可以卸载该插件。

#. 在 SunFounder 插件列表中找到 **Pi Config Wizard**，点击进入。

   .. image:: img/home_pi_config.png
      :width: 90%

#. 在 **Pi Config Wizard** 页面，点击 **INSTALL**，等待安装完成。

   .. image:: img/home_config_install.png
      :width: 90%

#. 安装完成后，切换到 **Log** 页面，确认是否有错误。

   .. image:: img/home_log.png
      :width: 90%

#. 如果没有错误，返回 **Info** 页面，点击 **START** 来启动该插件。

   .. image:: img/home_start.png
      :width: 90%

#. 现在打开 Web UI。

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. 在 Web UI 中，你会看到一个挂载 Boot 分区的选项。点击 **MOUNT** 来挂载该分区。

   .. image:: img/home_mount_boot.png
      :width: 90%

#. 挂载成功后，你将看到设置 I2C、SPI 并编辑 config.txt 文件的选项。勾选 I2C 和 SPI 以启用它们。当它们显示为已启用时，点击底部的重启按钮来重启 Raspberry Pi。

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. 重启后，刷新页面，你将再次返回到挂载 Boot 分区页面。再次点击 **MOUNT**。

   .. image:: img/home_mount_boot.png
      :width: 90%

#. 通常情况下，你会看到 SPI 已启用，但 I2C 没有，因为 I2C 需要重启两次。再次启用 I2C，然后重启 Raspberry Pi。

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. 重启后，再次返回 **MOUNT** 页面。此时你会看到 I2C 和 SPI 都已启用。

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * 如果刷新页面后没有进入挂载分区页面，你可以再次点击 **Settings** -> **Add-ons** -> **Pi Config Wizard**。
    * 检查此插件是否已启动。如果没有，点击 **START**。
    * 启动后，点击 **OPEN Web UI**，然后点击 **MOUNT** 来确认 I2C 和 SPI 是否已启用。

4. 安装 **Pironman 5** 插件
---------------------------------------------

现在正式开始安装 **Pironman 5** 插件。

#. 打开 **Settings** -> **Add-ons**。

   .. image:: img/home_setting_addon.png
      :width: 90%

#. 点击右下角的加号，进入插件商店。

   .. image:: img/home_addon.png
      :width: 90%

#. 在 **SunFounder** 插件列表中找到 **Pironman 5**，点击进入。

   .. image:: img/home_pironman5_addon.png
      :width: 90%

#. 现在安装 Pironman 5 插件。

   .. image:: img/home_install_pironman5.png
      :width: 90%

#. 安装完成后，点击 **START** 来启动此插件。你会看到 OLED 屏幕显示 Raspberry Pi 的 CPU、温度和其他相关信息。四个 WS2812 RGB LED 将以呼吸模式亮起，颜色为蓝色。

   .. image:: img/home_start_pironman5.png
      :width: 90%

#. 现在你可以点击 **OPEN WEB UI** 来打开 Pironman 5 的网页。你也可以在侧边栏中选中显示 Web UI，这样你就能在 Home Assistant 的左侧边栏看到 Pironman 5 选项，点击即可打开 Pironman 5 页面。

   .. image:: img/home_web_ui.png
      :width: 90%

#. 现在你可以查看 Raspberry Pi 的信息，配置 RGB 并控制风扇等。

   .. image:: img/home_web_new.png
      :width: 90%

.. note::

    有关此 Pironman 5 网页的更多信息和使用，请参考： :ref:`view_control_dashboard`。
