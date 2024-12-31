.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 エンスージアストコミュニティ（Facebook）へようこそ！Raspberry Pi、Arduino、ESP32 を愛する仲間たちとともに、さらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: 購入後の問題や技術的な課題を、コミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: スキル向上のためにヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表や先行情報をいち早く入手できます。
    - **特別割引**: 最新製品を特別価格で購入できます。
    - **プロモーションとプレゼント企画**: プレゼント企画や季節のプロモーションに参加できます。

    👉 新しい発見と創造の旅に出る準備はできましたか？[|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

FAQ
=====

1. 対応システムについて
------------------------

Raspberry Pi 5 で動作確認されたシステム：

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. 電源ボタンについて
-------------------------

電源ボタンは Raspberry Pi 5 の電源ボタンとして機能し、以下の操作が可能です。

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **シャットダウン**

  * Raspberry Pi **Bookworm Desktop** システムを実行している場合、電源ボタンを素早く2回押すことでシャットダウンできます。
  * Raspberry Pi **Bookworm Lite** システムを実行している場合、電源ボタンを1回押すだけでシャットダウンを開始します。
  * 強制的にハードシャットダウンするには、電源ボタンを長押ししてください。

* **電源オン**

  * Raspberry Pi がシャットダウン状態でも電源供給されている場合、電源ボタンを1回押すだけで電源を入れることができます。

* シャットダウンボタンをサポートしないシステムを使用している場合、電源ボタンを5秒間押し続けてハードシャットダウンを強制的に行い、その後、1回押して電源を入れることができます。

3. エアフローの方向について
-----------------------------

Pironman 5 のシャーシ内のエアフローは、冷却効率を最大化するように設計されています。冷たい空気は主に GPIO インターフェースや他の小さな開口部からケース内に入り、Tool Cooler を通過して内部温度を調整し、最終的に側面パネルにある2つのRGBファンを通じて排出されます。

詳細なデモンストレーションについては、以下の動画をご覧ください：

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="_static/video/airflow_direction.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>

4. タワークーラーの銅パイプの端について
------------------------------------------

タワークーラー上部のU字型ヒートパイプは、アルミフィンを通る銅パイプを固定するために圧縮されています。これは銅パイプの通常の製造工程の一部です。

   .. image:: img/tower_cooler1.png

5. Pironman 5 はレトロゲームシステムをサポートしますか？
---------------------------------------------------------

はい、対応しています。ただし、ほとんどのレトロゲームシステムは簡略化されたバージョンであり、追加のソフトウェアをインストールおよび実行できない場合があります。この制限により、Pironman 5 の一部コンポーネント（OLEDディスプレイ、2つのRGBファン、4つのRGB LEDなど）が正しく機能しない可能性があります。これらのコンポーネントには Pironman 5 のソフトウェアパッケージのインストールが必要です。

.. note::

   現在、Batocera.linux システムは Pironman 5 と完全に互換性があります。Batocera.linux はオープンソースで完全無料のレトロゲーム配信です。

   * :ref:`install_batocera`
   * :ref:`set_up_batocera`

6. OLEDスクリーンが動作しない場合
---------------------------------------

OLEDスクリーンが正しく表示されない場合、以下の手順でトラブルシューティングを行ってください：

#. OLEDスクリーンのFPCケーブルがしっかり接続されていることを確認してください。OLEDスクリーンを再接続し、デバイスを再起動することをお勧めします。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_oled_screen.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. Raspberry Pi が対応するオペレーティングシステムを実行していることを確認してください。Pironman 5 は以下のシステムのみをサポートします：

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   未対応のシステムをインストールしている場合は、ガイドに従って対応するOSをインストールしてください：:ref:`install_the_os`。

#. 初めてOLEDスクリーンに電源を入れると、ピクセルブロックのみが表示される場合があります。:ref:`set_up_pironman5` の指示に従い、適切に構成を完了してください。

#. 以下のコマンドを使用して、OLEDのI2Cアドレス ``0x3C`` が検出されているか確認してください：

   .. code-block:: shell

      sudo i2cdetect -y 1

   * I2Cアドレス ``0x3C`` が検出された場合、以下のコマンドを使用してPironman 5 サービスを再起動してください：

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * アドレスが検出されない場合は、I2Cを有効にしてください：

     * 次のコマンドで設定ファイルを編集：

       .. code-block:: shell

         sudo nano /boot/firmware/config.txt

     * ファイルの最後に以下の行を追加：

       .. code-block:: shell

         dtparam=i2c_arm=on

     * ``Ctrl+X`` を押してファイルを保存し、 ``Y`` を入力して終了。Pironman 5 を再起動し、問題が解決したか確認してください。

問題が解決しない場合は、service@sunfounder.com までメールでお問い合わせください。可能な限り迅速に対応いたします。

7. NVMe PIPモジュールが動作しない場合
------------------------------------------

1. NVMe PIPモジュールをRaspberry Pi 5に接続するFPCケーブルが確実に接続されていることを確認してください。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

2. SSDがNVMe PIPモジュールにしっかりと固定されていることを確認してください。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/connect_ssd.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

3. NVMe PIPモジュールのLEDステータスを確認してください：

   すべての接続を確認した後、Pironman 5 の電源を入れ、NVMe PIPモジュールの2つのインジケーターを観察してください：

   * **PWR LED**: 点灯している必要があります。
   * **STA LED**: 点滅している場合、正常に動作しています。

   .. image:: img/nvme_pip_leds.png

   * **PWR LED** が点灯しているが **STA LED** が点滅していない場合、NVMe SSD がRaspberry Pi に認識されていない可能性があります。
   * **PWR LED** が消灯している場合、モジュール上の「Force Enable」ピン（J4）を短絡してください。 **PWR LED** が点灯する場合、FPCケーブルの接続不良またはNVMeのサポート外構成である可能性があります。

     .. image:: img/nvme_pip_j4.png

4. NVMe SSD に適切なオペレーティングシステムがインストールされていることを確認してください。:ref:`install_the_os` を参照してください。

5. 配線が正しく、OSがインストールされている場合でもNVMe SSDが起動しない場合は、Micro SDカードから起動して他のコンポーネントの機能を確認してください。その後、:ref:`configure_boot_ssd` を参照してください。

上記の手順を実行しても問題が解決しない場合は、service@sunfounder.com までメールでお問い合わせください。可能な限り迅速に対応いたします。

8. RGB LEDが動作しない場合
--------------------------

#. J9上部のIOエクスパンダーの2つのピンは、RGB LEDをGPIO10に接続するために使用されます。これらのピンにジャンパーキャップが正しく装着されていることを確認してください。

   .. image:: advanced/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Raspberry Piが対応するオペレーティングシステムを実行していることを確認してください。Pironman 5は以下のOSバージョンのみをサポートしています。

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   未対応のOSをインストールしている場合は、ガイドに従って対応するOSをインストールしてください：:ref:`install_the_os`。

#. ``sudo raspi-config`` コマンドを実行して設定メニューを開きます。 **3 Interfacing Options** -> **I3 SPI** -> **YES** を選択し、 **OK** および **Finish** をクリックしてSPIを有効にします。SPIを有効にした後、Pironman 5を再起動してください。

上記の手順を実行しても問題が解決しない場合は、service@sunfounder.com までメールでお問い合わせください。可能な限り迅速に対応いたします。

9. CPUファンが動作しない場合
-----------------------------

CPU温度が設定されたしきい値に達していない場合、CPUファンは動作しません。

**温度に基づくファンスピード制御**  

PWMファンは、Raspberry Pi 5の温度に応じて速度を動的に調整します：  

* **50°C未満**: ファンはオフ（0%速度）。  
* **50°C**: ファンは低速で動作（30%速度）。  
* **60°C**: ファンは中速で動作（50%速度）。  
* **67.5°C**: ファンは高速で動作（70%速度）。  
* **75°C以上**: ファンは最大速度（100%速度）で動作。  

詳細については、:ref:`Fans` を参照してください。

10. Webダッシュボードを無効にする方法
-----------------------------------------

``pironman5`` モジュールのインストールを完了すると、:ref:`view_control_dashboard` にアクセスできるようになります。

この機能が不要でCPUおよびRAMの使用量を削減したい場合、 ``pironman5`` のインストール時に ``--disable-dashboard`` フラグを追加することでダッシュボードを無効化できます。

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

既に ``pironman5`` をインストール済みの場合、 ``dashboard`` モジュールと ``influxdb`` を削除し、Pironman 5を再起動して変更を適用できます：

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

11. ``pironman5`` コマンドを使用してコンポーネントを制御する方法
------------------------------------------------------------------

``pironman5`` コマンドを使用してPironman 5のコンポーネントを制御する方法については、以下のチュートリアルを参照してください：

* :ref:`view_control_commands`

12. コマンドを使用してRaspberry Piのブート順を変更する方法
-----------------------------------------------------------

Raspberry Piにログインしている場合、コマンドを使用してブート順を変更できます。詳細な手順は以下を参照してください：

* :ref:`configure_boot_ssd`

13. Raspberry Pi Imagerを使用してブート順を変更する方法
----------------------------------------------------------

EEPROM設定で ``BOOT_ORDER`` を変更するだけでなく、 **Raspberry Pi Imager** を使用してRaspberry Piのブート順を変更することもできます。

この手順では予備のカードを使用することをお勧めします。

* :ref:`update_bootloader`

14. SDカードからNVMe SSDにシステムをコピーする方法
----------------------------------------------------

NVMe SSDを持っているが、NVMeをコンピュータに接続するアダプタがない場合、最初にMicro SDカードにシステムをインストールします。Pironman 5が正常に起動した後、Micro SDカードからNVMe SSDにシステムをコピーすることができます。詳細な手順は以下を参照してください：

* :ref:`copy_sd_to_nvme_rpi`

15. アクリルパネルから保護フィルムを取り外す方法
-------------------------------------------------

パッケージには2枚のアクリルパネルが含まれており、どちらにも傷防止のために両面に黄色/透明の保護フィルムが貼られています。この保護フィルムは取り外しがやや難しい場合があります。ドライバーを使用して角を慎重にこすり、フィルム全体をゆっくりと剥がしてください。

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _openssh_powershell:

16. PowerShellを使用してOpenSSHをインストールする方法
--------------------------------------------------------

``ssh <username>@<hostname>.local`` または ``ssh <username>@<IP address>`` を使用してRaspberry Piに接続しようとした際、以下のエラーメッセージが表示される場合があります。

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

このエラーは、使用しているコンピューターのシステムが古く、 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ が事前にインストールされていないことを意味します。以下の手順に従い、手動でインストールしてください。

#. Windowsデスクトップの検索ボックスに ``powershell`` と入力し、 ``Windows PowerShell`` を右クリックして、表示されるメニューから ``管理者として実行`` を選択します。

   .. image:: img/powershell_ssh.png
      :width: 90%

#. 次のコマンドを使用して ``OpenSSH.Client`` をインストールします。

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. インストール後、次のような出力が返されます。

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 以下のコマンドを使用してインストールを確認します。

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. 次のメッセージが表示され、 ``OpenSSH.Client`` が正常にインストールされたことを示します。

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        上記のメッセージが表示されない場合は、Windowsシステムが非常に古いことを意味します。この場合は、|link_putty| のようなサードパーティ製SSHツールをインストールすることをお勧めします。

#. PowerShellを再起動し、管理者として実行を続行します。この時点で、 ``ssh`` コマンドを使用してRaspberry Piにログインできるようになり、以前設定したパスワードの入力を求められます。

   .. image:: img/powershell_login.png


17. OLEDスクリーンをオン/オフする方法
--------------------------------------

OLEDスクリーンはダッシュボードまたはコマンドラインからオン/オフを切り替えることができます。

1. ダッシュボードでOLEDスクリーンをオン/オフする方法

   .. note::

    ダッシュボードを使用する前に、Home Assistantで設定を行う必要があります。詳細については、:ref:`view_control_dashboard` を参照してください。

- セットアップが完了したら、以下の手順に従ってOLEDスクリーンをオン、オフ、または設定を変更します。

   .. image:: img/set_up_on_dashboard.jpg
      :width: 90%

2. コマンドラインでOLEDスクリーンをオン/オフする方法

- 以下のコマンドを使用してOLEDスクリーンをオンまたはオフにします。

.. code-block::

    sudo pironman5 -oe on/off

.. note::

    変更を有効にするには、pironman5サービスを再起動する必要がある場合があります。以下のコマンドを使用してサービスを再起動してください。

      .. code-block::

        sudo systemctl restart pironman5.service
