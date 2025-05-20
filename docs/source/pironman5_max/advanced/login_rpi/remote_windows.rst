.. note:: 

    こんにちは！SunFounder の Facebook コミュニティ「Raspberry Pi & Arduino & ESP32 愛好者グループ」へようこそ！Raspberry Pi、Arduino、ESP32 の世界を、熱意ある仲間たちと一緒にさらに深く探求しましょう。

    **参加するメリット**

    - **専門サポート**：購入後の問題や技術的な課題を、コミュニティと弊社サポートチームが一緒に解決します。
    - **学びと共有**：ヒントやチュートリアルを交換し、スキルを向上させましょう。
    - **先行プレビュー**：新製品の発表や試作品の情報をいち早く入手できます。
    - **限定割引**：最新製品を対象にしたメンバー限定の特別割引をご利用いただけます。
    - **キャンペーン & プレゼント企画**：イベントやプレゼントに参加してお得な体験を！

    👉 一緒に創造と冒険を始めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

Windows ユーザー向け
=======================

Windows 10 以降をご利用の方は、以下の手順で Raspberry Pi にリモートログインできます：

#. Windows の検索ボックスで ``powershell`` と入力し、 ``Windows PowerShell`` を右クリックして「管理者として実行」を選択します。

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. PowerShell にて ``ping -4 <hostname>.local`` と入力し、Raspberry Pi の IP アドレスを確認します。

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%
      

   Raspberry Pi がネットワークに接続されていれば、IP アドレスが表示されます。

   * ``Ping request could not find host pi.local. Please check the name and try again.`` と表示された場合は、ホスト名が正しく入力されているかを確認してください。
   * IP アドレスが取得できない場合は、Raspberry Pi 側のネットワークや Wi-Fi 設定を見直してください。

#. IPアドレスを確認したら、 ``ssh <username>@<hostname>.local`` または ``ssh <username>@<IP address>`` を使用してRaspberry Piにログインします。

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        ``The term 'ssh' is not recognized as the name of a cmdlet...`` というエラーが出た場合、SSH ツールがシステムにインストールされていない可能性があります。その場合は :ref:`max_openssh_powershell` に従って OpenSSH を手動でインストールするか、 |link_putty| のようなサードパーティツールをご利用ください。

#. 初回ログイン時にはセキュリティ確認のメッセージが表示されます。 ``yes`` と入力して接続を続行します。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 設定済みのパスワードを入力します。入力中に画面に文字が表示されないのは正常な動作です。

    .. note::
        パスワード入力時に文字が表示されないのはセキュリティ上の仕様です。正確に入力してください。

#. 接続が完了すれば、Raspberry Pi をリモート操作する準備が整いました。

   .. image:: img/sp221221_140628.png
      :width: 90%

