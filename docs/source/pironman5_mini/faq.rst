.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32の魅力を、同じ情熱を持つ仲間たちと一緒に深く探究しましょう。

    **なぜ参加するのか？**

    - **エキスパートサポート**：購入後のトラブルや技術的な課題も、コミュニティとSunFounderチームのサポートで安心。
    - **学びと共有**：チュートリアルやヒントを共有して、スキルを磨きましょう。
    - **新製品の先行公開**：新製品の先行情報やプレビューをいち早く入手。
    - **Special Discounts**：最新製品の限定割引をご利用いただけます。
    - **Festive Promotions and Giveaways**：季節限定イベントやプレゼント企画にも参加可能！

    👉 一緒にものづくりと探究を楽しみませんか？今すぐ [|link_sf_facebook|] をクリックしてご参加ください！

FAQ
============

1. 対応OSについて
-------------------------------

以下のオペレーティングシステムは、Raspberry Pi 5上で動作確認済みです：

.. image:: img/compitable_os.png
   :width: 600
   :align: center

2. 電源ボタンについて
--------------------------

この電源ボタンは、Raspberry Pi 5本体の電源ボタンと同様に機能します。

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **シャットダウン**

  * Raspberry Pi **Raspberry Pi OS Desktop** を使用している場合は、電源ボタンを素早く2回押すとシャットダウンします。
  * **Raspberry Pi OS Lite** を使用している場合は、1回押すだけでシャットダウンが開始されます。
  * 強制終了したい場合は、電源ボタンを長押ししてください。

* **電源オン**

  * Raspberry Piがシャットダウン状態で電源が供給されている場合、ボタンを1回押すことで起動します。

* シャットダウンボタンに対応していないOSを使用している場合も、5秒間長押しで強制終了が可能で、1回押しで再起動できます。

3. Raspberry Pi AI HAT+について
----------------------------------------------------------

Raspberry Pi AI HAT+は、Pironman 5と互換性がありません。

   .. image::  img/output3.png
        :width: 400

Raspberry Pi AI Kitは、Raspberry Pi M.2 HAT+とHailo AIアクセラレータモジュールで構成されています。

   .. image::  img/output2.jpg
        :width: 400

Hailo AI アクセラレータモジュールは Raspberry Pi AI Kit から取り外し、Pironman 5 Mini の HAT に直接装着することができます。

   .. .. image::  img/output4.png
   ..      :width: 800


4. PI5 が起動しない（赤色 LED）？
-------------------------------------------

この問題は、システムのアップデート、ブート順序の変更、またはブートローダーの破損によって発生する可能性があります。以下の手順を試して問題を解決してください。

#. 電源を再接続し、PI5 が正常に起動するか確認します。

#. ブートローダーの復元

   * それでも PI5 が起動しない場合、ブートローダーが破損している可能性があります。:ref:`update_bootloader_mini` のガイドに従い、SD カードまたは NVMe/USB からの起動を選択してください。
   * 準備した SD カードを PI5 に挿入し、電源を入れて少なくとも 10 秒待ちます。リカバリーが完了したら SD カードを取り外し、再フォーマットしてください。
   * その後、Raspberry Pi Imager を使用して最新の Raspberry Pi OS を書き込み、カードを再挿入して再起動を試みてください。


.. Pironman 5 Mini はレトロゲームシステムをサポートしていますか？
.. --------------------------------------------------------------

.. はい、互換性があります。ただし、多くのレトロゲームシステムは軽量化されたバージョンであり、追加ソフトウェアのインストールや実行ができません。この制限により、Pironman 5 Mini 上の RGB ファンや 4 つの RGB LED など、一部のコンポーネントが正常に機能しない場合があります。これらのコンポーネントは Pironman 5 のソフトウェアパッケージのインストールが必要です。


5. RGB LED が点灯しない？
--------------------------

#. Mini HAT 上の 2 本のピンは、GPIO10 に RGB LED を接続するために使用されます。これらの 2 本のピンにジャンパキャップが正しく取り付けられていることを確認してください。

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. 対応するOSを使用しているか確認してください。Pironman 5がサポートしているOSは以下のとおりです：

   .. image:: img/compitable_os.png
      :width: 600
      :align: center

   非対応のOSを使用している場合は、:ref:`install_the_os_mini` を参照して対応OSをインストールしてください。

#. ``sudo raspi-config`` を実行し、設定メニューを開きます。 **3 Interfacing Options** -> **I3 SPI** -> **YES** の順に選択し、 **OK** と **Finish** をクリックしてSPIを有効化。その後、Pironman 5を再起動します。

上記の手順でも問題が解決しない場合は、service@sunfounder.com までご連絡ください。できるだけ早く対応いたします。

6. CPUファンが回らない？
----------------------------------------------

CPUの温度が設定されたしきい値に達していない場合、CPUファンは作動しません。

**温度に応じたファン回転制御**

PWMファンは、Raspberry Pi 5の温度に応じて動作スピードを自動調整します：

* **50°C未満**：ファンは停止（0%）
* **50°C**：低速（30%）
* **60°C**：中速（50%）
* **67.5°C**：高速（70%）
* **75°C以上**：全速（100%）

詳細は :ref:`fan_mini` をご覧ください。

7. Webダッシュボードを無効にする方法
------------------------------------------------------

``pironman5`` モジュールをインストールすると、:ref:`view_control_dashboard_mini` にアクセスできるようになります。

この機能が不要で、CPUおよびメモリの使用量を削減したい場合は、インストール時に ``--disable-dashboard`` フラグを追加してください。

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

すでに ``pironman5`` をインストール済みの場合は、以下のコマンドで ``dashboard`` モジュールと ``influxdb`` をアンインストールし、再起動してください：

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

8. ``pironman5`` コマンドで各コンポーネントを操作する方法
----------------------------------------------------------------------
``pironman5`` コマンドを使用してPironman 5の各機能を操作する方法は、以下のチュートリアルを参照してください：

* :ref:`view_control_commands_mini`

9. コマンドを使って起動順序を変更するには
-------------------------------------------------------------

Raspberry Piにログイン済みであれば、コマンドで起動順序（BOOT_ORDER）を変更することが可能です。詳しくは以下をご覧ください：

* :ref:`configure_boot_ssd_mini`


10. Raspberry Pi Imagerで起動順序を変更する方法
---------------------------------------------------------------

``EEPROM`` 設定の ``BOOT_ORDER`` を直接編集する代わりに、 **Raspberry Pi Imager** を使って起動順序を設定することも可能です。

この操作には予備のSDカードを使用することをおすすめします。

* :ref:`update_bootloader_mini`

11. SDカードからNVMe SSDにシステムをコピーするには
-------------------------------------------------------------

NVMe SSDはあるがPCに接続するためのアダプターがない場合、まずMicro SDカードにシステムをインストールしてください。Pironman 5の起動が完了したら、SDカードからNVMe SSDへシステムをコピーすることが可能です。

詳しい手順は以下を参照：

* :ref:`copy_sd_to_nvme_rpi_mini`

12. アクリルパネルの保護フィルムの剥がし方
-----------------------------------------------------------------

同梱の2枚のアクリルパネルには、傷防止のため両面に黄色または透明の保護フィルムが貼られています。このフィルムは剥がしにくいことがありますが、ドライバーなどで角を軽く引っかけてから、ゆっくりと剥がしてください。

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center



.. _openssh_powershell_mini:

13. PowerShellでOpenSSHをインストールするには？
--------------------------------------------------

``ssh <username>@<hostname>.local``（または ``ssh <username>@<IP address>``）を実行しても、以下のようなエラーが表示される場合：

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


これは、お使いのWindowsが古く、 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ がプリインストールされていないことを意味します。以下の手順で手動インストールを行ってください。

#. Windowsの検索ボックスに「 ``powershell`` 」と入力し、 ``Windows PowerShell`` を右クリックして「 ``Run as administrator`` 」を選択します。

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

        上記の表示がされない場合は、Windowsがさらに古いバージョンである可能性があります。|link_putty| などのサードパーティ製SSHツールの使用をご検討ください。

#. PowerShellを再起動し、再度管理者権限で起動してください。これで ``ssh`` コマンドによる接続が可能になり、設定したパスワードの入力が求められます。

   .. image:: img/powershell_login.png
