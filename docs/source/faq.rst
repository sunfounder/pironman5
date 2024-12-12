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

1. 対応システムについて
-------------------------------

Raspberry Pi 5でテストを通過したシステム：

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. 電源ボタンについて
--------------------------

電源ボタンはRaspberry Pi 5の電源ボタンを引き出しており、Raspberry Pi 5の電源ボタンと同様に機能します。

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **シャットダウン**

  * Raspberry Pi **Bookworm Desktop** システムを使用している場合、電源ボタンを2回すばやく押すとシャットダウンできます。
  * Raspberry Pi **Bookworm Lite** システムを使用している場合、電源ボタンを1回押すとシャットダウンが開始されます。
  * 強制的にハードシャットダウンするには、電源ボタンを押し続けます。

* **電源オン**

  * Raspberry Piボードがシャットダウンしているが電源が供給されている場合、電源ボタンを1回押すことでシャットダウン状態から電源をオンにできます。

* シャットダウンボタンをサポートしないシステムを使用している場合、5秒間押し続けることで強制的にハードシャットダウンを行い、シャットダウン状態からの電源オンには1回押します。

3. エアフローの方向について
-------------------------------

Pironman 5のケース内のエアフローは、冷却効率を最大化するよう慎重に設計されています。冷たい空気は主にGPIOインターフェースやその他の小さな開口部を通じてケースに取り込まれ、均等な吸気を実現します。その後、内部温度を調整する高性能ファンが装備されたツールクーラーを通過し、最後に側面パネルの2つのRGBファンを通じて排出されます。

詳しいデモンストレーションについては、以下のビデオをご覧ください：

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="_static/video/airflow_direction.mp4"  type="video/mp4">
            お使いのブラウザはビデオタグをサポートしていません。
        </video>
    </div>

4. Pironman 5はレトロゲームシステムをサポートしていますか？
-----------------------------------------------------------

はい、互換性があります。ただし、多くのレトロゲームシステムは軽量化されたバージョンであるため、追加のソフトウェアをインストールおよび実行できません。この制限により、OLEDディスプレイ、2つのRGBファン、4つのRGB LEDなどのPironman 5の一部のコンポーネントが正しく機能しない場合があります。これらのコンポーネントは、Pironman 5のソフトウェアパッケージのインストールを必要とします。

.. note::

   Batocera.linuxシステムは現在、Pironman 5と完全に互換性があります。Batocera.linuxはオープンソースで完全に無料のレトロゲーム向けディストリビューションです。

   * :ref:`install_batocera`
   * :ref:`set_up_batocera`

5. OLEDスクリーンが動作しない場合？
-----------------------------------

OLEDスクリーンが表示されない、または正しく表示されない場合、以下の手順でトラブルシューティングを行ってください：

#. OLEDスクリーンのFPCケーブルが確実に接続されていることを確認してください。OLEDスクリーンを再接続してからデバイスの電源を入れることをお勧めします。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_oled_screen.mp4" type="video/mp4">
               お使いのブラウザはビデオタグをサポートしていません。
           </video>
       </div>

#. Raspberry Piが対応するオペレーティングシステムを実行していることを確認してください。Pironman 5は以下のシステムのみをサポートしています：

   .. image:: img/compitable_os.png  
      :width: 600  
      :align: center  

   非対応システムをインストールしている場合は、対応するOSをインストールするガイドを参照してください： :ref:`install_the_os`.

#. 初めてOLEDスクリーンの電源を入れると、ピクセルブロックのみが表示される場合があります。 :ref:`set_up_pironman5` の指示に従い、適切な情報を表示するための設定を完了してください。

#. 以下のコマンドを使用して、OLEDのI2Cアドレス ``0x3C`` が検出されているかを確認します：

   .. code-block:: shell

      sudo i2cdetect -y 1

   * I2Cアドレス ``0x3C`` が検出された場合、このコマンドを使用してPironman 5サービスを再起動してください：

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * アドレスが検出されない場合は、I2Cを有効にします：

     * 次のコマンドを実行して設定ファイルを編集します：

       .. code-block:: shell

         sudo nano /boot/firmware/config.txt

     * ファイルの最後に次の行を追加します：

       .. code-block:: shell

         dtparam=i2c_arm=on

     * ``Ctrl+X`` を押してファイルを保存し、 ``Y`` を押して終了します。その後、Pironman 5を再起動して問題が解決されたか確認してください。

上記の手順を実行しても問題が解決しない場合は、service@sunfounder.com にメールを送信してください。できる限り迅速に対応いたします。

6. NVMe PIPモジュールが動作しない場合？
---------------------------------------

1. NVMe PIPモジュールをRaspberry Pi 5に接続するFPCケーブルが確実に取り付けられていることを確認してください。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               お使いのブラウザはビデオタグをサポートしていません。
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               お使いのブラウザはビデオタグをサポートしていません。
           </video>
       </div>

2. SSDがNVMe PIPモジュールにしっかりと取り付けられていることを確認してください。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_ssd.mp4" type="video/mp4">
               お使いのブラウザはビデオタグをサポートしていません。
           </video>
       </div>

3. NVMe PIPモジュールのLEDの状態を確認します：

   すべての接続を確認した後、Pironman 5の電源を入れ、NVMe PIPモジュール上の2つのインジケータを観察します：

   * **PWR LED**: 点灯している必要があります。
   * **STA LED**: 点滅している場合は正常動作を示します。

   .. image:: img/nvme_pip_leds.png  

   * **PWR LED** が点灯しているが **STA LED** が点滅していない場合、Raspberry PiがNVMe SSDを認識していないことを示します。
   * **PWR LED** が点灯していない場合、モジュール上の「Force Enable」ピン (J4) を短絡させてください。 **PWR LED** が点灯した場合、FPCケーブルの接続不良またはNVMe用の非対応システム構成の可能性があります。

     .. image:: img/nvme_pip_j4.png  

4. NVMe SSDにオペレーティングシステムが正しくインストールされていることを確認してください。参照： :ref:`install_the_os`.

5. 配線が正しく、OSがインストールされているにもかかわらず、NVMe SSDが起動しない場合は、Micro SDカードから起動して他のコンポーネントの機能を確認してください。その後、 :ref:`configure_boot_ssd` に進んでください。

上記の手順を実行しても問題が解決しない場合は、service@sunfounder.com にメールを送信してください。できる限り迅速に対応いたします。

7. RGB LEDが動作しない場合？
----------------------------------

#. J9上のIOエキスパンダーの2つのピンは、RGB LEDをGPIO10に接続するために使用されます。これらのピンにあるジャンパーキャップが正しく配置されていることを確認してください。

   .. image:: advanced/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Raspberry Piが対応するオペレーティングシステムを実行していることを確認してください。Pironman 5は以下のOSバージョンのみをサポートしています：

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   非対応のOSをインストールしている場合、対応するOSをインストールするガイドを参照してください： :ref:`install_the_os`.

#. コマンド ``sudo raspi-config`` を実行して設定メニューを開きます。**3 Interfacing Options** -> **I3 SPI** -> **YES** を選択し、 **OK** と **Finish** をクリックしてSPIを有効化します。SPIを有効化した後、Pironman 5を再起動してください。

上記の手順を実行しても問題が解決しない場合は、service@sunfounder.com にメールを送信してください。できる限り迅速に対応いたします。

8. Webダッシュボードを無効にする方法
------------------------------------------------------

``pironman5`` モジュールのインストールを完了すると、 :ref:`view_control_dashboard` にアクセスできるようになります。
      
この機能が不要で、CPUとRAMの使用量を減らしたい場合、 ``pironman5`` をインストールする際に ``--disable-dashboard`` フラグを追加することでダッシュボードを無効にできます。
      
.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard
      
すでに ``pironman5`` をインストールしている場合は、 ``dashboard`` モジュールと ``influxdb`` を削除し、その後 pironman5 を再起動して変更を適用してください：
      
.. code-block:: shell
      
   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

9. ``pironman5`` コマンドを使用してコンポーネントを制御する方法
----------------------------------------------------------------------

``pironman5`` コマンドを使用してPironman 5のコンポーネントを制御する方法については、以下のチュートリアルを参照してください。

* :ref:`view_control_commands`

10. Raspberry Piの起動順序をコマンドで変更する方法
-------------------------------------------------------------

Raspberry Piにログイン済みの場合、コマンドを使用して起動順序を変更できます。詳細な手順は以下を参照してください：

* :ref:`configure_boot_ssd`

11. Raspberry Pi Imagerを使用して起動順序を変更する方法
---------------------------------------------------------------

EEPROM設定で ``BOOT_ORDER`` を変更することに加え、 **Raspberry Pi Imager** を使用してRaspberry Piの起動順序を変更することもできます。

この手順には予備のカードを使用することをお勧めします。

* :ref:`update_bootloader`

12. システムをSDカードからNVMe SSDにコピーする方法
-------------------------------------------------------------

NVMe SSDを持っているが、NVMeをコンピュータに接続するアダプターを持っていない場合、まずMicro SDカードにシステムをインストールします。Pironman 5が正常に起動したら、Micro SDカードからNVMe SSDにシステムをコピーできます。詳細な手順は以下を参照してください：

* :ref:`copy_sd_to_nvme_rpi`

13. アクリル板の保護フィルムを剥がす方法
-----------------------------------------------------------------

パッケージには2枚のアクリル板が含まれており、両面に傷を防ぐための黄色/透明の保護フィルムが貼られています。この保護フィルムは少し剥がしにくい場合があります。ドライバーを使用して角をそっと削り、フィルム全体を注意深く剥がしてください。

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _openssh_powershell:

14. PowerShellを使用してOpenSSHをインストールする方法
-----------------------------------------------------------

``ssh <username>@<hostname>.local`` （または ``ssh <username>@<IP address>``）を使用してRaspberry Piに接続しようとした際に、次のエラーメッセージが表示される場合：

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

これは、使用しているコンピュータのシステムが古いため、 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ が事前インストールされていないことを意味します。以下の手順に従って手動でインストールする必要があります。

#. Windowsデスクトップの検索ボックスに ``powershell`` と入力し、 ``Windows PowerShell`` を右クリックして、表示されるメニューから ``管理者として実行`` を選択します。

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. 次のコマンドを使用して ``OpenSSH.Client`` をインストールします。

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. インストールが完了すると、次の出力が返されます。

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 以下のコマンドを使用してインストールを確認します。

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. ``OpenSSH.Client`` が正常にインストールされたことを確認できます。

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning:: 

      上記のプロンプトが表示されない場合は、Windowsシステムが依然として古いため、|link_putty| のようなサードパーティのSSHツールをインストールすることをお勧めします。

#. PowerShellを再起動し、再度管理者として実行します。この時点で、 ``ssh`` コマンドを使用してRaspberry Piにログインできるようになり、以前に設定したパスワードを入力するよう求められます。

   .. image:: img/powershell_login.png
