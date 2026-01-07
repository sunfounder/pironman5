.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez vos problèmes après-vente et relevez vos défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives**: Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales**: Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et tirages au sort**: Participez à des tirages au sort et à des promotions festives.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

1. Que devez-vous préparer d’autre ?
======================================

Avant d’assembler et d’utiliser votre Pironman 5, veuillez vous assurer que vous disposez des composants suivants. Certains éléments sont requis pour un fonctionnement de base, tandis que d’autres sont optionnels et dépendent de l’utilisation que vous prévoyez pour votre Raspberry Pi.

Composants requis
------------------------------

* **Raspberry Pi 5**

  Le Pironman 5 est entièrement compatible avec le Raspberry Pi 5.

  .. image:: img/need_pi5.jpg
     :width: 500

* **Alimentation 27 W**

  Il est recommandé d’utiliser l’alimentation officielle 27 W ou |link_sf_27w_supply| pour les produits de la série Pironman 5 afin d’éviter une alimentation insuffisante, qui pourrait provoquer des redémarrages du Raspberry Pi 5.

  .. image:: img/need_power.png
     :width: 600

* **Carte Micro SD**

  Le Raspberry Pi ne dispose pas de disque dur intégré. Il démarre et stocke tous les fichiers sur une **carte Micro SD**.  
  
  .. image:: img/need_sd.jpg
    :width: 200

  * Minimum : **16 Go**  
  * Recommandé : **32 Go** pour une meilleure stabilité  
  * Marque : utilisez des options fiables telles que **SanDisk** ou **Samsung** afin d’éviter les erreurs de lecture/écriture  
  
Composants optionnels
------------------------

* **SSD M.2 NVMe**

  Le Pironman 5 est équipé d’un module NVMe PIP avec un connecteur SSD M.2, compatible avec quatre formats de SSD NVMe M.2 : 2230, 2242, 2260 et 2280. La connexion est certifiée pour des vitesses Gen 2.0 (5 GT/s), mais vous pouvez la forcer en Gen 3.0 (10 GT/s).

  .. image:: img/need_nvme.png
    :width: 500

* **Moniteur (HDMI ou TV)** 

  Pour les débutants, nous recommandons vivement un écran doté d’une entrée HDMI, afin de pouvoir configurer facilement Raspberry Pi OS et exécuter des programmes graphiques.  

  .. image:: img/need_screen.png
    :width: 400

* **Câble HDMI**

  Les ports HDMI du Raspberry Pi 5 ont été adaptés à des interfaces HDMI Type A standard via un adaptateur USB HDMI. Par conséquent, un câble HDMI vers HDMI standard est nécessaire pour connecter le Pironman 5 MAX à un écran.

  .. image:: img/need_hdmi.png
    :width: 400

* **Clavier et souris**

  Très utiles lors de la configuration initiale de Raspberry Pi OS. Par la suite, vous pourrez passer à un accès à distance (SSH/VNC), mais pour les débutants, nous recommandons de préparer un ensemble USB ou sans fil de base.  

  .. image:: img/need_keyboard_mouse.png
    :width: 500
 

**Conseils de préparation**

* Si vous avez acheté ce kit, la plupart des accessoires sont inclus, mais vous devez tout de même préparer séparément la carte Raspberry Pi, la carte Micro SD et l’adaptateur d’alimentation.  
* Vous ne savez pas quoi acheter ? Le choix le plus stable et universel est : **Raspberry Pi 5 (2 Go) + alimentation officielle + carte Micro SD de 32 Go**.  
