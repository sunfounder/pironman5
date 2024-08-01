.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

FAQ
============

Pironman 5はレトロゲームシステムをサポートしていますか？
----------------------------------------------------------

はい、互換性があります。ただし、ほとんどのレトロゲームシステムは、追加のソフトウェアをインストールして実行することができない簡素化されたバージョンです。この制限により、Pironman 5の一部のコンポーネント（OLEDディスプレイ、2つのRGBファン、タワークーラー上のCPUファンなど）が正常に動作しない場合があります。これらのコンポーネントは、Pironman 5のソフトウェアパッケージのインストールを必要とするためです。

``pironman5`` コマンドを使用してコンポーネントを制御する方法
----------------------------------------------------------------------
``pironman5`` コマンドを使用して Pironman 5 のコンポーネントを制御するには、以下のチュートリアルを参照してください。

* :ref:`view_control_commands`

コマンドを使用して Raspberry Pi の起動順序を変更する方法
-------------------------------------------------------------

Raspberry Pi にすでにログインしている場合、コマンドを使用して起動順序を変更できます。詳細な手順は以下の通りです：

* :ref:`configure_boot_ssd`

Raspberry Pi Imager で起動順序を変更する方法
---------------------------------------------------------------

EEPROM 設定で ``BOOT_ORDER`` を変更することに加えて、 **Raspberry Pi Imager** を使用して Raspberry Pi の起動順序を変更することもできます。

この手順には、予備のカードを使用することをお勧めします。

* :ref:`update_bootloader`

SD カードから NVMe SSD にシステムをコピーする方法
-------------------------------------------------------------

NVMe SSD を持っているが、NVMe をコンピュータに接続するためのアダプターがない場合は、最初に Micro SD カードにシステムをインストールできます。Pironman 5 が正常に起動したら、Micro SD カードから NVMe SSD にシステムをコピーできます。詳細な手順は以下の通りです：

* :ref:`boot_from_ssd`


OLED画面が表示されない？
--------------------------

OLED画面が表示されない、または正しく表示されない場合、以下の手順に従って問題をトラブルシューティングしてください。

OLED画面のFPCケーブルが正しく接続されているか確認してください。

#. 次のコマンドを使用してプログラムの実行ログを表示し、エラーメッセージがないか確認します。

    .. code-block:: shell

        cat /opt/pironman5/log

#. または、次のコマンドを使用してOLEDのi2cアドレス0x3Cが認識されているか確認します：
    
    .. code-block:: shell
        
        sudo i2cdetect -y 1

#. 最初の2つの手順で問題が見つからない場合は、pironman5サービスを再起動して問題が解決するか確認します。

    .. code-block:: shell

        sudo systemctl restart pironman5.service

.. _openssh_powershell:

Powershellを使ってOpenSSHをインストールする
----------------------------------------------------

``ssh <username>@<hostname>.local`` （または ``ssh <username>@<IP address>`` ）を使用してRaspberry Piに接続しようとしたとき、次のエラーメッセージが表示される場合があります。

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

これは、コンピューターのシステムが古く、 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ が事前にインストールされていないことを意味します。以下の手順に従って手動でインストールしてください。

#. Windowsデスクトップの検索ボックスに ``powershell`` と入力し、 ``Windows PowerShell`` を右クリックして、表示されるメニューから ``管理者として実行`` を選択します。

    .. image:: img/powershell_ssh.png
        :align: center

#. 次のコマンドを使用して ``OpenSSH.Client`` をインストールします。

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. インストール後、次の出力が返されます。

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 次のコマンドを使用してインストールを確認します。

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. これで ``OpenSSH.Client`` が正常にインストールされたことがわかります。

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        上記のプロンプトが表示されない場合、Windowsシステムがまだ古すぎることを意味します。 |link_putty| のようなサードパーティのSSHツールをインストールすることをお勧めします。

#. PowerShellを再起動し、再度管理者として実行します。この時点で ``ssh`` コマンドを使用してRaspberry Piにログインできるようになり、先に設定したパスワードの入力を求められます。

    .. image:: img/powershell_login.png

