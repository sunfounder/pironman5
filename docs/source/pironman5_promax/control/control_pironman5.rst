.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _control_commands_dashboard_promax:

5. 使用命令或仪表板进行控制
=======================================================

当您成功安装 ``pironman5`` 模块后，\ ``pironman5.service`` 会在系统重启时自动启动。

您可以通过命令行对 Pironman 5 Pro MAX 进行监控和控制，也可以通过浏览器访问 ``http://<ip>:34001`` 打开仪表板（dashboard）进行管理。

.. .. note::

..     * 对于 **Home Assistant** 系统，只能通过访问网页 ``http://<ip>:34001`` 的仪表板来监控和控制 Pironman 5 Pro MAX。

.. .. * 对于 **Batocera.linux** 系统，只能通过命令行方式监控和控制 Pironman 5 Pro MAX。需要注意的是，任何配置更改都需要通过执行 ``pironman5 restart`` 重启服务后才会生效。


.. toctree::
    :maxdepth: 1

    control_with_dashboard 
    control_with_commands
    conf_display