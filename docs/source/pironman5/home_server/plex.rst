配置 Plex
=======================================

Plex 是一个功能强大的媒体服务器平台，可以帮助你整理、流式播放并在多个设备上访问你的电影、电视剧、音乐和照片。  
通过在搭载 Raspberry Pi 的 Pironman5 系列上部署 Plex，你可以创建一个经济高效、能 24/7 全天候运行的家庭媒体中心。  
Raspberry Pi 具有体积小、功耗低、灵活性高的特点，非常适合用来托管 Plex，将你的设备变成一个可在家庭网络甚至远程访问的个人娱乐中心。


**准备工作**

* MicroSD 卡（16GB 以上，推荐 Class 10）  
* Raspberry Pi 官方系统 Raspberry Pi OS（或 Raspberry Pi OS Lite）  
* 稳定的网络连接（推荐有线以太网）  
* 外置硬盘或 U 盘（用于扩展存储）  


**安装 Portainer**

打开终端并输入以下命令：

1. 安装 Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. 安装 Portainer

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. 打开浏览器并访问你的 Portainer 地址: ``http://<your-rpi-ip-address>:9443`` 。

.. note::

   默认情况下，你可能会看到一个警告，提示该站点使用了未被权威证书颁发机构 (CA) 签发的自签名 SSL/TLS 证书。  
   大多数浏览器会显示此类警告。  
   在这种情况下，你可以放心忽略它，接受风险并继续访问。

   .. image:: img/home_server_app/private_save.png


4. 第一次登录时，你需要设置一个管理员密码。

   .. image:: img/home_server_app/ptn_new_admin.png

5. 创建管理员账户后，你将进入 Portainer 界面。在左侧导航栏点击 **Setting -> General**，找到 **App Templates**，并在输入框中填入以下地址：  
   ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

6. 点击 **Save Application Settings**。设置过程大约需要 10 秒完成。


**安装 Plex**

1. 在左侧导航栏点击 **Home -> local -> Templates -> Application**。在右上角搜索框中输入 *plex* 并选择它。

   .. image:: img/home_server_app/ptn_temp_plex.png

2. 将网络模式设置为 **host**。

   .. image:: img/home_server_app/ptn_plex_network_host.png

3. 展开 **Show advanced options**。

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

4. 在 **volume mapping** 部分，配置媒体文件的存储路径，并赋予 Plex 读/写权限。  
   默认路径为 ``/portainer/TV`` 和 ``/portainer/Movies``，且均启用了读/写权限。

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

5. 点击 **Deploy** 并等待 Plex 安装完成。


**配置 Plex 服务器**

1. 打开浏览器并输入: ``http://<your_ip>:32400/`` 。你现在应该能看到 Plex 界面。

   .. image:: img/home_server_app/plex_visit.png

2. 跳过付费订阅的提示。

3. 接下来会看到 **Server Setup** 页面。你可以选择 *Allow me to access my media outside my home* （允许我在外部访问我的媒体）。  
   建议暂时保持未勾选，必要时再进行配置。

   .. image:: img/home_server_app/plex_server_setup1.png

4. 系统会提示你整理媒体。你可以选择 *Skip* 并稍后通过设置添加媒体。  
   但推荐直接添加之前在 Portainer volume mapping 中配置的存储路径，以便 Plex 自动扫描和导入媒体。

   .. image:: img/home_server_app/plex_server_setup2.png

5. 选择媒体库类型，为你的媒体库命名，并选择语言。

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6. 添加文件夹。找到之前设置的媒体存储路径，然后点击 **Add Library**。

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7. 点击 **Finish**。至此，你的 Raspberry Pi Plex 服务器已成功配置。

   .. image:: img/home_server_app/plex_server_setup3.png

8. 现在你应该能在 Plex 服务器首页看到你的媒体文件。

   .. image:: img/home_server_app/plex_index.png
