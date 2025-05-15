.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Facebookで、他のエンスージアストたちと一緒にRaspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームのサポートで、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表や先行情報に早期アクセスが可能です。
    - **特別割引**: 最新製品を特別割引で購入できます。
    - **フェスティブプロモーションとプレゼント**: プレゼント企画やホリデープロモーションに参加できます。

    👉 私たちと一緒に発見と創造を始めましょう！ [|link_sf_facebook|] をクリックして、今すぐ参加してください！

Mac OS Xユーザー向け
==========================

Mac OS Xユーザーにとって、SSH（Secure Shell）はRaspberry Piにリモートアクセスし、操作するための安全で便利な方法です。これは特に、Raspberry Piがモニターに接続されていない場合やリモートで作業する場合に便利です。Macのターミナルアプリケーションを使用して、この安全な接続を確立できます。このプロセスでは、Raspberry Piのユーザー名とホスト名を含むSSHコマンドを使用します。最初の接続時には、Raspberry Piの認証確認を求められます。

#. Raspberry Piに接続するには、次のSSHコマンドを入力してください:

    .. code-block::

        ssh pi@raspberrypi.local

   .. image:: img/mac_vnc14.png

#. 初回ログイン時にセキュリティメッセージが表示されます。 **yes**  と入力して続行してください。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Raspberry Piのパスワードを入力します。セキュリティ上の理由から、入力中にパスワードは画面に表示されませんのでご注意ください。

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

