.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Facebookで、他のエンスージアストたちと一緒にRaspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームのサポートで、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表や先行情報に早期アクセスが可能です。
    - **特別割引**: 最新製品を特別割引で購入できます。
    - **フェスティブプロモーションとプレゼント**: プレゼント企画やホリデープロモーションに参加できます。

    👉 私たちと一緒に発見と創造を始めましょう！ [|link_sf_facebook|] をクリックして、今すぐ参加してください！

Windowsユーザー向け
=======================

Windows 10以降のユーザーがRaspberry Piにリモートログインするための手順は以下の通りです。

#. Windowsの検索ボックスに ``powershell`` と入力します。 ``Windows PowerShell`` を右クリックし、 ``Run as administrator`` を選択します。

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. PowerShellで ``ping -4 <hostname>.local`` を入力して、Raspberry PiのIPアドレスを確認します。

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%
      

   Raspberry Piがネットワークに接続されると、そのIPアドレスが表示されます。

   * ターミナルに ``Ping request could not find host pi.local. Please check the name and try again.`` と表示された場合は、入力したホスト名が正しいか確認してください。
   * IPアドレスが取得できない場合は、Raspberry Piのネットワーク設定またはWiFi設定を確認してください。

#. IPアドレスが確認できたら、 ``ssh <username>@<hostname>.local`` または ``ssh <username>@<IP address>`` を使用してRaspberry Piにログインします。

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        ``The term 'ssh' is not recognized as the name of a cmdlet...`` というエラーメッセージが表示された場合は、システムにSSHツールがインストールされていない可能性があります。その場合は、:ref:`openssh_powershell` に従ってOpenSSHを手動でインストールするか、|link_putty| などのサードパーティツールを使用してください。

#. 初回ログイン時にセキュリティメッセージが表示されます。 ``yes`` と入力して続行します。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 以前に設定したパスワードを入力します。セキュリティ上の理由から、入力した文字は表示されません。

    .. note::
        パスワード入力時に文字が表示されないのは正常です。正しいパスワードを入力してください。

#. 接続が成功すると、Raspberry Piはリモート操作の準備が整います。

   .. image:: img/sp221221_140628.png
      :width: 90%
      
