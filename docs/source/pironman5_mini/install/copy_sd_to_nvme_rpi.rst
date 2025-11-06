.. note::

    こんにちは！SunFounder Raspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！Raspberry Pi、Arduino、ESP32に関する知識を深め、仲間とともに学びましょう。

    **なぜ参加するのか？**

    - **エキスパートサポート**：購入後の問題や技術的な課題を、コミュニティや弊社スタッフがサポートします。
    - **学びと共有**：ヒントやチュートリアルを共有し、スキルを高めましょう。
    - **新製品の先行公開**：新製品の発表や先行情報をいち早くチェック。
    - **Special Discounts**：最新製品をお得に購入できる特別割引をご提供。
    - **Festive Promotions and Giveaways**：プレゼント企画や季節限定キャンペーンにも参加できます。

    👉 私たちと一緒にモノづくりの世界を探求しませんか？[|link_sf_facebook|] をクリックして今すぐ参加！

.. _copy_sd_to_nvme_rpi_mini:

Micro SDからNVMe SSDへのOSコピー
==================================================================

NVMe SSDをお持ちで、PCと接続するアダプターがない場合は、次の方法を試してみてください。まず、Micro SDカードにOSをインストールし、Pironman 5 Miniが正常に起動した後に、システムをMicro SDからNVMe SSDに転送する方法です。

* 最初に :ref:`install_os_sd_rpi_mini` を完了してください。
* 次に、Raspberry Piを起動してログインします。ログイン方法が分からない場合は、公式Raspberry Piサイト：|link_rpi_get_start| を参照してください。

上記の手順を完了してから、以下の操作に進んでください。


1. PCIeの有効化
--------------------

デフォルトでは、PCIeコネクタは無効になっています。

* 有効にするには ``/boot/firmware/config.txt`` ファイルを開きます。

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt

* ファイルに以下の行を追加してください。

  .. code-block:: shell
  
    # Enable the PCIe External connector.
    dtparam=pciex1

* ``pciex1`` には覚えやすい別名があり、代わりに ``/boot/firmware/config.txt`` ファイルに ``dtparam=nvme`` を追加することも可能です。

  .. code-block:: shell

    dtparam=nvme

* 接続はGen 2.0（5 GT/sec）に対応していますが、以下の行を ``/boot/firmware/config.txt`` に追加することで、Gen 3.0（10 GT/sec）へ強制的に切り替えることも可能です。

  .. code-block:: shell
  
    # Force Gen 3.0 speeds
    dtparam=pciex1_gen=3

  .. warning::

    Raspberry Pi 5はGen 3.0速度での正式な動作保証がされておらず、不安定になる可能性があります。

* 設定を保存するには ``Ctrl + X`` 、 ``Y`` 、 ``Enter`` を押します。


2. SSDへのOSインストール
----------------------------------------

OSをSSDにインストールする方法は2つあります：

**Micro SDカードからSSDにシステムをコピーする方法**

#. ディスプレイを接続するか、VNC ViewerでRaspberry Piにアクセスし、 **Raspberry Piロゴ** → **Accessories** → **SD Card Copier** をクリックします。

   .. image:: img/ssd_copy.png


#. **Copy From** と **Copy To** のデバイス選択を慎重に行い、誤らないよう注意してください。

   .. image:: img/ssd_copy_from.png

#. 「NEW Partition UUIDs」を選択して、システムが正しくデバイスを識別できるようにし、マウントの競合や起動エラーを防ぎます。

   .. image:: img/ssd_copy_uuid.png

#. 選択が完了したら **Start** をクリック。

   .. image:: img/ssd_copy_click_start.png

#. SSDの内容が消去される旨の警告が表示されます。必要に応じてバックアップを取り、「Yes」をクリックして進みます。

   .. image:: img/ssd_copy_erase.png

#. コピー完了までしばらく待ちます。

**Raspberry Pi Imagerでのシステムインストール**

Micro SDにデスクトップ版OSがある場合は、Raspberry Pi Imagerなどのツールを使って、システムをSSDに書き込むことも可能です。本例ではRaspberry Pi OS bookwormを使用していますが、他のOSでは先にImagerのインストールが必要な場合もあります。

#. ディスプレイを接続するか、VNC ViewerでRaspberry Piにアクセスし、 **Raspberry Piロゴ** → **Accessories** → **Imager** をクリック。

   .. image:: img/ssd_imager.png


#. |link_rpi_imager| で **Raspberry Pi Device** をクリックし、ドロップダウンから **Raspberry Pi 5** を選択。

   .. image:: img/ssd_pi5.png
      :width: 90%


#. **Operating System** を選び、推奨バージョンを指定。

   .. image:: img/ssd_os.png
      :width: 90%
    
#. **Storage** で接続済みのNVMe SSDを選択。

   .. image:: img/nvme_storage.png
      :width: 90%

#. **NEXT** → **EDIT SETTINGS** をクリックし、OSの設定を行います。

   .. note::

      モニターをお持ちの場合は次の手順をスキップし、「Yes」をクリックしてインストールを開始できます。設定は後から変更可能です。

   .. image:: img/os_enter_setting.png
      :width: 90%

#. Raspberry Piの **ホスト名** を設定。

   .. note::

      ホスト名はネットワーク識別子です。 ``<hostname>.local`` または ``<hostname>.lan`` でアクセス可能になります。

   .. image:: img/os_set_hostname.png


#. **ユーザー名** と **パスワード** を作成。

   .. note::

      初期状態ではパスワードが存在しないため、セキュリティ確保のために必ず設定してください。

   .. image:: img/os_set_username.png


#. 無線LANの **SSID** と **パスワード** を入力。

   .. note::

      ``Wireless LAN country`` には、お住まいの国のISO2桁コードを入力してください。

   .. image:: img/os_set_wifi.png

#. リモート接続のため、 **SSHを有効化** します。

   * **パスワード認証** の場合はGeneralタブで設定したユーザー名とパスワードを使用。
   * 公開鍵認証を選択する場合、RSA鍵を使用。なければ「Run SSH-keygen」で生成可能です。

   .. image:: img/os_enable_ssh.png



#. **Options** メニューでは、完了時の動作（音の再生、メディアの取り出し、テレメトリの有効化など）を設定可能。

   .. image:: img/os_options.png

#. OS設定が完了したら **Save** → **Yes** をクリックして設定を適用し、書き込みを開始します。

   .. image:: img/os_click_yes.png
      :width: 90%

#. NVMe SSDにデータがある場合は、事前にバックアップを行いましょう。問題なければ「Yes」をクリック。

   .. image:: img/nvme_erase.png
      :width: 90%

#. 「Write Successful」ポップアップが表示されたら、OSの書き込みと検証は完了です。NVMe SSDからの起動準備が整いました。

   .. image:: img/nvme_install_finish.png
      :width: 90%


.. _configure_boot_ssd_mini:

3. SSDからの起動を設定
---------------------------------------

このセクションでは、Raspberry PiをNVMe SSDから直接起動できるように設定し、SDカードよりも高速かつ高性能な起動環境を実現します。以下の手順を順に進めてください。

#. ターミナルを開き、次のコマンドで設定画面を起動：

   .. code-block:: shell

      sudo raspi-config

#. ``raspi-config`` メニューで矢印キーを使って **Advanced Options** を選択し、 ``Enter`` を押します。

   .. image:: img/nvme_open_config.png

#. **Advanced Options** 内で **Boot Order** を選びます。ここで起動デバイスの優先順位を指定します。

   .. image:: img/nvme_boot_order.png

#. **NVMe/USB boot** を選択。これにより、SDカードよりもNVMeやUSB接続のSSDを優先して起動します。

   .. image:: img/nvme_boot_nvme.png

#. 設定が完了したら **Finish** を押して終了します。 **Escape** キーでも閉じることができます。

   .. image:: img/nvme_boot_ok.png

#. 新しい起動設定を反映させるには、 ``sudo reboot`` を実行してRaspberry Piを再起動してください。

   .. code-block:: shell

      sudo reboot

   .. image:: img/nvme_boot_reboot.png

再起動後、Raspberry Piは接続されたNVMe SSDからの起動を試みます。これにより、より高いパフォーマンスと耐久性が得られます。
