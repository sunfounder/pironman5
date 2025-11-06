.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと一緒に、Raspberry Pi、Arduino、ESP32についてさらに深く掘り下げていきましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームのサポートを受け、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品発表や先行情報に早期アクセスできます。
    - **特別割引**: 最新製品の特別割引を楽しめます。
    - **フェスティブプロモーションとプレゼント企画**: プレゼント企画や季節ごとのプロモーションに参加できます。

    👉 探索と創造の準備ができましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _set_up_umbrel:

Umbrel OSでのセットアップ
======================================================================

Raspberry Pi 5にUmbrel OSをインストールしている場合は、コマンドラインを使用してPironman 5を設定する必要があります。以下に詳細な手順を示します。

#. Raspberry Pi 5をEthernetケーブルでネットワークに接続します。この手順は、Raspberry Piにインターネット接続を確保するために重要です。

#. ブラウザで次のURLにアクセスします： ``http://umbrel.local``。ページが開かない場合は、ルーターでUmbrelデバイスのIPアドレスを確認し、例：``http://192.168.1.50`` にアクセスしてください。

   .. image:: img/umbrel_local.png

#. ユーザー名とパスワードを設定してUmbrelアカウントを作成します。このパスワードは今後Umbrelへのリモートアクセスに使用されるため、忘れないようにしてください。

   .. image:: img/umbrel_account.png

#. **Next** をクリックしてUmbrelのセットアップを完了し、デスクトップ環境に入ります。

   .. image:: img/umbrel_desktop.png

#. ターミナルを開きます。デスクトップから **Settings** アイコンをクリックし、**Advanced Settings** を選択して **Open** をクリックします。

   .. image:: img/umbrel_setting.png

#. **Open Terminal** をクリックします。

   .. image:: img/umbrel_open_terminal.png

#. Umbrel OS内または特定のアプリ内でターミナルを開くことができます。どちらの方法でもターミナルインターフェースにアクセスできます。

   .. image:: img/umbrel_terminal.png

#. GitHubからコードをダウンロードし、``pironman5`` モジュールをインストールします。

   .. code-block:: shell

      cd ~
      git clone -b base https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

#. インストールが完了したら、次のコマンドを入力してRaspberry Piを再起動します。

   .. code-block:: shell

      sudo reboot

#. 再起動後、``pironman5.service`` が自動的に起動します。Pironman 5の主な初期設定は以下の通りです：
   
   * OLEDディスプレイには、CPU、RAM、ディスク使用量、CPU温度、Raspberry PiのIPアドレスが表示されます。
   * 4つのWS2812 RGB LEDが青色の呼吸モードで点灯します。
     
   .. note::
    
     RGBファンはデフォルトで **常時オン** モードに設定されています。作動温度の調整に関する情報は、:ref:`cc_control_fan` を参照してください。

#. ``systemctl`` ツールを使用して、``pironman5.service`` を ``start``、``stop``、``restart``、または ``status`` で操作できます。

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``：Pironman 5の設定変更を適用する際に使用します。
   * ``start/stop``：``pironman5.service`` を有効または無効にします。
   * ``status``：``systemctl`` ツールを使用して ``pironman5`` プログラムの動作状態を確認します。

.. note::

   これでPironman 5のセットアップは完了です。すぐに使用を開始できます。
   
   各コンポーネントの詳細な制御方法については、:ref:`control_commands_dashboard_5` を参照してください。



