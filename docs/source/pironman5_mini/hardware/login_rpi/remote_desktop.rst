.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！  
    同じ情熱を持つ仲間たちと一緒に、Raspberry Pi・Arduino・ESP32の世界をさらに深く探求しましょう。

    **Why Join?**

    - **Expert Support**：購入後のトラブルや技術的な問題に対し、コミュニティとサポートチームがしっかりサポートします。
    - **Learn & Share**：チュートリアルやヒントを共有して、スキルアップを目指しましょう。
    - **Exclusive Previews**：新製品の発表や先行情報をいち早く入手できます。
    - **Special Discounts**：最新製品の限定割引をご利用いただけます。
    - **Festive Promotions and Giveaways**：季節限定のキャンペーンやプレゼント企画に参加できます。

    👉 一緒に創造と発見の旅を始めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

.. _remote_desktop_mini:

Raspberry Pi のリモートデスクトップアクセス
==================================================

コマンドラインよりもグラフィカルユーザーインターフェース（GUI）を好む方には、Raspberry Pi のリモートデスクトップ機能が便利です。  
ここでは、リモートアクセスのための VNC（Virtual Network Computing）の設定方法をご紹介します。

VNCアクセスには `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ の使用を推奨します。

**Raspberry Pi 上でVNCサービスを有効にする**

Raspberry Pi OS にはVNCサービスがあらかじめインストールされていますが、デフォルトでは無効化されています。  
以下の手順で有効にしてください：

#. Raspberry Piのターミナルで以下のコマンドを入力します：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 矢印キーで **Interfacing Options** を選び、 **Enter** を押します。

   .. image:: img/bookwarm_config_interface.png
      :width: 90%


#. 表示された選択肢から **VNC** を選びます。

   .. image:: img/bookwarm_vnc.png
      :width: 90%


#. 矢印キーで **<Yes>** → **<OK>** → **<Finish>** を選んでVNCサービスを有効化します。

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%


**VNC Viewer からログインする**

#. 自分のPCに `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ をダウンロード・インストールします。

#. VNC Viewer を起動し、Raspberry Pi のホスト名またはIPアドレスを入力し、Enterキーを押します。

   .. image:: img/vnc_viewer1.png
      :width: 90%


#. ユーザー名とパスワードの入力を求められたら、Raspberry Pi のアカウント情報を入力し、 **OK** をクリックします。

   .. image:: img/vnc_viewer2.png
      :width: 90%


#. Raspberry Pi のデスクトップ画面にリモートアクセスできます。

   .. image:: img/bookwarm.png
      :width: 90%

