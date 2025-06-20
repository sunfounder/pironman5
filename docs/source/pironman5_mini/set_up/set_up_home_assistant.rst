在 Home Assistant 中进行设置
============================================

如果你已经安装了 Home Assistant 系统，需要在 Home Assistant 中添加并启动相应的附加组件，以启用 Pironman 5 Mini 的功能。

.. note::

    以下方法仅适用于原生安装了 Home Assistant 的系统。不适用于在 Raspberry Pi 上运行的 Home Assistant 扩展系统或 Docker 版本的 Home Assistant。

1. 登录 Home Assistant
-----------------------------

* 启动 Pironman 5 Mini 后，建议直接插入网线连接网络。然后在电脑浏览器中输入： ``homeassistant.local:8123`` 访问 Home Assistant。

  .. image:: img/home_login.png
   :width: 90%


* 点击 **CREATE MY SMART HOME**，创建你的账户。

  .. image:: img/home_account.png
   :width: 90%

* 按照引导选择位置和其他配置信息，完成后将进入 Home Assistant 控制面板。

  .. image:: img/home_dashboard.png
   :width: 90%


2. 添加 SunFounder 插件源
--------------------------------------------

Pironman 5 Mini 的功能以附加组件形式集成在 Home Assistant 中。首先需要添加 **SunFounder** 插件源。

#. 打开 **Settings** -> **Add-ons**。

   .. image:: img/home_setting_addon.png
      :width: 90%

#. 点击右下角的加号，进入插件商店。

   .. image:: img/home_addon.png
      :width: 90%

#. 在插件商店右上角点击菜单按钮，选择 **Repositories**。

   .. image:: img/home_add_res.png
      :width: 90%

#. 输入 SunFounder 插件源地址： ``https://github.com/sunfounder/home-assistant-addon``，然后点击 **ADD**。

   .. image:: img/home_res_add.png
      :width: 90%

#. 添加成功后，关闭弹窗并刷新页面，找到 SunFounder 插件列表。

   .. image:: img/home_addon_list.png
         :width: 90%

3. 安装 **Pi Config Wizard** 插件
------------------------------------------------------

**Pi Config Wizard** 插件可帮助启用 Pironman 5 Mini 所需的设置（如 I2C 和 SPI）。配置完成后可选择卸载此插件。

#. 在 SunFounder 插件列表中找到 **Pi Config Wizard** 并点击进入。

   .. image:: img/home_pi_config.png
      :width: 90%

#. 在插件页面点击 **INSTALL**，等待安装完成。

   .. image:: img/home_config_install.png
      :width: 90%

#. 安装完成后，切换至 **Log** 页面，确认是否有报错信息。

   .. image:: img/home_log.png
      :width: 90%

#. 若无错误，返回 **Info** 页面，点击 **START** 启动该插件。

   .. image:: img/home_start.png
      :width: 90%

#. 然后点击 **OPEN WEB UI** 打开网页界面。

   .. image:: img/home_open_web_ui.png
      :width: 90%

#. 在 Web UI 中，点击 **MOUNT** 挂载启动分区。

   .. image:: img/home_mount_boot.png
      :width: 90%

#. 成功挂载后，将显示 I2C、SPI 设置以及 config.txt 文件编辑选项。勾选启用 I2C 和 SPI，启用后点击底部的重启按钮重启 Raspberry Pi。

   .. image:: img/home_i2c_spi.png
      :width: 90%

#. 重启后，刷新页面，会再次进入挂载分区页面。点击 **MOUNT** 继续挂载。

   .. image:: img/home_mount_boot.png
      :width: 90%

#. 通常 SPI 会已启用，但 I2C 尚未启用，因为 I2C 需要重启两次。再次启用 I2C，然后重启树莓派。

   .. image:: img/home_enable_i2c.png
      :width: 90%

#. 再次重启后返回 **MOUNT** 页面，你将看到 I2C 和 SPI 都已启用。

   .. image:: img/home_i2c_spi_enable.png
      :width: 90%

.. note::

    * 如果刷新页面后未进入挂载分区界面，可通过 **Settings** -> **Add-ons** -> **Pi Config Wizard** 重新进入。
    * 检查插件是否已启动，若未启动请点击 **START**。
    * 启动后点击 **OPEN WEB UI**，再点击 **MOUNT** 检查 I2C 和 SPI 是否启用。


   
.. .. 这里要改PIRONMAN5 MINI的ADD ON 图


4. 安装 **Pironman 5 Mini** 插件
---------------------------------------------

现在开始正式安装 **Pironman 5 Mini** 插件。

#. 打开 **Settings** -> **Add-ons**。

   .. image:: img/home_setting_addon.png
      :width: 90%

#. 点击右下角的加号，进入插件商店。

   .. image:: img/home_addon.png
      :width: 90%

#. 在 **SunFounder** 插件列表中找到 **Pironman 5 Mini** 并点击进入。

   .. image:: img/home_pironman5_addon.png
      :width: 90%

#. 安装 Pironman 5 插件。

   .. image:: img/home_install_pironman5.png
      :width: 90%

#. 安装完成后点击 **START** 启动插件。你将看到四颗 WS2812 RGB 灯珠以蓝色呼吸灯模式点亮。

   .. image:: img/home_start_pironman5.png
      :width: 90%

#. 点击 **OPEN WEB UI** 打开 Pironman 5 Mini 页面。也可以勾选将其添加至侧边栏，方便在 Home Assistant 左侧菜单中快速访问。

   .. image:: img/home_web_ui.png
      :width: 90%

#. 在页面中你可以查看树莓派信息、配置 RGB 灯效、风扇控制等功能。

   .. image:: img/home_web.png
      :width: 90%

.. note::

    有关 Pironman 5 Mini 页面功能与使用说明，请参考：:ref:`view_control_dashboard_mini`。
