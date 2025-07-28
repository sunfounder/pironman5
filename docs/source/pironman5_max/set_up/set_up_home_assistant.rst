在 Home Assistant 上设置
============================================

如果你已经安装了 Home Assistant 系统，需要在 Home Assistant 中添加必要的附加组件并启动，以使 Pironman 5 MAX 正常运行。

.. note::

    以下方法仅适用于原生安装 Home Assistant 的系统。不适用于在 Raspberry Pi 系统上叠加安装 Home Assistant 或使用 Docker 版本的 Home Assistant。

1. 登录 Home Assistant
-----------------------------

* 启动 Pironman 5 MAX 后，建议直接插入网线。此时可在电脑浏览器中输入：``homeassistant.local:8123`` 访问 Home Assistant。

  .. image:: img/home_login.png
   :width: 90%


* 选择 **CREATE MY SMART HOME**，然后创建你的账户。

  .. image:: img/home_account.png
   :width: 90%

* 按照提示选择你的位置信息及其他配置。配置完成后将进入 Home Assistant 的控制面板。

  .. image:: img/home_dashboard.png
   :width: 90%


2. 添加 SunFounder 插件仓库
-------------------------------------------

Pironman 5 MAX 的功能通过插件的形式集成在 Home Assistant 中。首先需要添加 **SunFounder** 插件仓库。

#. 打开 **Settings** -> **Add-ons**。

   .. image:: img/home_setting_addon.png
      :width: 90%

#. 点击右下角的加号进入插件商店。

   .. image:: img/home_addon.png
      :width: 90%

#. 在插件商店中，点击右上角菜单，选择 **Repositories**。

   .. image:: img/home_add_res.png
      :width: 90%

#. 输入 **SunFounder** 插件仓库地址： ``https://github.com/sunfounder/home-assistant-addon``，点击 **ADD**。

   .. image:: img/home_res_add.png
      :width: 90%

#. 添加成功后关闭弹窗并刷新页面，即可在插件列表中看到 SunFounder 插件。

   .. image:: img/home_addon_list.png
      :width: 90%

3. 安装 **Pi Config Wizard** 插件
-------------------------------------------

**Pi Config Wizard** 可以帮助启用 Pironman 5 MAX 所需的配置项，如 I2C 和 SPI。配置完成后可以将其卸载。

#. 在 SunFounder 插件列表中找到 **Pi Config Wizard** 并点击进入。

   .. image:: img/home_pi_config.png
      :width: 90%

#. 在插件页面点击 **INSTALL**，等待安装完成。

   .. image:: img/home_config_install.png
      :width: 90%

#. 安装完成后，切换至 **Log** 页面检查是否有报错信息。

   .. image:: img/home_log.png
      :width: 90%

#. 若无报错，返回 **Info** 页面，点击 **START** 启动插件。

   .. image:: img/home_start.png
      :width: 90%

#. 启动后点击 **OPEN WEB UI** 打开网页界面。

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. 在网页界面中会出现挂载 Boot 分区的选项，点击 **MOUNT**。

   .. image:: img/home_mount_boot.png
      :width: 90%

#. 挂载成功后，可设置 I2C、SPI 以及编辑 config.txt 文件。勾选 I2C 和 SPI 启用，显示为启用状态后点击底部的重启按钮重启树莓派。

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. 重启后刷新页面，回到挂载 Boot 分区界面，再次点击 **MOUNT**。

   .. image:: img/home_mount_boot.png
      :width: 90%

#. 通常此时 SPI 已启用，而 I2C 仍未启用，因为 I2C 需要两次重启。请再次启用 I2C 并重启。

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. 重启后再次返回 **MOUNT** 页面，你将看到 I2C 和 SPI 均已启用。

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * 如果刷新页面后没有进入挂载分区页面，可前往 **Settings** -> **Add-ons** -> **Pi Config Wizard**。
    * 确认该插件是否已启动，若未启动请点击 **START**。
    * 启动后点击 **OPEN WEB UI**，再点击 **MOUNT** 检查 I2C 和 SPI 是否已启用。

4. 安装 **Pironman 5 MAX** 插件
-------------------------------------------

现在正式安装 **Pironman 5 MAX** 插件。

#. 打开 **Settings** -> **Add-ons**。

   .. image:: img/home_setting_addon.png
      :width: 90%

#. 点击右下角加号进入插件商店。

   .. image:: img/home_addon.png
      :width: 90%

#. 在 **SunFounder** 插件列表中找到 **Pironman 5 MAX** 并点击进入。

   .. image:: img/home_pironman5_addon.png
      :width: 90%

#. 安装 Pironman 5 MAX 插件。

   .. image:: img/home_install_pironman5.png
      :width: 90%

#. 安装完成后点击 **START** 启动插件。此时 OLED 屏幕将显示树莓派的 CPU、温度等信息，四颗 WS2812 RGB 灯将以呼吸灯模式亮起蓝光。

   .. image:: img/home_start_pironman5.png
      :width: 90%

#. 现在可点击 **OPEN WEB UI** 打开 Pironman 5 MAX 的网页控制界面。你也可以勾选在侧边栏显示 Web UI，这样你就能在 Home Assistant 的左侧边栏中看到 Pironman 5 MAX 入口，点击即可进入控制页面。

   .. image:: img/home_web_ui.png
      :width: 90%

#. 在该页面中，你可以查看树莓派信息，配置 RGB 灯效，以及控制风扇等功能。

   .. image:: img/home_web.png
      :width: 90%

.. note::

    有关 Pironman 5 MAX 网页界面的更多功能说明，请参考：:ref:`max_view_control_dashboard`。
