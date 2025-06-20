5. 使用命令或控制面板进行控制
=======================================================

成功安装 ``pironman5`` 模块后，系统重启时会自动启动 ``pironman5.service`` 服务。

你可以通过命令行进行监控与控制，或在网页 ``http://<ip>:34001`` 中访问控制面板来管理 Pironman 5。

.. note::

    * 若使用的是 **Home Assistant** 系统，只能通过访问网页 ``http://<ip>:34001`` 进入控制面板进行监控与控制。
    * 若使用的是 **Batocera.linux** 系统，只能通过命令行进行监控与控制。请注意，配置变更后需使用 ``pironman5 restart`` 命令重启服务以使更改生效。


.. toctree::
    :maxdepth: 1

    control_with dashboard 
    control_with_commands