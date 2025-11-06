.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！同じ趣味を持つ仲間たちと一緒に、Raspberry Pi・Arduino・ESP32 の世界をより深く楽しみましょう。

    **Why Join?**

    - **Expert Support**：購入後のトラブルや技術的課題を、コミュニティとサポートチームがサポートします。
    - **Learn & Share**：ヒントやチュートリアルを共有しながらスキルアップ。
    - **Exclusive Previews**：新製品の先行発表やプレビューにいち早くアクセス。
    - **Special Discounts**：最新製品に対する限定割引をご利用いただけます。
    - **Festive Promotions and Giveaways**：プレゼント企画や季節限定キャンペーンにもご参加いただけます。

    👉 私たちと一緒に創造と探求を始めましょう！[|link_sf_facebook|] をクリックして、今すぐ参加！

FAQ
============

1. 対応システムについて
-------------------------------

Raspberry Pi 5 でのテストに合格したシステム：

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. 電源ボタンについて
--------------------------

電源ボタンは Raspberry Pi 5 の電源ボタンを外に引き出すもので、Raspberry Pi 5 の電源ボタンと同じように動作します。

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **シャットダウン**

  * Raspberry Pi **Raspberry Pi OS Desktop** システムを使用している場合、電源ボタンを素早く 2 回押すとシャットダウンできます。
  * Raspberry Pi **Raspberry Pi OS Lite** システムを使用している場合、電源ボタンを 1 回押すとシャットダウンが開始されます。
  * 強制シャットダウンを行うには、電源ボタンを長押しします。

* **起動**

  * Raspberry Pi ボードがシャットダウンしていても電源が供給されている場合、電源ボタンを 1 回押すことで再び起動できます。

* シャットダウンボタンをサポートしていないシステムを使用している場合は、ボタンを 5 秒間長押しすることで強制的に電源を切り、1 回押すと再び電源が入ります。

3. Raspberry Pi AI HAT+ について
----------------------------------------------------------

Raspberry Pi AI HAT+ は Pironman 5 と互換性がありません。

   .. image::  img/output3.png
        :width: 400

Raspberry Pi AI Kit は、Raspberry Pi M.2 HAT+ と Hailo AI アクセラレータモジュールの組み合わせです。

   .. image::  img/output2.jpg
        :width: 400

Hailo AI アクセラレータモジュールは Raspberry Pi AI Kit から取り外し、Pironman 5 MAX の NVMe PIP モジュールに直接装着できます。

4. タワークーラーの銅パイプの端について
----------------------------------------------------------

タワークーラー上部の U 字型のヒートパイプは、銅パイプをアルミフィンに通すために押しつぶされた状態になっています。これは銅パイプの製造工程上、正常な仕様です。

   .. image::  img/tower_cooler1.png

5. PI5 が起動しない（赤色 LED）？
-------------------------------------------

この問題は、システムアップデート、ブート順の変更、またはブートローダーの破損が原因で発生することがあります。以下の手順をお試しください。

#. USB-HDMI アダプターの接続を確認

   * USB-HDMI アダプターが PI5 に正しく接続されているか慎重に確認してください。
   * USB-HDMI アダプターを一度外してから再接続してください。
   * その後、電源を再接続し、PI5 が正常に起動するか確認します。

#. ケースの外で PI5 をテスト

   * アダプターの再接続で問題が解決しない場合：
   * PI5 を Pironman 5 ケースから取り外します。
   * ケースを使わずに電源アダプターで直接 PI5 に給電します。
   * 正常に起動するか確認します。

#. ブートローダーを復元

   * それでも起動しない場合、ブートローダーが破損している可能性があります。:ref:`update_bootloader_max` のガイドに従い、SD カードまたは NVMe/USB からの起動を選択してください。
   * 準備した SD カードを PI5 に挿入し、電源を入れて少なくとも 10 秒待ちます。リカバリー完了後、SD カードを取り外して再フォーマットします。
   * Raspberry Pi Imager を使用して最新の Raspberry Pi OS を書き込み、再度挿入して起動を試みます。

6. OLED 画面が表示されない？
------------------------------

.. note:: OLED 画面は、一定時間操作がないと自動的にオフになり、省電力モードに入ります。ケースを軽く叩いて振動センサーを作動させることで画面を再点灯できます。

OLED 画面が何も表示しない、または誤表示する場合は、以下の手順でトラブルシューティングしてください。

1. **OLED 画面の接続を確認**

   FPC ケーブルが正しく接続されているか確認してください。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Oled-11.mp4" type="video/mp4">
               お使いのブラウザは video タグをサポートしていません。
           </video>
       </div>

2. **OS の互換性を確認**

   使用中の OS が対応システムであることを確認してください。

3. **I2C アドレスを確認**

   以下のコマンドで OLED の I2C アドレス（0x3C）が認識されているか確認します：

   .. code-block:: shell

      sudo i2cdetect -y 1

   認識されない場合は、次のコマンドで I2C を有効化します：

   .. code-block:: shell

      sudo raspi-config

4. **pironman5 サービスの再起動**

   `pironman5` サービスを再起動して、問題が解決するか確認します：

   .. code-block:: shell

      sudo systemctl restart pironman5.service

5. **ログファイルの確認**

   問題が続く場合はログファイルを確認し、サポートに連絡してください：

   .. code-block:: shell

      cat /var/log/pironman5/pm_auto.oled.log

7. NVMe PIP モジュールが動作しない？
---------------------------------------

1. NVMe PIP モジュールと Raspberry Pi 5 を接続する FPC ケーブルが正しく接続されているか確認してください。  

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(1)-11.mp4" type="video/mp4">
               お使いのブラウザは video タグをサポートしていません。
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(2)-11.mp4" type="video/mp4">
               お使いのブラウザは video タグをサポートしていません。
           </video>
       </div>

2. SSD が NVMe PIP モジュールに正しく装着されていることを確認してください。  

3. NVMe PIP モジュールの LED 状態を確認します：

   すべての接続が完了したら、Pironman 5 MAX の電源を入れ、モジュール上の 2 つのインジケーターを確認します：  

   * **PWR-LED**：点灯している必要があります。  
   * **STA-LED**：点滅していると正常動作を示します。  

   .. image:: img/dual_nvme_pip_leds.png  

   * **PWR-LED** が点灯し STA-LED が点滅しない場合は、NVMe SSD が Raspberry Pi に認識されていないことを意味します。  
   * **PWR-LED** が消灯している場合は「Force Enable」ピンをショートし、再度確認します。それでも点灯しない場合は、ケーブルの緩みまたは非対応 OS の可能性があります。

   .. image:: img/dual_nvme_pip_j4.png  

4. NVMe SSD に OS が正しくインストールされていることを確認してください。:ref:`max_install_the_os` を参照。

5. 配線や OS に問題がないのに起動しない場合は、一度 Micro SD カードから起動して他のコンポーネントが正常に動作するか確認し、その後 :ref:`max_configure_boot_ssd` に進んでください。

それでも解決しない場合は、service@sunfounder.com までご連絡ください。

8. RGB LED が点灯しない？
--------------------------

#. J9 上部の IO エクスパンダーの 2 ピンは、GPIO10 に RGB LED を接続するためのものです。ジャンパキャップが正しく取り付けられているか確認してください。

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Raspberry Pi が対応する OS を実行していることを確認してください。Pironman 5 は以下の OS のみをサポートします。

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   非対応の OS を使用している場合は、:ref:`install_the_os` に従い、対応 OS をインストールしてください。

#. ``sudo raspi-config`` コマンドを実行し、**3 Interfacing Options** -> **I3 SPI** -> **YES** を選択して SPI を有効にし、OK および Finish をクリックします。SPI 有効化後、Pironman 5 を再起動してください。

それでも解決しない場合は、service@sunfounder.com までご連絡ください。

9. CPU ファンが回らない？
----------------------------------------------

CPU 温度が設定された閾値に達していない場合、CPU ファンは動作しません。

**温度に応じたファン回転制御**  

PWM ファンは Raspberry Pi 5 の温度に応じて自動で速度を調整します：  

* **50°C 未満**：停止（0％ 回転）  
* **50°C**：低速（30％）  
* **60°C**：中速（50％）  
* **67.5°C**：高速（70％）  
* **75°C 以上**：最大速度（100％）  

詳細は :ref:`fan_max` を参照してください。

10. OLED 画面を再点灯する方法
---------------------------------------------------------------------------------

省電力と寿命延長のため、一定時間操作がないと OLED 画面は自動的にオフになります。これは正常な仕様であり、製品の機能には影響しません。

ケースを軽く叩くことで振動センサーが反応し、画面が再び点灯します。

.. note::

   OLED 画面の設定（オン/オフ、スリープ時間、回転など）については :ref:`max_view_control_dashboard` または :ref:`max_view_control_commands` を参照してください。


11. Web ダッシュボードを無効にする方法
------------------------------------------------------

``pironman5`` モジュールのインストールが完了すると、:ref:`max_view_control_dashboard` にアクセスできるようになります。

もしこの機能が不要で、CPU および RAM の使用量を削減したい場合は、``pironman5`` のインストール時に ``--disable-dashboard`` フラグを追加することで、ダッシュボードを無効にすることができます。

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

すでに ``pironman5`` をインストール済みの場合は、``dashboard`` モジュールと ``influxdb`` を削除し、pironman5 を再起動して変更を適用してください。

.. code-block:: shell

   /opt/pironman5/venv/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5


12. ``pironman5`` コマンドでコンポーネントを制御する方法
----------------------------------------------------------------------

``pironman5`` コマンドを使用して Pironman 5 MAX のコンポーネントを制御するチュートリアルについては、以下を参照してください。

* :ref:`max_view_control_commands`


13. コマンドで Raspberry Pi の起動順序を変更する方法
-------------------------------------------------------------

Raspberry Pi にログイン済みであれば、コマンドを使って起動順序を変更することができます。詳細な手順は以下を参照してください。

* :ref:`max_configure_boot_ssd`


14. Raspberry Pi Imager で起動順序を変更する方法
---------------------------------------------------------------

EEPROM 設定で ``BOOT_ORDER`` を変更するだけでなく、**Raspberry Pi Imager** を使用して Raspberry Pi の起動順序を変更することも可能です。

この作業では、予備のカードを使用することを推奨します。

* :ref:`update_bootloader_max`


15. SD カードから NVMe SSD にシステムをコピーする方法
-------------------------------------------------------------

NVMe SSD を持っているが、PC に接続するためのアダプターがない場合、まず Micro SD カードにシステムをインストールしてください。  
Pironman 5 MAX が正常に起動したら、Micro SD カードから NVMe SSD へシステムをコピーできます。詳細な手順は以下を参照してください。

* :ref:`max_copy_sd_to_nvme_rpi`


16. アクリルプレートの保護フィルムを剥がす方法
-----------------------------------------------------------------

パッケージには 2 枚のアクリルパネルが含まれており、両面に黄色または透明の保護フィルムが貼られています。  
このフィルムは傷防止用で、少し剥がしにくい場合があります。ドライバーなどで角を軽くこすり、端からゆっくりと剥がしてください。

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center


.. _max_openssh_powershell:

17. Powershell で OpenSSH をインストールする方法
--------------------------------------------------

``ssh <username>@<hostname>.local`` （または ``ssh <username>@<IP address>``）を使用して Raspberry Pi に接続しようとしたとき、以下のようなエラーメッセージが表示される場合があります。

.. code-block::

    ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
    spelling of the name, or if a path was included, verify that the path is correct and try again.

これは、お使いの Windows システムが古く、`OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ が事前インストールされていないことを意味します。以下の手順で手動インストールしてください。

#. Windows デスクトップの検索ボックスに ``powershell`` と入力し、``Windows PowerShell`` を右クリックして、「管理者として実行」を選択します。

   .. image:: img/powershell_ssh.png
      :width: 90%

#. 次のコマンドで ``OpenSSH.Client`` をインストールします。

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. インストール後、次のような出力が表示されます。

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 次のコマンドでインストールを確認します。

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. 以下のように表示されれば、``OpenSSH.Client`` が正常にインストールされています。

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        上記の表示が出ない場合は、Windows システムがさらに古いため、|link_putty| のようなサードパーティの SSH ツールを使用することを推奨します。

#. PowerShell を再起動し、再び管理者として実行してください。この時点で、``ssh`` コマンドで Raspberry Pi にログインでき、事前に設定したパスワードの入力を求められます。

   .. image:: img/powershell_login.png


18. OMV を設定した場合でも Pironman5 の機能は使用できますか？
--------------------------------------------------------------------------------------------------------

はい。OpenMediaVault は Raspberry Pi システム上で動作します。:ref:`max_set_up_pi_os` の手順に従って設定を続行してください。
