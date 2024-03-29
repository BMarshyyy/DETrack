import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pandastable import Table
import pandas as pd 


#Root
root = tk.Tk()
root.geometry('1200x600')
root.title("Daycare Expense Tracker")

#Create Notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

#Create Tabs
tab1 = ttk.Frame(notebook, width=800, height=600)
tab2 = ttk.Frame(notebook, width=800, height=600)
tab3 = ttk.Frame(notebook, width=800, height=600)

#Naming the Tabs
notebook.add(tab1, text = 'Time Space')
notebook.add(tab2, text = 'Expenses')
notebook.add(tab3, text = 'Mileage')

#Tab 1 Time/Space
class TimeSpace:
    def __init__(self, tab1):

        
        Hours_Label = tk.Label(tab1, text = "How many hours worked per week?")
        Hours_Label.grid(row = 0 , column = 0, padx = 15, pady = 50)

        DaycareSpace_Label = tk.Label(tab1, text = "What is total square footage used for daycare?")
        DaycareSpace_Label.grid(row = 1, column = 0, padx = 15, pady = 50)

        TotalSpace_Label = tk.Label(tab1, text = "What is the total square footage of your house?")
        TotalSpace_Label.grid(row = 2, column = 0, padx = 15, pady  =50)

        Hours_Entry = Entry(tab1)
        Hours_Entry.grid(row = 0, column = 1, padx = 15, pady = 50)

        DaycareSpace_Entry = Entry(tab1)
        DaycareSpace_Entry.grid (row = 1, column = 1, padx = 15, pady =50)

        TotalSpace_Entry = Entry(tab1) 
        TotalSpace_Entry.grid (row = 2, column = 1, padx = 15, pady = 50)
        
        def calc():
            try:
                
                ans = ((float(Hours_Entry.get())/168) * (float(DaycareSpace_Entry.get()) / float(TotalSpace_Entry.get())) * 100) 
                rounded_ans = "{:.1f}".format(ans)
                tk.Label(tab1, text = str(rounded_ans)+"%").grid (row = 3, column = 1, padx = 15, pady = 15)
                print(rounded_ans)

            except:
                messagebox.showwarning (title = 'Entry Error', message = 'You"ve entered an unsupported character, please try again')
                

        TSButton = tk.Button(tab1, text = "Calculate Time/Space Percentage", command=calc)
        TSButton.grid(row = 4, column = 1, padx = 15, pady = 15)
    
tab1_timespace = TimeSpace(tab1) 

#Tab 2 Expenses

class ChildRelatedSupplies:
    
        

    def __init__(self, tab2):
        
        #Entrybox Labels
        Store_Label = tk.Label(tab2, text = "Store Name")
        Store_Label.grid(row = 0, column = 0, padx = 100, pady = 15)
        
        Product_Label = tk.Label(tab2, text = "Product Purchased")
        Product_Label.grid(row = 0, column = 1, padx = 100, pady = 15)

        Price_Label = tk.Label(tab2, text = "Price Paid")
        Price_Label.grid(row = 0, column = 2, padx = 100, pady = 15)  
        
        #Getting Entries
        my_entries = []
        
        expense_dict = {}
        
        def access():
            entry_list1 = []
            entry_list2 = []
            entry_list3 = []
            
            list_pos = 0
            for entries in my_entries:
                if list_pos <= 4: 
                    entry_list1.append(entries.get())
                elif list_pos <= 9:
                    entry_list2.append(entries.get())
                else:
                    entry_list3.append(entries.get())
                list_pos += 1
            
            
            expense_dict.update({'Store Name' : entry_list1})
            expense_dict.update({'Product Purchased': entry_list2})
            expense_dict.update({'Price Paid' : entry_list3})
        
        
            pt.redrawVisible()
            print(expense_dict)


            
        #Create Multiple Entry Boxes
        for x in range(3):
                for y in range(1, 6):
                    Xcord_Entry = Entry(tab2)
                    Xcord_Entry.grid(row = y, column = x, padx = 10, pady = 10)
                    my_entries.append(Xcord_Entry)
                    
                    
        table_frame = tk.Frame (tab2)
        table_frame.grid (row = 11, column= 1)
        tk.Label(table_frame, text = "").grid (rowspan = 3, columnspan = 4)
                    
                    
        #df = TableModel.getSampleData() 
        df = pd.DataFrame(data=expense_dict)
        self.table = pt = Table(table_frame, dataframe=df, showtoolbar=True, showstatusbar=True) 
       
        pt.show()
        
        
        
            
        #Combobox Entry Label        
        Expense_Label = tk.Label(tab2, text = "Select Expense Category")
        Expense_Label.grid(row = 0, column = 3, padx = 100, pady = 15)
        
        #Create Combobox
        Expense_Var = tk.StringVar() 
        Expense_Combo = ttk.Combobox (tab2, value = Expense_Var)
        Expense_Combo.grid(row =  1, column = 3)
        Expense_Combo ['values'] = ['Child Related Supplies', 'Home Supplies', 'Improvements and Repairs', 'Furniture and Appliances', 'Office Supplies', 'Misc']
        Expense_Combo ['state'] = 'readonly'
        
      
        #Create Save Button    
        Save_Button = tk.Button(tab2, text = "Save", command = access)
        Save_Button.grid(row = 10, column = 1, padx = 10, pady = 10)
        
        #my_print = tk.Label (tab2,text = '')
        #my_print.grid(row = 11, column = 1, padx = 10, pady = 10)
        
tab2_CRS = ChildRelatedSupplies(tab2)










root.mainloop()
