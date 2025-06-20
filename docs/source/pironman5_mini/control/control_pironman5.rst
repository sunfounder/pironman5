5. 通过命令或仪表盘进行控制
=======================================================

成功安装 ``pironman5`` 模块后，系统将在重启时自动启动 ``pironman5.service`` 服务。

您可以通过命令行控制 Pironman 5 Mini，也可以在浏览器中访问 ``http://<ip>:34001`` 打开仪表盘进行监控和管理。

.. note::

    * 对于 **Home Assistant** 系统，仅支持通过浏览器访问 ``http://<ip>:34001`` 打开的仪表盘对 Pironman 5 Mini 进行监控与控制。

    .. * 对于 **Batocera.linux** 系统，仅支持使用命令行方式进行监控与控制。请注意，任何配置更改后都必须使用 ``pironman5 restart`` 命令重启服务以使更改生效。


.. toctree::
    :maxdepth: 1

    control_with dashboard 
    control_with_commands