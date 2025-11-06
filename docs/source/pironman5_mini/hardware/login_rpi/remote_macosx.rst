.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！  同じ情熱を持つ仲間たちと一緒に、Raspberry Pi・Arduino・ESP32の世界をさらに深く探求しましょう。

    **なぜ参加するのか？**

    - **エキスパートサポート**：購入後の問題や技術的な課題について、コミュニティおよび専門チームがサポートします。
    - **学びと共有**：チュートリアルやヒントを共有し、スキルの向上を目指しましょう。
    - **新製品の先行公開**：新製品の先行情報や発表をいち早く入手できます。
    - **Special Discounts**：最新製品に対する限定割引をご利用いただけます。
    - **Festive Promotions and Giveaways**：プレゼント企画や季節限定キャンペーンに参加可能です。

    👉 私たちと一緒に創造と発見の旅を始めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

Mac OS X ユーザー向け
==========================

Mac OS X を使用している場合、SSH（セキュアシェル）を利用することで、Raspberry Pi への安全かつ便利なリモートアクセスが可能です。これは、Raspberry Pi をモニターに接続せずに操作する際に特に便利です。  
Mac の「ターミナル」アプリケーションを使用して、安全な接続を確立します。  
SSHコマンドには、Raspberry Pi のユーザー名とホスト名を含めます。初回接続時には、Piの正当性を確認するセキュリティプロンプトが表示されます。

#. 以下のSSHコマンドを入力して、Raspberry Pi に接続します：

    .. code-block::

        ssh pi@raspberrypi.local

   .. image:: img/mac_vnc14.png

#. 初回ログイン時にセキュリティメッセージが表示されます。 **yes** と入力して接続を続行してください。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Raspberry Pi のパスワードを入力します。入力中は画面に何も表示されませんが、これはセキュリティ上正常な動作です。

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

