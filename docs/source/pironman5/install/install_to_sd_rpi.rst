.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと共に、Raspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームの支援を受けて、アフターサポートや技術的な課題を解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベントやプレゼント企画**: プレゼント企画や季節のプロモーションに参加できます。

    👉 探索と創造の旅に出る準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _install_os_sd_rpi_5:

オペレーティングシステムのインストール
================================================

Raspberry Pi を使用する前に、**Raspberry Pi OS** を microSD カードにインストールする必要があります。  
このガイドでは、**Raspberry Pi Imager** を使用して、初心者にも分かりやすい方法でインストールする手順を説明します。

**必要なもの**

* コンピューター（Windows、macOS、または Linux）
* microSD カード（16GB 以上；推奨ブランド：SanDisk、Samsung）
* microSD カードリーダー

-------------------

.. start_install_imager

1. Raspberry Pi Imager のインストール
-------------------------------------------

.. |shared_link_rpi_imager| raw:: html

    <a href="https://www.raspberrypi.com/software/" target="_blank">Raspberry Pi Imager</a>   

#. Raspberry Pi Imager の公式ダウンロードページ |shared_link_rpi_imager| にアクセスし、お使いのオペレーティングシステムに対応したインストーラーをダウンロードします。

   .. image:: img/imager_download.png
      :width: 70%

#. インストール手順（言語、インストール先、確認など）に従ってインストールします。インストール完了後、デスクトップまたはアプリケーションメニューから **Raspberry Pi Imager** を起動します。

   .. image:: img/imager_install.png
      :width: 90%

.. end_install_imager

-------------------

2. microSD カードに OS をインストールする
------------------------------------------------

1. カードリーダーを使用して microSD カードをコンピューターに挿入します。  
   作業を進める前に、重要なデータは必ずバックアップしてください。

   .. image:: img/insert_sd.png
      :width: 90%

2. Raspberry Pi Imager を起動すると、**Device** ページが表示されます。  
   リストから **Raspberry Pi 5** のモデルを選択します。

   .. image:: img/imager_device.png
      :width: 90%

3. **OS** セクションに移動し、推奨されている **Raspberry Pi OS (64-bit)** を選択します。

   .. image:: img/imager_os.png
      :width: 90%

4. **Storage** セクションで microSD カードを選択します。

   .. image:: img/imager_storage.png
      :width: 90%

   .. start_install_os

5. **Next** をクリックしてカスタマイズ手順に進みます。

   .. note::

      * モニター、キーボード、マウスを Raspberry Pi に直接接続する場合は、 **SKIP CUSTOMISATION** をクリックしても構いません。  
      * Raspberry Pi を **ヘッドレス** （Wi-Fi によるリモート接続）でセットアップする場合は、必ずカスタマイズ設定を完了してください。

   .. image:: img/imager_custom_skip.png
      :width: 90%

#. **ホスト名の設定**

   * Raspberry Pi に一意のホスト名を付けます。  
   * 後で ``hostname.local`` を使って接続できます。

   .. image:: img/imager_custom_hostname.png
      :width: 90%

#. **ローカリゼーションの設定**

   * お住まいの首都（都市）を選択します。
   * 選択内容に基づいて、タイムゾーンとキーボード配列が自動的に設定されます。必要に応じて調整し、**Next** を選択します。
   
   .. image:: img/imager_custom_local.png
      :width: 90%

#. **ユーザー名とパスワードの設定**

   Raspberry Pi 用のユーザーアカウントを作成します。
   
   .. image:: img/imager_custom_user.png
      :width: 90%

#. **Wi-Fi の設定**

   * Wi-Fi の **SSID**（ネットワーク名）と **パスワード** を入力します。  
   * 初回起動時に Raspberry Pi が自動的に接続されます。
   
   .. image:: img/imager_custom_wifi.png
      :width: 90%

#. **SSH を有効にする（任意だが推奨）**

   * SSH を有効にすると、コンピューターからリモートログインできます。  
   * ユーザー名／パスワードでログインするか、SSH キーを設定できます。
   
   .. image:: img/imager_custom_ssh.png
      :width: 90%

#. **Raspberry Pi Connect を有効にする（任意）**

   Raspberry Pi Connect を使用すると、Web ブラウザーから Raspberry Pi のデスクトップにアクセスできます。
   
   * **Raspberry Pi Connect** をオンにし、**OPEN RASPBERRY PI CONNECT** をクリックします。
   
     .. image:: img/imager_custom_connect.png
        :width: 90%

   * デフォルトのブラウザーで Raspberry Pi Connect の Web サイトが開きます。Raspberry Pi ID アカウントでログインするか、まだ持っていない場合は新規登録してください。

     .. image:: img/imager_custom_open.png
        :width: 90%

   * **New auth key** ページで、ワンタイム認証キーを作成します。
      
      * Raspberry Pi ID アカウントがどの組織にも属していない場合は、**Create auth key and launch Raspberry Pi Imager** を選択します。
      * 1 つ以上の組織に属している場合は、いずれかを選択してからキーを作成し、Imager を起動します。
      * キーの有効期限が切れる前に、Raspberry Pi の電源を入れてインターネットに接続してください。
   
     .. image:: img/imager_custom_authkey.png
        :width: 90%
   
   * ブラウザーが Raspberry Pi Imager を開くかどうか確認する場合がありますので、許可してください。

     * Imager は Raspberry Pi Connect タブで起動し、認証トークンが表示されます。
     * トークンが自動的に転送されない場合は、Raspberry Pi Connect ページの **Having trouble?** セクションを開き、トークンをコピーして Imager に手動で貼り付けてください。

     .. image:: img/imager_custom_connect_token.png
        :width: 90%

#. すべての設定を確認し、**WRITE** をクリックします。

   .. image:: img/imager_writing.png
      :width: 90%

#. すでにデータが入っているカードの場合、Raspberry Pi Imager はデバイス上のすべてのデータが消去されるという警告を表示します。正しいドライブが選択されていることを再確認し、**I UNDERSTAND, ERASE AND WRITE** をクリックして続行します。

   .. image:: img/imager_erase.png
      :width: 90%

#. 書き込みと検証が完了するまで待ちます。完了すると、Raspberry Pi Imager に **Write complete!** と選択内容の概要が表示されます。ストレージデバイスは自動的に取り出し（アンマウント）されるため、安全に取り外すことができます。

   .. image:: img/imager_finish.png
        :width: 90%

   .. end_install_os

#. microSD カードを取り外し、Raspberry Pi 底面のスロットに挿入します。これで、新しい OS を使って Raspberry Pi を起動する準備が整いました。

   .. image:: img/os_sd_to_pi.jpg
        :width: 70%

   
