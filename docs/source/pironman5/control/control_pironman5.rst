.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _control_commands_dashboard_5:

5. コマンドまたはダッシュボードでの制御
=======================================================

``pironman5`` モジュールを正常にインストールした後、再起動時に ``pironman5.service`` が自動的に開始されます。

Pironman 5はコマンドを使用して監視および制御することができ、または ``http://<ip>:34001`` でダッシュボードにアクセスして制御することができます。

.. note::

    * **Home Assistant** システムの場合、 ``http://<ip>:34001`` を開いてダッシュボードを通じてのみPironman 5を監視および制御することができます。


.. toctree::
    :maxdepth: 1

    control_with_dashboard
    control_with_commands