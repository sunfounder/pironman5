Combine With 3.5 inch LCD
=============================

Cette section s’adresse aux utilisateurs du Pironman 5 MAX ayant également acheté l’`écran LCD 3,5 pouces <https://www.sunfounder.com/products/touchscreen-02?_pos=2&_sid=839d5db5b&_ss=r>`_.

L’écran LCD peut être monté directement sur les broches GPIO du Raspberry Pi, offrant un affichage visuel ainsi qu’un contrôle tactile pour le Pironman 5 MAX. Veuillez suivre les étapes d’installation appropriées pour garantir un fonctionnement correct et éviter tout dommage matériel.

Vous pouvez en apprendre davantage sur cet écran LCD et son utilisation via le lien suivant :
`Documentation de l'écran LCD 3,5 pouces <http://wiki.sunfounder.cc/index.php?title=3.5_Inch_LCD_Touch_Screen_Monitor_for_Raspberry_Pi>`_.


**Assemble**

.. image:: ../img/lcd_to_max1.jpg
    :width: 340

.. image:: ../img/lcd_to_max2.jpg
    :width: 340


.. warning:: Lors de l’installation de l’écran LCD 3,5 pouces sur le Pironman 5 MAX, assurez-vous que les broches sont parfaitement alignées. L’en-tête du module LCD doit correspondre exactement à l’interface GPIO du Raspberry Pi, sans décalage ni mauvaise position. Des connexions incorrectes peuvent endommager l’écran LCD ou même le Raspberry Pi. Vérifiez soigneusement toutes les connexions avant la mise sous tension !


**Remove RGB Jumper**

Lors de l’utilisation du Pironman 5 MAX avec l’écran LCD 3,5 pouces, la LED RGB et l’écran LCD partagent les mêmes broches SPI. Pour éviter les conflits et assurer le bon fonctionnement de l’écran LCD, la connexion de la LED RGB doit être désactivée.

Suivez les étapes ci-dessous :

1. Sur la **carte d’extension IO**, **retirez le cavalier connecté aux broches RGB** pour déconnecter la LED RGB de l’interface SPI.

   .. image:: ../img/lcd_to_max0.jpg
      :width: 600
      :align: center


2. Exécutez les commandes suivantes pour **désactiver le service de contrôle de la LED RGB** :

   .. code-block:: bash

      pironman5 -re false
      sudo systemctl restart pironman5.service 

Cela libérera l’interface SPI pour l’écran LCD, évitant ainsi tout conflit ou problème d’affichage.


**Driver Installation**

Ce module LCD nécessite l’installation d’un pilote avant utilisation. Les étapes d’installation varient selon le système d’exploitation.

* Pour Raspberry Pi OS, utilisez la commande suivante pour installer le pilote :

   .. code-block:: bash

      sudo rm -rf LCD-show 
      git clone https://github.com/sunfounder/LCD-show.git 
      chmod -R 755 LCD-show 
      cd LCD-show/ 
      sudo ./LCD35-show

   Une fois l’exécution terminée, le bureau du Raspberry Pi s’affichera sur l’écran LCD 3,5 pouces.

   Pour faire pivoter l’affichage, vous pouvez exécuter la commande suivante :

   .. code-block:: bash

      cd LCD-show/
      sudo ./rotate.sh 90   

   Après l’exécution, le système redémarrera automatiquement et l’écran sera tourné de 90 degrés avec un affichage et un toucher corrects. Vous pouvez remplacer '90' par 0, 90, 180 ou 270 selon l’orientation souhaitée.

* Pour Ubuntu, utilisez la commande suivante pour installer le pilote :

   .. code-block:: bash

      sudo rm -rf LCD-show-ubuntu 
      git clone https://github.com/sunfounder/LCD-show-ubuntu.git 
      chmod -R 755 LCD-show-ubuntu 
      cd LCD-show-ubuntu/ 
      sudo ./LCD35-show

   Une fois l’exécution terminée, le bureau du Raspberry Pi s’affichera sur l’écran LCD 3,5 pouces.

   Pour faire pivoter l’affichage, vous pouvez exécuter la commande suivante :

   .. code-block:: bash

      cd LCD-show/
      sudo ./rotate.sh 90   

   Après l’exécution, le système redémarrera automatiquement et l’écran sera tourné de 90 degrés avec un affichage et un toucher corrects. Vous pouvez remplacer '90' par 0, 90, 180 ou 270 selon l’orientation souhaitée.

* Pour Kali Linux, utilisez la commande suivante pour installer le pilote :

   .. code-block:: bash

      sudo rm -rf LCD-show-kali 
      git clone https://github.com/sunfounder/LCD-show-kali.git 
      chmod -R 755 LCD-show-kali 
      cd LCD-show-kali/ 
      sudo ./LCD35-show

   Une fois l’exécution terminée, le bureau du Raspberry Pi s’affichera sur l’écran LCD 3,5 pouces.

   Pour faire pivoter l’affichage, vous pouvez exécuter la commande suivante :

   .. code-block:: bash

      cd LCD-show/
      sudo ./rotate.sh 90   

   Après l’exécution, le système redémarrera automatiquement et l’écran sera tourné de 90 degrés avec un affichage et un toucher corrects. Vous pouvez remplacer '90' par 0, 90, 180 ou 270 selon l’orientation souhaitée.
