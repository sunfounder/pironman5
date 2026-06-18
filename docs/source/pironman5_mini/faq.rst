.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



FAQ
============


Quick Troubleshooting
-------------------------------

* 電源ボタンが動作しない → :ref:`faq_power_button_not_work_mini`
* RGB LED が点灯しない → :ref:`faq_rgb_mini`
* CPU ファンが回らない → :ref:`faq_pwm_fan_mini`
* ダッシュボードにデータが表示されない → :ref:`faq_dashboard_mini`
* PI5 が起動しない → :ref:`faq_pi5_boot_fail_mini`



1. Hardware
-------------------------------


.. _com_os_mini:

Compatible Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os


Power Button
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

電源ボタンは Raspberry Pi 5 の電源ボタンを引き出したもので、Raspberry Pi 5 の電源ボタンと同様に機能します。

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **シャットダウン**

  * **Raspberry Pi OS Desktop** システムを実行している場合は、電源ボタンを素早く2回押すとシャットダウンします。
  * **Raspberry Pi OS Lite** システムを実行している場合は、電源ボタンを1回押すとシャットダウンが開始されます。
  * 強制的なハードシャットダウンを行うには、電源ボタンを長押しします。

* **電源オン**

  * Raspberry Pi ボードがシャットダウンしているが電源が供給されている場合、ボタンを1回押すとシャットダウン状態から起動します。

* シャットダウンボタンに対応していないシステムを実行している場合は、5秒間長押しすると強制的にハードシャットダウンし、シャットダウン状態から1回押すと電源が入ります。


.. _faq_power_button_not_work_mini:

Power Button Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button_not_work
   :end-before: end_faq_power_button_not_work


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Raspberry Pi AI HAT+ は Pironman 5 と互換性がありません。

   .. image::  img/output3.png
        :width: 400

Raspberry Pi AI Kit は、Raspberry Pi M.2 HAT+ と Hailo AI アクセラレータモジュールで構成されています。

   .. image::  img/output2.jpg
        :width: 400

Hailo AI アクセラレータモジュールは Raspberry Pi AI Kit から取り外し、Pironman 5 Mini の HAT に直接装着することができます。


Micro HDMI Cable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Raspberry Pi 公式の Micro HDMI ケーブルの使用をお勧めします。コネクタ部の長さが 65mm 未満のサードパーティ製ケーブルは、接触不良や表示の問題を引き起こす可能性があります。

.. image:: img/need_mini_hdmi.png
   :width: 400



2. Cooling and Fans
-------------------------------


.. _faq_pwm_fan_mini:

CPU Fan Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan



3. RGB
-------------------------------


.. |link_compatible_systems| replace:: :ref:`com_os_mini`

.. _faq_rgb_mini:

RGB LEDs Not Working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb



4. Dashboard and Software
-------------------------------


.. _faq_dashboard_mini:

The Dashboard Shows No Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard


.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard_mini`

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


.. |link_view_control_commands| replace:: :ref:`view_control_commands_mini`

How to Control Components Using the ``pironman5`` Command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command



5. Boot and Storage
-------------------------------


.. |link_update_bootloader| replace:: :ref:`update_bootloader_mini`

.. _faq_pi5_boot_fail_mini:

PI5 Fails to Boot (Red LED)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

この問題は、システムのアップデート、ブート順序の変更、またはブートローダーの破損によって発生する可能性があります。以下の手順を試して問題を解決してください：

#. 電源を再接続し、PI5 が正常に起動するか確認します。

#. ケースの外で PI5 をテスト

   * PI5 を Pironman 5 Mini ケースから取り外します。
   * 電源アダプターを PI5 に直接接続します（ケースを介さずに）。
   * 正常に起動できるか確認します。

#. ブートローダーの復元

   * PI5 がまだ起動できない場合、ブートローダーが破損している可能性があります。:ref:`update_bootloader_mini` のガイドに従い、SD カードまたは NVMe/USB からの起動を選択してください。
   * 準備した SD カードを PI5 に挿入し、電源を入れて少なくとも 10 秒待ちます。リカバリーが完了したら SD カードを取り外し、再フォーマットしてください。
   * その後、Raspberry Pi Imager を使用して最新の Raspberry Pi OS を書き込み、再起動を試みてください。


.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_mini`

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


.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_mini`

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


.. _openssh_powershell_mini:

How to Install OpenSSH via Powershell?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``ssh <username>@<hostname>.local`` （または ``ssh <username>@<IP address>``）を使用して Raspberry Pi に接続しようとすると、以下のエラーメッセージが表示される場合があります。

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


これは、お使いのコンピューターシステムが古く、`OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ がプリインストールされていないことを意味します。以下の手順で手動インストールを行ってください。

#. Windows の検索ボックスに「 ``powershell`` 」と入力し、 ``Windows PowerShell`` を右クリックして「 ``Run as administrator`` 」を選択します。

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
