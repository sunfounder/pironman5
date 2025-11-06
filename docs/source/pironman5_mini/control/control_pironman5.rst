.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！同じ情熱を持つ仲間たちと共に、Raspberry Pi・Arduino・ESP32の世界をさらに深く楽しみましょう。

    **なぜ参加するのか？**

    - **エキスパートサポート**：購入後のトラブルや技術的な課題を、コミュニティと専任チームがサポートします。
    - **学びと共有**：チュートリアルやヒントを共有し、スキルアップを図りましょう。
    - **新製品の先行公開**：新製品の先行情報や発表をいち早くチェック。
    - **Special Discounts**：最新製品に適用されるメンバー限定割引を提供。
    - **Festive Promotions and Giveaways**：プレゼント企画や季節限定のキャンペーンにも参加可能です。

    👉 探求と創造の旅を私たちと一緒に始めませんか？[|link_sf_facebook|] をクリックして、今すぐご参加ください！

.. _control_commands_dashboard_mini:

5. コマンドまたはダッシュボードによる操作
=======================================================

``pironman5`` モジュールのインストールが正常に完了すると、再起動時に ``pironman5.service`` が自動で起動します。

Pironman 5 Mini の状態監視や操作は、コマンドまたはWebブラウザから ``http://<ip>:34001`` にアクセスすることで利用可能なダッシュボードを通じて行えます。

.. note::

    * **Home Assistant** システムでは、Webページ ``http://<ip>:34001`` を開いてダッシュボード経由でのみPironman 5 Miniを監視・操作できます。

    .. * **Batocera.linux** システムでは、Pironman 5 Mini の操作はコマンド経由のみ対応しています。設定を変更した場合は ``pironman5 restart`` によるサービスの再起動が必要です。再起動しない限り、変更は反映されません。


.. toctree::
    :maxdepth: 1

    control_with dashboard 
    control_with_commands