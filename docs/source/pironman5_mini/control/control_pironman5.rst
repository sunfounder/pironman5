.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _control_commands_dashboard_mini:

5. Controlling with Commands or the Dashboard
=======================================================

Once you have successfully installed the ``pironman5`` module, the ``pironman5.service`` will automatically start upon reboot.

You can monitor and control the Pironman 5 Mini via commands, or by accessing the dashboard through the webpage at ``http://<ip>:34001``.

.. note::

    * For the **Home Assistant** system, you can only monitor and control the Pironman 5 Mini through the dashboard by opening the webpage at ``http://<ip>:34001``.

    .. * For the **Batocera.linux** system, you can only monitor and control the Pironman 5 Mini via commands. It is important to note that any changes to the configuration require a restart of the service using ``pironman5 restart`` to take effect.


.. toctree::
    :maxdepth: 1

    control_with_dashboard
    control_with_commands