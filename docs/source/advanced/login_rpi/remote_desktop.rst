.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Facebookで、他のエンスージアストたちと一緒にRaspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームのサポートで、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表や先行情報に早期アクセスが可能です。
    - **特別割引**: 最新製品を特別割引で購入できます。
    - **フェスティブプロモーションとプレゼント**: プレゼント企画やホリデープロモーションに参加できます。

    👉 私たちと一緒に発見と創造を始めましょう！ [|link_sf_facebook|] をクリックして、今すぐ参加してください！

.. _remote_desktop:

Raspberry Piのリモートデスクトップアクセス
==================================================

コマンドラインよりもグラフィカルユーザーインターフェース（GUI）を好む方のために、Raspberry Piはリモートデスクトップ機能をサポートしています。このガイドでは、VNC（Virtual Network Computing）を使用したリモートアクセスの設定と使用方法について説明します。

この目的には、 `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_  の使用をお勧めします。

**Raspberry PiでVNCサービスを有効化する方法**

Raspberry Pi OSにはVNCサービスがプリインストールされていますが、デフォルトでは無効になっています。以下の手順で有効にしてください。

#. Raspberry Piのターミナルで次のコマンドを入力します:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 矢印キーを使って **Interfacing Options** に移動し、 **Enter** を押します。

   .. image:: img/bookwarm_config_interface.png
      :width: 90%
      

#. オプションから **VNC** を選択します。

   .. image:: img/bookwarm_vnc.png
      :width: 90%
      

#. 矢印キーで **<Yes>** -> **<OK>** -> **<Finish>** を選択し、VNCサービスの有効化を完了します。

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%
      

**VNC Viewerを使ってログインする方法**

#. 個人用コンピュータに `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ をダウンロードしてインストールします。

#. インストール後、VNC Viewerを起動します。Raspberry Piのホスト名またはIPアドレスを入力してEnterキーを押します。

   .. image:: img/vnc_viewer1.png
      :width: 90%
      

#. ユーザー名とパスワードを入力し、 **OK** をクリックします。

   .. image:: img/vnc_viewer2.png
      :width: 90%
      

#. これで、Raspberry Piのデスクトップインターフェースにアクセスできます。

   .. image:: img/bookwarm.png
      :width: 90%
      

