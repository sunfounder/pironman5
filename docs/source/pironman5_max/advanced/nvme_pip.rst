.. note:: 

    Ciao, benvenuto nella community Facebook degli appassionati di Raspberry Pi, Arduino ed ESP32 targata SunFounder! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Why Join?**

    - **Expert Support**: Risolvi problemi post-vendita e sfide tecniche con l’aiuto della nostra community e del nostro team.
    - **Learn & Share**: Scambia consigli e tutorial per sviluppare le tue competenze.
    - **Exclusive Previews**: Ottieni accesso anticipato a nuovi annunci di prodotto e anteprime esclusive.
    - **Special Discounts**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Festive Promotions and Giveaways**: Partecipa a promozioni festive e concorsi a premi.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] ed entra nella community oggi stesso!

Dual Pi5 NVMe PIP
=====================

Il Pi5 NVMe PIP (PCIe Peripheral Board), come definito dalla Raspberry Pi Foundation, è una scheda adattatore PCIe progettata specificamente per unità a stato solido NVMe. Supporta quattro formati di SSD NVMe: 2230, 2242, 2260 e 2280, tutti compatibili con slot M.2 con chiave M.

.. image:: img/nvme_pip.png

* La scheda si collega tramite un cavo FFC (Flexible Flat Cable) inverso a 16 pin da 0,5 mm oppure un cavo FPC (Flexible Printed Circuit) su misura con impedenza controllata.
* **STA**: LED di stato.
* **PWR**: LED di alimentazione.
* L'alimentazione integrata da 3,3V supporta un’uscita massima di 3A. Tuttavia, l'interfaccia PCIe del Raspberry Pi può fornire solo 5V/1A (equivalente a 5W), quindi per un uso completo dei 3,3V/3A è possibile fornire alimentazione aggiuntiva al connettore J3 tramite una fonte a 5V.
* **FORCE ENABLE**: L'alimentatore integrato viene attivato da un segnale di switch proveniente dall’interfaccia PCIe. Dopo l'accensione del Raspberry Pi, viene inviato un segnale per attivare l’alimentazione a 3,3V. Se il sistema non supporta tale segnale o per altri motivi, è possibile cortocircuitare J4 FORCE ENABLE saldando un filo tra i due pad per forzare l’attivazione dell’alimentazione a 3,3V.

Informazioni sul modello
---------------------------

Gli SSD M.2, noti per le loro dimensioni compatte, si distinguono principalmente per il tipo di chiave (tacca sul connettore) e per l’interfaccia utilizzata. Ecco i principali tipi:

* **SSD M.2 SATA**: Utilizzano l’interfaccia SATA, come gli SSD SATA da 2,5", ma nel formato più compatto M.2. Le prestazioni sono limitate alla velocità massima SATA III di circa 600 MB/s. Questi SSD sono compatibili con slot M.2 con chiavi B e M.
* **SSD M.2 NVMe**: Utilizzano il protocollo NVMe su linee PCIe e offrono prestazioni significativamente superiori rispetto agli SSD M.2 SATA. Ideali per applicazioni che richiedono alte velocità di lettura/scrittura, come gaming, editing video e carichi di lavoro intensivi. Richiedono tipicamente slot con chiave M. Questi SSD usano l’interfaccia PCIe (Peripheral Component Interconnect Express), disponibile in versioni come 3.0, 4.0 e 5.0. Ogni versione raddoppia la velocità rispetto alla precedente. Il Raspberry Pi 5 utilizza l’interfaccia PCIe 3.0, in grado di raggiungere velocità di trasferimento fino a 3.500 MB/s.

Gli SSD M.2 sono disponibili in tre versioni di chiave: B, M e B+M. In seguito è stato introdotto lo standard B+M, che unisce le funzionalità di entrambe le chiavi, sostituendo di fatto la chiave B singola. Vedi immagine seguente:

.. image:: img/ssd_key.png


In genere, gli SSD M.2 SATA hanno chiave B+M (compatibili con slot B o M), mentre gli SSD M.2 NVMe per PCIe 3.0 x4 utilizzano la chiave M.

.. image:: img/ssd_model2.png

Informazioni sulla lunghezza
----------------------------------------

I moduli M.2 esistono in diverse dimensioni e possono essere utilizzati anche per Wi-Fi, WWAN, Bluetooth, GPS e NFC.

Pironman 5 supporta quattro formati di SSD M.2 NVMe (PCIe Gen 2.0 / Gen 3.0): 2230, 2242, 2260 e 2280. Il numero “22” indica la larghezza in millimetri (mm), mentre i numeri successivi rappresentano la lunghezza. Maggiore è la lunghezza, maggiore è lo spazio disponibile per i chip di memoria NAND e, di conseguenza, maggiore è la capacità.


.. image:: img/m2_ssd_size.png
  :width: 600

