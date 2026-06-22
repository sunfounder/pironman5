.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _openclaw_5_standard:

.. start_using_openclaw

使用 OpenClaw
========================================

**什么是 OpenClaw？**

可以把它想象成 ChatGPT 的升级版本。传统的聊天机器人只能说话（生成文本），而 OpenClaw 可以采取行动。它能理解你的自然语言指令，并能在你的计算机上实际执行操作，例如运行命令、管理文件以及调用各种工具。

以下是一些极佳的应用场景：

*   **个人全能助手：** 让它帮你管理日程、设置提醒、跟踪任务。你只需在聊天应用（如 Telegram、WhatsApp）中告诉它，它就会记住并执行。
*   **自动化“粘合剂”：** 它可以作为连接你各种服务的纽带。例如，你可以让它监控网站的价格变化。一旦检测到价格下降，它可以自动触发 n8n 自动化工作流，向你发送电子邮件通知。
*   **专用开发助手：** 让它帮你管理服务器、运行脚本、检查日志。你可以简单地说“帮我检查一下系统负载”，它就能通过 SSH 连接到你的服务器，执行命令，并返回结果。
*   **硬件“玩伴”：** 这是一个非常有趣的用例。你可以让 OpenClaw 控制连接到树莓派的硬件。例如，有位开发者用它来控制带机械臂的扫地机器人，甚至让它帮忙分析赛车模拟器数据并显示在 LED 屏幕上。树莓派官方团队甚至用它通过对话方式搭建了一个婚礼自动拍照亭，无需编写一行代码！

**为什么要在树莓派上安装 OpenClaw？**

将其安装在树莓派上有两个主要优点：

*   **安全隔离：** OpenClaw 需要较高的系统权限，这在主计算机上存在风险。使用树莓派作为专用设备，相当于给它一个“沙箱”；即使出现问题，也不会影响你的主系统。
*   **24/7 在线：** 树莓派功耗极低，可以一直保持开启，随时准备执行任务。

----------------------------------------------------------------

OpenClaw 快速入门
------------------------------

如果你想尽快体验 OpenClaw 的强大功能，请使用此方法。它会自动安装并启动一个交互式设置向导。

1.  打开树莓派的终端，直接运行以下命令。此命令会从官方网站下载安装脚本并执行：

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash

    .. note:: 由于新版本更新迅速，你的安装步骤略有不同是正常的。

2.  脚本会自动下载并安装 OpenClaw。

    .. image:: /pironman5/home_server/img/openclaw/install_open_claw.png

3.  然后你会看到一个安全提示，询问你是否信任 OpenClaw。一旦你确认它安全可靠，使用箭头键选择“Yes”，然后按 Enter 键。

    .. image:: /pironman5/home_server/img/openclaw/security_open_claw.png

4.  选择“Quick Start”，然后按 Enter 键。

    .. image:: /pironman5/home_server/img/openclaw/quickstart_open_claw.png

5.  选择你的模型，然后按 Enter 键。这里我们以 OpenAI 为例。

    .. image:: /pironman5/home_server/img/openclaw/model_provider_open_claw.png

6.  选择“OpenAI API Key”。

    .. image:: /pironman5/home_server/img/openclaw/api_key_open_claw.png

7.  现在粘贴 API 密钥。

    .. image:: /pironman5/home_server/img/openclaw/paste_api_key_open_claw.png


8.  访问 |link_openai_platform| 并登录。在 **API keys** 页面上，点击 **Create new secret key**\ 。

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_create.png

9.  填写详细信息（所有者、名称、项目以及必要的权限），然后点击 **Create secret key**\ 。

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_create_confirm.png

10. 密钥创建后，请立即复制——你将无法再次看到它。如果丢失，你需要生成一个新密钥。

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_copy.png

11. 将密钥粘贴到 OpenClaw 配置中。

    .. image:: /pironman5/home_server/img/openclaw/paste_api_key_enter_open_claw.png

12. 选择你想要使用的模型。在此示例中，我们将使用 **Keep current**\ 。

    .. image:: /pironman5/home_server/img/openclaw/model_config_open_claw.png

13. 接下来是频道选择。频道指的是 OpenClaw 支持的通信服务，例如 Telegram、WhatsApp、Discord 等。使用向下箭头键选择“Skip for now”选项，然后按 Enter 键。

    .. image:: /pironman5/home_server/img/openclaw/channel_open_claw.png

14. 接下来，系统会提示你立即配置技能。选择“Yes”，然后按 Enter 键。

    .. image:: /pironman5/home_server/img/openclaw/config_skill_open_claw.png

15. 安装你需要的技能。在以下示例中，我们选择“Skip for now”选项（按空格键选择），然后按 Enter 键。

    .. image:: /pironman5/home_server/img/openclaw/install_skill_open_claw.png

16. 接下来是钩子（Hooks）；我们将勾选“command-logger”和“session-memory”。

    .. image:: /pironman5/home_server/img/openclaw/hooks2_open_claw.png

17. 现在安装完成。选择“Hatch in TUI”并按 Enter 键即可启动 OpenClaw。

    .. image:: /pironman5/home_server/img/openclaw/hatch_open_claw.png

.. note::

   你也可以通过输入以下命令来启动 OpenClaw：

   .. code-block:: bash

      openclaw tui

   你可以按两次 Ctrl+c 退出 TUI 界面。

-----------------------------------------------------

.. end_using_openclaw

让 OpenClaw 操作 Pironman5
----------------------------------------------

为了让 OpenClaw 能够操作 Pironman5，我们需要安装 Pironman5 技能。

1.  确保你已经安装了 Pironman5。如果没有，请参考 :ref:`install_pironman5_module_5`。

2.  在终端中运行以下命令：

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-skill/ ~/.openclaw/skills/pironman5-skill/

3.  现在你可以在 ``openclaw tui`` 中操作 Pironman5 了。尝试在 TUI 中发送命令，例如尝试打开机箱上的 LED 灯、改变它们的颜色，或者让摄像头拍照。你甚至可以告诉它你有一个连接到 GPIO17 的 DHT11 模块，让它告诉你温度。

    .. note:: 如果 OpenClaw 仍然无法识别你导入的技能，请提醒它进行 rsync。

---------------------------------------

.. start_using_openclaw_telegram

使用 Telegram 操作你的系统
---------------------------------------

**概述**

通过 OpenClaw，你可以使用流行的消息应用来操作你的系统（这里我们以 Telegram 为例）。你甚至可以让 OpenClaw 帮你完成这个配置。

只需在 ``openclaw tui`` 中提问：*“我想把你连接到 Telegram，我该怎么做？”*

它会一步步指导你完成整个过程，你可以按照它的指示完成设置。

**前提条件**

开始之前，请确保你具备以下条件：

*   一个 **Telegram 帐户**
*   能够访问 Telegram 网络
*   OpenClaw 成功运行（用 ``openclaw status`` 验证）

**步骤 1：创建一个 Telegram 机器人**

1.  在 Telegram 上找到 **@BotFather** （官方机器人创建工具）
2.  **创建一个新机器人**\ ：发送 ``/newbot`` 命令
3.  **按照提示操作**\ ：
    *   为你的机器人起一个名字（例如： ``我的 OpenClaw 助手``\ ）
    *   为你的机器人设置一个用户名（必须以 ``bot`` 结尾，例如： ``my_openclaw_bot``\ ）
4.  **成功后，你会收到一条消息**\ ，其中包含你的 **机器人令牌**\ ，类似于：

    .. code-block:: text

       1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

    .. warning:: 请像保护密码一样保护此令牌！

**步骤 2：在 OpenClaw 中配置 Telegram**

在 ``openclaw tui`` 中，直接说：

> *“我想把我的 Telegram 机器人连接到 OpenClaw。这是我的机器人令牌：<你的令牌>。请帮我完成配置。”*

OpenClaw 将自动：

*   安装必要的依赖项（如 ``node-telegram-bot-api``\ ）
*   创建 Telegram 网关配置文件
*   测试连接是否成功

**步骤 3：测试连接**

1.  在 Telegram 上找到你新创建的机器人
2.  发送 ``/start`` 命令
3.  机器人应该会回复一个配对码，将此代码发送到 OpenClaw TUI（例如： ``配对码：ZAN4XI34``\ ）
4.  等待配置正确完成
5.  尝试发送简单的命令，如“你好”
6.  如果一切配置正确，你应该会看到来自你机器人的响应

**步骤 4：尽情享受！**

完成此配置后，你将能够：

*   随时随地通过 Telegram 控制你的树莓派
*   远程执行命令并检查系统状态
*   通过集成 GPIO 控制物理设备（如打开 LED）
*   享受与你的 AI 助手的智能交互体验

**安全配置（至关重要！）**

为防止陌生人控制你的系统，请务必实施以下安全措施：

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - 安全措施
     - 配置方法
     - 描述
   * - 限制用户
     - 在配置中设置 ``allowedUsers``
     - 只允许特定的 Telegram 用户
   * - 设置密码
     - 在配置中添加 ``"password": "你的密码"``
     - 执行命令前要求密码验证
   * - 限制命令
     - 创建命令白名单
     - 只允许特定的预定义命令
   * - 审计日志
     - 启用 ``command-logger`` 钩子
     - 记录所有通过 Telegram 执行的命令

**记住：安全第一！** 务必适当地限制用户和命令范围。如果在配置过程中遇到具体问题，请随时寻求帮助。

-------------------------------------

.. end_using_openclaw_telegram

.. start_using_openclaw_faq

OpenClaw 故障排除
-------------------------------------

问：安装过程中，出现错误 ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``\ 。我该怎么办？

    目前可以忽略，但后续步骤中可能会遇到问题。届时请逐一处理。

问：当我运行 ``openclaw tui`` 时，出现错误 ``-bash: openclaw: command not found``\ 。我该怎么办？

    执行以下命令：

    .. code-block:: bash

       echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
       source ~/.bashrc

    现在你应该可以用 ``openclaw tui`` 启动 TUI 界面了。

问：在 ``openclaw tui`` 中，我遇到 ``not connected to gateway — message not sent`` 或 ``gateway disconnected: closed`` 的消息。

    这是因为你的 OpenClaw Gateway 服务没有启动。打开另一个终端，执行以下命令来启动 OpenClaw Gateway：

    .. code-block:: bash

       openclaw gateway

    然后重新启动 ``openclaw tui``\ ，就可以直接使用了。

问：我想设置 OpenClaw Gateway 服务在后台运行/开机自启。怎么做？

    通常情况下，你的 OpenClaw Gateway 服务应该在开机时自动启动。如果没有，你可以用以下命令手动启动。

    1. 创建 ``~/.config/systemd/user`` 目录：

    .. code-block:: bash

       mkdir -p ~/.config/systemd/user

    2. 创建 ``openclaw-gateway.service`` 文件：

    .. code-block:: bash

       cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
       [Unit]
       Description=OpenClaw Gateway
       After=network.target

       [Service]
       Type=simple
       ExecStart=$HOME/.npm-global/bin/openclaw gateway run
       Restart=on-failure
       RestartSec=10
       Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
       Environment="NODE_ENV=production"

       [Install]
       WantedBy=default.target
       EOF

    3. 然后重新加载 systemd 配置：

    .. code-block:: bash

       systemctl --user daemon-reload

    4. 启动服务：

    .. code-block:: bash

       systemctl --user start openclaw-gateway

    此时，重新启动 ``openclaw tui``\ ，就可以直接使用了。

    5. 启用开机自启：

    .. code-block:: bash

       systemctl --user enable openclaw-gateway

问：我的 OpenClaw 无法操作系统，我该怎么办？

    新安装的 OpenClaw 默认可能没有操作你树莓派系统的权限；它只能聊天。我们需要手动配置权限。

    1. 打开 OpenClaw 配置文件：

       .. code-block:: bash

          nano ~/.openclaw/openclaw.json

    2. 找到 ``tools`` 选项，将其改为如下所示。

       .. code-block:: json

         "tools": {
            "profile": "coding",
            "exec": {
               "secrity": "full"
         },

    3. 保存并退出。

    4. 在终端中输入以下命令重启 OpenClaw Gateway：

       .. code-block:: bash

          openclaw gateway restart

    现在，OpenClaw 应该拥有了读写权限，能够操作你的树莓派系统了。

.. end_using_openclaw_faq