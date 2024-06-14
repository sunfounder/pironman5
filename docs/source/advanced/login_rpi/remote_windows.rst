.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

Windowsユーザー向け
=======================

Windows 10以降のユーザーがRaspberry Piにリモートログインするには、以下の手順に従ってください：

#. Windowsの検索ボックスに ``powershell`` を入力します。 ``Windows PowerShell`` を右クリックし、 ``管理者として実行`` を選択します。

    .. image:: img/powershell_ssh.png
        :align: center

#. PowerShellで ``ping -4 <hostname>.local`` と入力して、Raspberry PiのIPアドレスを確認します。

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    Raspberry Piがネットワークに接続されている場合、そのIPアドレスが表示されます。

    * ターミナルに ``Ping request could not find host pi.local. Please check the name and try again.`` と表示された場合、入力したホスト名が正しいか確認してください。
    * IPアドレスが取得できない場合、Raspberry PiのネットワークまたはWiFi設定を確認してください。

#. IPアドレスが確認できたら、 ``ssh <username>@<hostname>.local`` または ``ssh <username>@<IP address>`` を使用してRaspberry Piにログインします。

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        ``The term 'ssh' is not recognized as the name of a cmdlet...`` というエラーが表示された場合、システムにSSHツールがプリインストールされていない可能性があります。その場合は、手動でOpenSSHをインストールするか、 |link_putty| のようなサードパーティツールを使用してください。

#. 初回ログイン時にセキュリティメッセージが表示されます。続行するには ``yes`` と入力します。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 以前に設定したパスワードを入力します。入力中にパスワードが画面に表示されないことに注意してください。これは標準的なセキュリティ機能です。

    .. note::
        パスワードを入力しても文字が表示されないのは正常です。正しいパスワードを入力してください。

#. 接続が確立されると、Raspberry Piがリモート操作の準備が整います。

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center

