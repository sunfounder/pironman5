.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d’autres passionnés pour approfondir vos connaissances et vos projets autour du Raspberry Pi, d’Arduino et d’ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes techniques et après-vente grâce à l’aide de notre équipe et de notre communauté.
    - **Apprendre & Partager** : Échangez des astuces et tutoriels pour développer vos compétences.
    - **Avant-premières exclusives** : Soyez parmi les premiers à découvrir nos nouveaux produits et à accéder à des aperçus exclusifs.
    - **Réductions spéciales** : Bénéficiez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des concours et événements spéciaux pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _max_install_to_sd_ubuntu:

Installation du système d’exploitation sur une carte Micro SD
=====================================================================

Si vous utilisez une carte Micro SD, vous pouvez suivre le tutoriel ci-dessous pour y installer le système.


**Composants requis**

* Un ordinateur personnel
* Une carte Micro SD et un lecteur

**Étapes**

#. Rendez-vous sur la page |link_batocera_download|, sélectionnez **Raspberry Pi 5 B**, puis cliquez sur Télécharger.

   .. image:: img/batocera_download.png
      :width: 90%

#. Décompressez le fichier téléchargé ``batocera-xxx-xx-xxxxxxxx.img.gz``.

#. Insérez la carte SD dans votre ordinateur ou ordinateur portable à l’aide d’un lecteur.

#. Dans le |link_rpi_imager|, cliquez sur l’onglet **Operating System**.

   .. image:: img/os_choose_os.png
      :width: 90%

#. Faites défiler jusqu’en bas de la page et sélectionnez **Use Custom**.

   .. image:: img/batocera_os_use_custom.png
      :width: 90%


#. Sélectionnez le fichier système que vous venez de décompresser, ``batocera-xxx-xx-xxxxxxxx.img``, puis cliquez sur **Open**.

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. Cliquez sur **Choose Storage** et sélectionnez le périphérique de stockage approprié pour l’installation.

   .. image:: img/os_choose_sd.png
      :width: 90%


#. Cliquez maintenant sur **NEXT**. Si le support contient déjà des données, veillez à les sauvegarder. Cliquez sur **Yes** si aucune sauvegarde n’est nécessaire.

   .. image:: img/os_continue.png
      :width: 90%


#. Lorsque la fenêtre "Write Successful" apparaît, cela signifie que l’image a bien été écrite et vérifiée. Vous êtes maintenant prêt à démarrer votre Raspberry Pi depuis la carte Micro SD !
