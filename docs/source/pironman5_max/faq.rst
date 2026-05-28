.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

FAQ
============


クイックトラブルシューティング
-------------------------------

* OLEDスクリーンが動作しない → :ref:`faq_oled_max`
* RGB LEDが動作しない → :ref:`faq_rgb_max`
* GPIOファンが動作しない → :ref:`faq_gpio_fans_max`
* CPUファンが回らない → :ref:`faq_pwm_fan_max`
* ダッシュボードにデータが表示されない → :ref:`faq_dashboard_max`
* NVMe SSDが認識されない → :ref:`faq_nvme_max`



1. ハードウェア
-------------------------------


.. _com_os_max:

対応システム
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os

電源ボタン
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button
   :end-before: end_faq_power_button

タワークーラーの銅管端部
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copper_pipe_ends
   :end-before: end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_ai_hat
   :end-before: end_faq_ai_hat

Pironman5 Maxの振動スイッチ機能は使用できますか？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

v1.3.6より、OLEDのウェイクアップには電源ボタンを使用します。Raspberry PiのGPIOピンを占有して競合が発生する可能性を防ぐため、振動スイッチのジャンパーを必ず取り外してください。このジャンパーが存在するかご確認いただき、存在しない場合は本通知を無視してください。

.. image:: /pironman5_max/img/remove_vib_jumper.jpg

2. 冷却とファン
-------------------------------

.. _faq_pwm_fan_max:

CPUファンが動作しない
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan


.. _faq_gpio_fans_max:

GPIOファンが動作しない
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_gpio_fans
   :end-before: end_faq_gpio_fans


3. OLEDとRGB
-------------------------------


.. _faq_oled_max:

OLEDスクリーンが動作しない
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_compatible_systems| replace:: :ref:`com_os_max`
.. |link_set_up_pironman5| replace:: :ref:`max_set_up_pironman5`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_oled
   :end-before: end_faq_oled

.. _faq_rgb_max:

RGB LEDが動作しない
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb


.. _faq_customize_oled_max:

OLED表示をカスタマイズする方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_customize_oled
   :end-before: end_faq_customize_oled


4. ダッシュボードとソフトウェア
-------------------------------


.. _faq_dashboard_max:

ダッシュボードにデータが表示されない
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard

Webダッシュボードを無効化する方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_disable_dashboard
   :end-before: end_faq_disable_dashboard


Pironman 5ソフトウェアのアンインストールと再インストール方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_reinstall_pironman5
   :end-before: end_faq_reinstall_pironman5


``pironman5`` コマンドを使用してコンポーネントを制御する方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_commands| replace:: :ref:`max_view_control_commands`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command


5. 起動とストレージ
-------------------------------

OMVを設定した場合でもPironman5の機能は使用できますか？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

はい。OpenMediaVaultはRaspberry Piシステム上で動作します。:ref:`set_up_os_max` の手順に従って設定を続行してください。


PI5が起動しない（赤色LED）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_update_bootloader| replace:: :ref:`update_bootloader_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pi5_boot_fail
   :end-before: end_faq_pi5_boot_fail

.. _faq_nvme_max:

NVMe PIPモジュールが動作しない
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. NVMe PIPモジュールとRaspberry Pi 5を接続しているFPCケーブルがしっかりと取り付けられていることを確認してください。

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(1)-11.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(2)-11.mp4" type="video/mp4">
               Your browser does not support the video tag.
           </video>
       </div>

#. SSDがNVMe PIPモジュールに正しく固定されていることを確認してください。

#. NVMe PIPモジュールのLED状態を確認します：

   すべての接続が完了したら、Pironman 5 MAXの電源を入れ、NVMe PIPモジュール上の2つのインジケーターを確認します：

   * **PWR LED**: 点灯している必要があります。
   * **STA LED**: 点滅していると正常動作を示します。

   .. image:: img/dual_nvme_pip_leds.png

   * **PWR LED** が点灯し **STA LED** が点滅しない場合は、NVMe SSDがRaspberry Piに認識されていないことを意味します。
   * **PWR LED** が消灯している場合、モジュールの ``Force Enable`` ピンをショートしてください。 **PWR LED** が点灯した場合、FPCケーブルの緩みやサポートされていないシステム構成の可能性があります。

   .. image:: img/dual_nvme_pip_j4.png

#. NVMe SSDに適切なオペレーティングシステムがインストールされていることを確認してください。:ref:`install_the_os_max` を参照してください。

#. 問題が解決しない場合は、以下のログファイルを送信してください：

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

コマンドを使用してRaspberry Piのブート順序を変更する方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_command
   :end-before: end_faq_boot_order_command


Raspberry Pi Imagerを使用してブート順序を変更する方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_imager
   :end-before: end_faq_boot_order_imager

システムをSDカードからNVMe SSDにコピーする方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copy_sd_to_nvme
   :end-before: end_faq_copy_sd_to_nvme

6. 高度な使用方法
-------------------------------

保護フィルムの剥がし方
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_remove_film
   :end-before: end_faq_remove_film
