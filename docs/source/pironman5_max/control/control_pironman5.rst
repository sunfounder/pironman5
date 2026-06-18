.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _control_commands_dashboard_max:

5. コマンドまたはダッシュボードによる制御
=======================================================

``pironman5`` モジュールのインストールが完了すると、 ``pironman5.service`` は再起動時に自動で起動します。

Pironman 5 の状態監視や制御は、コマンドラインまたはウェブブラウザで ``http://<ip>:34001`` にアクセスすることでダッシュボード経由でも行えます。

.. note::

    * **Home Assistant** システムでは、 ``http://<ip>:34001`` を開いてダッシュボードからのみ操作・監視が可能です。


.. toctree::
    :maxdepth: 1

    control_with_dashboard
    control_with_commands