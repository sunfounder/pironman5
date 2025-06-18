.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Install the Raspberry Pi OS
================================================================================

You can choose the installation method based on whether you have a Micro SD or an NVMe SSD at hand.

* Installing directly onto the NVMe SSD involves an additional step compared to installing on the Micro SD: you must update the Raspberry Pi's bootloader because it defaults to boot from the Micro SD card. Update the bootloader to prioritize booting from the NVMe SSD.
* If you have an NVMe SSD but do not have an adapter to connect your NVMe to your computer, consider the third option to first install the system on your Micro SD card. Once the Pironman 5 boots up successfully, you can copy the system from your Micro SD card to your NVMe SSD.


.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi