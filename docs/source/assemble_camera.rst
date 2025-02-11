Ensamblaje del módulo de cámara
===========================================

Siga estos pasos para ensamblar el módulo de cámara:

1. Retire los dos paneles acrílicos de la carcasa.

   .. image:: img/IN_CMR/IN.CMR.1.png
      :width: 500
      :align: center

2. Desconecte el cable de 2 pines y el FPC como se muestra en la imagen.

   .. image:: img/IN_CMR/IN.CMR.2.png
      :width: 500
      :align: center

3. Desatornille los cuatro tornillos para retirar el grupo de módulos NVMe PIP y el convertidor del interruptor de alimentación.

   .. image:: img/IN_CMR/IN.CMR.3.png
      :width: 500
      :align: center

4. Desmonte el grupo de módulos. Esto implica retirar un remache, lo cual se debe hacer empujando el eje central del remache con un destornillador y luego retirando completamente el remache.

   .. image:: img/IN_CMR/IN.CMR.4.png
      :width: 500
      :align: center

5. Conecte el módulo de cámara al cable FPC.

   .. image:: img/IN_CMR/IN.CMR.5.png
      :width: 500
      :align: center

6. Pase el FPC a través del orificio "CAMERA" en la carcasa.

   .. image:: img/IN_CMR/IN.CMR.6.png
      :width: 500
      :align: center

7. Continúe pasando el FPC a través del orificio "CAMERA" en la carcasa.

   .. image:: img/IN_CMR/IN.CMR.7.png
      :width: 500
      :align: center

8. Conecte el FPC a la Raspberry Pi. Este paso es muy compacto y requiere un manejo cuidadoso.

   .. image:: img/IN_CMR/IN.CMR.8.png
      :width: 500
      :align: center

9. Encienda el dispositivo y verifique si el módulo de cámara está correctamente conectado.

   * Primero, conecte una pantalla a la Raspberry Pi o establezca una conexión VNC.
   * Una vez configurada la pantalla, abra un terminal y ejecute el siguiente comando: ``raspistill -o test.jpg``
   * Si el módulo de cámara funciona correctamente, este comando capturará una imagen y la guardará como ``test.jpg``.
   * Abra ``test.jpg`` para verificar que la imagen se haya capturado correctamente.

10. Vuelva a ensamblar el convertidor del interruptor de alimentación en la carcasa.

   .. image:: img/IN_CMR/IN.CMR.9.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.10.png
      :width: 500
      :align: center

11. Vuelva a ensamblar el NVMe PIP en la carcasa.

   .. image:: img/IN_CMR/IN.CMR.11.png
      :width: 500
      :align: center

   .. image:: img/IN_CMR/IN.CMR.12.png
      :width: 500
      :align: center

12. Vuelva a ensamblar la tapa de la carcasa.

   .. image:: img/IN_CMR/IN.CMR.13.png
      :width: 500
      :align: center

