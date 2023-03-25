# Önkormányzati Költségvetés PDF ből CSV és Excel átalakító  
Átalakítja az pdf formátumban lévő elemi költségvetés táblázatokat csv és excel formátummá.

Ahhoz hogy fusson a program, először fel kell installálni a pythont a számítógépedre.  
Az egyik modul Java-ra is támaszkodik ezért annak is kell lennie a gépen.  
Java valószínűleg van a gépeden, de ha mégsem, akkor innen tudsz letölteni:  
https://www.java.com/download/ie_manual.jsp  

1) Töltsd le innen a pythont:  
https://www.python.org/downloads/  
(Windows alatt a Microsoft store-ból is le lehet tölteni.  
Ekkor kihagyható a kettes pont.)  

2) Installáld a python csomagot.  
!!!  
Install közben pipáld be hogy "Add Pyhton to PATH"  
láasd: install.png  
!!!  
  
3) Futtasd a pdf_2_csv_install.bat filet  
Ez installálja a szükséges modulokat:  
* tabula  
* pandas   
* openpyxl  
  
4) Duplaklikkel indítsd el a költségvetés_pdf_to_csv.py programot.  

