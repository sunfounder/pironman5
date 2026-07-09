.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _install_os_sd_rpi_promax:

オペレーティングシステムのインストール
========================================================

Raspberry Piを使用する前に、microSDカードに **Raspberry Pi OS** をインストールする必要があります。
このガイドでは、初心者にもわかりやすい方法で **Raspberry Pi Imager** を使用する方法を説明します。

**必要なもの**

* コンピューター（Windows、macOS、Linux）
* microSDカード（16GB以上；推奨ブランド：SanDisk、Samsung）
* microSDカードリーダー

-------------------

.. start_install_imager

1. Raspberry Pi Imagerのインストール
-------------------------------------------

.. |shared_link_rpi_imager| raw:: html

    <a href="https://www.raspberrypi.com/software/" target="_blank">Raspberry Pi Imager</a>   

#. 公式Raspberry Pi Imagerのダウンロードページ |shared_link_rpi_imager| にアクセスします。お使いのオペレーティングシステムに適したインストーラーをダウンロードします。

   .. image:: img/imager_download.png
      :width: 70%

#. インストールのプロンプト（言語、インストールパス、確認）に従います。インストール後、デスクトップまたはアプリケーションメニューから **Raspberry Pi Imager** を起動します。

   .. image:: img/imager_install.png
      :width: 90%

.. end_install_imager

-------------------

2. OSをmicroSDカードにインストールする
------------------------------------------------

1. カードリーダーを使用してmicroSDカードをコンピューターに挿入します。続行する前に、重要なデータをバックアップしてください。

   .. image:: img/insert_sd.png
      :width: 90%

2. Raspberry Pi Imagerが開くと、**Device** ページが表示されます。リストからRaspberry Pi 5モデルを選択します。

   .. image:: img/imager_device.png
      :width: 90%

3. **OS** セクションに移動し、推奨される **Raspberry Pi OS (64-bit)** オプションを選択します。

   .. warning::

      必ず **64 ビット** 版を選択してください。**32 ビット** のシステムをインストールすると、一部のパッケージは ``aarch64``（64 ビット）版のみの提供となり、特定の機能がインストールできない、または正しく動作しない場合があります。

   .. image:: img/imager_os.png
      :width: 90%

4. **Storage** セクションで、microSDカードを選択します。

   .. image:: img/imager_storage.png
      :width: 90%

   .. start_install_os

5. **Next** をクリックしてカスタマイズステップに進みます。

   .. note::

      * モニター、キーボード、マウスをRaspberry Piに直接接続する場合は、 **SKIP CUSTOMISATION** をクリックしても構いません。
      * Raspberry Piを *ヘッドレス* （Wi-Fiリモートアクセス）でセットアップする場合は、カスタマイズ設定を完了する必要があります。

   .. image:: img/imager_custom_skip.png
      :width: 90%

#. **ホスト名の設定**

   * Raspberry Piに一意のホスト名を付けます。
   * 後で ``hostname.local`` を使用して接続できます。

   .. image:: img/imager_custom_hostname.png
      :width: 90%

#. **ローカライゼーションの設定**

   * お住まいの都市を選択します。
   * Imagerは選択に基づいてタイムゾーンとキーボードレイアウトを自動的に補完しますが、必要に応じて調整できます。Nextを選択します。

   .. image:: img/imager_custom_local.png
      :width: 90%

#. **ユーザー名とパスワードの設定**

   Raspberry Pi用のユーザーアカウントを作成します。

   .. image:: img/imager_custom_user.png
      :width: 90%

#. **Wi-Fiの設定**

   * Wi-Fiの **SSID**（ネットワーク名）と **パスワード** を入力します。
   * Raspberry Piは初回起動時に自動的に接続します。

   .. image:: img/imager_custom_wifi.png
      :width: 90%

#. **SSHの有効化（オプションですが推奨）**

   * SSHを有効にすると、コンピューターからリモートでログインできるようになります。
   * ユーザー名/パスワードを使用してログインするか、SSHキーを設定できます。

   .. image:: img/imager_custom_ssh.png
      :width: 90%

#. **Raspberry Pi Connectの有効化（オプション）**


   Raspberry Pi Connectを使用すると、WebブラウザからRaspberry Piのデスクトップにアクセスできます。

   * **Raspberry Pi Connect** をオンにし、**OPEN RASPBERRY PI CONNECT** をクリックします。

     .. image:: img/imager_custom_connect.png
        :width: 90%

   * Raspberry Pi Connectのウェブサイトがデフォルトのブラウザで開きます。Raspberry Pi IDアカウントにログインするか、まだお持ちでない場合はサインアップします。

     .. image:: img/imager_custom_open.png
        :width: 90%

   * **New auth key** ページで、ワンタイム認証キーを作成します。

      * Raspberry Pi IDアカウントがどの組織にも属していない場合は、**Create auth key and launch Raspberry Pi Imager** を選択します。
      * 1つ以上の組織に属している場合は、1つを選択し、キーを作成してImagerを起動します。
      * キーの有効期限が切れる前に、Raspberry Piの電源を入れ、インターネットに接続してください。

     .. image:: img/imager_custom_authkey.png
        :width: 90%

   * ブラウザがRaspberry Pi Imagerを開くよう求める場合があります — 許可します。

     * ImagerがRaspberry Pi Connectタブで開き、認証トークンが表示されます。
     * トークンが自動的に転送されない場合は、Raspberry Pi Connectページの **Having trouble?** セクションを開き、トークンをコピーしてImagerに手動で貼り付けます。

     .. image:: img/imager_custom_connect_token.png
        :width: 90%

#. すべての設定を確認し、**WRITE** をクリックします。

   .. image:: img/imager_writing.png
      :width: 90%

#. カードに既にデータが存在する場合、Raspberry Pi Imagerはデバイス上のすべてのデータが消去されるという警告を表示します。正しいドライブを選択したことを再確認し、**I UNDERSTAND, ERASE AND WRITE** をクリックして続行します。

   .. image:: img/imager_erase.png
      :width: 90%

#. 書き込みと検証が完了するまで待ちます。完了すると、Raspberry Pi Imagerは **Write complete!** と選択内容の要約を表示します。ストレージデバイスは自動的に取り出されるため、安全に取り外すことができます。


   .. image:: img/imager_finish.png
        :width: 90%

   .. end_install_os

#. microSDカードを取り外し、Raspberry Piの裏面のスロットに挿入します。これでRaspberry Piは新しいOSで起動する準備が整いました！

   .. image:: img/os_sd_to_pi.jpg
        :width: 70%