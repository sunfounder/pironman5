.. note:: 

    こんにちは！SunFounder の Facebook コミュニティ「Raspberry Pi & Arduino & ESP32 愛好者グループ」へようこそ！同じ興味を持つ仲間たちと一緒に、Raspberry Pi、Arduino、ESP32 の世界をさらに深く掘り下げましょう。

    **参加する理由**

    - **専門的なサポート**：購入後の問題や技術的課題に、コミュニティやサポートチームが対応します。
    - **学びと共有**：役立つヒントやチュートリアルを共有してスキルを向上させましょう。
    - **先行情報の入手**：新製品の発表やプレビューをいち早くチェックできます。
    - **特別割引**：最新製品に対する限定割引をご利用いただけます。
    - **季節限定プロモーションとプレゼント企画**：各種キャンペーンや抽選プレゼントに参加できます。

    👉 私たちと一緒に、ものづくりの冒険を始めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

Linux/Unix ユーザー向け
==========================

#. お使いの Linux/Unix システムで **ターミナル** を開きます。

#. Raspberry Pi が同じネットワークに接続されていることを確認します。以下のように入力して確認します： `ping <hostname>.local`。例：

    .. code-block::

        ping raspberrypi.local

    ネットワークに接続されていれば、Raspberry Pi の IP アドレスが表示されます。

    * ``Ping request could not find host pi.local. Please check the name and try again.`` のようなエラーメッセージが表示された場合は、ホスト名が正しく入力されているかを確認してください。
    * IP アドレスが取得できない場合は、Raspberry Pi 側のネットワークや Wi-Fi 設定を確認してください。

#. 以下のように入力して SSH 接続を開始します： ``ssh <username>@<hostname>.local`` または ``ssh <username>@<IP address>``。例えば：

    .. code-block::

        ssh pi@raspberrypi.local

#. 初回ログイン時にはセキュリティに関するメッセージが表示されます。 ``yes`` と入力して接続を進めます。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 事前に設定したパスワードを入力します。セキュリティの都合上、入力中の文字は表示されません。

    .. note::
        ターミナルにパスワードが表示されないのは正常です。正しく入力されていれば問題ありません。

#. ログインが成功すれば、Raspberry Pi に接続完了です。次のステップに進みましょう。
