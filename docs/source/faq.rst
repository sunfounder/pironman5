.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Raspberry Pi、Arduino、ESP32に情熱を注ぐ仲間たちと一緒に、これらの技術をさらに深く探求してみましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームのサポートを活用し、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューにいち早くアクセス可能です。
    - **特別割引**: 最新製品に対する特別な割引を楽しめます。
    - **フェスティブプロモーションとプレゼント**: プレゼント企画やプロモーションに参加してみましょう。

    👉 一緒に探求し、創造を楽しみましょう！今すぐ [|link_sf_facebook|] をクリックして参加してください！

FAQ
============

ウェブダッシュボードを無効にする方法
------------------------------------------------------------

``pironman5`` モジュールのインストールが完了すると、 :ref:`view_control_dashboard` にアクセスできるようになります。
      
この機能が不要で、CPUやRAMの使用量を減らしたい場合は、インストール時に ``--disable-dashboard`` フラグを追加して、 ``pironman5`` のダッシュボードを無効にすることができます。
      
.. code-block:: shell

  sudo python3 install.py --disable-dashboard

すでに ``pironman 5`` をインストールしている場合は、 ``dashboard`` モジュールと ``influxdb`` を削除し、pironman5を再起動して変更を適用することができます：

.. code-block:: shell

  /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
  sudo apt purge influxdb
  sudo systemctl restart pironman5





Pironman 5はレトロゲームシステムをサポートしていますか？
------------------------------------------------------------
はい、対応しています。しかし、多くのレトロゲームシステムはシンプルなバージョンであり、追加のソフトウェアをインストールして実行することができません。この制限により、Pironman 5のOLEDディスプレイ、2つのRGBファン、4つのRGB LEDなどのコンポーネントが正しく動作しない可能性があります。これらのコンポーネントにはPironman 5のソフトウェアパッケージのインストールが必要です。

.. note::

    現在、Batocera.linuxシステムはPironman 5と完全に互換性があります。Batocera.linuxは、オープンソースで完全に無料のレトロゲーム向けディストリビューションです。

    * :ref:`install_batocera`
    * :ref:`set_up_batocera`

``pironman5`` コマンドを使ってコンポーネントを制御する方法
----------------------------------------------------------------------
Pironman 5のコンポーネントを ``pironman5`` コマンドで制御する方法については、次のチュートリアルを参照してください。

* :ref:`view_control_commands`

Raspberry Piのブート順序をコマンドで変更する方法
-------------------------------------------------------------

すでにRaspberry Piにログインしている場合は、コマンドを使用してブート順序を変更できます。詳細な手順は以下のとおりです。

* :ref:`configure_boot_ssd`

Raspberry Pi Imagerでブート順序を変更する方法
---------------------------------------------------------------

EEPROM設定で ``BOOT_ORDER`` を変更することに加えて、 **Raspberry Pi Imager** を使用してRaspberry Piのブート順序を変更することもできます。

このステップでは、予備のカードを使用することをお勧めします。

* :ref:`update_bootloader`

SDカードからNVMe SSDにシステムをコピーする方法
-------------------------------------------------------------

NVMe SSDを持っているが、NVMeをコンピュータに接続するためのアダプターがない場合は、まずMicro SDカードにシステムをインストールします。Pironman 5が正常に起動したら、Micro SDカードからNVMe SSDにシステムをコピーできます。詳細な手順は以下のとおりです。

* :ref:`copy_sd_to_nvme_rpi`


OLEDスクリーンが動作しない場合
-------------------------------------

OLEDスクリーンが表示されない、または表示が不正確な場合は、次の手順に従って問題をトラブルシューティングしてください。

1. OLEDスクリーンのFPCケーブルが正しく接続されているか確認してください。

#. プログラムの実行ログを表示し、エラーメッセージがないか確認します。

   .. code-block:: shell

      cat /opt/pironman5/log

#. または、OLEDのi2cアドレス0x3Cが認識されているかを確認するために、次のコマンドを使用します。

   .. code-block:: shell

      sudo i2cdetect -y 1

#. 最初の2つの手順で問題が見つからない場合は、pironman5サービスを再起動して問題が解決するかどうかを確認してください。

   .. code-block:: shell

      sudo systemctl restart pironman5.service

.. _openssh_powershell:

Powershell経由でOpenSSHをインストールする方法
---------------------------------------------

``ssh <username>@<hostname>.local``（または ``ssh <username>@<IP address>`` ）を使用してRaspberry Piに接続しようとすると、次のエラーメッセージが表示されることがあります。

   .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


これは、コンピュータのシステムが古く、 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_  が事前にインストールされていないことを意味します。そのため、以下のチュートリアルに従って手動でインストールする必要があります。

#. Windowsのデスクトップの検索ボックスに ``powershell`` と入力し、 ``Windows PowerShell`` を右クリックして、表示されるメニューから ``管理者として実行`` を選択します。

   .. image:: img/powershell_ssh.png
      :width: 90%

#. 以下のコマンドを使用して ``OpenSSH.Client`` をインストールします。

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. インストールが完了すると、次の出力が返されます。

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 次のコマンドを使用してインストールを確認します。

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. ``OpenSSH.Client`` が正常にインストールされたことが表示されます。

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        上記のプロンプトが表示されない場合は、Windowsシステムがまだ古すぎるため、|link_putty| のようなサードパーティのSSHツールをインストールすることをお勧めします。

#. PowerShellを再起動し、再度管理者として実行してください。これで``ssh``コマンドを使用してRaspberry Piにログインできるようになります。ログイン時には、以前に設定したパスワードの入力が求められます。

   .. image:: img/powershell_login.png
