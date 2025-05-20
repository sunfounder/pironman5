.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！ 同じ情熱を持つ仲間たちとともに、Raspberry Pi、Arduino、ESP32の世界をさらに深く楽しみましょう。

    **Why Join?**

    - **Expert Support**：購入後のトラブルや技術的課題を、コミュニティと当社サポートチームが解決します。
    - **Learn & Share**：チュートリアルやヒントを共有してスキルアップ。
    - **Exclusive Previews**：新製品の先行情報をいち早く入手。
    - **Special Discounts**：最新製品に対する会員限定の割引を提供。
    - **Festive Promotions and Giveaways**：プレゼント企画や季節限定プロモーションに参加可能。

    👉 私たちと一緒に創造と発見を楽しみましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

Windowsユーザー向け
=======================

Windows 10 以降のユーザーは、以下の手順でRaspberry Piへのリモートログインが可能です：

#. Windowsの検索ボックスに ``powershell`` と入力し、 ``Windows PowerShell`` を右クリックして「管理者として実行」を選択します。

   .. image:: img/powershell_ssh.png
      :width: 90%


#. PowerShellで ``ping -4 <hostname>.local`` と入力して、Raspberry PiのIPアドレスを確認します。

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%


   Raspberry Pi がネットワークに接続されていれば、IPアドレスが表示されます。

   * ``Ping request could not find host pi.local. Please check the name and try again.`` と表示された場合は、ホスト名が正しいか確認してください。
   * IPアドレスが取得できない場合は、Raspberry Pi 側のネットワークやWi-Fiの設定を確認してください。

#. IPアドレスが確認できたら、以下のコマンドでログインします： ``ssh <username>@<hostname>.local`` または ``ssh <username>@<IP address>``

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        ``The term 'ssh' is not recognized as the name of a cmdlet...`` というエラーが表示された場合は、SSHツールがインストールされていない可能性があります。 その場合は、:ref:`openssh_powershell_mini` に従って OpenSSH を手動でインストールするか、|link_putty| のような外部ツールをご利用ください。

#. 初回ログイン時にはセキュリティメッセージが表示されます。 ``yes`` と入力して接続を進めてください。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 設定済みのパスワードを入力します。入力中、パスワードは画面に表示されませんが、これは正常な動作です。

    .. note::
        パスワード入力時に文字が表示されないのはセキュリティの仕様です。正しいパスワードを入力してください。

#. 接続が完了すると、Raspberry Pi がリモート操作可能になります。

   .. image:: img/sp221221_140628.png
      :width: 90%

