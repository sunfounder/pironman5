.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


NextCloudPi 配置
=======================================

NextCloud 是一个开源私有云存储解决方案，类似于 Google Drive 或 Dropbox。
它可用于存储文件、共享文档、同步照片以及管理日历和联系人。
与公共云服务不同，NextCloud 使用户能够完全控制自己的数据，使其成为重视隐私和数据安全的个人及小型团队的理想解决方案。

基于 Raspberry Pi 的 Pironman5 系列具有低功耗、紧凑尺寸和可靠性能的特点，是构建家庭私有云服务器的绝佳选择。结合 NextCloud，它可以作为一个经济实惠的 NAS 系统使用。

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

4. Raspberry Pi 启动后，打开网页浏览器并访问你的 Portainer 地址： ``https://<你的树莓派IP地址>:9443`` 。

5. 默认情况下，你会看到一个警告，提示该网站使用了未经权威认证机构（CA）颁发的自签名 SSL/TLS 证书。大多数浏览器都会显示此类警告。在这种情况下，你可以安全地忽略此警告，接受风险并继续。

   .. image:: img/home_server_app/private_save.png

#. 首次登录时，你需要设置一个管理员密码。

   .. image:: img/home_server_app/ptn_new_admin.png

#. 注册管理员账户后，你将进入 Portainer 界面。在左侧导航栏中，点击 **Settings（设置） -> General（常规）**\ ，找到 **App Templates（应用模板）**\ ，并在字段中输入以下 URL： ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#. 点击 **Save Application Settings（保存应用设置）**\ 。配置大约需要 10 秒钟。

**安装 NextCloud**

1. 在左侧导航栏中，点击 **Home（主页） -> local**

   .. image:: img/home_server_app/ptn_home_local.png

2. 进入 **Templates（模板） -> Application（应用）**\ 。在右上角的搜索栏中，输入 *nextcloud* 并点击它。

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

3. 点击 **Deploy the stack（部署堆栈）**\ ，然后等待部署完成。这通常需要大约两分钟。

   .. image:: img/home_server_app/ptn_temp_deploy.png

4. 完成后，NextCloud 即安装完毕。

   .. image:: img/home_server_app/ptn_temp_nextcloud_deploy_finish.png

**使用 NextCloud**

1. 打开浏览器并访问你的 NextCloud 地址： ``https://<你的树莓派IP地址>:32768`` 。

.. note::

   同样地，你会看到一个警告，提示该网站使用了未经权威认证机构（CA）颁发的自签名 SSL/TLS 证书。大多数浏览器都会显示此类警告。
   在这种情况下，你可以安全地忽略此警告，接受风险并继续。

   .. image:: img/home_server_app/private_save.png

2. 首次登录时，你需要设置一个管理员密码。

   .. image:: img/home_server_app/nc_admin_install.png

3. 注册后，你就可以开始使用 NextCloud 了。

   .. image:: img/home_server_app/nc_dashboard.png