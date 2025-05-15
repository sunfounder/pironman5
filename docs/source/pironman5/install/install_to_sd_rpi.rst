.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと一緒に、Raspberry Pi、Arduino、ESP32についてさらに深く掘り下げていきましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームのサポートを受け、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品発表や先行情報に早期アクセスできます。
    - **特別割引**: 最新製品の特別割引を楽しめます。
    - **フェスティブプロモーションとプレゼント企画**: プレゼント企画や季節ごとのプロモーションに参加できます。

    👉 探索と創造の準備ができましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _install_os_sd_rpi:

Micro SDカードにOSをインストールする
============================================================
Micro SDカードを使用している場合は、以下のチュートリアルに従ってMicro SDカードにシステムをインストールできます。

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/-5rTwJ0oMVM?start=343&end=414&si=je5SaLccHzjjEhuD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**必要なコンポーネント**

* パーソナルコンピュータ
* Micro SDカードおよびリーダー

**手順**

#. リーダーを使用してSDカードをコンピュータまたはノートパソコンに挿入します。

#. |link_rpi_imager| 内で、 **Raspberry Pi デバイス** をクリックし、ドロップダウンリストから **Raspberry Pi 5** モデルを選択します。

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. **オペレーティングシステム** を選択し、推奨されるオペレーティングシステムバージョンを選びます。

   .. image:: img/os_choose_os.png
      :width: 90%

#. **ストレージの選択** をクリックし、インストール先の適切なストレージデバイスを選びます。

   .. image:: img/os_choose_sd.png
      :width: 90%

#. **次へ** をクリックし、 **設定を編集** してOS設定をカスタマイズします。

   .. image:: img/os_enter_setting.png
      :width: 90%
      

   * Raspberry Piの **ホスト名** を定義します。ホスト名は、Raspberry Piのネットワーク識別子です。 ``<hostname>.local`` または ``<hostname>.lan`` を使用してPiにアクセスできます。

     .. image:: img/os_set_hostname.png
   

   * Raspberry Piの管理者アカウントの **ユーザー名** と **パスワード** を作成します。ユニークなユーザー名とパスワードを設定することは、デフォルトパスワードのないRaspberry Piを保護するために重要です。

     .. image:: img/os_set_username.png      

   * ワイヤレスLANを設定するために、ネットワークの **SSID** と **パスワード** を入力します。

     .. note::

       ``Wireless LAN country`` には、あなたの所在地に対応する2文字の `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ を設定してください。

     .. image:: img/os_set_wifi.png


   * Raspberry Piにリモート接続するために、サービスタブでSSHを有効にします。

     * **パスワード認証** の場合は、一般タブからユーザー名とパスワードを使用します。
     * 公開鍵認証の場合は、「公開鍵認証のみを許可」を選択します。RSAキーを持っている場合は、それが使用されます。持っていない場合は、「Run SSH-keygen」をクリックして新しいキーペアを生成してください。

     .. image:: img/os_enable_ssh.png

   * **オプション** メニューでは、書き込み中のImagerの動作を構成できます。書き込み完了時にサウンドを再生する、メディアを書き込み後に取り出す、テレメトリを有効にするなどのオプションが含まれます。

     .. image:: img/os_options.png

#. OSカスタマイズ設定の入力が完了したら、 **保存** をクリックしてカスタマイズを保存します。次に、イメージの書き込み時にカスタマイズを適用するために **Yes** をクリックします。

   .. image:: img/os_click_yes.png
      :width: 90%
      

#. SDカードに既存のデータが含まれている場合は、データ損失を防ぐためにバックアップを行ってください。バックアップが不要であれば、 **Yes** をクリックして続行します。

   .. image:: img/os_continue.png
      :width: 90%
      

#. 「書き込み成功」のポップアップが表示されたら、イメージが完全に書き込まれ、検証されています。これでMicro SDカードからRaspberry Piを起動する準備が整いました！

   .. image:: img/os_finish.png
      :width: 90%
      
