.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

Mac OS Xユーザー向け
==========================

Mac OS Xユーザーにとって、SSH（Secure Shell）はRaspberry Piにリモートアクセスして制御するための安全で便利な方法です。これは、Raspberry Piをリモートで操作する場合や、モニターに接続されていない場合に特に便利です。Macのターミナルアプリケーションを使用して、この安全な接続を確立できます。このプロセスでは、Raspberry Piのユーザー名とホスト名を含むSSHコマンドを使用します。初回接続時には、Raspberry Piの認証を確認するセキュリティプロンプトが表示されます。

#. Raspberry Piに接続するには、以下のSSHコマンドを入力します：

    .. code-block::

        ssh pi@raspberrypi.local

    .. image:: img/mac_vnc14.png

#. 初回ログイン時にセキュリティメッセージが表示されます。続行するには **yes** と回答します。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Raspberry Piのパスワードを入力します。入力中にパスワードが画面に表示されないことに注意してください。これは標準的なセキュリティ機能です。

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 
