3.5英寸触摸屏
=============================

.. note::

    Pironman 5 系列产品不包含 3.5 英寸触摸屏。  
    你需要自行准备，或在我们的官方网站购买：

   * `3.5英寸触摸屏 <https://www.sunfounder.com/products/touchscreen-02>`_

3.5 英寸触摸屏可以直接连接到树莓派的 GPIO 引脚，  
为 Pironman 5 提供显示和触控功能。  
请严格按照步骤操作，以确保正确安装并避免硬件损坏。

更多详情请参考：  
`3.5英寸触摸屏文档 <http://wiki.sunfounder.cc/index.php?title=3.5_Inch_LCD_Touch_Screen_Monitor_for_Raspberry_Pi>`_.


**组装**

.. image:: img/lcd_to_mini1.jpg
    :width: 340

.. image:: img/lcd_to_mini2.jpg
    :width: 340


.. warning:: 
   
   在将 3.5 英寸触摸屏安装到 Pironman 5 上时，请确保引脚完全对齐。  
   插针必须与树莓派的 GPIO 接口严格对应，不能有偏移。  
   错误的连接可能会损坏屏幕，甚至损坏树莓派。  
   上电前请再次仔细检查所有连接！


**移除 RGB 跳线**

当 Pironman 5 与 3.5 英寸触摸屏一起使用时，  
注意 IO Expander 上的 RGB LED 与屏幕共享同一个 SPI MOSI 引脚 (GPIO10)。  
为了避免冲突并确保屏幕正常工作，请按以下步骤操作：

1. 在 IO Expander 上，从 **RGB LED 引脚** （J9 上方）拔掉跳线帽。

   .. image:: img/lcd_to_mini0.jpg
      :width: 600
      :align: center

2. 禁用 RGB LED 控制服务：

   .. code-block:: bash

      pironman5 -re false
      sudo systemctl restart pironman5.service

这样可以释放 SPI 接口供 3.5 英寸触摸屏使用，从而避免显示问题。


**驱动安装**

在使用 3.5 英寸触摸屏之前，你需要先安装驱动。

通用提示：

* 确保已安装 git (``sudo apt install git``)。  
* 驱动安装大约需要 1–3 分钟。  
* 系统会自动重启。  

根据你所使用的操作系统，选择对应的安装步骤：  

* **Raspberry Pi OS**:

  .. code-block:: bash
  
     sudo rm -rf LCD-show 
     git clone https://github.com/sunfounder/LCD-show.git 
     chmod -R 755 LCD-show 
     cd LCD-show/ 
     sudo ./LCD35-show
  
  安装完成后，树莓派桌面会显示在 3.5 英寸触摸屏上。  
  
  如果需要旋转屏幕：
  
  .. code-block:: bash
  
     cd LCD-show/
     sudo ./rotate.sh 90   
  
  系统会自动重启，屏幕将旋转 90°。  
  你可以将 ``90`` 替换为 ``0``、 ``180`` 或 ``270`` 来设置角度。



* **Ubuntu**:

  .. code-block:: bash
  
     sudo rm -rf LCD-show-ubuntu 
     git clone https://github.com/sunfounder/LCD-show-ubuntu.git 
     chmod -R 755 LCD-show-ubuntu 
     cd LCD-show-ubuntu/ 
     sudo ./LCD35-show
  
  安装完成后，树莓派桌面会显示在 3.5 英寸触摸屏上。  
  
  如果需要旋转屏幕：
  
  .. code-block:: bash
  
     cd LCD-show-ubuntu/
     sudo ./rotate.sh 90   
  
  系统会自动重启。  
  你可以将 ``90`` 替换为 ``0``、 ``180`` 或 ``270`` 来设置角度。



* **Kali Linux**:

  .. code-block:: bash
  
     sudo rm -rf LCD-show-kali 
     git clone https://github.com/sunfounder/LCD-show-kali.git 
     chmod -R 755 LCD-show-kali 
     cd LCD-show-kali/ 
     sudo ./LCD35-show
  
  安装完成后，树莓派桌面会显示在 3.5 英寸触摸屏上。  
  
  如果需要旋转屏幕：
  
  .. code-block:: bash
  
     cd LCD-show-kali/
     sudo ./rotate.sh 90   
  
  系统会自动重启，并应用新的旋转角度。  
  你可以将 ``90`` 替换为 ``0``、 ``180`` 或 ``270`` 来设置角度。
