.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Pi5 NVMe PIP
=================

El Pi5 NVMe PIP (Placa de Expansión PCIe), como lo define la Fundación Raspberry Pi, es una placa adaptadora PCIe diseñada específicamente para unidades de estado sólido NVMe. Es compatible con cuatro tamaños diferentes de SSD NVMe: 2230, 2242, 2260 y 2280, todas encajando en una ranura M.2 con llave M.

.. image:: img/nvme_pip.png

* La placa se conecta a través de un cable FFC inverso de 16 pines y 0.5mm (Cable Plano Flexible) o un cable FPC (Circuito Impreso Flexible) con coincidencia de impedancia personalizada.
* **STA**: Un indicador LED de estado.
* **PWR**: Un indicador LED de alimentación.
* La fuente de alimentación de 3.3V integrada puede soportar hasta 3A de salida. Sin embargo, dado que la interfaz PCIe de Raspberry Pi está limitada a proporcionar 5V/1A de salida (equivalente a 5W), se puede suministrar alimentación adicional para el uso de 3.3V/3A a través del conector J3 desde una fuente de 5V.
* **FORCE ENABLE**: La fuente de alimentación integrada se activa mediante la señal de conmutación desde la interfaz PCIe. Después de que se enciende la Raspberry Pi, se envía una señal para encender la fuente de alimentación de 3.3V. Si algunos sistemas no admiten la señal de conmutación o por otras razones, se puede hacer un cortocircuito en J4 FORCE ENABLE soldando un cable entre las dos almohadillas flotantes para forzar la activación de la fuente de alimentación de 3.3V para alimentar el NVMe.

Acerca del Modelo
---------------------------

Los SSD M.2, conocidos por su tamaño compacto, vienen en varios tipos principalmente diferenciados por su clave (diseño de muesca en el conector) y la interfaz que utilizan. Aquí están los tipos principales:

* **SSD SATA M.2**: Estos utilizan la interfaz SATA, similar a los SSD SATA de 2.5 pulgadas pero en el formato más pequeño M.2. Están limitados por las velocidades máximas del SATA III de alrededor de 600 MB/s. Estos SSD son compatibles con las ranuras M.2 con claves B y M.
* **SSD NVMe M.2**: Estos SSD utilizan el protocolo NVMe sobre carriles PCIe y son significativamente más rápidos que los SSD SATA M.2. Son adecuados para aplicaciones que requieren altas velocidades de lectura/escritura como juegos, edición de video y tareas que requieren un uso intensivo de datos. Estos SSD generalmente requieren ranuras con clave M. Estas unidades utilizan la interfaz PCIe (Interconexión de Componentes Periféricos Express), con diferentes versiones como 3.0, 4.0 y 5.0. Cada nueva versión de PCIe efectivamente duplica la velocidad de transferencia de datos de su predecesora. Sin embargo, la Raspberry Pi 5 utiliza una interfaz PCIe 3.0, capaz de ofrecer velocidades de transferencia de hasta 3.500 MB/s.

Los SSD M.2 vienen en tres tipos de claves principales: clave B, clave M y clave B+M. Sin embargo, más tarde se introdujo la clave B+M, que combina las funcionalidades de la clave B y la clave M. Como resultado, reemplazó la clave B independiente. Consulta la imagen a continuación.

.. image:: img/ssd_key.png


En general, los SSD SATA M.2 tienen clave B+M (pueden encajar en ranuras para módulos con clave B y clave M), mientras que los SSD NVMe M.2 para PCIe 3.0 x4 son de clave M.

.. image:: img/ssd_model2.png

Acerca del Tamaño
-----------------------

Los módulos M.2 vienen en diferentes tamaños y también pueden utilizarse para Wi-Fi, WWAN, Bluetooth, GPS y NFC.

Pironman 5 admite cuatro tamaños de SSD NVMe M.2 (PCIe Gen 2.0 / PCIe Gen 3.0) basados en sus nombres: 2230, 2242, 2260 y 2280. El "22" es el ancho en milímetros (mm) y los dos números siguientes son la longitud. Cuanto más largo sea el disco, más chips de memoria NAND se pueden montar; por lo tanto, mayor será la capacidad.

.. image:: img/m2_ssd_size.png
  :width: 600
