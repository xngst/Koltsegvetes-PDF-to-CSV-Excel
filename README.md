# Önkormányzati Költségvetés PDF ből CSV és Excel átalakító  

## Leírás  
Átalakítja az pdf formátumban lévő elemi költségvetés táblázatokat csv és excel formátummá.
A következő táblákra ad releváns eredményt:  
  * K1-K8. Költségvetési kiadások  
  * B1-B7. Költségvetési bevételek  
  * K9. Finanszírozási kiadások  
  * B8. Finanszírozási bevételek  
  
Kimeneti oszlopok:
* \#	
* Megnevezés
* Összeg	
* K/B	
* Típus
* Év

## Install  
Ahhoz hogy fusson a program, először fel kell installálni pythont a számítógépedre.  
Az egyik modul Java-ra is támaszkodik ezért annak is kell lennie a gépen.  
Java valószínűleg van a gépeden, de ha mégsem, akkor innen tudsz letölteni:  
*https://www.java.com/download/ie_manual.jsp*  

1) Töltsd le innen a pythont:  
*https://www.python.org/downloads/*  
(Windows alatt a Microsoft store-ból is le lehet tölteni. Ekkor kihagyható a kettes pont.)  

2) Installáld a python csomagot!  
Install közben pipáld be a **"Add Pyhton to PATH"** rublikát!  
![alt text](https://github.com/xngst/Koltsegvetes-PDF-to-CSV-Excel/blob/main/install/install.png)
  
3) Futtasd a **pdf_2_csv_install.bat** filet!  
A bat installálja a szükséges modulokat:  
* tabula  
* pandas   
* openpyxl  
  
4) Dupla klikkel indítsd el a **költségvetés_pdf_to_csv.py** programot.  

