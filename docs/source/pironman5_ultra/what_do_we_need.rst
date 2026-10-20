.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



1. What Else Should You Prepare?
===================================

Before assembling and using your Pironman 5 Ultra, please make sure you have the following components ready. Some items are required for basic operation, while others are optional and depend on how you plan to use your Raspberry Pi.

.. note::

   Pironman 5 Ultra can only run on a **64-bit operating system**. Prepare a 64-bit image such as Raspberry Pi OS 64-bit or Ubuntu 64-bit. 32-bit systems are not supported.

Required Components
------------------------------

* **Raspberry Pi 5**

  Pironman 5 Ultra is fully compatible with the Raspberry Pi 5.

  .. image:: img/need_pi5.jpg
     :width: 500

* **Power Supply**

  Pironman 5 Ultra has the PiPower 5 module and a built-in 7.4V 2000mAh battery, so it can be turned on and used **without an external power supply**. Connect a **45W or higher USB Type-C PD** power supply to charge the battery and to run continuous high-load workloads at 5V/5A. The official 27W power supply or |link_sf_27w_supply| also works, but the charging power is then limited to 5W.

  .. image:: img/need_power.png
     :width: 600

* **Micro SD Card**

  The Raspberry Pi does not have a built-in hard drive. It boots and stores all files on a **Micro SD card**.  
  
  .. image:: img/need_sd.jpg
    :width: 200

  * Minimum: **16GB**  
  * Recommended: **32GB** for better stability  
  * Brand: Use reliable options such as **SanDisk** or **Samsung** to avoid read/write errors  
  
Optional Components
------------------------

* **M.2 NVMe SSD**

  Pironman 5 Ultra has two PCIe Gen 2 x1 M.2 M-key slots and supports four NVMe M.2 SSD sizes: 2230, 2242, 2260, and 2280. The link is certified for Gen 2.0 speeds (5 GT/sec).

  .. image:: img/need_nvme.png
    :width: 500

* **Monitor (HDMI or TV)** 

  For beginners, we strongly recommend a display with an HDMI input, so you can easily configure Raspberry Pi OS and run graphical programs.  

  .. image:: img/need_screen.png
    :width: 400

* **HDMI Cable**

  The Raspberry Pi 5's HDMI ports have been adapted to standard HDMI Type A interfaces via the HDMI adapter board. Therefore, a standard HDMI to HDMI cable is needed to connect Pironman 5 Ultra to a display.

  .. image:: img/need_hdmi.png
    :width: 400

* **Keyboard & Mouse**

  Very useful during the initial setup of Raspberry Pi OS. Later, you may switch to remote access (SSH/VNC), but for beginners we recommend preparing a basic USB or wireless set.  

  .. image:: img/need_keyboard_mouse.png
    :width: 500

* **3.5mm Headphones or Speakers** (optional)

  Pironman 5 Ultra has built-in stereo speakers. If you prefer external audio, you can also connect headphones or powered speakers to the 3.5mm jack.

**Tips for Preparation**

* If you purchased this kit, most accessories are included, including the **7.4V 2000mAh Power Pack** battery. You still need to prepare the Raspberry Pi board, Micro SD card, and power adapter separately.  
* Not sure what to buy? The most stable and universal choice is: **Raspberry Pi 5 (2GB) + 45W USB Type-C PD Power Supply + 32GB Micro SD card**.  
