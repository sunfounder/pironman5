组装摄像头模块
===========================================

请按照以下步骤组装摄像头模块：

1. 取下机壳上的两块亚克力面板。

   .. image:: img/IN_CMR/IN.CMR.1.png
      :width: 500
      :align: center

2. 如图所示，断开 2 针电源线和 FPC 排线。

   .. image:: img/IN_CMR/IN.CMR.2.png
      :width: 500
      :align: center

3. 拆下四颗螺丝，取出 NVMe PIP 和电源开关转换器模块组。

   .. image:: img/IN_CMR/IN.CMR.3.png
      :width: 500
      :align: center

4. 拆解模块组。过程中需要移除一个铆钉，可用螺丝刀从中部将铆钉轴顶出后，再将整个铆钉取出。

   .. image:: img/IN_CMR/IN.CMR.4.png
      :width: 500
      :align: center

5. 将摄像头模块连接到 FPC 排线上。

   .. image:: img/IN_CMR/IN.CMR.5.png
      :width: 500
      :align: center

6. 将 FPC 排线从机壳上的 CAMERA 开孔处穿入。

   .. image:: img/IN_CMR/IN.CMR.6.png
      :width: 500
      :align: center

7. 继续将 FPC 排线完整穿过 CAMERA 开孔。

   .. image:: img/IN_CMR/IN.CMR.7.png
      :width: 500
      :align: center

8. 将 FPC 连接到树莓派。这一步空间较小，请小心操作。

   .. image:: img/IN_CMR/IN.CMR.8.png
      :width: 500
      :align: center

9. 启动主机并检查摄像头模块是否连接成功。

   * 首先连接显示器或通过 VNC 登录树莓派；
   * 显示器连接好后，打开终端，执行以下命令： ``raspistill -o test.jpg``
   * 如果摄像头模块正常工作，该命令会拍摄一张照片并保存为 ``test.jpg``；
   * 打开 ``test.jpg`` ，检查图像是否成功捕获。

10. 将电源开关转换器重新安装回机壳内。

   .. image:: img/IN_CMR/IN.CMR.9.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.10.png
      :width: 500
      :align: center

11. 将 NVMe PIP 模块重新安装回机壳内。

   .. image:: img/IN_CMR/IN.CMR.11.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.12.png
      :width: 500
      :align: center

12. 最后将机壳盖板重新装回。

   .. image:: img/IN_CMR/IN.CMR.13.png
      :width: 500
      :align: center
