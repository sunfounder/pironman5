.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. Profundiza en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.


Pantalla táctil de 3.5 pulgadas
=========================================

.. note::

    La serie Pironman 5 no incluye una pantalla táctil de 3.5 pulgadas.  
    Necesitarás preparar una por tu cuenta o comprarla en nuestro sitio web oficial:

   * `Pantalla táctil de 3.5 pulgadas <https://www.sunfounder.com/products/touchscreen-02>`_

La pantalla táctil de 3.5 pulgadas se conecta directamente al encabezado GPIO de la Raspberry Pi,  
proporcionando tanto visualización como control táctil para el Pironman 5.  
Sigue los pasos cuidadosamente para garantizar la instalación correcta y evitar daños en el hardware.

Más detalles se pueden encontrar aquí:  
`Documentación de la pantalla táctil de 3.5 pulgadas <http://wiki.sunfounder.cc/index.php?title=3.5_Inch_LCD_Touch_Screen_Monitor_for_Raspberry_Pi>`_.


**Ensamblar**

.. image:: img/lcd_to_mini1.jpg
    :width: 340

.. image:: img/lcd_to_mini2.jpg
    :width: 340


.. warning:: 
   
   Al instalar la pantalla táctil de 3.5 pulgadas en el Pironman 5, asegúrate de que los pines estén perfectamente alineados.  
   El encabezado debe coincidir con la interfaz GPIO de la Raspberry Pi sin ningún desplazamiento.  
   Una mala alineación puede dañar la pantalla o incluso la Raspberry Pi.  
   ¡Verifica las conexiones antes de encenderla!

**Quitar el Jumper de RGB**

Al usar el Pironman 5 con la pantalla táctil de 3.5 pulgadas,  
ten en cuenta que los LED RGB en el IO Expander comparten el mismo pin SPI MOSI (GPIO10) que la pantalla.  
Para evitar conflictos y asegurar un funcionamiento adecuado:

1. En el IO Expander, retira el capuchón del jumper de los **pines RGB LED** (arriba de J9).

   .. image:: img/lcd_to_mini0.jpg
      :width: 600
      :align: center

2. Deshabilita el servicio de control de LED RGB:

   .. code-block:: bash

      sudo pironman5 -re false
      sudo systemctl restart pironman5.service

Esto libera la interfaz SPI para la pantalla táctil de 3.5 pulgadas y evita problemas de visualización.


**Instalación del Controlador**

Para obtener instrucciones detalladas, consulte |link_3.5_screen|, que describe la instalación del controlador para diferentes sistemas.
