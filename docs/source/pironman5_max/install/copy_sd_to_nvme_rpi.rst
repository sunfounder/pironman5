.. note:: 

    こんにちは！SunFounder の Facebook コミュニティ「Raspberry Pi & Arduino & ESP32 愛好者グループ」へようこそ！Raspberry Pi、Arduino、ESP32 に熱中する仲間たちと一緒に、これらの技術をもっと深く掘り下げていきましょう。

    **参加する理由**

    - **専門サポート**：購入後の技術的な問題を、コミュニティと私たちのチームが協力して解決します。
    - **学びと共有**：ノウハウやチュートリアルを交換してスキルを磨きましょう。
    - **新製品の先行情報**：新製品の発表やプロトタイプをいち早くチェックできます。
    - **会員限定割引**：新商品に関する特別割引をご利用いただけます。
    - **イベントやプレゼント企画**：キャンペーンや抽選に参加して楽しめます。

    👉 一緒に創造と探求を始めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

.. _max_copy_sd_to_nvme_rpi:

Micro SD から NVMe SSD へ OS をコピーする
==================================================================

NVMe SSD を持っているけれどパソコンに接続するアダプタがない場合は、次の方法が使えます。まず Micro SD カードにシステムをインストールし、Pironman 5 MAX の起動後にシステムを NVMe SSD へコピーする手順です。

* まず、:ref:`max_install_os_sd_rpi` を完了してください。
* その後、Raspberry Pi を起動してログインします。ログイン方法が分からない場合は、Raspberry Pi 公式サイト（|link_rpi_get_start|）をご参照ください。

上記手順を完了してから、以下の手順に進んでください。


1. PCIe を有効化する
-------------------------

デフォルトでは PCIe コネクタは無効になっています。

* 有効にするには、 ``/boot/firmware/config.txt`` ファイルを開きます。

  .. code-block:: shell

    sudo nano /boot/firmware/config.txt

* 次に、以下の行をファイルに追加します。

  .. code-block:: shell

    # 外部 PCIe コネクタを有効化
    dtparam=pciex1

* ``pciex1`` にはエイリアス ``dtparam=nvme`` があるため、こちらを使用しても構いません。

  .. code-block:: shell

    dtparam=nvme

.. * この接続は Gen 2.0（5 GT/sec）に対応していますが、以下の設定で Gen 3.0（10 GT/sec）に強制できます。

..   .. code-block:: shell

..     # Gen 3.0 に強制設定
..     dtparam=pciex1_gen=3

..   .. warning::

..     Raspberry Pi 5 は Gen 3.0 に公式対応しておらず、不安定になる可能性があります。

* 起動時に PCIe スイッチ経由で NVMe ドライブを認識させるため、PCIe 起動遅延を無効にします。

  .. code-block:: shell

    dtparam=pciex1_no_10s=on


* ``Ctrl + X`` → ``Y`` → ``Enter`` で保存して終了します。


**BOOT_ORDER の設定**

複数の NVMe システムドライブがある場合、起動対象を選ぶには ``/boot/firmware/cmdline.txt`` の ``ROOT=PARTUUID=xxxxxxxxx`` を変更してください。ディスクの UUID は以下のコマンドで確認できます。

.. code-block:: shell

   ls /dev/disk/by-id/


2. SSD に OS をインストールする
----------------------------------------

OS を SSD にインストールする方法は2つあります：

**Micro SD カードから SSD へコピーする方法**

#. ディスプレイを接続、または VNC Viewer 経由でデスクトップにアクセスし、 **Raspberry Pi ロゴ** → **アクセサリ** → **SD Card Copier** を選択。

   .. image:: img/ssd_copy.png


#. **Copy From** と **Copy To** のデバイスを正しく選択してください。逆にしないよう注意。

   .. image:: img/ssd_copy_from.png

#. 「NEW Partition UUIDs」を選択して、UUID 重複によるマウントや起動エラーを防ぎます。

   .. image:: img/ssd_copy_uuid.png

#. 選択後、 **Start** をクリック。

   .. image:: img/ssd_copy_click_start.png

#. データ消去の確認が表示されるので、必要ならバックアップをとってから **Yes** をクリック。

   .. image:: img/ssd_copy_erase.png

#. コピー完了までしばらく待ちます。


**Raspberry Pi Imager を使ってインストール**

Micro SD にデスクトップ版 OS が入っている場合、Raspberry Pi Imager などのツールを使って SSD に OS を書き込むことができます。

#. ディスプレイを接続、または VNC Viewer でデスクトップにアクセスし、 **Raspberry Pi ロゴ** → **アクセサリ** → **Imager** を選択。

   .. image:: img/ssd_imager.png


#. |link_rpi_imager| 内で、 **Raspberry Pi Device** → **Raspberry Pi 5** を選択。

   .. image:: img/ssd_pi5.png
      :width: 90%


#. **Operating System** を選び、推奨バージョンを選択。

   .. image:: img/ssd_os.png
      :width: 90%

#. **Storage** で NVMe SSD を選択。

   .. image:: img/nvme_storage.png
      :width: 90%

#. **NEXT** をクリック後、 **EDIT SETTINGS** でOS設定をカスタマイズ。

   .. note::

      ディスプレイがある場合は「Yes」を押してインストールを続行できます。設定は後から変更可能です。

   .. image:: img/os_enter_setting.png
      :width: 90%

#. **ホスト名** を設定（例：raspberrypi）。

   .. note::

      ネットワーク上では ``<hostname>.local`` などでアクセス可能になります。

   .. image:: img/os_set_hostname.png


#. **ユーザー名とパスワード** を設定（管理者用アカウント）。

   .. note::

      セキュリティ向上のため、デフォルトパスワードはありません。任意のユーザー名とパスワードを設定してください。

   .. image:: img/os_set_username.png


#. 無線LAN設定（SSIDとパスワード）を入力。

   .. note::

      お住まいの地域に対応する2文字の `ISO/IEC alpha2コード <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ を「 ``Wireless LAN country``」に設定してください。

   .. image:: img/os_set_wifi.png

#. **Services** タブで **enable SSH** を有効化。

   * **パスワード認証** ： **General** タブのユーザー名・パスワードを使用。
   * 公開鍵認証：RSA鍵を使用、または「Run SSH-keygen」で作成可能。

   .. image:: img/os_enable_ssh.png



#. **Options** メニューでは、書き込み後の動作（サウンド再生、メディアの取り出しなど）を設定可能。

   .. image:: img/os_options.png

#. 設定完了後 **Save** をクリックし、 **Yes** を押して書き込みを実行。

   .. image:: img/os_click_yes.png
      :width: 90%

#. SSD に既存データがある場合はバックアップをとり、 **Yes** を押して続行。

   .. image:: img/nvme_erase.png
      :width: 90%

#. 「Write Successful」画面が表示されたら、書き込みと検証は完了です。NVMe SSD からの起動が可能になります。

   .. image:: img/nvme_install_finish.png
      :width: 90%


.. _max_configure_boot_ssd:

3. SSD からの起動を設定する
---------------------------------------

ここでは、Raspberry Pi を SD カードではなく NVMe SSD から直接起動するよう設定します。

#. ターミナルで以下のコマンドを入力し、設定画面を開きます。

   .. code-block:: shell

      sudo raspi-config

#. ``raspi-config`` メニューでは、矢印キーを使って **Advanced Options** を選択し、 ``Enter`` を押して詳細設定に進みます。

   .. image:: img/nvme_open_config.png

#. **Advanced Options** 内で **Boot Order** を選択します。この設定では、Raspberry Pi が起動可能なデバイスを検索する順序を指定できます。

   .. image:: img/nvme_boot_order.png

#. 続いて **NVMe/USB boot** を選択します。これにより、SDカードよりもUSB接続のSSDやNVMeドライブからの起動を優先するように設定されます。

   .. image:: img/nvme_boot_nvme.png

#. 起動順を選択したら、 **Finish** を押して raspi-config を終了します。 **Escape** キーでも設定ツールを閉じることができます。

   .. image:: img/nvme_boot_ok.png

#. 新しい起動設定を反映するには、 ``sudo reboot`` を実行して Raspberry Pi を再起動してください。

   .. code-block:: shell

      sudo raspi-config

   .. image:: img/nvme_boot_reboot.png

再起動後、Raspberry Pi は接続された NVMe SSD から起動を試み、より高速で信頼性の高いシステム動作を実現します。


