.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _control_commands_dashboard_5:

5. 使用命令或控制面板进行管理
=======================================================

在成功安装 ``pironman5`` 模块后，系统将在重启时自动启动 ``pironman5.service`` 服务。

您可以通过命令行进行监控和控制，也可以通过网页控制面板访问 ``http://<ip>:34001`` 来管理 Pironman 5。

.. note::

    * 在 **Home Assistant** 系统中，仅可通过打开网页 ``http://<ip>:34001`` 使用控制面板进行监控与管理。


.. toctree::
    :maxdepth: 1

    control_with_dashboard 
    control_with_commands