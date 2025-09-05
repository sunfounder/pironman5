配置 NextCloudPi
=======================================

NextCloud 是一个开源的私人云存储解决方案，类似于 Google Drive 或 Dropbox。  
它可用于存储文件、共享文档、同步照片以及管理日历和联系人。  
与公共云服务不同，NextCloud 让用户能够完全掌控自己的数据，非常适合重视隐私和数据安全的个人和小型团队。

由 Raspberry Pi 驱动的 Pironman5 系列具备低功耗、体积小、性能稳定等特点，是家庭私有云服务器的理想选择。结合 NextCloud，它可以作为一个高性价比的 NAS 系统使用。


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

   默认情况下，你会看到一个警告，提示该站点使用了未被权威证书颁发机构 (CA) 签发的自签名 SSL/TLS 证书。  
   大多数浏览器都会显示此类警告。  
   在这种情况下，你可以放心忽略该警告，接受风险并继续访问。

   .. image:: img/home_server_app/private_save.png


4. 第一次登录时，你需要设置一个管理员密码。

   .. image:: img/home_server_app/ptn_new_admin.png

5. 注册管理员账户后，你将进入 Portainer 界面。在左侧导航栏点击 **Setting -> General**，找到 **App Templates**，并在输入框中填入以下地址：  
   ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

6. 点击 **Save Application Settings**。设置大约需要 10 秒钟完成。


**安装 NextCloud**

1. 在左侧导航栏点击 **Home -> local -> Templates -> Application**。在右上角搜索框输入 *nextcloud* 并点击它。

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

2. 点击 **Deploy the stack**，等待部署完成。通常需要大约两分钟。

   .. image:: img/home_server_app/ptn_temp_deploy.png

部署完成后，NextCloud 就会安装成功。


**使用 NextCloud**

1. 打开浏览器并访问你的 NextCloud 地址: ``http://<your-rpi-ip-address>:32768`` 。

.. note::

   同样，你会看到一个警告，提示该站点使用了未被权威证书颁发机构 (CA) 签发的自签名 SSL/TLS 证书。  
   大多数浏览器都会显示此类警告。  
   在这种情况下，你可以放心忽略该警告，接受风险并继续访问。

   .. image:: img/home_server_app/private_save.png

2. 第一次登录时，你需要设置一个管理员密码。

   .. image:: img/home_server_app/nc_admin_install.png

3. 注册完成后，你就可以开始使用 NextCloud 了。

   .. image:: img/home_server_app/nc_dashboard.png
