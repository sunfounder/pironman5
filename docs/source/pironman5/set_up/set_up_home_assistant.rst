在 Home Assistant 上进行设置
============================================

如果您已经安装了 Home Assistant 系统，则需要在 Home Assistant 中添加相关插件并启动它们，以便让 Pironman 5 正常工作。

.. note::

    以下方法仅适用于原生安装 Home Assistant 的系统，不适用于在其他系统上安装 Home Assistant 的树莓派环境或基于 Docker 的 Home Assistant 版本。

1. 登录 Home Assistant
-----------------------------

* 启动 Pironman 5 后，建议直接连接网线。随后，在电脑浏览器中输入： ``homeassistant.local:8123`` 以访问 Home Assistant。

  .. image:: img/home_login.png
   :width: 90%


* 选择 **CREATE MY SMART HOME**，并创建您的账户。

  .. image:: img/home_account.png
   :width: 90%

* 按照引导完成位置等设置后，您将进入 Home Assistant 的控制面板。

  .. image:: img/home_dashboard.png
   :width: 90%


2. 添加 SunFounder 插件源
------------------------------------------

Pironman 5 的功能以插件形式集成在 Home Assistant 中。首先，需要添加 **SunFounder** 插件源。

#. 打开 **Settings** -> **Add-ons**。

   .. image:: img/home_setting_addon.png
      :width: 90%

#. 点击右下角的加号进入插件商店。

   .. image:: img/home_addon.png
      :width: 90%

#. 在插件商店页面，点击右上角菜单并选择 **Repositories**。

   .. image:: img/home_add_res.png
      :width: 90%

#. 输入 **SunFounder** 插件源地址： ``https://github.com/sunfounder/home-assistant-addon`` ，点击 **ADD**。

   .. image:: img/home_res_add.png
      :width: 90%

#. 添加成功后关闭弹窗并刷新页面，即可看到 SunFounder 插件列表。

   .. image:: img/home_addon_list.png
         :width: 90%

3. 安装 **Pi Config Wizard** 插件
------------------------------------------

**Pi Config Wizard** 插件可以帮助启用 Pironman 5 所需的配置，如 I2C 和 SPI。配置完成后也可将其卸载。

#. 在 SunFounder 插件列表中找到 **Pi Config Wizard** 并点击进入。

   .. image:: img/home_pi_config.png
      :width: 90%

#. 在插件页面点击 **INSTALL** 开始安装，等待安装完成。

   .. image:: img/home_config_install.png
      :width: 90%

#. 安装完成后，切换至 **Log** 页面查看是否有报错。

   .. image:: img/home_log.png
      :width: 90%

#. 若无错误，返回 **Info** 页面，点击 **START** 启动插件。

   .. image:: img/home_start.png
      :width: 90%

#. 然后点击 **OPEN WEB UI** 打开配置界面。

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. 在 Web UI 中，点击 **MOUNT** 挂载 Boot 分区。

   .. image:: img/home_mount_boot.png
      :width: 90%

#. 挂载成功后，将出现 I2C、SPI 的启用选项和 config.txt 的编辑入口。勾选 I2C 和 SPI 项启用后，点击底部的重启按钮重启树莓派。

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. 重启后刷新页面，系统将再次进入挂载 Boot 分区页面，点击 **MOUNT** 继续。

   .. image:: img/home_mount_boot.png
      :width: 90%

#. 通常情况下，SPI 会已启用，而 I2C 仍未启用，因为 I2C 需两次重启。请再次启用 I2C，并重启树莓派。

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. 再次重启后，返回 **MOUNT** 页面，您将看到 I2C 与 SPI 均已启用。

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * 若刷新页面后未跳转至挂载分区页面，请点击 **Settings** -> **Add-ons** -> **Pi Config Wizard** 再次进入。
    * 检查插件是否已启动，若未启动请点击 **START**。
    * 启动后点击 **OPEN WEB UI**，再点击 **MOUNT**，确认 I2C 与 SPI 状态。

4. 安装 **Pironman 5** 插件
---------------------------------------------

现在，正式开始安装 **Pironman 5** 插件。

#. 打开 **Settings** -> **Add-ons**。

   .. image:: img/home_setting_addon.png
      :width: 90%

#. 点击右下角的加号进入插件商店。

   .. image:: img/home_addon.png
      :width: 90%

#. 在 **SunFounder** 插件列表中找到 **Pironman 5** 并点击进入。

   .. image:: img/home_pironman5_addon.png
      :width: 90%

#. 开始安装 Pironman 5 插件。

   .. image:: img/home_install_pironman5.png
      :width: 90%

#. 安装完成后点击 **START** 启动插件。此时 OLED 屏幕将显示树莓派的 CPU、温度等信息，四颗 WS2812 RGB 灯会以蓝色呼吸模式点亮。

   .. image:: img/home_start_pironman5.png
      :width: 90%

#. 接着可点击 **OPEN WEB UI** 打开 Pironman 5 的网页界面。您也可以勾选将其显示在侧边栏，这样您可以在 Home Assistant 左侧边栏中快速访问 Pironman 5 页面。

   .. image:: img/home_web_ui.png
      :width: 90%

#. 在该网页中，您可以查看树莓派的详细信息，配置 RGB 灯效，控制风扇等功能。

   .. image:: img/home_web_new.png
      :width: 90%

.. note::

    关于该 Pironman 5 网页的更多使用说明，请参考：:ref:`view_control_dashboard`。
