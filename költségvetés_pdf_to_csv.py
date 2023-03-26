"""
__MKKP__
\ \__/ /
 \O  O/     
 _\  /_ 
|  \/  |
"""
"""
2023-03-25
feher.aron@gmail.com
https://github.com/xngst/Koltsegvetes-PDF-to-CSV-Excel

installok:
pip install tabula
pip install pandas
pip install openpyxl
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# I M P O R T S
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("Az ügyintéző mindjárt megjelenik...") 
import warnings
import tabula
import threading
import pandas as pd

from pathlib import Path
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox, PhotoImage, scrolledtext, Text

warnings.simplefilter("ignore")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# R O O T & F R A M E
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

root = Tk()
root.geometry('350x350')
root.title('MKKP Informatika')

notebook = ttk.Notebook(root,width=300, height=300)
notebook.pack(pady=10, expand=False)

# create frames
mkkp_frame = Frame(notebook, width=300, height=300)

# add frames to notebook
notebook.add(mkkp_frame, text='MKKP Elemi költségvetés átalakító szerkezet')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# D E F S
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def select_file():
    ""
    file_path = Path(filedialog.askopenfilename(title="Tallózni tessék!"))
    file_path_var.set(file_path)
    return
    
def run_task():
    ""
    Tk.update(mkkp_frame)
    threading.Thread(target=run_main).start()
    
def get_col_name(columns):
    ""
    try:
        for col in columns:
            if "Unnamed" in col:
                pass
            else:
                col_name = col
    except TypeError as te:
        col_name = col

    return col_name
 
def run_main():
    ""
    statusbar.config(text = "A Savköpő menyétek felkészítése..")
    
    pdf_path = Path(file_path_var.get())
    year_in = year_input.get(1.0, "end-1c")
    year = str(year_in)
    
    dfs = tabula.read_pdf(pdf_path, pages='all')
    
    my_dfs = {}
    
    for i in range(1,len(dfs)):
        
        df = pd.DataFrame(dfs[i])
        df.fillna(0,inplace=True)
        
        col_list = []
        
        try:
            for number, value in enumerate(df.iloc[2,:]):
                if value != 0:
                    col_list.append(number)

            col_name = get_col_name(df.columns)
        except IndexError as ie:
            print(ie)
            pass
        
        try:
        
            cleaned = df.iloc[2:,col_list]
            cleaned.columns = ["#","Megnevezés","Összeg"]
            cleaned.dropna(subset="Megnevezés", inplace=True)
            
            try:
                cleaned.iloc[:,2] = cleaned.iloc[:,2].str.replace(" ","")
                cleaned.iloc[:,2] = cleaned.iloc[:,2].astype(float)
                
            except ['AttributeError','ValueError'] as err:
                print(err.args)
                pass
            
            #cleaned["K/B"] = cleaned["Megnevezés"].apply(lambda x: get_kb_num(x))
            cleaned["Típus"] = [col_name] * len(cleaned)
            cleaned["Év"] = [year] * len(cleaned)
            
        except Exception as err:
            print(err.args)
            
        my_dfs[i] = cleaned
        
    collector = pd.DataFrame()
    
    for key, value in my_dfs.items():
        if value.shape[1] == 5:
            collector = pd.concat([collector,value])

    statusbar.config(text = "Iktatás..")
    
    orig_file_name = pdf_path.parts[-1]
    xl_file_name = orig_file_name.split(".")[0]+f"_{year}.xlsx"
    csv_file_name = orig_file_name.split(".")[0]+f"_{year}.csv"
    
    collector.to_excel(pdf_path.parent/xl_file_name, 
    index=False)
    collector.to_csv(pdf_path.parent/csv_file_name, 
    index=False, encoding="utf-16")
    
    statusbar.config(text = "---Meg is vagyunk!---")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# G U I
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global File path variable
file_path_var = StringVar(mkkp_frame)

label = Label(mkkp_frame, text="""Átalakítja az önkormányzati \n 
pdf költségvetéseket \n
csv és excel formátummá.""", 
anchor="e", 
justify=LEFT)

label.grid(sticky="EW", row=0, column=0, pady=5, padx=5)

separator1 = ttk.Separator(mkkp_frame).grid(row=1, column=0, columnspan=4, ipadx=100) 


label = Label(mkkp_frame, text='File kiválasztás: ')
label.grid(sticky="EW", row=2, column=0, pady=5, padx=5)

select_file_button = Button(mkkp_frame, text="Tallózás",
command=lambda: select_file())
select_file_button.grid(sticky="EW", row=2, column=1, pady=5, padx=5)


year_label = Label(mkkp_frame, text='Költségvetési év: ')
year_label.grid(sticky="EW", row=3, column=0, pady=5, padx=5)


year_input = Text(mkkp_frame, height=1, width=4)         
year_input.grid(sticky="EW", row=3, column=1,  pady=5, padx=5)
    

run_button = Button(mkkp_frame, text="Futtatás", 
command=lambda: run_task())
run_button.grid(sticky="EW", row=4, column=1, pady=5, padx=5)  


statusbar = Label(mkkp_frame, text="") 
statusbar.grid(sticky="EW", row=5, column=0, pady=5, padx=5) 

separator2 = ttk.Separator(mkkp_frame).grid(row=6, column=0, columnspan=4, ipadx=100)                    
                        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
threading.Thread(target=root.mainloop()).start()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

