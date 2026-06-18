.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



FAQ
============


Quick Troubleshooting
-------------------------------

* 電源ボタンが動作しない → :ref:`faq_power_button_not_work_promax`
* OLED 画面が動作しない → :ref:`faq_oled_promax`
* RGB LED が点灯しない → :ref:`faq_rgb_promax`
* ファンが動作しない → :ref:`promax_fan_faq`
* ダッシュボードにデータが表示されない → :ref:`faq_dashboard_promax`
* NVMe SSD が認識されない → :ref:`faq_nvme_promax`
* NVMe SSD が認識されるがシステムが再起動する → :ref:`faq_nvme_link_down_promax`
* PI5 が起動しない → :ref:`faq_pi5_boot_fail_promax`



1. Hardware
-------------------------------


.. _com_os_promax:

Compatible Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os


.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_promax`

Power Button
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button
   :end-before: end_faq_power_button


.. _faq_power_button_not_work_promax:

Power Button Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button_not_work
   :end-before: end_faq_power_button_not_work


Copper Pipe Ends on the Tower Cooler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copper_pipe_ends
   :end-before: end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Raspberry Pi AI HAT+ は Pironman 5 Pro MAX と互換性がありません。

.. image:: img/output3.png
    :width: 400

Raspberry Pi AI Kit は、Raspberry Pi M.2 HAT+ と Hailo AI アクセラレータモジュールを組み合わせたものです。

.. image:: img/output2.jpg
    :width: 400

Raspberry Pi AI Kit から Hailo AI アクセラレータモジュールを取り外し、Pironman 5 Pro MAX の NVMe PIP モジュールに直接挿入できます。


4.3-Inch Screen Is Black / Not Displaying?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

4.3インチ DSI スクリーンはプラグアンドプレイで、追加のドライバーインストールは必要ありません。

.. note::

   HDMI/USB ボードの **ON/AUTO** ジャンパーは、スピーカーのオーディオ出力のみを制御します。画面表示には **影響しません**。

画面が黒いまま、または表示されない場合は、以下を確認してください：

#. DSI リボンケーブルが Raspberry Pi 5 の正しい DSI ポートに接続されていることを確認します。

#. リボンケーブルが完全に挿入されているか、クランプがしっかりと押さえられているか、接点が正しい方向を向いているかを確認します。

#. 以下のコマンドを実行して、システムが DSI スクリーンを認識しているか確認します：

   .. code-block:: shell

      sudo dmesg | grep -i dsi

   スクリーンが認識されている場合、``DSI display found`` のような出力が表示されます。出力がない場合は、スクリーンが認識されていません — 物理的な接続を再確認してください。


External HDMI Screen — Taskbar Only Appears on the 4.3-Inch Screen?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pironman 5 Pro MAX に外部 HDMI モニターを接続すると、デスクトップのタスクバーが外部ディスプレイではなく、内蔵の 4.3インチ DSI スクリーンに表示される場合があります。これは、システムがデフォルトで DSI スクリーンをプライマリディスプレイとして設定しているためです。

起動時に HDMI モニターをプライマリ画面として設定するには：

#. 起動スクリプトを作成します：

   .. code-block:: shell

      sudo nano /usr/local/bin/fix-primary-screen.sh

#. スクリプトに以下の内容を追加します：

   .. code-block:: bash

      #!/bin/bash
      # Check if an external HDMI monitor is connected
      if wlr-randr | grep -q "HDMI-A-1"; then
          # Turn off the DSI screen first
          wlr-randr --output DSI-1 --off
          sleep 2
          # Re-enable DSI and place it to the right of HDMI
          wlr-randr --output DSI-1 --on --right-of HDMI-A-1
      fi

#. スクリプトを実行可能にします：

   .. code-block:: shell

      sudo chmod +x /usr/local/bin/fix-primary-screen.sh

#. スクリプトを自動起動に追加します。labwc の自動起動ファイルを編集します：

   .. code-block:: shell

      nano ~/.config/labwc/autostart

   以下の行を追加します（ ``&`` でバックグラウンド実行）：

   .. code-block:: text

      /usr/local/bin/fix-primary-screen.sh &


2. Cooling and Fans
-------------------------------


.. _promax_fan_faq:

Fan Not Working / Cannot Be Controlled?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pro MAX は公式の Raspberry Pi PWM ファン制御ソリューションを採用しています。3 つの冷却ファンはすべて Raspberry Pi システムによって直接制御されており、pironman5 サービスに依存していません（そのため、コマンドラインツールやダッシュボードにはファン制御オプションは表示されません）。

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan


Dashboard Does Not Show Fan Speed?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pro MAX はカスタムの **5ピン** ファンを使用しており、ピン配置は以下の通りです：**PWM / 5V / GND / RGB Data In / RGB Data Out**

これらのファンには **タコメーター（速度フィードバック）ピンがありません** ので、システムは実際の RPM を読み取ることができません。ダッシュボードにファン速度が表示されないのは正常であり、仕様です。

ファン速度は Raspberry Pi のネイティブ PWM 温度カーブによって制御されます：

* < 50°C: オフ（0%）
* 50°C 以上: 低速（30%）
* 60°C 以上: 中速（50%）
* 67.5°C 以上: 高速（70%）
* 75°C 以上: 全速（100%）



3. OLED and RGB
-------------------------------


.. _faq_oled_promax:

OLED Screen Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_set_up_pironman5| replace:: :ref:`promax_set_up_pi_os`
.. |link_compatible_systems| replace:: :ref:`com_os_promax`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_oled
   :end-before: end_faq_oled


.. _faq_customize_oled_promax:

How to Customize the OLED Display?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_customize_oled
   :end-before: end_faq_customize_oled


.. _faq_rgb_promax:

RGB LEDs Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb


How to Wake Up the OLED Screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

省電力と画面の寿命を延ばすため、OLED 画面は一定時間操作がないと自動的にオフになります。これは通常の設計であり、製品の機能に影響を与えるものではありません。

.. note::

   OLED 画面の設定（オン/オフ、スリープ時間、回転など）については、:ref:`promax_view_control_dashboard` または :ref:`promax_view_control_commands` を参照してください。



4. Dashboard and Software
-------------------------------


.. _faq_dashboard_promax:

The Dashboard Shows No Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard


.. |link_view_control_dashboard| replace:: :ref:`promax_view_control_dashboard`

How to Disable the Web Dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_disable_dashboard
   :end-before: end_faq_disable_dashboard


How to Uninstall and Reinstall the Pironman 5 Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_reinstall_pironman5
   :end-before: end_faq_reinstall_pironman5


.. |link_view_control_commands| replace:: :ref:`promax_view_control_commands`

How to Control Components Using the ``pironman5`` Command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command


.. _faq_piper_tts_32bit_promax:

``pip install piper-tts`` Fails with "Could Not Find a Version"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pironman 5 Pro MAX に ``sunfounder-voice-assistant`` をインストールする際、以下のエラーが発生する場合があります：

.. code-block:: text

   ERROR: Could not find a version that satisfies the requirement piper-tts==1.3.0
   ERROR: No matching distribution found for piper-tts==1.3.0

このエラーは、``piper-tts`` 1.3.0 が **64ビット**（``aarch64``）のホイールのみを提供しているために発生します。Raspberry Pi が **32ビット** のオペレーティングシステムを実行している場合、pip は互換性のあるパッケージを見つけることができません。

**解決策：** 64ビット版の Raspberry Pi OS をインストールしてください。

#. 現在のシステムアーキテクチャを確認します：

   .. code-block:: shell

      uname -m

   * ``aarch64`` → 64ビット（問題なし）
   * ``armv7l`` → 32ビット（アップグレードが必要）

#. `Raspberry Pi Imager <https://www.raspberrypi.com/software/>`_ を使用して、ストレージデバイスに **64ビット** の Raspberry Pi OS イメージを書き込みます。

#. 64ビット OS をインストールした後、``pironman5`` ソフトウェアと ``sunfounder-voice-assistant`` を再インストールします。


5. Boot and Storage
-------------------------------


.. |link_update_bootloader| replace:: :ref:`update_bootloader_promax`

.. _faq_pi5_boot_fail_promax:

PI5 Fails to Boot (Red LED)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pi5_boot_fail
   :end-before: end_faq_pi5_boot_fail


.. _faq_nvme_promax:

NVMe PIP Module Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_install_the_os_dual| replace:: :ref:`install_the_os_promax`

.. include:: ../pironman5_max/faq.rst
   :start-after: start_faq_nvme_pip_dual
   :end-before: end_faq_nvme_pip_dual

#. 配線が正しく、OS がインストールされているにもかかわらず NVMe SSD が起動しない場合は、Micro SD カードから起動して他のコンポーネントの機能を確認します。確認後、:ref:`configure_boot_ssd_promax` に進みます。

#. 上記の手順を実行しても問題が解決しない場合は、service@sunfounder.com までメールをお送りください。できるだけ早く対応いたします。


.. _faq_nvme_link_down_promax:

NVMe SSD Detected but Causes System Restart on Read/Write?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_nvme_link_down
   :end-before: end_faq_nvme_link_down


.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_promax`

How to Change the Raspberry Pi Boot Order Using Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_command
   :end-before: end_faq_boot_order_command


How to Modify the Boot Order with Raspberry Pi Imager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_imager
   :end-before: end_faq_boot_order_imager


.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_promax`

How to Copy the System from the SD Card to an NVMe SSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copy_sd_to_nvme
   :end-before: end_faq_copy_sd_to_nvme



6. Advanced Usage
-------------------------------


How to Remove the Protective Film
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_remove_film
   :end-before: end_faq_remove_film


.. _promax_openssh_powershell:

How to Install OpenSSH via Powershell?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``ssh <username>@<hostname>.local`` （または ``ssh <username>@<IP address>``）を使用して Raspberry Pi に接続しようとすると、以下のエラーメッセージが表示される場合があります。

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


これは、お使いのコンピューターシステムが古く、`OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ がプリインストールされていないことを意味します。以下の手順で手動インストールを行ってください。

#. Windows の検索ボックスに 「 ``powershell`` 」と入力し、 ``Windows PowerShell`` を右クリックして「 ``Run as administrator`` 」を選択します。

   .. image:: img/powershell_ssh.png
      :width: 90%


#. 以下のコマンドで ``OpenSSH.Client`` をインストールします。

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. インストール後、以下のような出力が返ってきます。

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 以下のコマンドでインストール状況を確認します。

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. これで ``OpenSSH.Client`` のインストールが正常に完了したことが確認できます。

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        上記の表示がされない場合は、Windows がさらに古いバージョンである可能性があります。|link_putty| などのサードパーティ製 SSH ツールの使用をご検討ください。

#. PowerShell を再起動し、再度管理者権限で起動してください。これで ``ssh`` コマンドによる接続が可能になり、設定したパスワードの入力が求められます。

   .. image:: img/powershell_login.png


If I Set Up OMV, Can I Still Use the Pironman5's Function?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

はい、OpenMediaVault は Raspberry Pi システム上で設定されます。:ref:`promax_set_up_pi_os` の手順に従って設定を続行してください。


Raspberry Pi Camera Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

カメラが動作しない場合、90% の原因はリボンケーブルの接続またはカメラハードウェア自体に関連しています。

まず、``rpicam-hello --list-cameras`` を使用してカメラが認識されているか確認します。正常に認識されている場合、以下のようなメッセージが表示されます：

.. code-block:: bash

   Available cameras
   -----------------
   0 : ov5647 [2592x1944] (/base/axi/pcie@1000120000/rp1/i2c@88000/ov5647@36)

カメラが認識されない場合は、リボンケーブルが逆になっていないか、完全に挿入されていないかを確認します。問題が解決しない場合は、リボンケーブルまたはカメラモジュールを交換してクロステストを試みてください。


Can I Install Home Assistant OS on the Pironman 5 Pro MAX?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pironman 5 Pro MAX には専用の Home Assistant アドオンはありません。ただし、**Pironman 5 MAX** アドオンを代わりに使用できます。`SunFounder アドオンリポジトリガイド <https://docs.sunfounder.com/projects/pironman5/en/latest/pironman5_max/set_up/set_up_home_assistant.html#add-the-sunfounder-add-ons-repository>`_ に従ってください。

以下の制限事項に注意してください：

* **4.3インチ画面**：Home Assistant OS はデスクトップ環境のない **Lite** システムです。Pro MAX に内蔵された 4.3インチ画面は何も表示しません。

* **NVMe PIP デュアル SSD**：Home Assistant OS は Pro MAX のデュアル NVMe PIP モジュール上の両方の NVMe SSD を読み取ることができません。

* **OLED 画面と RGB LED**：アドオンをインストールした後、これらのコンポーネントは追加設定なしで正常に動作します。

* **CPU ファン**：Home Assistant OS で CPU ファンを動作させるには手動設定が必要です。以下を ``/boot/firmware/config.txt`` に追加します：

  .. code-block:: text

     dtparam=cooling_fan=on
     dtparam=fan_temp0=40000
     dtparam=fan_temp0_hyst=10000
     dtparam=fan_temp0_speed=125

  保存して再起動すると、CPU ファンは CPU 温度に基づいて Raspberry Pi システムによって制御されます。``pinctrl`` コマンドで手動制御することもできます。:ref:`promax_fan_faq` を参照してください。
