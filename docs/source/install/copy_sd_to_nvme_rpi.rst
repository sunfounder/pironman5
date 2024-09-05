.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと共に、Raspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームの助けを借りて、アフターサポートや技術的な課題を解決します。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベントやプレゼント企画**: プレゼント企画や季節のプロモーションに参加できます。

    👉 探索と創造の旅に出る準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _copy_sd_to_nvme_rpi:

Micro SDからNVMe SSDへのOSのコピー
==================================================================

NVMe SSDを持っているが、コンピュータに接続するためのアダプターがない場合、別の方法として最初にMicro SDカードにシステムをインストールし、Pironman 5が正常に起動した後にMicro SDカードからNVMe SSDへシステムを転送することができます。

* まず、:ref:`install_os_sd_rpi` を参照してシステムをインストールします。
* 次に、Raspberry Piを起動し、ログインします。ログイン方法が不明な場合は、公式Raspberry Piサイト: |link_rpi_get_start| を参照してください。

上記の手順を完了した後、以下の手順に進みます。


1. PCIeを有効化する
--------------------

デフォルトではPCIeコネクタは無効化されています。

* 有効化するには、 ``/boot/firmware/config.txt`` ファイルを開きます。

  .. code-block:: shell
  
    sudo nano /boot/firmware/config.txt
  
* 次に、ファイルに以下の行を追加します。

  .. code-block:: shell
  
    # PCIe外部コネクタを有効化
    dtparam=pciex1
  
* より覚えやすいエイリアス ``pciex1`` が存在するため、代わりに ``dtparam=nvme`` を ``/boot/firmware/config.txt`` に追加することも可能です。

  .. code-block:: shell
  
    dtparam=nvme

* 接続はGen 2.0の速度(5 GT/sec)に対応していますが、次の行を追加することでGen 3.0 (10 GT/sec)に強制することもできます。

  .. code-block:: shell
  
    # Gen 3.0速度を強制
    dtparam=pciex1_gen=3
  
  .. warning::
  
    Raspberry Pi 5はGen 3.0の速度での認証を受けておらず、この速度でPCIeデバイスに接続すると、接続が不安定になる可能性があります。

* ``Ctrl + X``, ``Y`` 、そして ``Enter`` を押して変更を保存します。


2. SSDへのOSインストール
----------------------------------------

SSDにOSをインストールする方法は2つあります：

**Micro SDカードからSSDにシステムをコピーする**

#. ディスプレイを接続するか、VNC Viewerを通じてRaspberry Piデスクトップにアクセスします。次に **Raspberry Piロゴ**  -> **アクセサリ** -> **SDカードコピーツール** をクリックします。

   .. image:: img/ssd_copy.png
      
    
#. 正しい **コピー元** および **コピー先** デバイスを選択してください。間違えないよう注意してください。

   .. image:: img/ssd_copy_from.png
      
#. 選択後、 **開始** をクリックします。

   .. image:: img/ssd_copy_start.png

#. SSD上のコンテンツが消去されるというプロンプトが表示されます。データをバックアップしてから **Yes** をクリックしてください。

   .. image:: img/ssd_copy_erase.png

#. 少し待つとコピーが完了します。


**Raspberry Pi Imagerを使用したシステムインストール**

Micro SDカードにデスクトップ版のシステムがインストールされている場合、イメージングツール（Raspberry Pi Imagerなど）を使用してシステムをSSDに書き込むことができます。この例ではRaspberry Pi OS bookwormを使用していますが、他のシステムでは最初にイメージングツールのインストールが必要になる場合があります。

#. ディスプレイを接続するか、VNC Viewerを通じてRaspberry Piデスクトップにアクセスします。次に **Raspberry Piロゴ**  -> **アクセサリ** -> **イメージャ** をクリックします。

   .. image:: img/ssd_imager.png

      
#. |link_rpi_imager| で **Raspberry Piデバイス** をクリックし、ドロップダウンリストから **Raspberry Pi 5** モデルを選択します。

   .. image:: img/ssd_pi5.png
      :width: 90%


#. **オペレーティングシステム** を選択し、推奨されるOSバージョンを選びます。

   .. image:: img/ssd_os.png
      :width: 90%
    
#. **ストレージ** オプションで挿入されたNVMe SSDを選択します。

   .. image:: img/nvme_storage.png
      :width: 90%
    
#. **次へ** をクリックし、 **設定を編集** してOS設定をカスタマイズします。

   .. note::

      Raspberry Piにモニターがある場合、次のステップをスキップしてインストールを開始するために「Yes」をクリックできます。その他の設定は後でモニターで調整できます。

   .. image:: img/os_enter_setting.png
      :width: 90%

#. Raspberry Piの **ホスト名** を設定します。

   .. note::

      ホスト名はRaspberry Piのネットワーク識別子です。 ``<hostname>.local`` または ``<hostname>.lan`` を使用してアクセスできます。

   .. image:: img/os_set_hostname.png
      

#. Raspberry Piの管理者アカウント用に **ユーザー名** と **パスワード** を作成します。

   .. note::

      一意のユーザー名とパスワードを設定することは、デフォルトのパスワードがないRaspberry Piのセキュリティを確保するために重要です。

   .. image:: img/os_set_username.png
      

#. ワイヤレスLANを設定し、ネットワークの **SSID** と **パスワード** を入力します。

   .. note::

      ``Wireless LAN country`` をあなたの所在地に対応する2文字の `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ に設定してください。

   .. image:: img/os_set_wifi.png

#. Raspberry Piにリモート接続するために、 **サービス** タブで **SSHを有効にする** を選択します。

   * **パスワード認証** の場合、 **一般** タブのユーザー名とパスワードを使用します。
   * 公開鍵認証の場合は「公開鍵認証のみを許可」を選択します。RSAキーがある場合、それが使用されます。ない場合は、「SSHキー生成を実行」をクリックして新しい鍵ペアを生成します。

   .. image:: img/os_enable_ssh.png

      

#. **オプション** メニューで、書き込み中のImagerの動作を設定できます。例えば、終了時に音を鳴らす、メディアを取り出す、テレメトリを有効にするなどの設定が可能です。

   .. image:: img/os_options.png
    
#. OSのカスタマイズ設定が完了したら、 **保存** をクリックしてカスタマイズを保存し、イメージを書き込む際に適用するために **Yes** をクリックします。

   .. image:: img/os_click_yes.png
      :width: 90%
      
#. NVMe SSDに既存のデータが含まれている場合、データ損失を防ぐためにバックアップを確実に行ってください。バックアップが不要であれば、 **Yes** をクリックして続行します。

   .. image:: img/nvme_erase.png
      :width: 90%

#. 「書き込み成功」のポップアップが表示されたら、イメージが完全に書き込まれ、検証されています。これでNVMe SSDからRaspberry Piを起動する準備が整いました！

   .. image:: img/nvme_install_finish.png
      :width: 90%
      

.. _configure_boot_ssd:

3. SSDからの起動を設定
---------------------------------------
* 起動サポートを有効にするには、ブートローダー構成で ``BOOT_ORDER`` を変更する必要があります。EEPROM構成を編集します。

  .. code-block:: shell
  
    sudo rpi-eeprom-config --edit
  
* 次に、 ``BOOT_ORDER`` 行を以下のように変更します。 ``0xf416`` : 最初にNVMe SSDを試し、次にSDカード、最後にUSBを試します。

  .. code-block:: shell
  
    BOOT_ORDER=0xf416

  .. note::
    
    Raspberry Piの起動順序を変更するだけで、他の起動方法を削除しないでください。これにより、常に正しく起動できるようになります。


``BOOT_ORDER`` 設定により、異なるブートモードの優先順位を柔軟に構成できます。32ビットの符号なし整数として表され、各ニブルがブートモードを表します。ブートモードは、最下位ビットから最上位ビットの順に試行されます。
``BOOT_ORDER`` プロパティは、異なるブートモードの順序を定義します。右から左に読み、最大8桁まで定義できます。

.. image:: img/boot_order.png
      :width: 90%
      

* ``0xf41``: 最初にSDカードを試し、その後USB-MSDを試し、繰り返す（ ``BOOT_ORDER`` が空の場合のデフォルト）。
* ``0xf14``: 最初にUSBを試し、その後SDカードを試し、繰り返す。

* 更新が完了したら、これらの変更を有効にするためにRaspberry Piを再起動します。

.. code-block:: shell

    sudo reboot

