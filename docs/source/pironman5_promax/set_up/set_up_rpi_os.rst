.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _promax_set_up_pi_os:

Set Up on Raspberry Pi/Ubuntu/Kali/Homebridge OS
==================================================

.. image:: ../img/Pironman-5-Pro-Max.png
    :width: 400
    :align: center

如果你在 Raspberry Pi 上安装了 Raspberry Pi OS、Ubuntu、Kali Linux 或 Homebridge，则需要通过命令行来配置 Pironman 5 Pro MAX。以下是详细教程。

.. note::

  在开始配置之前，请先启动并登录你的 Raspberry Pi。如果不确定如何登录，可以访问 Raspberry Pi 官方网站：|link_rpi_get_start|。


.. _safe_shutdown_promax:

1. Configuring Shutdown to Deactivate GPIO Power
------------------------------------------------------------

为防止关机后由 GPIO 供电的 OLED 屏幕和 RGB 风扇仍然工作，需要设置 Raspberry Pi 在关机时关闭 GPIO 电源。

#. 打开 EEPROM 配置工具：

   .. code-block::

      sudo raspi-config

#. 进入 **Advanced Options → A12 Shutdown Behaviour**\ 。

   .. image:: img/shutdown_behaviour.png

#. 选择 **B1 Full Power Off**\ 。

   .. image:: img/run_power_off.png

#. 保存更改。系统会提示你重启以使新设置生效。


.. _install_pironman5_module_promax:

2. Installing the ``pironman5`` Module
-----------------------------------------------------------

#. 从 GitHub 下载并安装 ``pironman5`` 模块。

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/pironman5/v1/install.sh" | sudo bash


   .. note::

      1. 如果你使用的是 **Ubuntu**\ ，请先安装 ``curl``\ ：\ ``sudo apt install curl -y``

      2. 如果你同时使用 Pironman 5 系列和 **PiPower 5**\ ，请运行以下命令：

      .. code-block:: shell

         curl -sSL "https://raw.githubusercontent.com/sunfounder/pironman5/v1/install.sh" | sudo bash -s -- --pipower5

#. 运行安装程序后，选择你的 Pironman 5 型号（1~4）。

   .. code-block:: shell

      Pironman 5 Installer v1.0.1
      Supports: 5 | 5 Mini | 5 Max | 5 Pro Max

      Please select your product model:
      1) Pironman 5
      2) Pironman 5 Mini
      3) Pironman 5 Max
      4) Pironman 5 Pro Max

      Enter number [1-4]:

#. 安装完成后，按照提示重启 Raspberry Pi。首次启动可能需要最多 30 秒，服务将在此过程中初始化。

   #. Pironman 5 Pro MAX 成功启动后，检查以下组件是否正常工作。

   * **OLED Screen**

     * 显示 CPU 使用率、RAM 使用率、CPU 温度和 IP 地址。
     * 10 秒后自动关闭。
     * 短按电源按钮可唤醒屏幕或切换页面。

   * **Power Button**

     * 短按：开机 / 唤醒 OLED / 切换 OLED 页面。
     * 长按 2 秒：安全关机（需配置 :ref:`safe_shutdown_promax`）。
     * 长按 5 秒：强制关机。

   * **WS2812 RGB LEDs**

     * 蓝色呼吸效果亮起。

   * **PWM Fans**

     * 默认设置为 **Always On（始终开启）** 模式。
     * 可通过命令或仪表盘配置工作模式。

   * **CPU Fan（Tower Cooler Fan）**

     * 根据 CPU 温度自动调整转速。
     * 默认风扇曲线：

       * < 50°C：关闭（0%）
       * 50°C+：低速（30%）
       * 60°C+：中速（50%）
       * 67.5°C+：高速（70%）
       * 75°C+：全速（100%）

#. 使用 ``systemctl`` 管理 ``pironman5.service``\ 。

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   根据需要将 ``restart`` 替换为 ``start``\ 、\ ``stop`` 或 ``status`` 以管理服务。

.. note::

   Pironman 5 Pro MAX 现已配置完成，可以开始使用。

   如需更高级的控制和仪表盘功能，请参阅 :ref:`control_commands_dashboard_promax`。
