
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _view_control_dashboard_mini:

View and Control from Dashboard
=========================================

Once you have successfully installed the ``pironman5`` module, the ``pironman5.service`` will start automatically upon reboot.

Now you can open the monitoring page in your browser to see the information about your Raspberry Pi, configure the RGB, and control the fan, etc. The page link is: ``http://<ip>:34001``.

This page has **Dashboard**, **History**, **Log**, and a **Settings** page.

.. image:: img/dashboard_tab.png
  :width: 90%
  
  
Dashboard
-----------------------

There are multiple cards to view the relevant status of the Raspberry Pi, including:

* **Fan**: View the Raspberry Pi's CPU temperature and the PWM fan speed. **GPIO Fan State** indicates the status of the RGB fan. At the current temperature, the RGB fan is off.

  .. image:: img/dashboard_pwm_fan.png
    :width: 90%
    

* **Storage**: Displays the storage capacity of a Raspberry Pi, showing various disk partitions with their used and available space.

  .. image:: img/dashboard_storage.png
    :width: 90%
    

* **Memory**: Shows the Raspberry Pi's RAM usage and percentage.

  .. image:: img/dashboard_memory.png
    :width: 90%
    

* **Network**: Displays the current network connection type, upload, and download speeds.

  .. image:: img/dashboard_network.png
    :width: 90%
    

* **Processor**: Illustrates the Raspberry Pi's CPU performance, including the status of its four cores, operating frequencies, and CPU usage percentage.

  .. image:: img/dashboard_processor.png
    :width: 90%
    

History
--------------

The History page allows you to view historical data. Check the data you want to view in the left sidebar, then select the time range to see the data for that period, and you can also click to download it.

.. image:: img/dashboard_history.png
  :width: 90%
  

Log
------------

The Log page is used to view the logs of the currently running pironman5 service. The pironman5 service includes multiple sub-services, each with its own log. Select the log you want to view, and you can see the log data on the right. If it is blank, it may mean there is no log content.

* Each log has a fixed size of 10MB. When it exceeds this size, a second log will be created.
* The number of logs for the same service is limited to 10. If the number exceeds this limit, the oldest log will be automatically deleted.
* There are filter tools above the log area on the right. You can select the log level, filter by keywords, and use several convenient tools, including **Line Wrap**, **Auto Scroll** and **Auto Update**.
* Logs can also be downloaded locally.

.. image:: img/dashboard_log.png
  :width: 90%
  

Settings
-----------------

There is a settings menu in the upper right corner of the page. 

.. note::
    
    After modifying, you need to click the **SAVE** button at the bottom to save the settings.

.. image:: img/dashboard_settings.png
  :width: 90%
  

* **Dark Mode**: Toggle between light and dark mode themes. The theme option is saved in the browser cache. Changing the browser or clearing the cache will revert to the default light theme.
* **Temperature Unit**: Set the temperature unit displayed by the system.
* **Fan Mode**: You can set the operating mode of the RGB fan. These modes determine the conditions under which the RGB fan will activate.

    * **Quiet**: The RGB fan will activate at 70°C.
    * **Balanced**: The RGB fan will activate at 67.5°C.
    * **Cool**: The RGB fan will activate at 60°C.
    * **Performance**: The RGB fan will activate at 50°C.
    * **Always On**: The RGB fan will always be on.

    For instance, if set to **Performance** mode, the RGB fan will activate at 50°C.

    After saving, if the CPU temperature exceeds 50°C, you will see the **GPIO Fan State** change to ON in the Dashboard, and the RGB fan will start spinning.

  .. image:: img/dashboard_rgbfan_on.png
    :width: 300
    

* **RGB Brightness**: You can adjust the brightness of the RGB LEDs with a slider.
* **RGB Color**: Set the color of the RGB LEDs.
* **RGB Style**: Choose the RGB LEDs display mode. Options include **Solid**, **Breathing**, **Flow**, **Flow_reverse**, **Rainbow**, **Rainbow Reverse**, and **Hue Cycle**.

.. note::

  If you set the **RGB Style** to **Rainbow**, **Rainbow Reverse**, and **Hue Cycle**, you will not be able to set the color.


* **RGB Speed**: Set the speed of the RGB LED changes.

**About Core Fan**

The core fan connects to a dedicated 4-pin PWM fan port on the Raspberry Pi 5. Its default control strategy is a firmware-managed, multi-level intelligent speed adjustment scheme based on CPU temperature. This means that when you use an official or compatible PWM fan and connect it correctly, the system will automatically adjust the fan speed according to changes in CPU temperature (starting to operate above 50°C) without any manual intervention from you.
