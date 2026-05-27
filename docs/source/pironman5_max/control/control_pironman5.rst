.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _control_commands_dashboard_max:

5. Control con comandos o panel de control
=======================================================

Una vez que hayas instalado correctamente el módulo ``pironman5``, el servicio ``pironman5.service`` se iniciará automáticamente al reiniciar el sistema.

Puedes monitorear y controlar el Pironman 5 mediante comandos o accediendo al panel de control desde la página web en ``http://<ip>:34001``.

.. note::

    * En el sistema **Home Assistant**, solo puedes monitorear y controlar el Pironman 5 a través del panel de control accediendo a la página web en ``http://<ip>:34001``.

.. * En el sistema **Batocera.linux**, solo puedes monitorear y controlar el Pironman 5 mediante comandos. Es importante tener en cuenta que cualquier cambio en la configuración requiere reiniciar el servicio usando ``pironman5 restart`` para que los cambios surtan efecto.


.. toctree::
    :maxdepth: 1

    control_with_dashboard
    control_with_commands
