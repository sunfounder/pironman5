Assembling the Camera Module
===========================================

Follow these steps to assemble the Camera Module:

1. Remove the two acrylic panels from the case.

   .. image:: img/IN_CMR/IN.CMR.1.png
      :width: 500
      :align: center

2. Detach the 2-pin wire and FPC as shown in the image.

   .. image:: img/IN_CMR/IN.CMR.2.png
      :width: 500
      :align: center

3. Unscrew the four screws to remove the NVMe PIP and Power Switch Converter module group.

   .. image:: img/IN_CMR/IN.CMR.3.png
      :width: 500
      :align: center

4. Disassemble the module group. This involves removing a rivet, which should be done by pushing the central shaft of the rivet out with a screwdriver, then removing the entire rivet.

   .. image:: img/IN_CMR/IN.CMR.4.png
      :width: 500
      :align: center

5. Connect the Camera Module to the FPC cable.

   .. image:: img/IN_CMR/IN.CMR.5.png
      :width: 500
      :align: center

6. Thread the FPC through the CAMERA hole in the case.

   .. image:: img/IN_CMR/IN.CMR.6.png
      :width: 500
      :align: center

7. Continue to thread the FPC through the CAMERA hole in the case.

   .. image:: img/IN_CMR/IN.CMR.7.png
      :width: 500
      :align: center

8. Connect the FPC to the Raspberry Pi. This step is very compact and requires careful handling.

   .. image:: img/IN_CMR/IN.CMR.8.png
      :width: 500
      :align: center

9. Power on the host and check if the Camera Module is properly connected.

   * First, connect a display to the Raspberry Pi or establish a VNC connection.
   * Once the display is set up, open a terminal and run the following command:  ``raspistill -o test.jpg``
   * If the Camera Module is functioning correctly, this command will capture an image and save it as ``test.jpg``.
   * Open ``test.jpg`` to verify that the image has been successfully captured.

10. Reassemble the Power Switch Converter back into the case.

   .. image:: img/IN_CMR/IN.CMR.9.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.10.png
      :width: 500
      :align: center

11. Reassemble the NVMe PIP back into the case.

   .. image:: img/IN_CMR/IN.CMR.11.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.12.png
      :width: 500
      :align: center

12. Reassemble the case cover.

   .. image:: img/IN_CMR/IN.CMR.13.png
      :width: 500
      :align: center
