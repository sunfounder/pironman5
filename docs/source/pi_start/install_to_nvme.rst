.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

NVMe SSDへのOSインストール
===================================

 **必要なコンポーネント** 

* パーソナルコンピュータ
* NVMe SSD
* NVMeからUSBへのアダプタ
* Micro SDカードとリーダー

1. Raspberry Pi Imagerのインストール
----------------------------------------

#. `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_ のRaspberry Piソフトウェアダウンロードページにアクセスし、使用しているオペレーティングシステムに対応するImagerバージョンを選択します。ファイルをダウンロードして開き、インストールを開始します。

    .. image:: img/os_install_imager.png
        :align: center

#. インストール中にセキュリティプロンプトが表示される場合があります。たとえば、Windowsでは警告メッセージが表示されることがあります。その場合、 **詳細情報** を選択してから **実行** を選択します。画面の指示に従ってRaspberry Pi Imagerのインストールを完了します。

    .. image:: img/os_info.png
        :align: center

#. Raspberry Pi Imagerアプリケーションを起動するには、そのアイコンをクリックするか、ターミナルで ``rpi-imager`` と入力します。

    .. image:: img/os_open_imager.png
        :align: center

.. _update_bootloader:

2. ブートローダーの更新
---------------------------

まず、NVMeからの起動を試みる前に、Raspberry Pi 5のブートローダーを更新する必要があります。

.. note::

    このステップでは、予備のMicro SDカードを使用することをお勧めします。最初にこのMicro SDカードにブートローダーを書き込み、それをすぐにRaspberry Piに挿入してNVMeデバイスからの起動を有効にします。
    
    または、最初にNVMeデバイスに直接ブートローダーを書き込み、それをRaspberry Piに挿入してブート方法を変更します。その後、NVMe SSDをコンピュータに接続してオペレーティングシステムをインストールし、インストールが完了したら再びRaspberry Piに戻します。

#. 予備のMicro SDカードまたはNVMe SSDをリーダーを使用してコンピュータまたはラップトップに挿入します。

#. Imager内で、 **Raspberry Pi Device** をクリックし、ドロップダウンリストから **Raspberry Pi 5** モデルを選択します。

    .. image:: img/os_choose_device_pi5.png
        :align: center

#.  **Operating System** タブで下にスクロールし、 **Misc utility images** を選択します。

    .. image:: img/nvme_misc.png
        :align: center

#.  **Bootloader (Pi 5 family)** を選択します。

    .. image:: img/nvme_bootloader.png
        :align: center

#. Raspberry Pi 5をNVMeから起動できるようにするために、 **NVMe/USB Boot** を選択します。

    .. image:: img/nvme_nvme_boot.png
        :align: center

#.  **Storage** オプションで、挿入したNVMe SSDを選択します。

    .. note::

        正しいストレージデバイスを選択してください。混乱を避けるために、複数のストレージデバイスが接続されている場合は他のデバイスを取り外します。

    .. image:: img/nvme_ssd_storage.png
        :align: center

#.  **NEXT** をクリックします。ストレージデバイスに既存のデータがある場合、データ損失を防ぐためにバックアップを作成してください。バックアップが不要な場合は **Yes** をクリックして進みます。

    .. image:: img/nvme_erase.png
        :align: center

#.  **NVMe/USB Boot** がストレージデバイスに書き込まれたことを示すプロンプトが表示されます。

    .. image:: img/nvme_boot_finish.png
        :align: center

#. Micro SDカードまたはNVMe SSDを |link_pironman5| に挿入します。Type Cアダプタで |link_pironman5| に電源を供給すると、Micro SDカードまたはNVMe SSDからブートローダーがRaspberry PiのEEPROMに書き込まれます。

.. note::

    その後、Raspberry PiはUSBやSDカードを試みる前にNVMeから起動します。
    
    |link_pironman5| の電源を切り、Micro SDカードまたはNVMe SSDを取り外します。

3. NVMe SSDにOSをインストール
---------------------------------------

これでNVMe SSDにオペレーティングシステムをインストールできます。

#. Imager内で、 **Raspberry Pi Device** をクリックし、ドロップダウンリストから **Raspberry Pi 5** モデルを選択します。

    .. image:: img/os_choose_device_pi5.png
        :align: center

#.  **Operating System** を選択し、推奨されるオペレーティングシステムバージョンを選択します。

    .. image:: img/os_choose_os.png
        :align: center

#.  **Storage** オプションで、挿入したNVMe SSDを選択します。

    .. note::

        正しいストレージデバイスを選択してください。混乱を避けるために、複数のストレージデバイスが接続されている場合は他のデバイスを取り外します。

    .. image:: img/nvme_ssd_storage.png
        :align: center

#.  **NEXT** をクリックし、 **EDIT SETTINGS** をクリックしてOSの設定を調整します。

    .. note::

        Raspberry Pi用のモニターがある場合は、次のステップをスキップして「Yes」をクリックしてインストールを開始できます。その他の設定は後でモニターで調整します。

    .. image:: img/os_enter_setting.png
        :align: center

#. Raspberry Piの **ホスト名** を設定します。

    .. note::

        ホスト名はRaspberry Piのネットワーク識別子です。 ``<hostname>.local`` または ``<hostname>.lan`` を使用してPiにアクセスできます。

    .. image:: img/os_set_hostname.png
        :align: center

#. Raspberry Piの管理者アカウントの **ユーザー名** と **パスワード** を作成します。

    .. note::

        固有のユーザー名とパスワードを設定することは、デフォルトのパスワードがないRaspberry Piを保護するために重要です。

    .. image:: img/os_set_username.png
        :align: center

#. ワイヤレスLANの設定を行い、ネットワークの **SSID** と **パスワード** を入力します。

    .. note::

        ``Wireless LAN country`` は、居住地に対応する2文字の `ISO/IEC alpha2コード <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ に設定してください。

    .. image:: img/os_set_wifi.png
        :align: center

#. Raspberry Piにリモート接続するために、 **Services** タブで **SSHを有効** にします。

    * **パスワード認証** の場合、 **General** タブのユーザー名とパスワードを使用します。
    * 公開鍵認証の場合、「公開鍵認証のみを許可」を選択します。RSAキーがある場合、それが使用されます。ない場合は、「SSH-keygenを実行」をクリックして新しいキーを生成します。

    .. image:: img/os_enable_ssh.png
        :align: center

#.  **Options** メニューでは、書き込み時のImagerの動作（完了時の音を鳴らす、メディアの取り出し、テレメトリの有効化など）を設定できます。

    .. image:: img/os_options.png
        :align: center

#. OSのカスタマイズ設定を入力し終えたら、 **保存** をクリックしてカスタマイズを保存します。その後、イメージを書き込む際に適用するために **Yes** をクリックします。

    .. image:: img/os_click_yes.png
        :align: center

#. NVMe SSDに既存のデータがある場合、データ損失を防ぐためにバックアップを作成してください。バックアップが不要な場合は **Yes** をクリックして進みます。

    .. image:: img/nvme_erase.png
        :align: center

#. 「Write Successful」のポップアップが表示されたら、イメージが完全に書き込まれ、検証されたことを意味します。これでNVMe SSDからRaspberry Piを起動する準備が整いました！

    .. image:: img/nvme_install_finish.png
        :align: center

#. NVMe SSDを |link_pironman5| のNVMe PiPボードに挿入します。

    .. image:: img/nvme_assemble.png
        :width: 500
        :align: center

