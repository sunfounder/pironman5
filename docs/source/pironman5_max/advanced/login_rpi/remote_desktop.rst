.. note:: 

    こんにちは！SunFounder の Facebook コミュニティ「Raspberry Pi & Arduino & ESP32 愛好者グループ」へようこそ！同じ情熱を持つ仲間たちと一緒に、Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加するメリット**

    - **専門的なサポート**：購入後の問題や技術的な課題を、コミュニティと当社チームがサポートします。
    - **学びと共有**：スキル向上に役立つヒントやチュートリアルを共有し合いましょう。
    - **新製品の先行情報**：発売前の製品情報やプレビューをいち早く入手できます。
    - **限定割引**：最新製品を対象としたメンバー限定の特別割引をお楽しみください。
    - **キャンペーンやプレゼント企画**：季節ごとのプロモーションやプレゼントに参加できます。

    👉 一緒に創造と冒険を始めましょう！[|link_sf_facebook|] をクリックして、今すぐ参加！

.. _max_remote_desktop:

Raspberry Pi のリモートデスクトップ接続
==================================================

コマンドラインよりもグラフィカルユーザーインターフェース（GUI）を好む方のために、Raspberry Pi はリモートデスクトップ機能に対応しています。本ガイドでは、リモート接続用の VNC（Virtual Network Computing）の設定と使用方法について説明します。

この目的には、 `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ の使用を推奨します。

**Raspberry Pi で VNC サービスを有効化する**

Raspberry Pi OS には VNC サービスがプリインストールされていますが、初期状態では無効になっています。以下の手順で有効化しましょう：

#. Raspberry Pi のターミナルで以下のコマンドを入力します：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 矢印キーで **Interfacing Options** に移動し、 **Enter** を押します。

   .. image:: img/bookwarm_config_interface.png
      :width: 90%
      

#. オプションから **VNC** を選択します。

   .. image:: img/bookwarm_vnc.png
      :width: 90%
      

#. 矢印キーを使って **<Yes>** → **<OK>** → **<Finish>** を選択し、VNC サービスを有効化します。

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%
      

**VNC Viewer によるログイン**

#. ご使用のパソコンに `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ をダウンロードしてインストールします。

#. インストール後、VNC Viewer を起動し、Raspberry Pi のホスト名または IP アドレスを入力して Enter キーを押します。

   .. image:: img/vnc_viewer1.png
      :width: 90%
      

#. ユーザー名とパスワードを求められたら、Raspberry Pi の認証情報を入力して **OK** をクリックします。

   .. image:: img/vnc_viewer2.png
      :width: 90%
      

#. Raspberry Pi のデスクトップ画面にリモートでアクセスできるようになります。

   .. image:: img/bookwarm.png
      :width: 90%

