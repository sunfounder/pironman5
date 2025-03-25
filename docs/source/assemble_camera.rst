组装摄像头模块
===========================================

按照以下步骤组装摄像头模块：

1. 从机箱中取下两个亚克力面板。

   .. image:: img/IN_CMR/IN.CMR.1.png
      :width: 500
      :align: center

2. 如图所示，拆下 2 针线和 FPC。

   .. image:: img/IN_CMR/IN.CMR.2.png
      :width: 500
      :align: center

3. 拆卸四颗螺丝，移除 NVMe PIP 和电源开关转换模块组。

   .. image:: img/IN_CMR/IN.CMR.3.png
      :width: 500
      :align: center

4. 拆解模块组。这需要移除一个铆钉，使用螺丝刀推开铆钉的中央轴心，然后取出整个铆钉。

   .. image:: img/IN_CMR/IN.CMR.4.png
      :width: 500
      :align: center

5. 将摄像头模块连接到 FPC 电缆。

   .. image:: img/IN_CMR/IN.CMR.5.png
      :width: 500
      :align: center

6. 将 FPC 电缆穿过机箱中的摄像头孔。

   .. image:: img/IN_CMR/IN.CMR.6.png
      :width: 500
      :align: center

7. 继续将 FPC 电缆穿过机箱中的摄像头孔。

   .. image:: img/IN_CMR/IN.CMR.7.png
      :width: 500
      :align: center

8. 将 FPC 电缆连接到 Raspberry Pi。此步骤非常紧凑，需要小心操作。

   .. image:: img/IN_CMR/IN.CMR.8.png
      :width: 500
      :align: center

9. 打开主机并检查摄像头模块是否正确连接。

   * 首先，将显示器连接到 Raspberry Pi 或建立 VNC 连接。
   * 设置好显示器后，打开终端并运行以下命令： ``raspistill -o test.jpg``
   * 如果摄像头模块正常工作，此命令将拍摄一张照片并保存为 ``test.jpg`` 。
   * 打开 ``test.jpg`` ，验证图片是否成功捕获。

10. 将电源开关转换器重新组装回机箱。

   .. image:: img/IN_CMR/IN.CMR.9.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.10.png
      :width: 500
      :align: center

11. 将 NVMe PIP 模块重新组装回机箱。

   .. image:: img/IN_CMR/IN.CMR.11.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.12.png
      :width: 500
      :align: center

12. 重新组装机箱盖。

   .. image:: img/IN_CMR/IN.CMR.13.png
      :width: 500
      :align: center
