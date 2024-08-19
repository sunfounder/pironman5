.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと共に、Raspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームの支援を受けて、アフターセールスの問題や技術的な課題を解決。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベントやプレゼント企画**: プレゼント企画や季節のプロモーションに参加できます。

    👉 探索と創造の旅に出る準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

USB HDMIアダプター
==========================================

.. image:: img/hdmi_adapter.jpeg

このUSB HDMIアダプターボードは、Raspberry Pi 5専用に設計されています。主な機能は、USBおよびHDMI接続をRaspberry PiのUSBインターフェース側に再配置し、アクセスの向上とケーブル管理の効率化を実現することです。

さらに、HDMIポートは標準のHDMI Type Aインターフェースに変換され、より広範な互換性を提供します。

**NVMe追加電源供給**

このボードには、NVMe PIP電源供給用の5V電源ヘッダーが装備されています。拡張ヘッダーと組み合わせることで、NVMeの追加電源インターフェースに接続し、さらなる電源供給が可能です。

**1220RTCバッテリーホルダー**

RTCバッテリーの取り付けを簡単にするために、1220RTCバッテリーホルダーが組み込まれています。このホルダーはSH1.0 2Pリバースケーブルを介してRaspberry PiのRTCインターフェースに接続されます。

バッテリーホルダーは、CR1220およびML1220バッテリーに対応しています。ML1220（リチウム二酸化マンガン電池）を使用する場合、Raspberry Pi上で直接充電設定が可能です。なお、CR1220は充電できません。

**トリクル充電の有効化**

.. warning::

  CR1220バッテリーを使用する場合、トリクル充電を有効にしないでください。バッテリーに不可逆的なダメージを与え、ボードの破損リスクもあります。

デフォルトでは、バッテリーのトリクル充電機能は無効になっています。現在のトリクル充電電圧と制限値は、 ``sysfs`` ファイルで確認できます：

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    0
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

トリクル充電を有効にするには、 ``/boot/firmware/config.txt`` に ``rtc_bbat_vchg`` を追加します：

  * ``/boot/firmware/config.txt`` を開きます。
  
    .. code-block:: shell
    
      sudo nano /boot/firmware/config.txt
      
  * ``rtc_bbat_vchg``を ``/boot/firmware/config.txt`` に追加します。
  
    .. code-block:: shell
    
      dtparam=rtc_bbat_vchg=3000000
  
再起動後、システムは以下を表示します：

.. code-block:: shell

    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage
    3000000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_max
    4400000
    pi@raspberrypi:~ $ cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/charging_voltage_min
    1300000

これで、バッテリーがトリクル充電下にあることが確認されます。この機能を無効にするには、 ``config.txt`` から ``dtparam`` 行を削除してください。
