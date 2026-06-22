.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


配置显示
===================================================================

本章节将指导您配置 Pironman 5 Pro MAX 的显示设置，包括启用节能的屏幕自动熄屏功能，以及在特殊安装方向下设置屏幕翻转。


-------------------------------------------------------------------

**设置屏幕空闲休眠**


当您暂时不使用 Pironman 5 Pro MAX 时，可以启用屏幕自动休眠功能以节省电量。当设备在设定时间内处于空闲状态时，主显示屏将自动关闭并进入低功耗状态。

请按照以下步骤进行配置：

1. 点击屏幕左下角的 **Menu -> Preferences**\ ，然后找到并打开 **Control Centre**\ 。

   .. image:: img/sleep_screen1.png

2. 在 Control Centre 界面中，点击进入 **Display** 设置。

3. 找到 **Screen Blanking** 选项，并将其打开。

   .. image:: img/sleep_screen2.png



----------------------------------------------------------------------

**翻转 Pironman 5 Pro MAX**

Pironman 5 Pro MAX 支持翻转安装。在这种安装方式下，触摸屏将位于顶部，而 GPIO 接口位于底部，为各种项目提供更大的安装灵活性。该方式非常适合需要更方便查看屏幕或在连接传感器时更容易访问 GPIO 引脚的应用场景。

翻转设备时，需要分别调整两个显示设备：

   * 主触摸屏 —— 需要在操作系统层面设置屏幕旋转
   * OLED 状态屏 —— 需要通过命令行进行配置

请按照以下步骤翻转 Pironman 5 Pro MAX：


1. 物理准备

   从 Pironman 5 Pro MAX 上取下摄像头，将整个设备翻转，然后重新安装摄像头。安装方式与原始方向保持对称。

   .. image:: img/inverted_screen0.png

2. 设置触摸屏方向

   启动设备。在触摸屏桌面上长按以打开菜单，然后选择 **Desktop Preferences**\ 。

   .. image:: img/inverted_screen1.png

   向下滚动找到 **Screens** 选项，然后在显示界面中长按屏幕图标，选择 **Orientation → Inverted**\ 。

   .. image:: img/inverted_screen2.png

   点击 **Apply**\ ，更新窗口会显示新的屏幕方向，您需要点击 **OK** 进行确认。

   .. image:: img/inverted_screen3.png

3. 配置 OLED 屏幕

   在终端中运行以下命令，将 OLED 屏幕旋转 180°：

   .. code-block:: bash

      sudo pironman5 -or 180

----------------------------------------------------

**注意**

- 翻转设备后，请确保设备放置在稳定的表面上，以防倾倒。
- 如果触控出现偏移，请在系统设置中重新校准触摸屏。
- 若需要更多显示相关的高级设置，请参考 :ref:`promax_view_control_commands` 章节，其中包含更多 OLED 和屏幕旋转相关的命令。