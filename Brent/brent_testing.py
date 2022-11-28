import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pandastable import Table
import pandas as pd 
import json
import openpyxl

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
    with open('C:\\Users\\Brent\\OneDrive\\Desktop\\Programming\\Python\Anna CE Track\\data_storage.json', 'r') as data_file:    
        data = json.load(data_file)
    data_file.close()
    return data

def update_json(dictionary): #  expense_dict, 'expenses'
    with open('C:\\Users\\Brent\\OneDrive\\Desktop\\Programming\\Python\Anna CE Track\\data_storage.json', "w") as data_file:
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

        # ACCESSIBLE INDEX VAL
        self.table_selected_index = None
        
            # JSON TABLE DATA
        expense_dict = load_json()
        
            # CREATES DATA TABLE 
        def create_table():
            df = pd.DataFrame(data=expense_dict['expenses'])
            create_table.out_df = df 
            self.table = pt = Table(table_frame3, dataframe=df, showtoolbar=False, showstatusbar=False, cellwidth = 140) 
            
            pt.show()
            pt.redraw()

                # ALLOWS RETURN OF INDEX FROM SELECTING A ROW
            def handle_left_click(event):
                rowclicked_single = pt.get_row_clicked(event)

                self.table_selected_index = rowclicked_single # Index Variable

                pt.setSelectedRow(rowclicked_single)
                pt.redraw()
                
                # BINDING EVENT TO TABLE 
            pt.rowheader.bind('<Button-1>', handle_left_click)

            


        def delete_table_item():
                # DELETING ITEM FOR HEADER DICT KEY
            col_headers = list(create_table.out_df.columns)
            for header in col_headers:
                del expense_dict['expenses'][header][self.table_selected_index]
                # REFRESHING TABLE
            create_table()
            update_json(expense_dict)


            # SAVE BUTTON FUNCTIONALITY 
        def save_func():
            #if deleting_entries is not None:
            try:
                entry_list = []
                dict_keys = ['Date', 'Store Name', 'Purchase', 'Price Paid', 'Category']
                    # CREATING DATA SET FOR TABLE DISPLAY
                count = 0
                for entry in my_entries:
                    entry_list.append(entry.get())
                        # STORES ENTRIES INTO DICTIONARY
                    expense_dict['expenses'][dict_keys[count]] += remove_items(entry_list, "")
                    
                        # RESETTING COUNT TO LOOP KEYS TEXT
                    if count == 4:
                        count -= 5
                    count += 1

                        # RESETTING LIST 
                    entry_list = []

                #if deleting_entries is not None:
                    

                    # NEEDS TO HAPPEN FIRST TO RAISE ERROR BEFORE ADDING TO JSON
                create_table()
                update_json(expense_dict)
                
            except:
                    # HANDLES ERROR OF NOT FILLING ALL BOXES IN A ROW
                messagebox.showwarning("Incomeplete Entry", "Please ensure all entries on a specifc row are complete and a number if applicable.")
            

            
            # ENTRY BOX LABELS
        date_purchased_Label = tk.Label(table_frame1, text = "Date")
        date_purchased_Label.grid(row = 0, column = 0, padx = 50, pady = 15)

        Store_Label = tk.Label(table_frame1, text = "Store Name")
        Store_Label.grid(row = 0, column = 1, padx = 50, pady = 15)
        
        Product_Label = tk.Label(table_frame1, text = "Product Purchased")
        Product_Label.grid(row = 0, column = 2, padx = 50, pady = 15)

        Price_Label = tk.Label(table_frame1, text = "Price Paid")
        Price_Label.grid(row = 0, column = 3, padx = 50, pady = 15)  
        
        
            # STORING ENTRY.GET() VALUES
        my_entries = []
            # CREATING ENTRY BOXES AND COMBO BOXES
        count = 1
        row = 1
        for y in range(1, 6):
            for x in range(5):
                if count % 5 == 0:
                    Expense_Var = tk.StringVar()
                    Expense_Combo = ttk.Combobox(table_frame1, value = Expense_Var)
                    my_entries.append(Expense_Combo) 
                    
                    Expense_Combo.grid(row =  row, column = 4, padx= 5, pady= 5)
                    Expense_Combo ['values'] = ['Child Related Supplies', 'Home Supplies', 'Improvements and Repairs', 'Furniture and Appliances', 'Office Supplies', 'Misc']
                    Expense_Combo ['state'] = 'readonly'
                    row += 1
                else:
                    Xcord_Entry = tk.Entry(table_frame1)
                    Xcord_Entry.grid(row = y, column = x, padx = 5, pady = 5)
                    my_entries.append(Xcord_Entry)

                count += 1
        
            # CREATING TABLE BASED ON JSON (SEE FUNCTION)           
        create_table()      
                 
            # COMBOBOX ENTRY LABEL   
        Expense_Label = tk.Label(table_frame1, text = "Select Expense Category")
        Expense_Label.grid(row = 0, column = 4, padx = 50, pady = 15)
        
      
        # SAVE BUTTON  
        export_button = tk.Button(table_frame2, text = "Delete", command = delete_table_item).grid(row = 10, column = 0, padx = 10, pady = 10)
        save_button = tk.Button(table_frame2, text = "Save", command = save_func).grid(row = 10, column = 1, padx = 10, pady = 10)
        export_button = tk.Button(table_frame2, text = "Export", command = delete_table_item).grid(row = 10, column = 2, padx = 10, pady = 10)
        
        
        
tab2_CRS = ChildRelatedSupplies(tab2)










root.mainloop()
