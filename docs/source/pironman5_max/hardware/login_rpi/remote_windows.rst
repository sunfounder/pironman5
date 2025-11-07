.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 ! Plongez dans l’univers du Raspberry Pi, de l’Arduino et de l’ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l’aide de notre équipe et de notre communauté.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Soyez informé en avant-première des nouvelles sorties produits et obtenez des aperçus privilégiés.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des tirages au sort et à des promotions spéciales pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

Pour les utilisateurs de Windows
=======================================

Pour les utilisateurs de Windows 10 ou version ultérieure, la connexion à distance au Raspberry Pi peut se faire via les étapes suivantes :

#. Recherchez ``powershell`` dans la barre de recherche Windows. Faites un clic droit sur ``Windows PowerShell`` et sélectionnez ``Run as administrator``.

   .. image:: img/powershell_ssh.png
      :width: 90%


#. Déterminez l’adresse IP de votre Raspberry Pi en tapant ``ping -4 <hostname>.local`` dans PowerShell.

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
      :width: 90%


   L’adresse IP de votre Raspberry Pi s’affichera une fois qu’il est connecté au réseau.

   * Si le terminal affiche ``Ping request could not find host pi.local. Please check the name and try again.``, vérifiez que le nom d’hôte saisi est correct.
   * Si l’adresse IP reste introuvable, vérifiez les paramètres réseau ou Wi-Fi de votre Raspberry Pi.

#. Une fois l’adresse IP confirmée, connectez-vous à votre Raspberry Pi avec la commande ``ssh <username>@<hostname>.local`` ou ``ssh <username>@<IP address>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Si une erreur apparaît indiquant ``The term 'ssh' is not recognized as the name of a cmdlet...``, cela signifie que les outils SSH ne sont pas installés sur votre système. Dans ce cas, vous devrez installer manuellement OpenSSH en suivant :ref:`max_openssh_powershell`, ou utiliser un outil tiers comme |link_putty|.

#. Lors de votre première connexion, un message de sécurité s’affichera. Tapez ``yes`` pour continuer.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Entrez le mot de passe que vous avez défini précédemment. Pour des raisons de sécurité, les caractères ne s’affichent pas à l’écran pendant la saisie.

    .. note::
        Il est normal que les caractères du mot de passe ne soient pas visibles lors de la saisie. Assurez-vous simplement d’entrer le bon mot de passe.

#. Une fois connecté, votre Raspberry Pi est prêt à être utilisé à distance.

   .. image:: img/sp221221_140628.png
      :width: 90%

