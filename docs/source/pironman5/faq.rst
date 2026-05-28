.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

FAQ
============


クイックトラブルシューティング
-------------------------------

* OLEDスクリーンが動作しない → :ref:`faq_oled_5`
* RGB LEDが動作しない → :ref:`faq_rgb_5`
* GPIOファンが動作しない → :ref:`faq_gpio_fans_5`
* CPUファンが回らない → :ref:`faq_pwm_fan_5`
* ダッシュボードにデータが表示されない → :ref:`faq_dashboard_5`
* NVMe SSDが認識されない → :ref:`faq_nvme_5`



1. ハードウェア
-------------------------------


.. _compatible_systems_5:

対応システム
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_com_os

Raspberry Pi 5でテスト済みの対応システム：

.. image:: img/compitable_os.png
   :width: 600
   :align: center

.. end_faq_com_os

電源ボタン
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_5`

.. start_faq_power_button

電源ボタンは、Raspberry Pi 5の電源ボタンを外部に引き出したもので、同じように動作します。

* 短く押す: 電源オン / OLED起動 / OLEDページ切り替え。
* 2秒間長押し: 安全なシャットダウン（|link_safe_shutdown| が必要です）。
* 5秒間長押し: 強制シャットダウン。

.. image:: img/power_button.jpg
    :width: 400
    :align: center

.. end_faq_power_button


エアフローの方向
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_airflow_direction

Pironman 5内のエアフローは、冷却効率を最大化するように設計されています。冷たい空気はGPIO開口部やその他の通気口から入り、タワークーラーを通過し、2つの側面GPIOファンから排出されます。

詳細なデモについては、以下のビデオを参照してください：

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="../_static/video/airflow_direction.mp4"  type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>

.. end_faq_airflow_direction


タワークーラーの銅管端部
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_copper_pipe_ends

U字型の銅製ヒートパイプの平らになった端部は、通常の製造工程の一部であり、ヒートパイプがアルミフィンを通過できるようにするためのものです。

.. image:: img/tower_cooler1.png

.. end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_ai_hat

Raspberry Pi AI HAT+はPironman 5に対応していません。

.. image:: img/output3.png
    :width: 400

Raspberry Pi AI Kitは、Raspberry Pi M.2 HAT+とHailo AIアクセラレータモジュールを組み合わせたものです。

.. image:: img/output2.jpg
    :width: 400

Hailo AIアクセラレータモジュールをRaspberry Pi AI Kitから取り外し、Pironman 5のNVMe PIPモジュールに直接挿入することができます。

.. image:: img/output4.png
    :width: 800

.. end_faq_ai_hat



2. 冷却とファン
-------------------------------


.. _faq_pwm_fan_5:

CPUファンが動作しない
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_pwm_fan

Pironman 5のCPUファンはRaspberry Piシステムによって制御されています。CPUファンの速度はRaspberry Pi 5のCPU温度に依存します。

デフォルトのCPUファンカーブ：

* < 50°C: オフ（0%）
* 50°C以上: 低速（30%）
* 60°C以上: 中速（50%）
* 67.5°C以上: 高速（70%）
* 75°C以上: 全速（100%）

現在のCPU温度を確認します（出力例： ``temp=48.7'C``）：

.. code-block:: shell

   vcgencmd measure_temp

以下のコマンドを使用してCPUファンを手動で制御できます：

.. code-block:: shell

   pinctrl FAN_PWM op dl   # ファンを有効にする（Low Active）
   pinctrl FAN_PWM op dh   # ファンを無効にする（High Active）
   pinctrl FAN_PWM a0      # 自動モード

以下のファイルを編集して、CPUファンの温度しきい値を調整することもできます：

.. code-block:: shell

   nano /boot/firmware/config.txt

以下を追加します：

.. code-block:: text

   dtparam=cooling_fan=on
   dtparam=fan_temp0=40000
   dtparam=fan_temp0_hyst=10000
   dtparam=fan_temp0_speed=125

この設定により、CPUファンが40°CでPWM速度レベル125で起動します。

ファイルを保存した後、Raspberry Piを再起動して変更を反映させます。

.. end_faq_pwm_fan


.. _faq_gpio_fans_5:

GPIOファンが動作しない
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_gpio_fans

まず、IOエクスパンダーボードのFANジャンパーキャップが正しく取り付けられているか確認してください。

.. image:: hardware/img/io_board_fan_j9.png

次に、GPIOファンを ``Always On`` モードに設定し、ファンが回転を開始するか確認します。

.. code-block:: shell

   sudo pironman5 -gm 0

GPIOファンをRaspberry Piの ``5V`` と ``GND`` ピンに直接接続してテストすることもできます。

直接接続した場合にファンが正常に回転する場合、問題はIOエクスパンダーボードに関連している可能性があります。サポートについてはお問い合わせください。

問題が解決しない場合は、ダッシュボードの **ログ** ページを開き、エラーメッセージを確認してください。以下のログファイルを送信することもできます：

.. code-block:: shell

   cat /var/log/pironman5/pironman5.log

.. end_faq_gpio_fans

3. OLEDとRGB
-------------------------------


.. _faq_oled_5:

OLEDスクリーンが動作しない
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_set_up_pironman5| replace:: :ref:`set_up_pironman5_5`
.. |link_compatible_systems| replace:: :ref:`compatible_systems_5`

.. start_faq_oled

OLEDスクリーンが表示されない、または正しく表示されない場合、以下のトラブルシューティング手順を試してください：

#. OLEDスクリーンのFPCケーブルが確実に接続されていることを確認してください。OLEDを再接続してからデバイスの電源を入れることをお勧めします。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_oled_screen.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. Raspberry Piがサポートされているオペレーティングシステムを実行していることを確認してください。

   |link_compatible_systems| を参照してください。

#. OLEDスクリーンの初回電源投入時は、ピクセルブロックのみが表示される場合があります。|link_set_up_pironman5| の手順に従って設定を完了すると、正しい情報が表示されるようになります。

#. 以下のコマンドを使用して、OLEDのI2Cアドレス ``0x3C`` が検出されているか確認してください：

   .. code-block:: shell

      sudo i2cdetect -y 1

   * I2Cアドレス ``0x3C`` が検出された場合、Pironman 5サービスを再起動します：

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * アドレスが検出されない場合、I2Cを有効にします：

     .. code-block:: shell

        sudo nano /boot/firmware/config.txt

     以下を追加します：

     .. code-block:: shell

        dtparam=i2c_arm=on

     ファイルを保存し、Raspberry Piを再起動します。

#. 問題が解決しない場合は、以下のログファイルを送信してください：

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_oled


.. _faq_rgb_5:

RGB LEDが動作しない
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. start_faq_rgb

#. J9上のIOエクスパンダーにある2つのピンは、RGB LEDをGPIO10に接続するために使用されます。これらのピンにジャンパーキャップが正しく取り付けられていることを確認してください。

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Raspberry Piがサポートされているオペレーティングシステムを実行していることを確認してください。

   |link_compatible_systems| を参照してください。

#. 以下のコマンドを実行してSPIを有効にします：

   .. code-block:: shell

      sudo raspi-config

   ``3 Interfacing Options`` → ``I3 SPI`` → ``YES`` に移動します。

   その後、Raspberry Piを再起動します。

#. 問題が解決しない場合は、以下のログファイルを送信してください：

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_rgb

.. _faq_customize_oled_5:

OLED表示をカスタマイズする方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_customize_oled

OLED表示をカスタマイズしたい場合（カスタム2〜4桁の画像表示の追加など）、以下のいずれかの方法でOLEDページファイルを変更できます。

* **方法1: インストール済みファイルを直接変更する**

  #. OLEDページファイルを一覧表示します：

     .. code-block:: shell

        ls /opt/pironman5/venv/lib/python3.13/site-packages/pm_auto/addons/oled/pages/

  #. 目的のPythonファイルを変更します。

  #. サービスを再起動して変更を反映します：

     .. code-block:: shell

        sudo systemctl restart pironman5.service


* **方法2: ``pm_auto`` をクローンして再インストールする**

  #. ``pm_auto`` リポジトリをクローンします：

     .. code-block:: shell

        git clone -b 1.4.x https://github.com/sunfounder/pm_auto/

  #. 変更後、変更したパッケージを再インストールします：

     .. code-block:: shell

        sudo /opt/pironman5/venv/bin/pip3 uninstall pm_auto -y && \
        sudo /opt/pironman5/venv/bin/pip3 install ~/pm_auto --no-build-isolation && \
        sudo chown -R pironman5:pironman5 /opt/pironman5

  #. サービスを再起動します：

     .. code-block:: shell

        sudo systemctl restart pironman5.service

* **テストとデバッグ**

  実行時のログを表示するには：

  .. code-block:: shell

     journalctl -xefu pironman5.service

  サービスを停止して手動で実行し、より迅速にテストすることもできます：

  .. code-block:: shell

     sudo systemctl stop pironman5.service
     sudo systemctl restart pironman5.service

.. end_faq_customize_oled

4. ダッシュボードとソフトウェア
-------------------------------


.. _faq_dashboard_5:

ダッシュボードにデータが表示されない
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_dashboard

ダッシュボードにデータが表示されない場合、まずダッシュボードの **ログ** ページを開き、 ``influxdb`` に関連するエラーメッセージがないか確認してください。

よくあるエラー：

* ``database not found``
* ``failed to connect to influxdb``
* ``connection refused``
* ``timeout``

以下の手順で問題を解決できる場合があります。

#. ブラウザのキャッシュをクリアするか、 **シークレット/プライベート** モードでダッシュボードページを再度開いてください。

#. 以下のサービスが正常に実行されているか確認してください：

   .. code-block:: shell

      sudo systemctl status pironman5 --no-pager
      sudo systemctl status influxdb --no-pager

   両方のサービスに次のように表示される必要があります：

   .. code-block:: text

      active (running)

#. いずれかのサービスが正常に実行されていない場合、再起動します：

   .. code-block:: shell

      sudo systemctl restart influxdb
      sudo systemctl restart pironman5

   その後、約30秒待ってからダッシュボードページを更新してください。

#. ``pironman5`` データベースが存在するか確認します：

   .. code-block:: shell

      influx

   次に実行します：

   .. code-block:: text

      SHOW DATABASES;

   次のように表示される必要があります：

   .. code-block:: text

      pironman5
      _internal

#. データベースがないか破損している場合、ダッシュボードから履歴データをクリアしてみてください：

   ``Settings → Clear All Data``

#. 上記のすべての手順を試しても問題が解決しない場合は、Raspberry Pi OSとPironman 5ソフトウェアの再インストールを推奨します。

.. end_faq_dashboard


Webダッシュボードを無効化する方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard_5`

.. start_faq_disable_dashboard

``pironman5`` モジュールのインストールが完了すると、|link_view_control_dashboard| にアクセスできるようになります。

この機能が不要で、CPUやRAMの使用量を削減したい場合は、インストール時に ``--disable-dashboard`` フラグを追加することでダッシュボードを無効にできます。

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

すでに ``pironman5`` をインストール済みの場合は、ダッシュボードモジュールと ``influxdb`` を削除できます：

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

.. end_faq_disable_dashboard


Pironman 5ソフトウェアのアンインストールと再インストール方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_reinstall_pironman5

#. 現在の ``pironman5`` ソフトウェアをアンインストールします：

   .. code-block:: shell

      cd ~/pironman5
      sudo python3 install.py --uninstall

#. 指示に従ってRaspberry Piを再起動し、その後 ``pironman5`` ディレクトリを削除します：

   .. code-block:: shell

      cd ~/
      sudo rm -rf pironman5

#. 以下のコマンドを実行して、お使いのPironman 5モデル用のソフトウェアを再インストールします：

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash

.. end_faq_reinstall_pironman5


``pironman5`` コマンドを使用してコンポーネントを制御する方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_commands| replace:: :ref:`view_control_commands_5`

.. start_faq_pironman5_command

以下のチュートリアルを参照して、 ``pironman5`` コマンドを使用してPironman 5シリーズのコンポーネントを制御できます。

* |link_view_control_commands|

.. end_faq_pironman5_command



5. 起動とストレージ
-------------------------------


PI5が起動しない（赤色LED）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_update_bootloader| replace:: :ref:`update_bootloader_5`

.. start_faq_pi5_boot_fail

この問題は、システムのアップデート、ブート順序の変更、またはブートローダーの破損が原因で発生する可能性があります。以下の手順を試して問題を解決してください：

#. USB-HDMIアダプターの接続を確認

   * USB-HDMIアダプターがPI5にしっかりと接続されているか慎重に確認してください。
   * USB-HDMIアダプターを一度抜き、再度接続してみてください。
   * その後、電源を再接続し、PI5が正常に起動するか確認してください。

#. ケース外でPI5をテスト

   * アダプターの再接続で問題が解決しない場合：
   * PI5をPironman 5シリーズのケースから取り外してください。
   * 電源アダプターでPI5に直接給電してください（ケースなし）。
   * 正常に起動できるか確認してください。

#. ブートローダーを復元

   * それでもPI5が起動しない場合、ブートローダーが破損している可能性があります。|link_update_bootloader| のガイドに従い、SDカードまたはNVMe/USBからの起動を選択してください。
   * 準備したSDカードをPI5に挿入し、電源を入れて少なくとも10秒待ちます。リカバリーが完了したら、SDカードを取り外して再フォーマットしてください。
   * その後、Raspberry Pi Imagerを使用して最新のRaspberry Pi OSを書き込み、再度起動を試みてください。

.. end_faq_pi5_boot_fail


.. _faq_nvme_5:

NVMe PIPモジュールが動作しない
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_install_the_os| replace:: :ref:`install_the_os_5`
.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_5`

.. start_faq_nvme_pip

#. NVMe PIPモジュールとRaspberry Pi 5を接続しているFPCケーブルがしっかりと取り付けられていることを確認してください。

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

#. SSDがNVMe PIPモジュールに正しく固定されていることを確認してください。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_ssd.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. NVMe PIPモジュールのLED状態を確認します：

   * **PWR LED**: 点灯している必要があります。
   * **STA LED**: 正常動作時に点滅します。

   .. image:: img/nvme_pip_leds.png

   * **PWR LED** が点灯していても **STA LED** が点滅しない場合、NVMe SSDが認識されていません。
   * **PWR LED** が消灯している場合、 ``Force Enable`` ピン（J4）をショートしてください。

     .. image:: img/nvme_pip_j4.png

#. NVMe SSDに有効なオペレーティングシステムが含まれていることを確認してください。

   |link_install_the_os| を参照してください。

#. SSDがまだ起動しない場合、最初にMicro SDカードから起動し、NVMeブートを設定してください：

   * |link_configure_boot_ssd|

#. 問題が解決しない場合は、以下のログファイルを送信してください：

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_nvme_pip


コマンドを使用してRaspberry Piのブート順序を変更する方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_boot_order_command

Raspberry Piにログイン済みの場合、コマンドを使用してブート順序を変更できます。

* |link_configure_boot_ssd|

.. end_faq_boot_order_command


Raspberry Pi Imagerを使用してブート順序を変更する方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_boot_order_imager

EEPROM設定の ``BOOT_ORDER`` を変更する以外にも、 **Raspberry Pi Imager** を使用してブート順序を変更できます。

* |link_update_bootloader|

.. end_faq_boot_order_imager


システムをSDカードからNVMe SSDにコピーする方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_5`

.. start_faq_copy_sd_to_nvme

NVMe-USBアダプターがない場合、まずMicro SDカードにシステムをインストールし、正常に起動した後、システムをNVMe SSDにコピーできます。

* |link_copy_sd_to_nvme|

.. end_faq_copy_sd_to_nvme



6. 高度な使用方法
-------------------------------


保護フィルムの剥がし方
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_remove_film

パッケージには2枚のアクリル板が含まれており、両面に黄色または透明の保護フィルムが貼られていて、傷を防ぎます。

保護フィルムは剥がしにくい場合があります。ドライバーを使用して角を持ち上げ、慎重に全体を剥がしてください。

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. end_faq_remove_film
