.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Dual NVMe PIP
=====================

El **Dual NVMe PIP** (Placa Periférica PCIe), según lo definido por la Fundación Raspberry Pi, es un adaptador PCIe diseñado específicamente para unidades de estado sólido NVMe.

La interfaz PCIe de la Raspberry Pi 5 ofrece de forma nativa un único carril **Gen2 x1** (500 MB/s). Al integrar el chip conmutador PCIe **ASM1182e**, el Dual NVMe PIP lo expande a **dos carriles independientes Gen2 x1**, permitiéndote conectar:

* **Dos SSD NVMe M.2**, o  
* **Un SSD NVMe M.2 + un acelerador de IA M.2 Hailo-8/8L**  

**Notas Clave**:

* No se soporta Gen3  
* Soporta tamaños de SSD NVMe: **2230**, **2242**, **2260**, **2280** (todos en ranuras M.2 con llave M)  

.. image:: img/nvme_pip.png

* La placa se conecta a través de un cable FFC (Flexible Flat Cable) inverso de 16 pines y 0.5mm o un cable FPC (Flexible Printed Circuit) personalizado con impedancia adaptada.  
* **STA**: Indicador LED de estado.  
* **PWR**: Indicador LED de encendido.  
* La fuente de alimentación integrada de 3.3V puede soportar hasta 3A de salida. Sin embargo, dado que la interfaz PCIe de la Raspberry Pi está limitada a proporcionar 5V/1A de salida (equivalente a 5W), se puede suministrar energía adicional para el uso de 3.3V/3A a través del conector J3 desde una fuente de 5V.  
* **FORCE ENABLE**: La fuente de alimentación integrada se activa mediante la señal de interruptor de la interfaz PCIe. Después de encender la Raspberry Pi, esta envía una señal para activar la fuente de 3.3V. Si algunos sistemas no soportan la señal de interruptor o por otras razones, puedes hacer un cortocircuito en J4 FORCE ENABLE soldando un cable entre las dos almohadillas libres para forzar que la fuente de 3.3V integrada alimente al NVMe.

Sobre el modelo
---------------------------

Los SSD M.2, conocidos por su formato compacto, se presentan en varias versiones que se diferencian principalmente por el tipo de llave (notch) y la interfaz que utilizan. A continuación se describen los principales tipos:

* **SSD M.2 SATA**: Utilizan la interfaz SATA, similar a los SSD de 2.5 pulgadas pero en formato M.2. Están limitados por la velocidad máxima de SATA III (~600 MB/s). Son compatibles con ranuras M.2 con llave B o M.
* **SSD M.2 NVMe**: Usan el protocolo NVMe sobre carriles PCIe y son mucho más rápidos que los SATA. Son ideales para tareas que requieren altas velocidades de lectura/escritura como juegos, edición de video o procesamiento de datos. Generalmente requieren ranuras con llave M. Utilizan la interfaz PCIe (Peripheral Component Interconnect Express), con versiones como 3.0, 4.0 y 5.0. Cada nueva versión duplica la velocidad de transferencia respecto a la anterior. No obstante, el Raspberry Pi 5 utiliza PCIe 3.0, capaz de alcanzar velocidades de hasta 3,500 MB/s.

Existen tres tipos de llaves en SSD M.2: llave B, llave M y llave B+M. Esta última combina la funcionalidad de ambas y ha reemplazado a la llave B en la mayoría de los casos. Consulta la siguiente imagen.

.. image:: img/ssd_key.png


En general, los SSD M.2 SATA usan llave B+M (compatibles tanto con ranuras B como M), mientras que los SSD M.2 NVMe PCIe 3.0 x4 usan llave M.

.. image:: img/ssd_model2.png

Sobre la longitud
-----------------------

Los módulos M.2 están disponibles en diferentes tamaños y también pueden utilizarse para Wi-Fi, WWAN, Bluetooth, GPS y NFC.

El Pironman 5 MAX admite cuatro tamaños de SSD NVMe M.2 (PCIe Gen 2.0 / Gen 3.0): 2230, 2242, 2260 y 2280. El número "22" indica el ancho en milímetros, y los siguientes dos dígitos indican la longitud. Cuanto más largo sea el módulo, mayor será el número de chips de memoria NAND que puede alojar, lo que se traduce en mayor capacidad.


.. image:: img/m2_ssd_size.png
  :width: 600

