.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _openclaw_5_standard:

.. start_using_openclaw

OpenClaw の使用
========================================

**OpenClaw とは？**

ChatGPT のアップグレード版と考えてください。従来のチャットボットは会話（テキスト生成）しかできませんが、OpenClaw は行動を起こすことができます。あなたの自然言語による指示を理解し、コマンドの実行、ファイルの管理、さまざまなツールの呼び出しなど、コンピューター上で実際に操作を実行できます。

以下は、素晴らしいアプリケーションシナリオの例です：

* **パーソナル万能アシスタント:** スケジュール管理、リマインダー設定、タスク追跡などを任せられます。チャットアプリ（Telegram、WhatsApp など）で指示するだけで、それを記憶して実行します。
* **自動化の「接着剤」:** 様々なサービスのバインダーとして機能します。例えば、Webサイトの価格変更を監視させることができます。価格下落が検出されると、自動的に n8n 自動化ワークフローをトリガーして、メール通知を送信させることができます。
* **専用開発アシスタント:** サーバーの管理、スクリプトの実行、ログの確認などを手伝ってもらえます。「システムの負荷を確認して」と言うだけで、SSH でサーバーに接続し、コマンドを実行し、結果を返すことができます。
* **ハードウェアの「遊び相手」:** これは非常に興味深いユースケースです。Raspberry Pi に接続されたハードウェアを OpenClaw に制御させることができます。例えば、ある開発者はこれを使って、ロボットアーム付きのロボット掃除機を制御したり、レーシングシミュレーターのデータを分析して LED スクリーンに表示させたりしました。Raspberry Pi の公式チームでさえ、コードを1行も書かずに、会話だけで結婚式の自動写真撮影ブースを構築するためにこれを使用しました！

**なぜ Raspberry Pi に Openclaw をインストールするのか？**

Raspberry Pi にインストールすることには、主に2つの利点があります：

* **セキュリティ分離:** OpenClaw は高いシステム権限を必要とするため、メインのコンピューターではリスクがあります。Raspberry Pi を専用デバイスとして使用することは、いわば「サンドボックス」を与えるようなもので、たとえ問題が発生しても、メインのシステムに影響を与えません。
* **24時間365日オンライン:** Raspberry Pi は消費電力が非常に低いため、常にオンにしておくことができ、いつでもタスクを実行する準備ができています。

----------------------------------------------------------------

OpenClaw クイックスタート
------------------------------

OpenClaw のパワーをできるだけ早く体験したい場合は、この方法を使用してください。自動的にインストールされ、対話型のセットアップウィザードが起動します。

1.  Raspberry Pi でターミナルを開き、次のコマンドを直接実行します。このコマンドは、公式ウェブサイトからインストールスクリプトをダウンロードして実行します：

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash
   
    .. note:: 新しいバージョンは急速に更新されるため、インストール手順が少し異なっていても問題ありません。

2.  スクリプトは自動的に OpenClaw をダウンロードしてインストールします。

    .. image:: /pironman5/home_server/img/openclaw/install_open_claw.png


3.  次に、OpenClaw を信頼するかどうかを尋ねるセキュリティプロンプトが表示されます。安全で信頼できると確信したら、矢印キーを使用して "Yes" に移動し、Enter キーを押します。

    .. image:: /pironman5/home_server/img/openclaw/security_open_claw.png


4.  「Quick Start」を選択し、Enter キーを押します。

    .. image:: /pironman5/home_server/img/openclaw/quickstart_open_claw.png

5.  モデル (Model) を選択し、Enter キーを押します。ここでは例として OpenAI を使用します。

    .. image:: /pironman5/home_server/img/openclaw/model_provider_open_claw.png

6.  「OpenAI API Key」を選択します。

    .. image:: /pironman5/home_server/img/openclaw/api_key_open_claw.png

7.  ここで API キーを貼り付けます。

    .. image:: /pironman5/home_server/img/openclaw/paste_api_key_open_claw.png

8.|link_openai_platform| にアクセスしてログインします。**API keys** ページで、**Create new secret key** をクリックします。

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_create.png

9.  詳細（Owner、Name、Project、必要に応じて権限）を入力し、**Create secret key** をクリックします。

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_create_confirm.png

10. キーが作成されたら、すぐにコピーしてください。再度表示することはできません。紛失した場合は、新しいキーを生成する必要があります。

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_copy.png

11. キーを OpenClaw 設定に貼り付けます。

    .. image:: /pironman5/home_server/img/openclaw/paste_api_key_enter_open_claw.png

12. 使用するモデル (Model) を選択します。この例では、**Keep current** (現在の設定を保持) を使用します。

    .. image:: /pironman5/home_server/img/openclaw/model_config_open_claw.png

13. 次はチャンネル (Channel) の選択です。チャンネルとは、OpenClaw がサポートする通信サービス（Telegram、WhatsApp、Discord など）を指します。下矢印キーを使用して "Skip for now" (今はスキップ) オプションを選択し、Enter キーを押します。

    .. image:: /pironman5/home_server/img/openclaw/channel_open_claw.png

14. 次に、スキル (skills) を今すぐ設定するかどうかを尋ねられます。"Yes" を選択し、Enter キーを押します。

    .. image:: /pironman5/home_server/img/openclaw/config_skill_open_claw.png

15. 必要なスキルをインストールします。次の例では、"Skip for now" (今はスキップ) オプションを選択し（スペースバーを押して選択）、Enter キーを押します。

    .. image:: /pironman5/home_server/img/openclaw/install_skill_open_claw.png


16. 次はフック (Hooks) です。"command-logger" と "session-memory" をチェックします。

    .. image:: /pironman5/home_server/img/openclaw/hooks2_open_claw.png


17. インストールが完了しました。"Hatch in TUI" を選択して Enter キーを押すと、OpenClaw を起動できます。

   .. image:: /pironman5/home_server/img/openclaw/hatch_open_claw.png


.. note:: 
   
   以下のコマンドを入力して OpenClaw を起動することもできます：

    .. code-block:: bash

       openclaw tui

   TUI インターフェースを終了するには、Ctrl+c を2回押します。




-----------------------------------------------------

.. end_using_openclaw

OpenClaw に Pironman5 を操作させる
----------------------------------------------

OpenClaw に Pironman5 を操作させるには、Pironman5 スキルをインストールする必要があります。

1.  Pironman5 がすでにインストールされていることを確認してください。インストールされていない場合は、:ref:`install_pironman5_module_5` を参照してください。

2.  ターミナルで次のコマンドを実行します：

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-skill/ ~/.openclaw/skills/pironman5-skill/

3.  これで、 ``openclaw tui`` で Pironman5 を操作できるようになります。TUI でコマンドを送信してみてください。例えば、ケースの LED ライトをオンにしたり、色を変更したり、カメラで写真を撮らせたりしてみてください。GPIO17 に DHT11 モジュールが接続されていることを伝えて、温度を教えてもらうこともできます。

   .. note:: それでも OpenClaw がインポートしたスキルを認識できない場合は、rsync するように促してみてください。

---------------------------------------

.. start_using_openclaw_telegram

Telegram でシステムを操作する
---------------------------------------


**概要**

OpenClaw を通じて、一般的なメッセージングアプリを使用してシステムを操作できます（ここでは例として Telegram を使用します）。OpenClaw にこの設定を手伝ってもらうことさえできます。

``openclaw tui`` で次のように尋ねるだけです：*「あなたを Telegram に接続したいのですが、どうすればいいですか？」*

OpenClaw がステップバイステップでプロセスを案内してくれるので、その指示に従って設定を完了できます。


**前提条件**

始める前に、以下のものを用意してください：

- **Telegram アカウント**
- Telegram へのネットワークアクセス
- OpenClaw が正常に実行されていること (``openclaw status`` で確認)

**ステップ 1: Telegram ボットを作成する**

1. **Telegram で @BotFather を見つける** (公式ボット作成アカウント)
2. **新しいボットを作成する**: ``/newbot`` コマンドを送信する
3. **プロンプトに従う**:

   - ボットに名前を付けます (例： ``My OpenClaw Helper``)
   - ボットのユーザー名を設定します (``_bot`` で終わる必要があります。例： ``my_openclaw_bot``)

4. **成功すると、メッセージが届きます**。そこには **ボットトークン** が含まれており、次のようになります：

   .. code-block:: text

      1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

   .. warning:: このトークンはパスワードのように厳重に保管してください！

**ステップ 2: OpenClaw で Telegram を設定する**

``openclaw tui`` で、直接次のように伝えます：

> *「私の Telegram ボットを OpenClaw に接続したいです。これが私のボットトークンです：<あなたのトークン>。設定を完了するのを手伝ってください。」*

OpenClaw は自動的に以下の処理を行います：

- 必要な依存関係 (``node-telegram-bot-api`` など) をインストールする
- Telegram ゲートウェイ設定ファイルを作成する
- 接続が成功したかテストする


**ステップ 3: 接続をテストする**

1. Telegram で新しく作成したボットを見つける
2. ``/start`` コマンドを送信する
3. ボットがペアリングコードで応答するはずなので、このコードを OpenClaw TUI に送信します（例： ``Pairing code: ZAN4XI34``）
4. 正しく設定されるのを待つ
5. 「こんにちは」のような簡単なコマンドを送信してみる
6. すべてが正しく設定されていれば、ボットからの応答が表示されるはずです

**ステップ 4: 楽しみましょう！**

この設定が完了すると、以下のことができるようになります：

* いつでもどこでも Telegram を介して Raspberry Pi を制御できる
* コマンドをリモートで実行し、システムステータスを確認できる
* GPIO と連携して物理デバイスを制御できる (LED を点灯させるなど)
* AI アシスタントとのインテリジェントな対話体験を楽しめる


**セキュリティ設定 (非常に重要！)**

見知らぬ人があなたのシステムを制御できないようにするために、必ず以下のセキュリティ対策を実装してください：

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - セキュリティ対策
     - 設定方法
     - 説明
   * - ユーザー制限
     - 設定ファイルで ``allowedUsers`` を設定
     - 特定の Telegram ユーザーのみを許可する
   * - パスワード設定
     - 設定ファイルに ``"password": "あなたのパスワード"`` を追加
     - コマンド実行前にパスワード認証を要求する
   * - コマンド制限
     - コマンドのホワイトリストを作成
     - 特定の事前定義されたコマンドのみを許可する
   * - 監査ログ
     - ``command-logger`` フックを有効にする
     - Telegram 経由で実行されたすべてのコマンドを記録する


**忘れないでください：セキュリティが第一です！** 常にユーザーとコマンド範囲を適切に制限してください。設定中に特定の問題が発生した場合は、お気軽に助けを求めてください。

-------------------------------------

.. end_using_openclaw_telegram

.. start_using_openclaw_faq

OpenClaw トラブルシューティング
-------------------------------------

Q. インストール中に、 ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service`` というエラーが表示されます。どうすればよいですか？

   今のところは無視して構いませんが、次のステップで問題が発生する可能性があります。その際は、その都度一つずつ対処してください。


Q. ``openclaw tui`` を実行すると、 ``-bash: openclaw: command not found`` というエラーが表示されます。どうすればよいですか？

   次のコマンドを実行してください：

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   これで、 ``openclaw tui`` で TUI インターフェースを起動できるようになります。



Q. ``openclaw tui`` で、 ``not connected to gateway — message not sent`` または ``gateway disconnected: closed`` というメッセージが表示されます。

   これは、OpenClaw Gateway サービスが起動していないためです。別のターミナルを開き、次のコマンドを実行して OpenClaw Gateway を起動してください：

   .. code-block:: bash

      openclaw gateway

   その後、 ``openclaw tui`` を再起動すると、直接使用できるようになります。


Q. OpenClaw Gateway サービスをバックグラウンドで実行/起動時に自動開始するように設定したいのですが、どうすればよいですか？

   通常、OpenClaw Gateway サービスは起動時に自動的に開始されるはずです。そうでない場合は、以下のコマンドで手動で開始できます。

   1. ``~/.config/systemd/user`` ディレクトリを作成します：

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user


   2. ``openclaw-gateway.service`` ファイルを作成します：

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


   3. 次に、systemd 設定をリロードします：

   .. code-block:: bash

      systemctl --user daemon-reload

   4. サービスを開始します：

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   この時点で、 ``openclaw tui`` を再起動すると、直接使用できるようになります。

   5. 起動時に自動開始するように有効化します：

   .. code-block:: bash

      systemctl --user enable openclaw-gateway


Q. 私の OpenClaw がシステムを操作できません。どうすればよいですか？

   新しくインストールされた OpenClaw は、デフォルトでは Raspberry Pi システムを操作する権限がない場合があります。チャットのみ可能です。手動で権限を設定する必要があります。

   1.  OpenClaw 設定ファイルを開きます：

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  ``tools`` オプションを見つけ、 ``tools`` に変更します。

      .. code-block:: json

        "tools": {
            "profile": "coding",
            "exec": {
               "secrity": "full"
            }
        },

   3.  保存して終了します。

   4.  ターミナルで次のコマンドを入力して、OpenClaw Gateway を再起動します：

      .. code-block:: bash

         openclaw gateway restart

   これで、OpenClaw に読み取りおよび書き込み権限が付与され、Raspberry Pi システムを操作できるようになります。

.. end_using_openclaw_faq