.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _fans:

Ventiladores
===============

Ventilador de la CPU
---------------------

El ventilador de la CPU en el Pironman 5 es gestionado por el sistema Raspberry Pi y constituye la base de su solución de enfriamiento inteligente, especialmente bajo cargas pesadas. Este sistema combina un ventilador de la CPU principal con dos ventiladores GPIO suplementarios para un rendimiento de enfriamiento mejorado, integrados estrechamente con el sistema de gestión térmica del Raspberry Pi 5.

.. image:: img/fan_tower_cooler.png  
  :width: 600  
  :align: center  

**Características Eléctricas**

* **Voltaje Nominal**: 5 VDC  
* **Voltaje de Inicio**: 4.0 V (a 25°C Encendido/Apagado)  
* **Rango de Voltaje Operativo**: 4.0 ~ 5.5 VDC  
* **Corriente Nominal**: 0.05 A / MÁX. 0.08 A  
* **Potencia Nominal**: 0.25 W / MÁX. 0.40 W  
* **Velocidad Nominal**: 3500±10% RPM (a 25°C, probado después de 3 minutos de operación)  
* **Flujo de Aire Máximo**: 2.46 (MÍN. 2.21) CFM (a presión estática cero)  
* **Presión Estática Máxima**: 0.62 (MÍN. 0.496) mmH2O (a flujo de aire cero)  
* **Ruido Acústico**: 22.31 dB(A) MÁX. 25.31 dB(A)  
* **Expectativa de Vida Útil**: 40,000 horas (a 25°C, 65% de humedad, condiciones normales de habitación)  

**Características Mecánicas**

* **Dimensiones**: 40x10.4x40 mm (LxAxH)  
* **Material del Marco**: Plástico PBT  
* **Material del Impulsor**: Plástico PBT  
* **Tipo de Rodamiento**: Rodamiento Hidráulico  

**Parámetros Ambientales**

* **Temperatura Operativa**: -10°C ~ 70°C  
* **Temperatura de Almacenamiento**: -40°C ~ 75°C  
* **Humedad Operativa**: 5% ~ 90% RH  
* **Humedad de Almacenamiento**: 5% ~ 95% RH  

**Control de Velocidad del Ventilador Según la Temperatura**  

El ventilador de la CPU opera de manera dinámica, ajustando su velocidad de acuerdo con la temperatura del Raspberry Pi 5:

* **Por debajo de 50°C**: El ventilador permanece apagado (0% de velocidad).  
* **A 50°C**: El ventilador opera a baja velocidad (30% de velocidad).  
* **A 60°C**: El ventilador aumenta a velocidad media (50% de velocidad).  
* **A 67.5°C**: El ventilador incrementa a alta velocidad (70% de velocidad).  
* **A 75°C y más**: El ventilador opera a velocidad máxima (100% de velocidad).  

Este control de temperatura a velocidad incluye una histéresis de 5°C para evitar cambios frecuentes en la velocidad. Por ejemplo, el ventilador reducirá su velocidad solo después de que la temperatura baje 5°C por debajo de cada umbral.  

Los siguientes comandos permiten a los usuarios monitorear la operación del ventilador de la CPU:  

Para verificar el estado actual del ventilador:  

.. code-block:: shell

  cat /sys/class/thermal/cooling_device0/cur_state

Ventiladores GPIO
----------------------

.. image:: img/size_fan.png

* **Dimensiones externas**: 40*40*10MM
* **Peso**: 13.5±5g/pcs
* **Duración**: 40,000 horas (temperatura ambiente 25°C)
* **Flujo de aire máximo**: 2.46CFM
* **Presión de aire máxima**: 0.62mm-H2O
* **Sonido acústico**: 22.31dBA
* **Potencia de entrada nominal**: 5V/0.1A
* **Velocidad nominal**: 3500±10%RPM
* **Temperatura de funcionamiento**: -10℃~+70℃
* **Temperatura de almacenamiento**: -30℃~+85℃

