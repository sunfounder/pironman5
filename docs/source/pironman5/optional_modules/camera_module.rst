.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    * **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    * **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    * **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    * **Special Discounts**: Enjoy exclusive discounts on our newest products.
    * **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!


Camera Module
===========================================

Follow these steps to assemble the Camera Module:

1. Remove the two acrylic panels from the case.

   .. image:: img/IN.CMR.1.png
      :align: center

2. Detach the 2-pin wire and FPC as shown in the image.

   .. image:: img/IN.CMR.2.png
      :align: center

3. Unscrew the four screws to remove the NVMe PIP and Power Switch Converter module group.

   .. image:: img/IN.CMR.3.png
      :align: center

4. Disassemble the module group. This involves removing a rivet, which should be done by pushing the central shaft of the rivet out with a screwdriver, then removing the entire rivet.

   .. image:: img/IN.CMR.4.png
      :align: center

5. Connect the Camera Module to the FPC cable.

   .. image:: img/IN.CMR.5.png
      :align: center

6. Thread the FPC through the CAMERA hole in the case.

   .. image:: img/IN.CMR.6.png
      :align: center

7. Continue to thread the FPC through the CAMERA hole in the case.

   .. image:: img/IN.CMR.7.png
      :align: center

8. Connect the FPC to the Raspberry Pi. This step is very compact and requires careful handling.

   .. image:: img/IN.CMR.8.png
      :align: center

9. Power on the host and check if the Camera Module is properly connected.

   * First, connect a display to the Raspberry Pi or establish a VNC connection.
   * Once the display is set up, open a terminal and run the following command:  ``raspistill -o test.jpg``
   * If the Camera Module is functioning correctly, this command will capture an image and save it as ``test.jpg``.
   * Open ``test.jpg`` to verify that the image has been successfully captured.

10. Reassemble the Power Switch Converter back into the case.

   .. image:: img/IN.CMR.9.png
      :align: center

   .. image:: img/IN.CMR.10.png
      :align: center

11. Reassemble the NVMe PIP back into the case.

   .. image:: img/IN.CMR.11.png
      :align: center

   .. image:: img/IN.CMR.12.png
      :align: center

12. Reassemble the case cover.

   .. image:: img/IN.CMR.13.png
      :align: center
