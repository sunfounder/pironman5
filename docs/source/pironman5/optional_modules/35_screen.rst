.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi, Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Avant-premières exclusives**: Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales**: Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et tirages au sort**: Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !


Écran tactile 3,5 pouces  
=============================

.. note::

    La série Pironman 5 n’inclut pas d’écran tactile de 3,5 pouces.  
    Vous devrez en préparer un vous-même ou l’acheter sur notre site officiel :

   * `Écran tactile 3,5 pouces <https://www.sunfounder.com/products/touchscreen-02>`_

L’écran tactile de 3,5 pouces se connecte directement à l’en-tête GPIO du Raspberry Pi,  
fournissant à la fois l’affichage et le contrôle tactile pour le Pironman 5.  
Veuillez suivre attentivement les étapes afin de garantir une installation correcte et d’éviter tout dommage matériel.

Plus de détails peuvent être trouvés ici :  
`Documentation de l’écran tactile 3,5 pouces <http://wiki.sunfounder.cc/index.php?title=3.5_Inch_LCD_Touch_Screen_Monitor_for_Raspberry_Pi>`_.


**Assemblage**

.. image:: img/lcd_to_pironman5.png
    :width: 340

.. image:: img/lcd_to_pironman5.jpg
    :width: 340


.. warning:: 
   
   Lors de l’installation de l’écran tactile 3,5 pouces sur le Pironman 5, assurez-vous que les broches soient parfaitement alignées.  
   L’en-tête doit correspondre exactement à l’interface GPIO du Raspberry Pi, sans décalage.  
   Un mauvais alignement peut endommager l’écran ou même le Raspberry Pi.  
   Vérifiez soigneusement les connexions avant la mise sous tension !

**Retirer le cavalier RGB**

Lorsque vous utilisez le Pironman 5 avec l’écran tactile 3,5 pouces,  
notez que les LED RGB de l’IO Expander partagent la même broche SPI MOSI (GPIO10) que l’écran.  
Pour éviter les conflits et garantir un fonctionnement correct :

1. Sur l’IO Expander, retirez le cavalier des **broches RGB LED** (au-dessus de J9).

   .. image:: img/lcd_to_max0.jpg
      :width: 600
      :align: center

2. Désactivez le service de contrôle des LED RGB :

   .. code-block:: bash

      sudo pironman5 -re false
      sudo systemctl restart pironman5.service

Cela libère l’interface SPI pour l’écran tactile 3,5 pouces et évite les problèmes d’affichage.


**Installation du pilote**

Avant d’utiliser l’écran tactile 3,5 pouces, vous devrez installer les pilotes.

Conseils généraux :

* Assurez-vous que git est installé (``sudo apt install git``).  
* L’installation du pilote prend 1 à 3 minutes.  
* Le système redémarrera automatiquement.

Suivez les instructions selon votre système d’exploitation ci-dessous :

* **Pour Raspberry Pi OS** :

  .. code-block:: bash
  
     sudo rm -rf LCD-show 
     git clone https://github.com/sunfounder/LCD-show.git 
     chmod -R 755 LCD-show 
     cd LCD-show/ 
     sudo ./LCD35-show
  
  Après l’installation, le bureau s’affichera sur l’écran tactile 3,5 pouces.
  
  Pour faire pivoter l’affichage :
  
  .. code-block:: bash
  
     cd LCD-show/
     sudo ./rotate.sh 90   
  
  Le système redémarrera et l’écran sera pivoté de 90°.  
  Vous pouvez remplacer ``90`` par ``0``, ``180`` ou ``270`` selon vos besoins.



* **Pour Ubuntu** :

  .. code-block:: bash
  
     sudo rm -rf LCD-show-ubuntu 
     git clone https://github.com/sunfounder/LCD-show-ubuntu.git 
     chmod -R 755 LCD-show-ubuntu 
     cd LCD-show-ubuntu/ 
     sudo ./LCD35-show
  
  Après l’installation, le bureau s’affichera sur l’écran tactile 3,5 pouces.
  
  Pour pivoter :
  
  .. code-block:: bash
  
     cd LCD-show-ubuntu/
     sudo ./rotate.sh 90   
  
  Le redémarrage suivra automatiquement.  
  Remplacez ``90`` par ``0``, ``180`` ou ``270`` selon vos besoins.



* **Pour Kali Linux** :

  .. code-block:: bash
  
     sudo rm -rf LCD-show-kali 
     git clone https://github.com/sunfounder/LCD-show-kali.git 
     chmod -R 755 LCD-show-kali 
     cd LCD-show-kali/ 
     sudo ./LCD35-show
  
  Après l’installation, le bureau s’affichera sur l’écran tactile 3,5 pouces.
  
  Pour pivoter :
  
  .. code-block:: bash
  
     cd LCD-show-kali/
     sudo ./rotate.sh 90   
  
  Le système redémarrera avec la nouvelle rotation.  
  Remplacez ``90`` par ``0``, ``180`` ou ``270`` selon vos besoins.
