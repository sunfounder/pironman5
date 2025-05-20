カメラモジュールの組み立て  
===========================================

以下の手順に従って、カメラモジュールを正しく組み立ててください：

1. ケースから2枚のアクリルパネルを取り外します。

   .. image:: img/IN_CMR/IN.CMR.1.png
      :width: 500
      :align: center

2. 下図のように、2ピンワイヤーとFPCケーブルを取り外します。

   .. image:: img/IN_CMR/IN.CMR.2.png
      :width: 500
      :align: center

3. 4本のネジを外し、NVMe PIPおよび電源スイッチコンバーターモジュールを取り外します。

   .. image:: img/IN_CMR/IN.CMR.3.png
      :width: 500
      :align: center

4. モジュールを分解します。リベットを外すには、ドライバーで中央のシャフト部分を押し出し、リベット全体を取り除きます。

   .. image:: img/IN_CMR/IN.CMR.4.png
      :width: 500
      :align: center

5. カメラモジュールをFPCケーブルに接続します。

   .. image:: img/IN_CMR/IN.CMR.5.png
      :width: 500
      :align: center

6. FPCケーブルをケースの「CAMERA」穴に通します。

   .. image:: img/IN_CMR/IN.CMR.6.png
      :width: 500
      :align: center

7. FPCケーブルをさらに奥まで通します。

   .. image:: img/IN_CMR/IN.CMR.7.png
      :width: 500
      :align: center

8. FPCケーブルをRaspberry Pi本体に接続します。この作業は非常にスペースが狭いため、慎重に行ってください。

   .. image:: img/IN_CMR/IN.CMR.8.png
      :width: 500
      :align: center

9. 本体の電源を入れて、カメラモジュールが正しく接続されているか確認します。

   * まず、Raspberry Piにディスプレイを接続するか、VNCでリモート接続します。
   * ディスプレイが使える状態になったら、ターミナルを開き以下のコマンドを実行します： ``raspistill -o test.jpg``
   * カメラが正しく動作していれば、コマンドにより画像が撮影され、 ``test.jpg`` として保存されます。
   * ``test.jpg`` を開いて、画像が正しく撮影されているかを確認してください。

10. 電源スイッチコンバーターモジュールをケースに再び取り付けます。

   .. image:: img/IN_CMR/IN.CMR.9.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.10.png
      :width: 500
      :align: center

11. NVMe PIPをケースに再取り付けします。

   .. image:: img/IN_CMR/IN.CMR.11.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.12.png
      :width: 500
      :align: center

12. ケースカバーを元に戻して組み立てを完了します。

   .. image:: img/IN_CMR/IN.CMR.13.png
      :width: 500
      :align: center

