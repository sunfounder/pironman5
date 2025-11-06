.. note::

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ。他の愛好者と一緒にRaspberry Pi、Arduino、ESP32の世界をより深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームのサポートを受けて、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品の発表やプレビュー情報を早期に入手できます。
    - **特別割引**: 最新製品に関する限定割引をお楽しみください。
    - **特別なプロモーションとプレゼント**: プレゼント企画や特別イベントに参加できます。

    👉 探索と創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

FAQ
============

1. 対応するシステムについて
-------------------------------

Raspberry Pi 5でテスト済みの対応システム：

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. 電源ボタンについて
--------------------------

Pironman 5の電源ボタンは、Raspberry Pi 5の電源ボタンを外部に引き出したもので、同じように動作します。

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **シャットダウン**

  * Raspberry Pi **Raspberry Pi OS Desktop** システムを使用している場合、電源ボタンを素早く2回押すとシャットダウンできます。
  * Raspberry Pi **Raspberry Pi OS Lite** システムを使用している場合、電源ボタンを1回押すだけでシャットダウンが開始されます。
  * 強制的なシャットダウンを行うには、電源ボタンを長押ししてください。

* **電源オン**

  * Raspberry Piボードがシャットダウン状態でも電源が供給されている場合、電源ボタンを1回押すだけで起動できます。

* シャットダウンボタンをサポートしていないシステムを使用している場合、電源ボタンを5秒間長押しすると強制的なシャットダウンが行われ、1回押すことで起動できます。

3. エアフローの方向について
-------------------------------

Pironman 5のシャーシ内のエアフローは、冷却効率を最大化するよう慎重に設計されています。冷たい空気は主にGPIOインターフェースやその他の小さな開口部からケース内に入り、均一な吸気を確保します。その後、Tool Coolerを通過し、内蔵の高性能ファンで内部温度を調整し、最終的には側面パネルの2つのRGBファンを通じて排出されます。

詳しいデモンストレーションについては以下のビデオをご覧ください：

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="../_static/video/airflow_direction.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>

4. タワークーラーについて
----------------------------------------------------------

#. タワークーラーの上部にあるU字型のヒートパイプは、銅管がアルミフィンを通過しやすいように圧縮されています。これは銅管の通常の製造工程の一部です。

   .. image::  img/tower_cooler1.png

#. タワークーラーの取り付け時の注意事項:

**パッドの取り付け**: タワークーラーを取り付ける前に、Raspberry Pi にパッドを取り付けて、損傷や傷を防いでください。

 .. image::  img/tower_cooler_thermal.png

**正しい向き**: タワークーラーの向きを確認してください。Raspberry Pi の位置決め穴と合わせ、スプリングネジを押し込んで固定します。

 .. image::  img/tower_cooler_place.jpg

**慎重な取り外し**: タワークーラーが誤った向きで取り付けられた場合、またはパッドが適用されていない場合は、無理に取り外さないでください。

- タワークーラーを安全に取り外すには、以下の手順に従ってください。

  ピンセットまたはプライヤーを使用してスプリングナットの先端をつかみ、ゆっくりと上に押し上げて取り外します。

     .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/remove_tower_cooler.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>


5. Raspberry Pi AI HAT+について
----------------------------------------------------------

Raspberry Pi AI HAT+はPironman 5に対応していません。

   .. image:: img/output3.png
        :width: 400

Raspberry Pi AIキットは、Raspberry Pi M.2 HAT+とHailo AIアクセラレータモジュールを組み合わせたものです。

   .. image:: img/output2.jpg
        :width: 400

Hailo AIアクセラレータモジュールをRaspberry Pi AIキットから取り外し、Pironman 5のNVMe PIPモジュールに直接挿入することができます。

   .. image:: img/output4.png
        :width: 800

6. PI5 が起動しない（赤色 LED）場合
-------------------------------------------

この問題は、システムのアップデート、ブート順序の変更、またはブートローダーの破損が原因で発生する可能性があります。以下の手順を試して問題を解決してください。

#. USB-HDMI アダプター接続の確認

   * USB-HDMI アダプターが PI5 にしっかりと接続されているか慎重に確認してください。
   * USB-HDMI アダプターを一度抜き、再度接続してみてください。
   * その後、電源を再接続し、PI5 が正常に起動するか確認します。

#. ケース外で PI5 をテストする

   * アダプターの再接続で問題が解決しない場合：
   * PI5 を Pironman 5 ケースから取り外してください。
   * ケースを使用せずに、電源アダプターで直接 PI5 に給電します。
   * 正常に起動できるか確認してください。

#. ブートローダーを復元する

   * それでも PI5 が起動しない場合、ブートローダーが破損している可能性があります。:ref:`update_bootloader_5` のガイドに従い、SD カードまたは NVMe/USB からの起動を選択してください。
   * 準備した SD カードを PI5 に挿入し、電源を入れて少なくとも 10 秒待ちます。リカバリーが完了したら、SD カードを取り外し、再フォーマットしてください。
   * その後、Raspberry Pi Imager を使用して最新の Raspberry Pi OS を書き込み、カードを再度挿入して起動を試みてください。


.. 6. Pironman 5はレトロゲームシステムをサポートしていますか？
.. --------------------------------------------------------------

.. はい、対応しています。ただし、ほとんどのレトロゲームシステムは軽量化されたバージョンであるため、追加のソフトウェアをインストールして実行することができません。この制限により、Pironman 5の一部のコンポーネント（OLEDディスプレイ、2つのRGBファン、4つのRGB LEDなど）が正常に機能しない可能性があります。これらのコンポーネントはPironman 5のソフトウェアパッケージのインストールを必要とします。

.. .. note::

..    Batocera.linuxシステムは現在Pironman 5と完全互換です。Batocera.linuxはオープンソースで完全に無料のレトロゲーム用ディストリビューションです。

..    * :ref:`install_batocera`
..    * :ref:`set_up_batocera`

7. OLEDスクリーンが動作しない場合
-----------------------------------

OLEDスクリーンが表示されない、または正しく表示されない場合、以下のトラブルシューティング手順を試してください：

#. OLEDスクリーンのFPCケーブルが確実に接続されていることを確認してください。再接続してからデバイスを再起動することをお勧めします。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_oled_screen.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. Raspberry Piが対応するオペレーティングシステムを実行していることを確認してください。Pironman 5は以下のシステムのみをサポートしています：  

   .. image:: img/compitable_os.png  
      :width: 600  
      :align: center  

   非対応のシステムをインストールした場合、互換性のあるOSをインストールするためのガイドに従ってください： :ref:`install_the_os` .

#. 初回電源投入時、OLEDスクリーンにはピクセルブロックのみが表示される場合があります。この場合、:ref:`set_up_pironman5` の手順に従い、設定を完了してください。

#. 以下のコマンドを使用して、OLEDのI2Cアドレス ``0x3C`` が検出されているか確認してください：

   .. code-block:: shell

      sudo i2cdetect -y 1

   * I2Cアドレス ``0x3C`` が検出された場合、以下のコマンドを実行してPironman 5サービスを再起動してください：

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * アドレスが検出されない場合は、I2Cを有効にしてください：

     * 以下のコマンドを実行して設定ファイルを編集します：

       .. code-block:: shell

         sudo nano /boot/firmware/config.txt

     * ファイルの末尾に以下の行を追加します：

       .. code-block:: shell

         dtparam=i2c_arm=on

     * ``Ctrl+X`` を押して保存し、 ``Y`` を押して終了します。その後、Pironman 5を再起動して問題が解決したか確認してください。

これらの手順を実行しても問題が解決しない場合は、service@sunfounder.comまでメールでお問い合わせください。できるだけ早く対応いたします。

8. NVMe PIPモジュールが動作しない場合
---------------------------------------

1. NVMe PIPモジュールとRaspberry Pi 5を接続しているFPCケーブルがしっかり接続されていることを確認してください。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

2. SSDがNVMe PIPモジュールに正しく固定されていることを確認してください。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_ssd.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

3. NVMe PIPモジュールのLED状態を確認します：

   接続を確認した後、Pironman 5の電源を入れ、NVMe PIPモジュール上のインジケーターを確認してください：

   * **PWR LED** : 点灯している必要があります。
   * **STA LED** : 正常動作を示すため点滅する必要があります。

   .. image:: img/nvme_pip_leds.png  

   * **PWR LED** が点灯していても **STA LED** が点滅しない場合、NVMe SSDがRaspberry Piに認識されていない可能性があります。
   * **PWR LED** が消灯している場合、モジュール上の「Force Enable」ピン（J4）をショートしてください。 **PWR LED** が点灯した場合、FPCケーブルの緩みや、システム構成の問題の可能性があります。

     .. image:: img/nvme_pip_j4.png  

4. NVMe SSDに適切なOSがインストールされていることを確認してください。詳細は: :ref:`install_the_os` .

5. 配線が正しく、OSもインストールされているのにNVMe SSDが起動しない場合は、Micro SDカードから起動して他のコンポーネントの機能を確認してください。確認後、:ref:`configure_boot_ssd` に進んでください。

これらの手順を実行しても問題が解決しない場合は、service@sunfounder.comまでメールでお問い合わせください。できるだけ早く対応いたします。

9. RGB LEDが動作しない場合
----------------------------

#. J9上のIOエクスパンダーにある2つのピンは、RGB LEDをGPIO10に接続するために使用されます。これらのピンにジャンパーキャップが正しく取り付けられていることを確認してください。

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Raspberry Piが対応するオペレーティングシステムを実行していることを確認してください。Pironman 5は以下のOSバージョンのみをサポートしています：

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   非対応のOSをインストールした場合は、互換性のあるOSをインストールするガイドを参照してください： :ref:`install_the_os`.

#. ``sudo raspi-config`` コマンドを実行して設定メニューを開きます。 **3 Interfacing Options** -> **I3 SPI** -> **YES** を選択し、 **OK** および **Finish** をクリックしてSPIを有効にします。SPIを有効にした後、Pironman 5を再起動してください。

上記の手順を実行しても問題が解決しない場合は、service@sunfounder.com までメールでお問い合わせください。可能な限り迅速に対応いたします。


10. CPUファンが動作しない場合
----------------------------------------------

CPU温度が設定されたしきい値に達していない場合、CPUファンは動作しません。

**温度に基づくファン速度制御**  

PWMファンはRaspberry Pi 5の温度に応じて動的に速度を調整します：

* **50°C未満**: ファンは停止したまま（0%の速度）。
* **50°Cで**: ファンは低速で動作（30%の速度）。
* **60°Cで**: ファンは中速に増加（50%の速度）。
* **67.5°Cで**: ファンは高速に加速（70%の速度）。
* **75°C以上**: ファンは全速で動作（100%の速度）。

詳細については: :ref:`Fans` を参照してください。

11. ウェブダッシュボードを無効化する方法
------------------------------------------------------

``pironman5`` モジュールのインストールが完了すると、:ref:`view_control_dashboard` にアクセスできるようになります。

この機能が不要で、CPUやRAMの使用量を削減したい場合は、 ``pironman5`` のインストール時に ``--disable-dashboard`` フラグを追加することでダッシュボードを無効にできます。

.. code-block:: shell
      
   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

すでに ``pironman5`` をインストール済みの場合は、 ``dashboard`` モジュールと ``influxdb`` を削除し、Pironman5を再起動して変更を反映させます：

.. code-block:: shell

   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

12. ``pironman5`` コマンドを使用してコンポーネントを制御する方法
----------------------------------------------------------------------

``pironman5`` コマンドを使用してPironman 5のコンポーネントを制御する方法については、以下のチュートリアルを参照してください：

* :ref:`view_control_commands`

13. コマンドを使用してRaspberry Piのブート順序を変更する方法
-------------------------------------------------------------

Raspberry Piにログイン済みの場合、コマンドを使用してブート順序を変更できます。詳細な手順は以下の通りです：

* :ref:`configure_boot_ssd`

14. Raspberry Pi Imagerを使用してブート順序を変更する方法
---------------------------------------------------------------

EEPROM設定で ``BOOT_ORDER`` を変更する以外にも、 **Raspberry Pi Imager** を使用してRaspberry Piのブート順序を変更することができます。

この手順には予備のSDカードを使用することをお勧めします。

* :ref:`update_bootloader_5`

15. システムをSDカードからNVMe SSDにコピーする方法
-------------------------------------------------------------

NVMe SSDを持っているが、NVMeをコンピュータに接続するためのアダプターがない場合、まずMicro SDカードにシステムをインストールします。その後、Pironman 5が正常に起動したら、Micro SDカードからNVMe SSDにシステムをコピーできます。詳細な手順は以下を参照してください：

* :ref:`copy_sd_to_nvme_rpi`

16. アクリル板の保護フィルムを取り外す方法
-----------------------------------------------------------------

パッケージには2枚のアクリル板が含まれており、両面に黄色または透明の保護フィルムが付いています。このフィルムは傷を防ぐためのものですが、取り外すのが少し難しい場合があります。ドライバーを使用して角をそっと削り、フィルム全体を慎重に剥がしてください。

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. _openssh_powershell:

17. PowerShellを使用してOpenSSHをインストールする方法
--------------------------------------------------------

Raspberry Piに接続する際に、 ``ssh <username>@<hostname>.local`` または ``ssh <username>@<IP address>`` を使用し、以下のようなエラーメッセージが表示される場合：

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

これは、コンピュータのシステムが古く、 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_  が事前にインストールされていないことを意味します。以下の手順に従って手動でインストールしてください。

#. Windowsデスクトップの検索ボックスに ``powershell`` と入力し、 ``Windows PowerShell`` を右クリックして、表示されるメニューから ``管理者として実行`` を選択します。

   .. image:: img/powershell_ssh.png
      :width: 90%

#. 以下のコマンドを使用して ``OpenSSH.Client`` をインストールします。

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. インストール後、次の出力が表示されます。

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 以下のコマンドを使用してインストールを確認します。

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. これにより、 ``OpenSSH.Client`` が正常にインストールされたことが確認されます。

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent


  .. warning ::

    上記のプロンプトが表示されない場合、Windowsシステムがさらに古いため |link_putty| のようなサードパーティSSHツールのインストールを検討してください。

6. PowerShellを再起動し、再度管理者として実行してください。この時点で ``ssh`` コマンドを使用してRaspberry Piにログインできるようになります。セットアップ時に指定したパスワードの入力が求められます。

   .. image:: img/powershell_login.png


18. なぜ有機表示画面は自動的に消えるのですか？
---------------------------------------------------------------------------------

電力を節約し、画面の寿命を延ばすため、有機表示画面は一定時間操作がないと自動的に消えます。  
これは通常の設計の一部であり、製品の機能には影響しません。

装置のボタンを一度押すだけで、有機表示画面が再び点灯し、表示を再開します。

.. note::

   有機表示画面の設定（点灯／消灯、休止時間、回転など）については、:ref:`view_control_dashboard` または :ref:`view_control_commands` を参照してください。
