.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


设置 Home Assistant
======================================

Home Assistant 是一个家庭自动化平台，可运行在中央控制设备（如 Raspberry Pi、PC 等）上。它可用于控制和监控各种设备，例如灯光、恒温器、安全摄像头以及智能家居设备。

**准备工作**

开始之前，请确保具备以下条件：

* 一台可以运行 Home Assistant 的 Raspberry Pi。
* 稳定的互联网连接。
* 一个 Home Assistant Cloud 账户（可选，但建议用于远程访问）。

**安装**

打开终端并输入以下命令：

1. 安装 Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash


2. 安装 Home Assistant

.. code-block:: bash

   sudo docker pull homeassistant/home-assistant


**运行 Home Assistant 容器**

这里我们使用 Docker Compose 来运行 Home Assistant。可以将 Docker Compose 理解为一个“自动化脚本”，它会将所有配置（例如镜像名称、端口、数据卷挂载、环境变量等）写入 ``docker-compose.yml`` 文件。之后只需执行简单的命令 ``docker compose up -d``\ ，Docker 就会根据该“脚本”自动创建并启动所有配置好的容器。


1. **进入项目目录**\ ：进入该文件夹。

   .. code-block:: bash

      cd ~/homeassistant


2. **创建配置文件**\ ：在 ``~/homeassistant`` 目录中创建一个名为 ``docker-compose.yml`` 的文件，并将以下配置内容复制进去。

   .. code-block:: bash

      sudo nano docker-compose.yml


3. 将以下内容粘贴到 ``docker-compose.yml`` 文件中：

   .. note:: 请将 ``- TZ=Asia/Shanghai`` 替换为您所在的时区。

   .. code-block:: bash

      version: '3'
      services:
      homeassistant:
         image: ghcr.io/home-assistant/raspberrypi5-64-homeassistant:stable
         container_name: homeassistant
         restart: unless-stopped
         privileged: true
         network_mode: host
         environment:
            - TZ=Asia/Shanghai
         volumes:
            - ./config:/config

4. 按 ``Ctrl+X`` 退出编辑器，然后按 ``Y`` 保存更改。

5. **启动 Home Assistant**\ ：在 ``~/homeassistant`` 目录中运行以下命令。Docker Compose 会自动拉取镜像并启动容器。

   .. code-block:: bash

      sudo docker compose up -d

   * ``up``\ ：创建并启动服务。
   * ``-d``\ ：在后台运行（分离模式）。


6. **检查运行状态**\ ：

    .. code-block:: bash

      docker compose ps

   您应该看到 ``homeassistant`` 的状态显示为 ``Up``\ 。

7. **查看日志** （如果启动出现问题）：

   .. code-block:: bash

      docker compose logs -f

8. 更多命令请查看：

   .. code-block:: bash

      docker compose --help


**设置**

现在，您可以在电脑浏览器中输入： ``http://<Your Raspberry Pi Address>:8123`` 来访问 Home Assistant。

.. image:: img/home_assistant/ha_welcome.png


选择 **CREATE MY SMART HOME**\ ，然后创建您的账户。

.. image:: img/home_assistant/ha_onboarding.png

按照提示选择您的位置以及其他配置。完成后，您将进入 Home Assistant 的控制面板。

.. image:: img/home_assistant/ha_overview.png