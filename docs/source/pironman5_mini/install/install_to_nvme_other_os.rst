.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _install_to_nvme_other_mini:

Installation du système d’exploitation sur un SSD NVMe
=============================================================

Si vous utilisez un SSD NVMe et disposez d’un adaptateur pour connecter le SSD NVMe à votre ordinateur afin d’installer le système, vous pouvez suivre le tutoriel ci-dessous pour une installation rapide.

   .. image:: img/m2_nvme_adapter.png
        :width: 300
        :align: center  

**Composants requis**

* Un ordinateur personnel
* Un SSD NVMe
* Un adaptateur NVMe vers USB
* Une carte Micro SD et un lecteur de cartes

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installer le système d’exploitation sur la carte microSD
------------------------------------------------------------------

#. Insérez le **SSD NVMe** dans votre ordinateur à l’aide de l’adaptateur.

2. Lorsque **Raspberry Pi Imager** s’ouvre, vous verrez la page **Device**.  
   Sélectionnez votre modèle de **Raspberry Pi 5** dans la liste.

   .. image:: img/imager_device.png
      :width: 90%

3. Allez dans la section **OS**, faites défiler jusqu’en bas de la page et sélectionnez votre système d’exploitation.

   .. note::

      * Pour **Ubuntu**, cliquez sur **Other general-purpose OS** → **Ubuntu**, puis sélectionnez  
        **Ubuntu Desktop 24.04 LTS (64-bit)** ou **Ubuntu Server 24.04 LTS (64-bit)**.
      * Pour **Kali Linux**, **Home Assistant** et **Homebridge**, cliquez sur  
        **Other specific-purpose OS**, puis sélectionnez le système correspondant.

   .. image:: img/imager_other_os.png
      :width: 90%

4. Dans la section **Storage**, sélectionnez votre **SSD NVMe**. 

   .. image:: img/nvme_storage.png
      :width: 90%

#. Cliquez sur **NEXT**.

   .. note::

      * Pour les systèmes qui **ne peuvent pas être préconfigurés**, cliquer sur **NEXT** ignorera l’étape **Customisation** et passera directement à **Writing**, où le système d’exploitation est écrit sur la carte microSD.
      * Pour les systèmes qui **prennent en charge la préconfiguration**, suivez les étapes de **Customisation** afin de configurer des options telles que le **Hostname**, le **WiFi** et l’**activation de SSH**.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. Lorsque la fenêtre contextuelle **« Write Successful »** apparaît, l’image a été entièrement écrite et vérifiée. Vous pouvez maintenant retirer la carte microSD en toute sécurité et l’utiliser pour démarrer votre Raspberry Pi.
