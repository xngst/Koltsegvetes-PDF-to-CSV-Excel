# Önkormányzati Költségvetés PDF ből CSV és Excel átalakító  

## Leírás  
Átalakítja az pdf formátumban lévő elemi költségvetés táblázatokat csv és excel formátummá.  
A következő táblákra ad releváns eredményt:    
  * K1-K8. Költségvetési kiadások  
  * B1-B7. Költségvetési bevételek  
  * K9. Finanszírozási kiadások  
  * B8. Finanszírozási bevételek  

Bemenet:  
A pdf azon táblái, amelyik 3 oszloppal (\#, Megnevezés, Eredeti előirányzat) rendelkeznek.
![alt text](https://github.com/xngst/Koltsegvetes-PDF-to-CSV-Excel/blob/main/példák/sample_input.png)

Kimeneti oszlopok:  
* \#  
  A bemeneti táblázat első oszlopa  
* Megnevezés   
  A bemeneti táblázat második oszlopa  
* Összeg   
  A bemeneti táblázat harmadik oszlopa  
* K/B    
  Kiadás / Bevétel könyvelési számjele, például K1101

* Típus  
  Megmutatja az eredeti tábla fejlécéből származó címet, például *01 - K1-K8. Költségvetési kiadások*
* Év  
  A felhasználó adja meg programfuttatás közben  

![alt text](https://github.com/xngst/Koltsegvetes-PDF-to-CSV-Excel/blob/main/példák/sample_output.png)  
  

## Telepítés    
Ahhoz hogy fusson a program, először fel kell telepíteni python interpretert a számítógépedre.  
Az egyik modul Java-ra is támaszkodik ezért annak is kell lennie a gépen.  
Java valószínűleg van a gépeden, de ha mégsem, akkor innen tudsz letölteni:  
*https://www.java.com/download/ie_manual.jsp*  

1) Töltsd le innen a pythont:  
*https://www.python.org/downloads/*  
(Windows alatt a Microsoft store-ból is le lehet tölteni. Ekkor kihagyható a kettes pont.)  

2) Installáld a python csomagot!  
Install közben pipáld be a **"Add Pyhton to PATH"** rublikát!  
![alt text](https://github.com/xngst/Koltsegvetes-PDF-to-CSV-Excel/blob/main/install/install.png)
  
3) Az [install](https://github.com/xngst/Koltsegvetes-PDF-to-CSV-Excel/tree/main/install) mapppában találsz egy bat filet.  
Futtasd a **pdf_2_csv_install.bat** filet!  
A bat installálja a szükséges modulokat:  
* tabula-py  
https://pypi.org/project/tabula-py/
* pandas   
https://pypi.org/project/pandas/
* openpyxl  
https://pypi.org/project/openpyxl/
  
4) Dupla klikkel indítsd el a **költségvetés_pdf_to_csv.py** programot.  

