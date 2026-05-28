.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Raspberry Pi OS のインストール
================================================================================

Micro SD カードまたは NVMe SSD の有無に応じて、インストール方法を選択できます。

**Micro SD カードのみを使用する場合**

  Micro SD カードのみを使用する場合は、以下の最初の方法に従ってください。

**M.2 NVMe SSD を使用する場合**

  * **M.2 NVMe SSD エンクロージャーアダプター** をお持ちの場合は、そのアダプターを使用して SSD をコンピューターに接続し、2 番目の方法に従って OS をインストールできます。  

    .. image:: img/m2_nvme_adapter.png  
        :width: 300
        :align: center
  
  * 上記のアダプターをお持ちでない場合は、まず最初の方法を使用して Micro SD カードに OS をインストールし、その後 3 番目の方法を使用して Micro SD カードから M.2 NVMe SSD にシステムをコピーしてください。  

.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi