.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！同じ情熱を持つ仲間たちと一緒に、Raspberry Pi・Arduino・ESP32の世界をさらに深く探求しましょう。

    **Why Join?**

    - **Expert Support**：購入後のサポートや技術的課題を、コミュニティやサポートチームがサポートします。
    - **Learn & Share**：チュートリアルやヒントを共有し、スキルアップにつなげましょう。
    - **Exclusive Previews**：新製品の情報や先行公開をいち早く入手できます。
    - **Special Discounts**：最新製品を対象とした限定割引をお楽しみください。
    - **Festive Promotions and Giveaways**：プレゼント企画や季節限定キャンペーンにも参加可能です。

    👉 一緒に探求と創造を楽しみましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

FAQ（よくある質問）
======================

Webダッシュボードを無効にする方法は？
------------------------------------------------------

``pironman5`` モジュールのインストールが完了すると、:ref:`max_view_control_dashboard` にアクセスできるようになります。

この機能が不要で、CPUやメモリの使用量を抑えたい場合は、インストール時に ``--disable-dashboard`` オプションを付けてダッシュボードを無効化できます。

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

すでに ``pironman 5`` をインストール済みの場合は、以下のコマンドで ``dashboard`` モジュールと ``influxdb`` を削除し、pironman5 を再起動してください。

.. code-block:: shell

   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

Pironman 5 MAXはレトロゲームシステムに対応していますか？
------------------------------------------------------
はい、対応しています。ただし、多くのレトロゲームシステムは軽量化されたシステムであり、追加のソフトウェアをインストールできないことがあります。そのため、OLEDディスプレイ、RGBファン、4つのRGB LEDなど、一部のPironman 5機能が動作しない可能性があります。


.. note::

    Batocera.linux は現在、Pironman 5 と完全に互換性があります。Batocera.linux はオープンソースかつ完全無料のレトロゲーム向けOSです。

    * :ref:`max_install_batocera`
    * :ref:`max_set_up_batocera`

``pironman5`` コマンドで各種コンポーネントを制御する方法
----------------------------------------------------------------------
``pironman5`` コマンドを使って各種コンポーネントを制御する方法については、以下のチュートリアルを参照してください。

* :ref:`max_view_control_commands`

コマンドでRaspberry Piの起動順を変更するには？
-------------------------------------------------------------

すでにRaspberry Piにログインしている場合、以下の手順に従って起動順をコマンドで変更できます。

* :ref:`max_configure_boot_ssd`


Raspberry Pi Imagerで起動順を変更するには？
---------------------------------------------------------------

``EEPROM`` の ``BOOT_ORDER`` を変更する方法に加えて、 **Raspberry Pi Imager** を使ってブート順を変更することもできます。

この操作は、予備のSDカードを使用することを推奨します。

* :ref:`max_update_bootloader`

SDカードからNVMe SSDにシステムをコピーする方法は？
-------------------------------------------------------------

NVMe SSDを持っているが、PCに接続するためのアダプターがない場合、まずMicro SDカードにシステムをインストールしてください。Pironman 5 MAXが正常に起動した後、SDカードからNVMe SSDへシステムをコピーできます。詳細手順は以下をご覧ください：


* :ref:`max_copy_sd_to_nvme_rpi`


NVMe PIP モジュールが動作しない場合
---------------------------------------

1. NVMe PIP モジュールとらずべりーぱい5を接続するFPCけーぶるが、しっかりと差し込まれていることを確認してください。

2. SSDがNVMe PIP モジュールに正しく固定されていることを確認してください。

3. NVMe PIP モジュールの発光表示（LED）の状態を確認してください：

   すべての接続を確認した後、「Pironman 5 MAX」の電源を入れ、NVMe PIP モジュール上のふたつの表示灯を観察してください：

   * **電源表示（PWR LED）**：点灯している必要があります。  
   * **状態表示（STA LED）**：点滅していれば正常に動作しています。

   .. image:: img/dual_nvme_pip_leds.png  

   * **PWR LED**が点灯していて、**STA LED**が点滅していない場合、NVMe SSDがらずべりーぱいに認識されていないことを示しています。  
   * **PWR LED**が消灯している場合、モジュール上の「強制有効（Force Enable）」端子を短絡してください。**PWR LED**が点灯すれば、FPCけーぶるの接触不良、またはNVMeに対応していない環境の可能性があります。

   .. image:: img/dual_nvme_pip_j4.png  

4. NVMe SSDに正しく作動するおぺれーてぃんぐしすてむが書き込まれていることを確認してください。以下を参照：:ref:`max_install_the_os`

5. 配線とおぺれーてぃんぐしすてむに問題がない場合でもNVMe SSDから起動できないときは、まずMicro SD から起動して他の部品が正常に動作しているか確認してください。その後、以下を参照して起動設定を行ってください：:ref:`max_configure_boot_ssd`

上記をお試しいただいても解決しない場合は、お手数ですが service@sunfounder.com までご連絡ください。できるだけ早く対応いたします。


OLED 画面が表示されない場合
--------------------------

.. note:: OLED 画面は一定時間操作がない場合、電力節約のため自動的に消灯することがあります。かるく筐体をたたくと振動感知により再表示されます。

OLED 画面が表示されない、または正しく表示されない場合は、以下の手順にしたがって確認してください：

1. **画面けーぶるの接続を確認する**

   OLED 画面のFPCけーぶるが正しく接続されているか確認してください。

2. **おぺれーてぃんぐしすてむの対応状況を確認する**

   らずべりーぱい上で、対応するおぺれーてぃんぐしすてむが動作していることを確認してください。

3. **I2C 接続を確認する**

   以下のこまんどで、OLEDの I2C あどれす（0x3C）が認識されているか確認します：

   .. code-block:: shell

      sudo i2cdetect -y 1

   あどれすが表示されない場合は、以下のこまんどで I2C を有効にしてください：

   .. code-block:: shell

      sudo raspi-config

4. **pironman5 さーびすを再起動する**

   ``pironman5`` さーびすを再起動し、問題が解消するか確認します：

   .. code-block:: shell

      sudo systemctl restart pironman5.service

5. **記録ろぐを確認する**

   それでも解決しない場合は、以下のこまんどでろぐふぁいるの内容を確認し、内容をサポートにお知らせください：

   .. code-block:: shell

      cat /var/log/pironman5/pm_auto.oled.log





.. _max_openssh_powershell:

PowerShellを使ってOpenSSHをインストールする方法
---------------------------------------------------

``ssh <username>@<hostname>.local`` または ``ssh <username>@<IP address>`` でRaspberry Piに接続しようとした際に、以下のエラーメッセージが表示された場合：

.. code-block::

    ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
    spelling of the name, or if a path was included, verify that the path is correct and try again.


これは、使用しているWindowsが古く、 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ がプレインストールされていないことを意味しています。以下の手順に従って手動でインストールしてください。

#. Windowsの検索バーに ``powershell`` と入力し、表示された ``Windows PowerShell`` を右クリックして「管理者として実行」を選択します。

   .. image:: img/powershell_ssh.png
      :width: 90%


#. 次のコマンドで ``OpenSSH.Client`` をインストールします。

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. インストールが完了すると、以下のような出力が表示されます。

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 次のコマンドでインストールが完了したか確認します。

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. これで ``OpenSSH.Client`` が正常にインストールされたことが確認できます。

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        上記の表示が出ない場合、Windowsのバージョンが古すぎる可能性があります。その場合は、|link_putty| などのサードパーティ製SSHツールをご使用ください。

#. PowerShellを再起動し、再び「管理者として実行」してください。これで ``ssh`` コマンドが使えるようになり、Raspberry Piへ接続する際にパスワード入力が求められます。

   .. image:: img/powershell_login.png



OMVを設定した場合でもPironman5の機能は使えますか？
--------------------------------------------------------------------------------------------------------

はい、OpenMediaVault は Raspberry Pi OS 上に構築されているため、:ref:`max_set_up_pi_os` の手順に従って設定を続けることで、Pironman5 の機能をご利用いただけます。