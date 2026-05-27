.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _control_commands_dashboard_mini:

5. Control mediante comandos o desde el panel web
=======================================================

Una vez que hayas instalado correctamente el módulo ``pironman5``, el servicio ``pironman5.service`` se iniciará automáticamente tras reiniciar el sistema.

Puedes supervisar y controlar el Pironman 5 Mini mediante comandos o accediendo al panel web desde la dirección ``http://<ip>:34001``.

.. note::

    * En el sistema **Home Assistant**, solo podrás monitorear y controlar el Pironman 5 Mini a través del panel web, accediendo a ``http://<ip>:34001``.

    .. * En el sistema **Batocera.linux**, solo es posible controlar y monitorear el Pironman 5 Mini mediante comandos. Es importante tener en cuenta que cualquier cambio en la configuración requiere reiniciar el servicio con ``pironman5 restart`` para que tenga efecto.


.. toctree::
    :maxdepth: 1

    control_with_dashboard
    control_with_commands