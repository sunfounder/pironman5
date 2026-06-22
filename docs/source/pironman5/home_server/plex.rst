.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Plex 配置
=======================================

Plex 是一个强大的媒体服务器平台，可让您在多台设备上组织、流式传输和访问您的电影、电视剧、音乐和照片。
通过在基于 Raspberry Pi 的 Pironman5 系列上配置 Plex，您可以创建一个经济实惠、低功耗且 24/7 运行的家庭媒体中心。
Raspberry Pi 的紧凑尺寸、低功耗和灵活性使其成为托管 Plex 的绝佳选择，将您的 Pi 转变为可通过家庭网络甚至远程访问的个人娱乐中心。

**准备工作**

*  MicroSD 卡（建议 16GB 以上，Class 10）
*  Raspberry Pi OS 官方系统（或 Raspberry Pi OS Lite）
*  稳定的网络连接（建议使用有线以太网）
*  外部硬盘或 U 盘（用于扩展存储空间）

**安装 Portainer**

打开终端并输入以下命令：

1. 安装 Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. 安装 Portainer

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. 重启你的 Raspberry Pi。（然后 **立即** 执行后续步骤。）

4. Raspberry Pi 启动后，打开网页浏览器并访问你的 Portainer 地址： ``http://<你的树莓派IP地址>:9443`` 。

5. 默认情况下，你可能会看到一个警告，提示该网站使用了未经权威认证机构（CA）颁发的自签名 SSL/TLS 证书。大多数浏览器都会显示此类警告。在这种情况下，你可以安全地忽略此警告，接受风险并继续。

   .. image:: img/home_server_app/private_save.png

#. 首次登录时，你需要设置一个管理员密码。

   .. image:: img/home_server_app/ptn_new_admin.png

#. 创建管理员账户后，你将进入 Portainer 界面。在左侧导航栏中，点击 **Settings（设置） -> General（常规）**\ ，找到 **App Templates（应用模板）**\ ，并在字段中输入以下 URL： ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. 点击 **Save Application Settings（保存应用设置）**\ 。配置大约需要 10 秒钟。

**安装 Plex**

1. 在左侧导航栏中，点击 **Home（主页） -> local**\ 。

   .. image:: img/home_server_app/ptn_home_local.png

2. 进入 **Templates（模板） -> Application（应用）**\ 。在右上角的搜索栏中，输入 *plex* 并点击它。

   .. image:: img/home_server_app/ptn_temp_plex.png

#. 将网络模式设置为 **host（主机）**\ 。

   .. image:: img/home_server_app/ptn_plex_network_host.png

#. 展开 **Show advanced options（显示高级选项）**\ 。

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

#. 在 **volume mapping（卷映射）** 部分，配置媒体文件的存储路径并授予 Plex 读写权限。默认路径是 ``/portainer/TV`` 和 ``/portainer/Movies``\ ，两者都启用了读写访问。

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

#. 点击 **Deploy（部署）**\ ，然后等待 Plex 安装完成。

**配置 Plex 服务器**

1. 打开浏览器并输入： ``http://<你的IP地址>:32400/web`` 。你现在应该能看到 Plex 的界面了。

   .. image:: img/home_server_app/plex_visit.png

2. 忽略高级订阅的推荐。

3. 接下来，你会看到 **服务器设置** 屏幕。你可以勾选 *允许我在家庭网络之外访问我的媒体*。目前建议保持此选项未选中，如有需要可在以后配置。

   .. image:: img/home_server_app/plex_server_setup1.png

4. 接下来，系统会要求你整理媒体。你可以选择 *跳过*，稍后通过设置添加媒体。但是，建议直接添加你在 Portainer 卷映射中配置的存储路径，以便 Plex 能够自动扫描和导入你的媒体。

   .. image:: img/home_server_app/plex_server_setup2.png

5. 选择你的媒体库类型，为你的媒体库命名并选择语言。

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6. 添加文件夹。找到你之前定义的媒体存储路径，然后点击 **添加库**\ 。

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7. 点击 **完成**\ 。你的 Raspberry Pi 上的 Plex 服务器现已完全配置好。

   .. image:: img/home_server_app/plex_server_setup3.png

8. 你现在应该能看到你的媒体文件显示在 Plex 服务器的主页上。

   .. image:: img/home_server_app/plex_index.png