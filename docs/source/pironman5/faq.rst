常见问题（FAQ）
==================

1. 关于兼容系统
-------------------------------

以下系统已通过 Raspberry Pi 5 的兼容性测试：

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. 关于电源按钮
--------------------------

该电源按钮为 Raspberry Pi 5 的扩展电源键，其功能与树莓派 5 自带电源按钮完全一致。

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **关机操作**

  * 若运行的是 **Raspberry Pi OS Desktop** 系统，快速按下电源按钮两次即可关机；
  * 若运行的是 **Raspberry Pi OS Lite** 系统，按下一次电源按钮即可触发关机；
  * 若需强制关机，请长按电源按钮。

* **开机操作**

  * 若树莓派处于关机但仍通电状态，短按电源按钮可重新开机。

* 若系统不支持关机按钮，长按 5 秒可实现强制关机，之后短按一次即可开机。

3. 关于风道设计
-------------------------------

Pironman 5 机箱的内部风道经过精心设计，以最大化散热效率。冷空气主要从 GPIO 接口及其他开口进入机箱内部，并通过配备高性能风扇的塔式散热器进行降温，最后由侧边的两颗 RGB 风扇将热空气排出。

详细演示请参考下方视频：

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="../_static/video/airflow_direction.mp4"  type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>


4. 关于塔式散热器铜管尾端
----------------------------------------------------------

塔式散热器顶部的 U 型热管在出厂时会进行压扁处理，以便更好地穿过铝制散热鳍片，这属于正常的生产工艺。

   .. image::  img/tower_cooler1.png

5. 关于 Raspberry Pi AI HAT+
----------------------------------------------------------

Raspberry Pi AI HAT+ 与 Pironman 5 不兼容。

   .. image::  img/output3.png
        :width: 400

Raspberry Pi AI 套件由 Raspberry Pi M.2 HAT+ 与 Hailo AI 加速模块组成。

   .. image::  img/output2.jpg
        :width: 400

您可以将 Hailo AI 加速模块从套件中拆下，直接插入 Pironman 5 的 NVMe PIP 模块中使用。

   .. image::  img/output4.png
        :width: 800

6. PI5 无法启动（红灯常亮）？
-------------------------------------------

此问题可能是由于系统更新、启动顺序更改或引导程序损坏导致的。您可以尝试以下步骤来解决该问题：

#. 检查 USB-HDMI 适配器连接

   * 请仔细检查 USB-HDMI 适配器是否牢固连接到 PI5。
   * 尝试拔下并重新插入 USB-HDMI 适配器。
   * 然后重新连接电源，检查 PI5 是否能正常启动。

#. 在机箱外测试 PI5

   * 如果重新插拔适配器仍未解决问题：
   * 将 PI5 从 Pironman 5 机箱中取出。
   * 使用电源适配器直接为 PI5 供电（不通过机箱）。
   * 检查是否能够正常启动。

#. 恢复引导程序

   * 如果 PI5 仍无法启动，可能是引导程序已损坏。您可以参考此教程：:ref:`update_bootloader_5`，并选择从 SD 卡或 NVMe/USB 启动。
   * 将准备好的 SD 卡插入 PI5，通电后至少等待 10 秒。恢复完成后，取出并重新格式化 SD 卡。  
   * 然后使用 Raspberry Pi Imager 烧录最新的 Raspberry Pi OS 镜像，将卡插回，再次尝试启动。

.. 6. Pironman 5 支持复古游戏系统吗？
.. ------------------------------------------------------

.. 支持，但需注意多数复古游戏系统为简化版，无法安装额外软件。这会导致 Pironman 5 的部分硬件功能（如 OLED 显示屏、两个 RGB 风扇和四颗 RGB 灯）无法正常工作，因为它们需要依赖 Pironman 5 的软件包。

.. .. note::

..    Batocera.linux 系统现已全面兼容 Pironman 5。它是一款开源、完全免费的复古游戏系统发行版。

..    * :ref:`install_batocera`
..    * :ref:`set_up_batocera`

7. OLED 屏幕无法正常显示？
-----------------------------------

若 OLED 屏幕没有显示或显示异常，请依照以下步骤排查：

#. 确保 OLED 屏幕的 FPC 排线已牢固连接，建议重新连接后再上电启动。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_oled_screen.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. 确保当前运行的系统为 Pironman 5 支持的系统：

   .. image:: img/compitable_os.png  
      :width: 600  
      :align: center  

   如使用了不兼容系统，请参考 :ref:`install_the_os_5` 更换为支持的操作系统。

#. OLED 屏幕首次通电可能只显示方块图像，请根据 :ref:`set_up_pironman5` 的说明完成配置，之后即可正常显示信息。

#. 执行以下命令，检测 OLED 是否被识别（I2C 地址为 ``0x3C``）：

   .. code-block:: shell

      sudo i2cdetect -y 1

   * 若检测到 ``0x3C``，请使用以下命令重启 Pironman 5 服务：

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * 若未检测到，请开启 I2C 功能：

     * 执行以下命令编辑配置文件：

       .. code-block:: shell

         sudo nano /boot/firmware/config.txt

     * 在文件末尾添加以下行：

       .. code-block:: shell


         dtparam=i2c_arm=on

     * 按 ``Ctrl+X``，再按 ``Y`` 保存并退出。重启 Pironman 5 后再次确认 OLED 显示状态。

若执行以上步骤后问题仍未解决，请发送邮件至 service@sunfounder.com，我们将尽快为您提供支持。

8. NVMe PIP 模块无法正常工作？
---------------------------------------

1. 请确保连接 NVMe PIP 模块与 Raspberry Pi 5 的 FPC 排线已牢固连接。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

2. 确认您的 SSD 是否已正确安装并固定在 NVMe PIP 模块上。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_ssd.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

3. 检查 NVMe PIP 模块上的指示灯状态：

   在确认所有连接无误后，启动 Pironman 5，观察 NVMe PIP 模块上的两个指示灯状态：

   * **PWR LED**：应常亮；
   * **STA LED**：应闪烁，表示运行正常。

   .. image:: img/nvme_pip_leds.png

   * 若 **PWR LED** 亮但 **STA LED** 不闪烁，说明 Raspberry Pi 未识别到 NVMe SSD；
   * 若 **PWR LED** 不亮，请短接模块上的 “Force Enable” 引脚（J4）。若短接后 PWR LED 亮起，可能是排线松动或系统配置不支持 NVMe。

     .. image:: img/nvme_pip_j4.png


4. 确保您的 NVMe SSD 上已正确安装操作系统。参考：:ref:`install_the_os_5`。

5. 若接线无误且系统已安装，但仍无法从 NVMe SSD 启动，请尝试使用 Micro SD 卡启动，确认其他硬件功能是否正常。如一切正常，请继续参考：:ref:`configure_boot_ssd_5`。

如以上步骤仍无法解决问题，请发送邮件至 service@sunfounder.com，我们将尽快协助您处理。

9. RGB 灯无法点亮？
--------------------------

#. J9 上方的 IO 扩展板有两个引脚用于连接 RGB 灯至 GPIO10，请确保这两个引脚上的跳线帽已正确安装。

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. 确保树莓派运行的是兼容的操作系统。Pironman 5 仅支持以下系统版本：

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   如果您安装了不受支持的系统，请参考：:ref:`install_the_os_5` 进行更换。

#. 执行命令 ``sudo raspi-config`` 打开配置菜单，进入 **3 Interfacing Options** -> **I3 SPI** -> **YES**，然后点击 **OK** 和 **Finish** 启用 SPI。启用后重启 Pironman 5。

若执行上述步骤后问题仍未解决，请发送邮件至 service@sunfounder.com，我们会尽快为您提供支持。

10. CPU 风扇不转？
----------------------------------------------

如果 CPU 温度未达到设定阈值，风扇不会启动。

**风扇转速控制逻辑（基于温度）**

PWM 风扇根据树莓派 5 的温度自动调节转速：

* **低于 50°C**：风扇关闭（转速 0%）  
* **达到 50°C**：低速运行（转速 30%）  
* **达到 60°C**：中速运行（转速 50%）  
* **达到 67.5°C**：高速运行（转速 70%）  
* **达到 75°C 及以上**：满速运行（转速 100%）  

详情请参考：:ref:`fan`

11. 如何禁用 Web 控制面板？
------------------------------------------------------

安装 ``pironman5`` 模块后，您可以访问 :ref:`view_control_dashboard`。

若不需要该功能，并希望减少 CPU 和内存占用，可以在安装 ``pironman5`` 时添加 ``--disable-dashboard`` 参数来禁用控制面板：

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

如果您已经安装了 ``pironman 5``，可以卸载 ``dashboard`` 模块和 ``influxdb``，然后重启 pironman5 服务以使更改生效：

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

12. 如何使用 ``pironman5`` 命令控制组件？
----------------------------------------------------------------------

您可以参考以下教程，使用 ``pironman5`` 命令控制 Pironman 5 的各个组件：

* :ref:`view_control_commands`

13. 如何通过命令更改树莓派启动顺序
-------------------------------------------------------------

如果您已登录树莓派系统，可以通过命令修改启动顺序。详细操作请参考：

* :ref:`configure_boot_ssd_5`


14. 如何通过 Raspberry Pi Imager 修改启动顺序？
-------------------------------------------------------------

除了在 EEPROM 配置中修改 ``BOOT_ORDER``，您还可以使用 **Raspberry Pi Imager** 工具更改树莓派的启动顺序。

建议使用一张备用的 Micro SD 卡进行此操作。

* :ref:`update_bootloader_5`

15. 如何将系统从 SD 卡复制到 NVMe SSD？
-------------------------------------------------------------

如果您有 NVMe SSD，但没有适配器可连接到电脑，您可以先将系统安装到 Micro SD 卡上。在成功启动 Pironman 5 后，再将系统从 Micro SD 卡复制到 NVMe SSD。详细操作请参考：


* :ref:`copy_sd_to_nvme_5`

16. 如何撕除亚克力板保护膜
-------------------------------------------------------------

包装内包含两块亚克力板，正反两面均贴有黄色或透明保护膜，用于防止刮花。保护膜可能较难揭除，可使用螺丝刀轻轻刮起角落，再慢慢撕下整张膜。

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center



.. _openssh_powershell:

17. 如何通过 PowerShell 安装 OpenSSH？
-------------------------------------------------------------

当您尝试使用 ``ssh <用户名>@<主机名>.local``（或 ``ssh <用户名>@<IP地址>``）连接树莓派时，若出现以下错误提示：

.. code-block::

    ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
    spelling of the name, or if a path was included, verify that the path is correct and try again.


说明您的 Windows 系统版本较旧，未预装 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_，需要手动安装。

#. 在 Windows 桌面搜索栏中输入 ``powershell``，右键点击 ``Windows PowerShell``，选择 ``以管理员身份运行``。

   .. image:: img/powershell_ssh.png
      :width: 90%


#. 输入以下命令安装 ``OpenSSH.Client``：

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. 安装成功后，会出现以下输出：

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 使用以下命令验证安装结果：

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. 若输出如下内容 ``OpenSSH.Client``，即表示 OpenSSH 安装成功：

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        若未显示上述提示，说明系统版本过旧，建议改用第三方 SSH 工具，例如 |link_putty|。

6. 重启 PowerShell 并继续以管理员身份运行。此时您即可使用 ``ssh`` 命令登录树莓派，系统将提示您输入先前设置的密码。

   .. image:: img/powershell_login.png


.. 18. 为什么 OLED 屏幕会自动关闭？
.. ---------------------------------------------------------------------------------

.. 为了节省电力并延长屏幕的使用寿命，OLED 屏幕会在一段时间无操作后自动关闭。  
.. 这是正常的设计，不会影响产品的功能。

.. 只需按下一次设备上的按钮即可唤醒 OLED 屏幕并恢复显示。

.. .. note::

..    关于 OLED 屏幕的配置（如开/关、休眠时间、旋转等），请参考: :ref:`view_control_dashboard` 或 :ref:`view_control_commands`。
