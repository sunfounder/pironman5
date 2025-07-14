Combine With 3.5 inch LCD
=============================

Esta sección es para los usuarios de Pironman 5 que también hayan adquirido la `pantalla LCD de 3,5 pulgadas <https://www.sunfounder.com/products/touchscreen-02?_pos=2&_sid=839d5db5b&_ss=r>`_.

La pantalla LCD se puede montar directamente en los pines GPIO de la Raspberry Pi, proporcionando funcionalidad de visualización y control táctil para el Pironman 5. Por favor, siga los pasos de instalación correctamente para garantizar el funcionamiento adecuado y evitar daños al hardware.

Puede obtener más información sobre la pantalla LCD y cómo utilizarla en el siguiente enlace:  
`Documentación de la pantalla LCD de 3,5 pulgadas <http://wiki.sunfounder.cc/index.php?title=3.5_Inch_LCD_Touch_Screen_Monitor_for_Raspberry_Pi>`_.


**Assemble**

.. image:: ../img/lcd_to_max1.jpg
    :width: 340

.. image:: ../img/lcd_to_max2.jpg
    :width: 340


.. warning:: Al instalar la pantalla LCD de 3,5 pulgadas en el Pironman 5, asegúrese de que los pines estén perfectamente alineados. El conector del módulo LCD debe coincidir exactamente con la interfaz GPIO de la Raspberry Pi, sin desplazamientos ni desalineaciones. Las conexiones incorrectas pueden dañar la pantalla LCD o incluso la propia Raspberry Pi. ¡Verifique todas las conexiones cuidadosamente antes de encender!


**Remove RGB Jumper**

Cuando se utiliza el Pironman 5 con la pantalla LCD de 3,5 pulgadas, el LED RGB y la pantalla LCD comparten los mismos pines SPI. Para evitar conflictos y garantizar el funcionamiento correcto de la pantalla, se debe desactivar la conexión del LED RGB.

Siga los siguientes pasos:

1. En la **placa de expansión IO**, **retire el jumper conectado a los pines RGB** para desconectar el LED RGB de la interfaz SPI.

   .. image:: ../img/lcd_to_max0.jpg
      :width: 600
      :align: center


2. Ejecute los siguientes comandos para **desactivar el servicio de control del LED RGB**:

   .. code-block:: bash

      pironman5 -re false
      sudo systemctl restart pironman5.service 

Esto liberará la interfaz SPI para la pantalla LCD, evitando conflictos o problemas de visualización.


**Driver Installation**

Este módulo LCD requiere la instalación de un controlador antes de su uso. Los pasos varían según el sistema operativo.

* Para Raspberry Pi OS, puede usar el siguiente comando para instalar el controlador:

   .. code-block:: bash

      sudo rm -rf LCD-show 
      git clone https://github.com/sunfounder/LCD-show.git 
      chmod -R 755 LCD-show 
      cd LCD-show/ 
      sudo ./LCD35-show

   Después de una ejecución exitosa, verá el escritorio de Raspberry Pi en la pantalla LCD de 3,5 pulgadas.

   Si desea rotar la pantalla, puede ejecutar el siguiente comando:

   .. code-block:: bash

      cd LCD-show/
      sudo ./rotate.sh 90   

   Después de la ejecución, el sistema se reiniciará automáticamente y la pantalla se rotará 90 grados con visualización y funcionalidad táctil correctas. Puede reemplazar '90' por 0, 90, 180 o 270 según el ángulo de rotación deseado.

* Para Ubuntu, puede usar el siguiente comando para instalar el controlador:

   .. code-block:: bash

      sudo rm -rf LCD-show-ubuntu 
      git clone https://github.com/sunfounder/LCD-show-ubuntu.git 
      chmod -R 755 LCD-show-ubuntu 
      cd LCD-show-ubuntu/ 
      sudo ./LCD35-show

   Después de una ejecución exitosa, verá el escritorio de Raspberry Pi en la pantalla LCD de 3,5 pulgadas.

   Si desea rotar la pantalla, puede ejecutar el siguiente comando:

   .. code-block:: bash

      cd LCD-show/
      sudo ./rotate.sh 90   

   Después de la ejecución, el sistema se reiniciará automáticamente y la pantalla se rotará 90 grados con visualización y funcionalidad táctil correctas. Puede reemplazar '90' por 0, 90, 180 o 270 según el ángulo de rotación deseado.

* Para Kali Linux, puede usar el siguiente comando para instalar el controlador:

   .. code-block:: bash

      sudo rm -rf LCD-show-kali 
      git clone https://github.com/sunfounder/LCD-show-kali.git 
      chmod -R 755 LCD-show-kali 
      cd LCD-show-kali/ 
      sudo ./LCD35-show

   Después de una ejecución exitosa, verá el escritorio de Raspberry Pi en la pantalla LCD de 3,5 pulgadas.

   Si desea rotar la pantalla, puede ejecutar el siguiente comando:

   .. code-block:: bash

      cd LCD-show/
      sudo ./rotate.sh 90   

   Después de la ejecución, el sistema se reiniciará automáticamente y la pantalla se rotará 90 grados con visualización y funcionalidad táctil correctas. Puede reemplazar '90' por 0, 90, 180 o 270 según el ángulo de rotación deseado.
