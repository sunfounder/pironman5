5. 通过命令或仪表盘进行控制
=======================================================

成功安装 ``pironman5`` 模块后， ``pironman5.service`` 将在重启后自动启动。

你可以通过命令行监控和控制Pironman 5，或者通过网页访问仪表盘，网址为 ``http://<ip>:34001`` 。

.. note::

    * 对于 **Home Assistant** 系统，你只能通过打开 ``http://<ip>:34001`` 的网页访问仪表盘来监控和控制Pironman 5。
    * 对于 **Batocera.linux** 系统，你只能通过命令来监控和控制Pironman 5。需要注意的是，任何配置的更改都需要重启服务，使用 ``pironman5 restart`` 命令才能生效。


.. toctree::
    :maxdepth: 1

    control_with dashboard 
    control_with_commands