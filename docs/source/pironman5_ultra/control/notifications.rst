.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _notifications_ultra:

Email and Buzzer Notifications
=========================================

Pironman 5 Ultra can notify you when something happens to the power supply, for example when the external power is disconnected or the battery level runs low. Two channels are available:

* **Email**: send a message to a mailbox through your own SMTP server.
* **Buzzer**: play a short tune on the PiPower 5 board.

Both channels use the same set of events, and each channel can be enabled separately. The events are listed in :ref:`pipower5_events_ultra`.


Email Notifications
----------------------

PiPower 5 sends the email through your own mail account, so you need an SMTP server. Most mail providers offer SMTP access.

#. Turn on SMTP in your mail provider. For Gmail, SMTP is already enabled — you only need to create an **App Password**.

#. Note down the connection details:

   * **SMTP server**: for example ``smtp.gmail.com``
   * **SMTP port**: for example ``465`` for SSL or ``587`` for TLS
   * **Security**: ``None``, ``SSL`` or ``TLS``
   * **SMTP account**: usually your email address
   * **SMTP password**: the dedicated SMTP password or app password

#. Choose the mailbox that receives the notifications. It can be the same as the SMTP account, which means the account sends mail to itself.

#. Enter the details on the Dashboard (**Settings → Send Email**), send a test message with **Test SMTP**, and select the events that should trigger an email.

You can also configure the same settings from the command line:

.. code-block:: shell

   sudo pipower5 -seo low_battery power_disconnected power_restored
   sudo pipower5 -set you@example.com
   sudo pipower5 -ss smtp.gmail.com -smp 465 -se you@gmail.com -spw <APP_PASSWORD> -ssc ssl

* ``-seo`` sets the events that send an email.
* ``-set`` sets the receiving address.
* ``-ss`` / ``-smp`` / ``-se`` / ``-spw`` / ``-ssc`` set the server, port, account, password and security type.

.. note::

   After changing a setting, restart the service to apply it:

   .. code-block:: shell

      sudo systemctl restart pironman5.service


Buzzer Notifications
------------------------

The PiPower 5 board has a buzzer that beeps when a selected event happens. Set the events and the volume on the Dashboard (**Settings → Buzzer**), or with the command line:

.. code-block:: shell

   sudo pipower5 -bzo power_disconnected low_battery
   sudo pipower5 -bzv 5
   sudo pipower5 -bzt power_disconnected

* ``-bzo`` sets the events that trigger the buzzer.
* ``-bzv`` sets the volume, from ``0`` to ``10``.
* ``-bzt`` plays the sound of one event so you can test the volume.

.. note::

   After changing a setting, restart the service to apply it:

   .. code-block:: shell

      sudo systemctl restart pironman5.service
