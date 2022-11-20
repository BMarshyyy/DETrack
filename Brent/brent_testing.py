import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pandastable import Table, TableModel
import pandas as pd 
import json
import string

    # INITIAL WINDOW
root = tk.Tk()
root.title("Daycare Expense Tracker")

    # TAB CONTROLS / TABS
notebook = ttk.Notebook(root)
notebook.pack(expand=1)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

    # TAB NAMES
notebook.add(tab1, text = 'Time Space')
notebook.add(tab2, text = 'Expenses')
notebook.add(tab3, text = 'Mileage')

################################################################################################################################################################

# GLOBAL FUNCTIONS / VARIABLES

def remove_items(item_list, item):
    # using list comprehension to perform the task
    res = [i for i in item_list if i != item]
    return res

def load_json():
    with open('C:\\Users\\annam\\Desktop\\Python\\brent\\data_storage.json', 'r') as data_file:    
        data = json.load(data_file)
    data_file.close()
    return data

def update_json(dictionary): #  expense_dict, 'expenses'
    with open('C:\\Users\\annam\\Desktop\\Python\\brent\\data_storage.json', "w") as data_file:
        json.dump(dictionary, data_file)
    data_file.close()
    
################################################################################################################################################################


#TAB 2 EXPENSES 

class ChildRelatedSupplies:
    def __init__(self, tab2):
            # FRAMES INSIDE OF TAB 2
        table_frame1 = tk.Frame(tab2) # ENTRY BOXES
        table_frame1.pack()
        
        table_frame2 = tk.Frame(tab2) # SAVE + SPACING
        table_frame2.pack()
        
        table_frame3 = tk.Frame(tab2) # TABLE
        table_frame3.pack() 
        
        
            # JSON TABLE DATA
        expense_dict = load_json()
        
            # CREATES DATA TABLE 
        def create_table():
            df = pd.DataFrame(data=expense_dict['expenses'])
            self.table = pt = Table(table_frame3, dataframe=df, showtoolbar=True, showstatusbar=True, cellwidth = 130) 
            pt.show()
            pt.redraw()


            # SAVE BUTTON FUNCTIONALITY 
        def save_func():
           # try:
                entry_list = []
                
                    # CREATING DATA SET FOR TABLE DISPLAY
                count = 1
                for entry in my_entries:
                    tot_len = len(my_entries) / 4
                    entry_list.append(entry.get())
                
                        # STORES ENTRIES INTO DICTIONARY
                    if count == tot_len:
                        expense_dict['expenses']['Store Name'] += remove_items(entry_list, "")
                    elif count == (tot_len*2):
                        expense_dict['expenses']['Purchase'] += remove_items(entry_list, "")
                    elif count == (tot_len*3):
                        expense_dict['expenses']['Price Paid'] += remove_items(entry_list, "")
                    elif count == (tot_len*4):
                        expense_dict['expenses']['Category'] += remove_items(entry_list, "")
                        
                        # RESETTING LIST 
                    if count == (tot_len*1) or count == (tot_len*2) or count == (tot_len*3) or count == (tot_len*4):
                        entry_list = []
                    count +=1
                
                
                update_json(expense_dict)
                
                
                create_table()
                
            #except:
                    # HANDLES ERROR OF NOT FILLING ALL BOXES IN A ROW
           #     messagebox.showwarning("Incomeplete Entry", "Please ensure all entries on a specifc row are complete and a number if applicable.")
            
            
            # ENTRY BOX LABELS
        Store_Label = tk.Label(table_frame1, text = "Store Name")
        Store_Label.grid(row = 0, column = 0, padx = 50, pady = 15)
        
        Product_Label = tk.Label(table_frame1, text = "Product Purchased")
        Product_Label.grid(row = 0, column = 1, padx = 50, pady = 15)

        Price_Label = tk.Label(table_frame1, text = "Price Paid")
        Price_Label.grid(row = 0, column = 2, padx = 50, pady = 15)  
        
        
            # STORING ENTRY.GET() VALUES
        my_entries = []
            # CREATING ENTRY BOXES
        for x in range(3):
            for y in range(1, 6):
                Xcord_Entry = Entry(table_frame1)
                Xcord_Entry.grid(row = y, column = x, padx = 5, pady = 5)
                my_entries.append(Xcord_Entry)
        
        
            # CREATING TABLE BASED ON JSON (SEE FUNCTION)           
        create_table()      
      
                               
            # COMBOBOX ENTRY LABEL   
        Expense_Label = tk.Label(table_frame1, text = "Select Expense Category")
        Expense_Label.grid(row = 0, column = 3, padx = 50, pady = 15)
        
        # CREATING COMBOBOX
        for x in range(1, 6):
            Expense_Var = tk.StringVar()
            Expense_Combo = ttk.Combobox (table_frame1, value = Expense_Var, )
            my_entries.append(Expense_Combo) 
            
            Expense_Combo.grid(row =  x, column = 3)
            Expense_Combo ['values'] = ['Child Related Supplies', 'Home Supplies', 'Improvements and Repairs', 'Furniture and Appliances', 'Office Supplies', 'Misc']
            Expense_Combo ['state'] = 'readonly'
      
        # SAVE BUTTON  
        Save_Button = tk.Button(table_frame2, text = "Save", command = save_func).grid(row = 10, column = 1, padx = 10, pady = 10)
        
        
        
tab2_CRS = ChildRelatedSupplies(tab2)










root.mainloop()