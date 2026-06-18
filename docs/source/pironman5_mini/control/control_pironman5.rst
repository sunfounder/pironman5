.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


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

    control_with_dashboard
    control_with_commands