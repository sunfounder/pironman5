.. _view_control_dashboard_mini:

通过仪表盘查看与控制
=========================================

成功安装 ``pironman5`` 模块后，系统将在重启时自动启动 ``pironman5.service`` 服务。

现在，您可以在浏览器中打开监控页面，查看 Raspberry Pi 的运行信息，设置 RGB 灯光，控制风扇等。页面地址为： ``http://<ip>:34001``。

该页面包括 **Dashboard**、 **History**、 **Log** 以及 **Settings** 四个子页面。

.. image:: img/dashboard_tab.png
  :width: 90%
  
  
Dashboard（仪表盘）
-----------------------

仪表盘页面包含多个卡片，可用于查看 Raspberry Pi 的相关状态信息，包括：

* **Fan**：查看 Raspberry Pi 的 CPU 温度和 PWM 风扇转速。 **GPIO Fan State** 表示 RGB 风扇的当前状态。当前温度下，RGB 风扇处于关闭状态。

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%
    

* **Storage**：显示 Raspberry Pi 的存储容量，展示各个磁盘分区的已用空间与可用空间。

  .. image:: img/dashboard_storage.png
    :width: 90%
    

* **Memory**：显示 Raspberry Pi 的内存使用情况及使用率百分比。

  .. image:: img/dashboard_memory.png
    :width: 90%
    

* **Network**：显示当前网络连接类型、上传速度和下载速度。

  .. image:: img/dashboard_network.png
    :width: 90%
    

* **Processor**：展示 Raspberry Pi 的 CPU 性能信息，包括四个核心的运行状态、频率和使用率。

  .. image:: img/dashboard_processor.png
    :width: 90%
    

History（历史记录）
---------------------

在历史记录页面，您可以查看设备的历史运行数据。勾选左侧栏中希望查看的项目，然后选择时间范围，即可查看该时间段内的相关数据，还可以点击按钮下载数据。

.. image:: img/dashboard_history.png
  :width: 90%
  

Log（日志）
---------------

日志页面用于查看当前运行的 pironman5 服务的日志信息。pironman5 服务包含多个子服务，每个子服务都有自己的独立日志。选择要查看的日志后，右侧将显示相应内容。如为空，可能表示当前暂无日志信息。

* 每个日志文件的最大容量为 10MB，超出后将自动生成新的日志文件。
* 同一服务最多保留 10 个日志文件，超出后最早的日志将被自动删除。
* 右侧日志区域上方提供过滤工具，可按日志等级筛选、关键词过滤，并使用 **自动换行**、 **自动滚动** 和 **自动更新** 等功能。
* 日志也可下载到本地保存。

.. image:: img/dashboard_log.png
  :width: 90%
  

Settings（设置）
--------------------

页面右上角提供设置菜单。

.. note::

    修改设置后，请务必点击页面底部的 **SAVE** 按钮以保存更改。

.. image:: img/dashboard_settings.png
  :width: 90%
  

* **Dark Mode**：切换亮色或暗色主题。主题配置会保存在浏览器缓存中，若更换浏览器或清除缓存，主题将恢复为默认亮色模式。
* **Temperature Unit**：设置系统显示的温度单位。
* **Fan Mode**：设置 RGB 风扇的工作模式，不同模式决定风扇启动的温度阈值：

    * **Quiet**：风扇在 70°C 启动。
    * **Balanced**：风扇在 67.5°C 启动。
    * **Cool**：风扇在 60°C 启动。
    * **Performance**：风扇在 50°C 启动。
    * **Always On**：风扇始终开启。

    例如，当设置为 **Performance** 模式时，RGB 风扇将在温度达到 50°C 时启动。

    保存设置后，如果 CPU 温度超过 50°C，您将在仪表盘中看到 **GPIO Fan State** 状态变为 ON，RGB 风扇将开始运转。

  .. image:: img/dashboard_rgbfan_on.png
    :width: 300
  

* **RGB Brightness**：通过滑块调节 RGB 灯的亮度。
* **RGB Color**：设置 RGB 灯的颜色。
* **RGB Style**：选择 RGB 灯的显示模式。可选样式包括： **Solid**、 **Breathing**、 **Flow**、 **Flow_reverse**、 **Rainbow**、 **Rainbow Reverse** 和 **Hue Cycle**。

.. note::

  若选择的 **RGB Style** 为 **Rainbow**、 **Rainbow Reverse** 或 **Hue Cycle**，将无法手动设置颜色。


* **RGB Speed**：设置 RGB 灯效的变化速度。