.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！  
    同じ興味を持つ仲間たちと一緒に、Raspberry Pi・Arduino・ESP32の世界をさらに深く探求しましょう。

    **なぜ参加するのか？**

    - **エキスパートサポート**：購入後の問題や技術的な課題を、コミュニティと当社チームがサポートします。
    - **学びと共有**：チュートリアルやヒントを共有してスキルアップに役立てましょう。
    - **新製品の先行公開**：新製品の発表やプレビューをいち早くチェック。
    - **特別割引**：最新製品に適用される特別割引を受けられます。
    - **季節イベントとプレゼント企画**：プレゼント企画や季節イベントに参加可能です。

    👉 私たちと一緒に創造と冒険を始めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

Linux/Unix ユーザー向け
==========================

#. Linux/Unixシステムで **ターミナル** を開きます。

#. Raspberry Pi が同じネットワークに接続されていることを確認します。以下のように入力して接続を確認します：

    .. code-block::

        ping raspberrypi.local

    Raspberry Pi がネットワークに接続されていれば、IPアドレスが表示されます。

    * もし ``Ping request could not find host pi.local. Please check the name and try again.`` のようなメッセージが表示された場合は、ホスト名に誤りがないか再確認してください。
    * IPアドレスが取得できない場合は、Raspberry Pi 側のネットワークまたはWi-Fi設定を確認してください。

#. 次に、以下のようにSSH接続を開始します： ``ssh <username>@<hostname>.local`` または ``ssh <username>@<IP address>``  
   例：

    .. code-block::

        ssh pi@raspberrypi.local

#. 初回接続時にはセキュリティ警告が表示されます。 ``yes`` と入力して接続を続行してください。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. あらかじめ設定しておいたパスワードを入力します。セキュリティ上の理由から、入力中にパスワードは表示されません。

    .. note::
        パスワード入力時に文字が表示されないのは正常です。正しいパスワードを入力してください。

#. ログインが成功すると、Raspberry Pi への接続が完了し、次のステップに進む準備が整います。
