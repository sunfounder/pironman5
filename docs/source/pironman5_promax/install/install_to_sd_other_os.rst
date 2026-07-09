.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _install_to_sd_other_promax:

Installation du système d'exploitation sur une carte Micro SD
==================================================================================

Si vous utilisez une carte Micro SD, vous pouvez suivre le tutoriel ci-dessous pour installer le système sur votre carte Micro SD.

**Composants requis**

* Un ordinateur personnel
* Une carte Micro SD et un lecteur de carte

.. include:: install_to_sd_rpi.rst
   :start-after: start_install_imager
   :end-before: end_install_imager

2. Installer le système d'exploitation sur la carte microSD
------------------------------------------------------------------------

1. Insérez votre carte microSD dans votre ordinateur à l'aide d'un lecteur de carte.
   Avant de continuer, sauvegardez toutes les données importantes sur la carte, car elles seront effacées.

   .. image:: img/insert_sd.png
      :width: 90%

2. Lorsque **Raspberry Pi Imager** s'ouvre, vous verrez la page **Périphérique**.
   Sélectionnez votre modèle **Raspberry Pi 5** dans la liste.

   .. image:: img/imager_device.png
      :width: 90%

3. Allez dans la section **Système d'exploitation**, descendez en bas de la page et sélectionnez votre système d'exploitation.

   .. note::

      * Pour **Ubuntu**, cliquez sur **Autres systèmes d'exploitation généralistes** → **Ubuntu**, puis sélectionnez
        **Ubuntu Desktop 24.04 LTS (64-bit)** ou **Ubuntu Server 24.04 LTS (64-bit)**.
      * Pour **Kali Linux** et **Homebridge**, cliquez sur
        **Autres systèmes d'exploitation spécifiques**, puis sélectionnez le système correspondant.

   .. warning::

      Quel que soit le système choisi, veillez à sélectionner une version **64 bits**. Sur un système **32 bits**, certains paquets ne sont disponibles que pour ``aarch64`` (64 bits), et certaines fonctionnalités risquent de ne pas s’installer ou de ne pas fonctionner correctement.

   .. image:: img/imager_other_os.png
      :width: 90%

4. Dans la section **Stockage**, sélectionnez votre carte microSD.
   Par sécurité, il est recommandé de débrancher les autres périphériques de stockage USB afin que seule la carte microSD apparaisse dans la liste.

   .. image:: img/imager_storage.png
      :width: 90%

#. Cliquez sur **SUIVANT**.

   .. note::

      * Pour les systèmes qui **ne peuvent pas être configurés à l'avance**, cliquer sur **SUIVANT** ignorera l'étape de **Personnalisation** et passera directement à **Écriture**, où le système d'exploitation est écrit sur la carte microSD.
      * Pour les systèmes qui **prennent en charge la pré-configuration**, suivez les étapes de **Personnalisation** pour configurer des options telles que **Nom d'hôte**, **WiFi** et **Activer SSH**.

   .. image:: img/imager_write_other_os.png
      :width: 90%

#. Lorsque la fenêtre contextuelle **« Écriture réussie »** apparaît, l'image a été entièrement écrite et vérifiée. Vous pouvez maintenant retirer la carte microSD en toute sécurité et l'utiliser pour démarrer votre Raspberry Pi.