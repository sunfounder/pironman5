.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d’autres passionnés pour approfondir vos connaissances sur Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Résolvez les problèmes techniques et après-vente avec l’aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits.
    - **Réductions spéciales** : Profitez d’offres exclusives sur nos dernières nouveautés.
    - **Promotions festives et cadeaux** : Participez à des concours et des promotions lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

Pour les utilisateurs de Windows
===================================

Pour les utilisateurs de Windows 10 ou version ultérieure, la connexion à distance au Raspberry Pi peut se faire en suivant les étapes ci-dessous :

#. Recherchez ``powershell`` dans la barre de recherche Windows. Faites un clic droit sur ``Windows PowerShell`` et sélectionnez ``Run as administrator``.

   .. image:: img/powershell_ssh.png
      :width: 90%
      

#. Identifiez l’adresse IP de votre Raspberry Pi en tapant ``ping -4 <hostname>.local`` dans PowerShell.

   .. code-block::

      ping -4 raspberrypi.local

   .. image:: img/sp221221_145225.png
     :width: 90%
      

   Une fois connecté au réseau, l’adresse IP du Raspberry Pi s’affichera.

   * Si le terminal affiche ``Ping request could not find host pi.local. Please check the name and try again.``, vérifiez que vous avez saisi le bon nom d’hôte.
   * Si l’adresse IP ne s’affiche toujours pas, examinez les paramètres réseau ou Wi-Fi du Raspberry Pi.

#. Une fois l’adresse IP confirmée, connectez-vous au Raspberry Pi à l’aide de la commande ``ssh <username>@<hostname>.local`` ou ``ssh <username>@<IP address>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Si un message d’erreur indique ``The term 'ssh' is not recognized as the name of a cmdlet...``, il se peut que votre système ne dispose pas des outils SSH. Dans ce cas, vous devez installer OpenSSH manuellement comme indiqué dans :ref:`openssh_powershell_mini`, ou utiliser un outil tiers comme |link_putty|.

#. Lors de la première connexion, un message de sécurité apparaîtra. Tapez ``yes`` pour continuer.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Saisissez le mot de passe que vous avez défini précédemment. Notez que, pour des raisons de sécurité, les caractères du mot de passe ne s’afficheront pas à l’écran.

    .. note::
        L’absence d’affichage des caractères lors de la saisie du mot de passe est normale. Veillez simplement à entrer le mot de passe correct.

#. Une fois connecté, votre Raspberry Pi est prêt pour des opérations à distance.

   .. image:: img/sp221221_140628.png
      :width: 90%

