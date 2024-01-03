FAQ
============

OLED Screen Not Working?
--------------------------

If the OLED Screen is not displaying or displaying incorrectly, you can follow these steps to troubleshoot the issue:

Check if the FPC cable of the OLED Screen is properly connected.

#. Use the following command to view the program's run logs and check for error messages.

    .. code-block:: shell

        cat /opt/pironman5/log

#. Alternatively, use the following command to check if the OLED's i2c address 0x3C is recognized:
    
    .. code-block:: shell
        
        sudo i2cdetect -y 1

#. If the first two steps don't reveal any issues, try restarting the pironman5 service to see if that resolves the problem.


    .. code-block:: shell

        sudo pironman5 restart



