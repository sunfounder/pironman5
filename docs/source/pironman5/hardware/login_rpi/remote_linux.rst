.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Facebookで、他のエンスージアストたちと一緒にRaspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームのサポートで、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表や先行情報に早期アクセスが可能です。
    - **特別割引**: 最新製品を特別割引で購入できます。
    - **フェスティブプロモーションとプレゼント**: プレゼント企画やホリデープロモーションに参加できます。

    👉 私たちと一緒に発見と創造を始めましょう！ [|link_sf_facebook|] をクリックして、今すぐ参加してください！

Linux/Unixユーザー向け
==========================

#. Linux/Unixシステムで **Terminal** を開きます。

#. Raspberry Piが同じネットワークに接続されていることを確認します。以下のコマンドを入力して確認してください: `ping <hostname>.local` 例えば:

    .. code-block::

        ping raspberrypi.local

    Raspberry Piがネットワークに接続されている場合、そのIPアドレスが表示されます。

    * ターミナルに ``Ping request could not find host pi.local. Please check the name and try again.`` のようなメッセージが表示された場合、入力したホスト名を再確認してください。
    * IPアドレスを取得できない場合は、Raspberry PiのネットワークやWiFi設定を確認してください。

#. SSH接続を開始するには、 ``ssh <username>@<hostname>.local`` または ``ssh <username>@<IP address>`` を入力します。例として:

    .. code-block::

        ssh pi@raspberrypi.local

#. 初回ログイン時にはセキュリティメッセージが表示されます。 ``yes`` と入力して進めてください。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 以前に設定したパスワードを入力します。セキュリティのため、入力中にパスワードは表示されません。

    .. note::
        ターミナルにパスワードが表示されないのは通常のことです。正しいパスワードを入力してください。

#. ログインに成功すると、Raspberry Piに接続され、次のステップに進む準備が整います。

