.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32の世界を、同じ興味を持つ仲間たちと一緒により深く探究しましょう。

    **なぜ参加するのか？**

    - **エキスパートサポート**：購入後の問題や技術的な課題も、コミュニティやSunFounderチームのサポートで安心。
    - **学びと共有**：役立つヒントやチュートリアルを共有して、スキルをさらにレベルアップ。
    - **新製品の先行公開**：新製品の発表やプレビューにいち早くアクセス可能。
    - **Special Discounts**：最新製品を対象とした特別割引が受けられます。
    - **Festive Promotions and Giveaways**：プレゼント企画や季節限定キャンペーンにも参加可能！

    👉 一緒に創造と発見の旅を始めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

.. _set_up_umbrel:

Umbrel OSでのセットアップ
======================================================================

Raspberry Pi 5にUmbrel OSをインストールしている場合は、コマンドラインを使用してPironman 5 Miniを設定する必要があります。以下に詳細な手順を示します。

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

#. 再起動後、``pironman5.service`` が自動的に起動します。Pironman 5 Miniの主な初期設定は以下の通りです：
   
   * OLEDディスプレイには、CPU、RAM、ディスク使用量、CPU温度、Raspberry PiのIPアドレスが表示されます。
   * 4つのWS2812 RGB LEDが青色の呼吸モードで点灯します。
     
   .. note::
    
     RGBファンはデフォルトで **常時オン** モードに設定されています。作動温度の調整に関する情報は、:ref:`cc_control_fan` を参照してください。

#. ``systemctl`` ツールを使用して、``pironman5.service`` を ``start``、``stop``、``restart``、または ``status`` で操作できます。

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``：Pironman 5 Miniの設定変更を適用する際に使用します。
   * ``start/stop``：``pironman5.service`` を有効または無効にします。
   * ``status``：``systemctl`` ツールを使用して ``pironman5`` プログラムの動作状態を確認します。

.. note::

   これでPironman 5 Miniのセットアップは完了です。すぐに使用を開始できます。
   
   各コンポーネントの詳細な制御方法については、:ref:`control_commands_dashboard_mini` を参照してください。
