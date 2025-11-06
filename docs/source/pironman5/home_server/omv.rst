.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと一緒に、Raspberry Pi、Arduino、ESP32についてさらに深く掘り下げていきましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームのサポートを受け、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品発表や先行情報に早期アクセスできます。
    - **特別割引**: 最新製品の特別割引を楽しめます。
    - **フェスティブプロモーションとプレゼント企画**: プレゼント企画や季節ごとのプロモーションに参加できます。

    👉 探索と創造の準備ができましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！


.. _omv_5:



OpenMediaVaultの設定
=====================================

.. warning::

   OpenMediaVault は **Raspberry Pi OS デスクトップ版には対応していません**。


   ⚠️ **Raspberry Pi OS Lite のバージョン 11（Bullseye）および 12（Bookworm）のみがサポートされています。**


   必ず対応するOSがインストールされており、ネットワーク設定が完了していることを確認してください。
   本手順は :ref:`install_os_sd_rpi` と同様ですが、OSイメージ選択時は Raspberry Pi OS (other) の中から Raspberry Pi OS Lite を選択してください。

   .. image:: img/omv/omv-install-1.png

OpenMediaVault（略称：OMV）は、Debian Linuxをベースとしたオープンソースのネットワーク接続ストレージ（NAS）向けOSで、家庭や小規模オフィス向けにストレージ管理の簡素化と豊富なネットワーク機能を提供します。

以下の手順に従って、Raspberry Pi に OpenMediaVault をインストールしてください。

1. Raspberry Pi にSSH接続
-----------------------------------------------------------

   ターミナルに以下のコマンドを入力します：

   .. code-block:: bash

      ssh pi@raspberrypi.local

   Windowsをお使いの場合は、PuTTYなどのSSHクライアントを使用してください。

2. OpenMediaVaultのインストール
----------------------------------

   ターミナルに以下のコマンドを入力します：

   .. code-block:: bash

      wget https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install  
      chmod +x install  
      sudo ./install -n

   このスクリプトがOpenMediaVaultのインストールを行います。インストール完了後は、Raspberry Piを再起動しないでください。

3. OpenMediaVaultにアクセス
------------------------------

   ブラウザで以下のURLにアクセスしてください：

   .. code-block:: bash

      http://raspberrypi.local

   .. note:: 上記URLでアクセスできない場合は、代わりにIPアドレスを使用してください（例： http://192.168.1.100）。

   ログイン画面が表示されるので、デフォルトのユーザー名とパスワードでログインします。ユーザー名は ``admin`` 、パスワードは ``openmediavault`` です。

   .. image:: img/omv/omv-login.png

   ログイン後、OpenMediaVaultのメイン画面が表示されます。

   .. image:: img/omv/omv-main.png

   これでOpenMediaVaultのインストールとアクセスが完了しました。ストレージの設定・管理を開始できます。



4. RAIDの設定（オプション）
---------------------------------------

   NVMe RAIDは、複数のNVMe SSDをRAID技術で統合し、NVMeの高速性とRAIDの冗長性・性能強化を活かすための構成です。代表的なモードにはRAID 0、1、5、10などがありますが、2基のNVMe SSDを使う場合はRAID 0またはRAID 1が主に使用されます。

   * RAID 0 はストライピング技術で、データを複数のストライプに分割して複数のディスクに分散配置し、読み書き速度を向上させます。ただし冗長性はなく、1台でも障害が発生すると全データが失われます。

   * RAID 1 はミラーリング技術で、同じデータを複数のディスクに複製するため、冗長性が確保されます。読み書き速度は単体ディスクに依存しますが、1台故障してもデータを保持できます。

   .. note:: RAID 0 または RAID 1 を構成するには、最低2台のディスクが必要です。RAID 0では全ディスクの合計容量がRAID容量になりますが、RAID 1では最小のディスク容量がRAID容量になります。

   1. ``System`` メニューから ``Plugins`` を選択し、 ``openmediavault-md`` プラグインを検索してインストールします。

   .. image:: img/omv/omv-raid-1.png

   2. ``Storage`` メニューから ``Disks`` を開き、2台のSSDを消去します。
   
   .. image:: img/omv/omv-raid-2.png

   3. この操作によりすべてのデータが削除されますので、事前にバックアップを取ってください。

   .. image:: img/omv/omv-raid-3.png

   4. 消去モードは ``QUICK`` を選択すれば十分です。

   .. image:: img/omv/omv-raid-4.png

   5. ``Multiple Device`` タブに移動し、 ``Create`` をクリックします。

   .. image:: img/omv/omv-raid-5.png

   6. Levelでは ``Stripe（RAID 0） `` または ``Mirror（RAID 1） `` を選択し、Devicesで消去済みのディスクを指定します。 ``Save`` をクリックし、RAID設定が完了するまで待ちます。

   .. image:: img/omv/omv-raid-6.png

   .. note:: ``500 - Internal Server Error`` が表示された場合は、OMVシステムを再起動してください。

   7. ``Apply`` ボタンをクリックして設定を適用します。

   .. image:: img/omv/omv-raid-7.png

   8. RAIDの状態が ``100%`` になるまで待機してください。

   .. image:: img/omv/omv-raid-8.png

   9. RAID構成が完了すると、ディスクはRAID 0またはRAID 1として一体化され、単一のストレージとして利用できます。

5. ストレージの構成
-----------------------

   OpenMediaVaultのメイン画面で左メニューの ``Storage`` → ``Disks`` を開きます。接続されているすべてのディスクが表示されるので、NVMeストレージが認識されているか確認してください。

   .. image:: img/omv/omv-disk.png

   1. 左側のメニューから ``File System`` を選択し、ファイルシステムを作成してマウントします。ファイルシステムの種類は ``ext4`` を選択してください。

   .. image:: img/omv/omv-mount.png

   2. デバイスを選択し、保存します。
   
   .. note:: RAID構成済みの場合は、RAIDデバイスが一覧に表示されるので、それを選択してください。

   .. image:: img/omv/omv-mount-2.png

   3. ファイルシステム作成中のメッセージが表示されますので、しばらく待ちます。

   .. image:: img/omv/omv-mount-3.png

   4. 完了後、 ``Mount`` 画面に移動します。作成したファイルシステムを選択し、Raspberry Pi にマウントします。

   .. image:: img/omv/omv-mount-4.png

   .. note:: RAIDを使用せず2台のドライブを接続している場合は、もう1台についても上記の手順を繰り返してください。

   5. マウント完了後、 ``Apply`` をクリックして設定を適用すると、ファイルシステム上にディスクが表示されます。

   .. image:: img/omv/omv-mount-5.png

   これでOpenMediaVaultの設定とディスクのマウントが完了しました。以後、ストレージ管理が可能です。


6. 共有フォルダの作成  
---------------------------------------

1. ``Storage`` ページで ``Shared Folders`` タブに移動し、 ``Create`` ボタンをクリックします。

   .. image:: img/omv/omv-share-1.png

2. ``Create Shared Folder`` ページで、共有フォルダの名前、共有するハードドライブ、フォルダのパス、アクセス権限を入力し、 ``Save`` をクリックします。

   .. image:: img/omv/omv-share-2.png

3. 作成した共有フォルダが表示されます。内容に問題がなければ ``Apply`` をクリックして反映します。

   .. image:: img/omv/omv-share-3.png

これで共有フォルダの作成が完了しました。


7. 新しいユーザーの作成  
---------------------------------------

共有フォルダにアクセスするには、新しいユーザーを作成する必要があります。以下の手順に従ってください。

1. ``User`` ページで ``Create`` ボタンをクリックします。

   .. image:: img/omv/omv-user-1.png

2. ``Create User`` ページで、ユーザー名とパスワードを入力し、 ``Save`` をクリックします。

   .. image:: img/omv/omv-user-2.png

これで新しいユーザーの作成が完了しました。


8. 新規ユーザーのアクセス権設定  
---------------------------------------

1. ``Shared Folders`` ページで先ほど作成した共有フォルダを選択し、 ``Permissions`` をクリックします。

   .. image:: img/omv/omv-user-3.png

2. ``Permissions`` ページで、権限を設定し、 ``Save`` をクリックします。

   .. image:: img/omv/omv-user-4.png

3. 最後に ``Apply`` をクリックして設定を反映させます。

   .. image:: img/omv/omv-user-5.png

これでこのユーザーで共有フォルダにアクセスできるようになりました。


9. SMBサービスの設定  
---------------------------------------

1. ``Services`` ページで ``SMB/CIFS`` > ``Setting`` タブを開き、 ``Enable`` にチェックを入れて ``Save`` をクリックします。

   .. image:: img/omv/omv-smb-1.png

2. ``Apply`` をクリックして変更を適用します。

   .. image:: img/omv/omv-smb-2.png

3. ``Shares`` ページに移動し、 ``Create`` をクリックします。

   .. image:: img/omv/omv-smb-3.png

4. ``Create Share`` ページで、共有フォルダのパスを選択し、必要に応じて他のオプションも設定したうえで、 ``Save`` をクリックします。

   .. image:: img/omv/omv-smb-4.png

5. ``Apply`` をクリックして保存します。

   .. image:: img/omv/omv-smb-5.png

これでSMBサービスの設定が完了し、SMBプロトコルを使って共有フォルダにアクセスできるようになります。


10. Windowsから共有フォルダにアクセス  
---------------------------------------

1. ``PC`` を開き、 ``Map network drive`` をクリックします。

   .. image:: img/omv/omv-network-location-1.png

2. ダイアログで、 ``Folder`` 欄に Raspberry Pi のIPアドレス（例： ``\\192.168.1.100\`` ）またはホスト名（例： ``\\pi.local\``）を入力します。

   .. image:: img/omv/omv-network-location-2.png

3. ``参照`` ボタンをクリックし、アクセスしたい共有フォルダを選択します。このとき、先ほど作成したユーザー名とパスワードの入力が求められます。

   .. image:: img/omv/omv-network-location-3.png

4. 「サインイン時に再接続する」にチェックを入れ、 ``Finish`` をクリックします。

   .. image:: img/omv/omv-network-location-4.png

5. これでNASの共有フォルダにアクセスできます。

   .. image:: img/omv/omv-network-location-5.png

10. Macから共有フォルダにアクセス  
-------------------------------------

1. ``Go`` メニューから ``Connect to Server`` を選択します。

   .. image:: img/omv/omv-mac-1.png

2. ダイアログに、Raspberry Pi のIP（例： ``smb://192.168.1.100``）またはホスト名（例： ``smb://pi.local``）を入力します。

   .. image:: img/omv/omv-mac-2.png

3. ``Connect`` をクリックします。

   .. image:: img/omv/omv-mac-3.png

4. ユーザー名とパスワードを入力して ``Connect`` をクリックします。

   .. image:: img/omv/omv-mac-4.png

5. これでMacからNAS共有フォルダにアクセスできます。

   .. image:: img/omv/omv-mac-5.png
