カメラモジュールの組み立て
===========================================

以下の手順に従ってカメラモジュールを組み立ててください:

1. ケースから2枚のアクリルパネルを取り外します。

   .. image:: img/IN_CMR/IN.CMR.1.png
      :width: 500
      :align: center

2. 画像のように2ピンワイヤーとFPCを取り外します。

   .. image:: img/IN_CMR/IN.CMR.2.png
      :width: 500
      :align: center

3. 4本のネジを外し、NVMe PIPと電源スイッチコンバーターモジュール群を取り外します。

   .. image:: img/IN_CMR/IN.CMR.3.png
      :width: 500
      :align: center

4. モジュール群を分解します。リベットを取り外す必要があり、ドライバーを使ってリベットの中央シャフトを押し出し、リベット全体を取り外します。

   .. image:: img/IN_CMR/IN.CMR.4.png
      :width: 500
      :align: center

5. カメラモジュールをFPCケーブルに接続します。

   .. image:: img/IN_CMR/IN.CMR.5.png
      :width: 500
      :align: center

6. FPCをケースの「CAMERA」穴に通します。

   .. image:: img/IN_CMR/IN.CMR.6.png
      :width: 500
      :align: center

7. FPCをさらに「CAMERA」穴を通して進めます。

   .. image:: img/IN_CMR/IN.CMR.7.png
      :width: 500
      :align: center

8. FPCをRaspberry Piに接続します。このステップは非常にコンパクトで、慎重に取り扱う必要があります。

   .. image:: img/IN_CMR/IN.CMR.8.png
      :width: 500
      :align: center

9. ホストの電源を入れ、カメラモジュールが正しく接続されているか確認します。

   * まず、Raspberry Piにディスプレイを接続するか、VNC接続を確立します。
   * ディスプレイが設定されたら、ターミナルを開いて以下のコマンドを実行します: ``raspistill -o test.jpg``
   * カメラモジュールが正しく動作していれば、このコマンドにより画像が撮影され、 ``test.jpg`` として保存されます。
   * ``test.jpg`` を開き、画像が正常に撮影されているか確認します。

10. 電源スイッチコンバーターをケースに再組み立てします。

   .. image:: img/IN_CMR/IN.CMR.9.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.10.png
      :width: 500
      :align: center

11. NVMe PIPをケースに再組み立てします。

   .. image:: img/IN_CMR/IN.CMR.11.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.12.png
      :width: 500
      :align: center

12. ケースカバーを再組み立てします。

   .. image:: img/IN_CMR/IN.CMR.13.png
      :width: 500
      :align: center

