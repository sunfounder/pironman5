.. note:: 

    こんにちは！SunFounder の Facebook コミュニティ「Raspberry Pi & Arduino & ESP32 愛好者グループ」へようこそ！Raspberry Pi、Arduino、ESP32 に情熱を持つ仲間たちと共に、より深く学び、つながりましょう。

    **参加するメリット**

    - **専門的なサポート**：購入後の問題や技術的な課題を、コミュニティと当社サポートチームが協力して解決します。
    - **学びと共有**：チュートリアルやノウハウを交換し、スキルを高めましょう。
    - **先行プレビュー**：新製品の発表や内部情報をいち早くチェックできます。
    - **特別割引**：最新製品を対象にしたメンバー限定の割引を提供。
    - **季節限定キャンペーン＆プレゼント企画**：楽しいイベントやプレゼントにご参加いただけます。

    👉 一緒に創造と発見の旅を始めましょう！[|link_sf_facebook|] をクリックして、今すぐ参加！

Mac OS X ユーザー向け
==========================

Mac OS X をお使いの方には、SSH（Secure Shell）によるリモートアクセスが便利で安全な方法として推奨されます。Raspberry Pi をモニターなしで操作する場合や、離れた場所から作業する際に特に有効です。Mac のターミナルアプリを使えば、Pi のユーザー名とホスト名を用いて簡単に接続が行えます。初回接続時には、セキュリティ確認のメッセージが表示されます。

#. Raspberry Pi に接続するには、以下の SSH コマンドを入力します：

    .. code-block::

        ssh pi@raspberrypi.local

   .. image:: img/mac_vnc14.png

#. 初回ログイン時にセキュリティメッセージが表示されます。 **yes** と入力して続行してください。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Raspberry Pi のパスワードを入力します。入力中は画面に表示されませんが、これは通常のセキュリティ仕様です。

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

