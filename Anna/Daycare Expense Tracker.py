import tkinter as tk
from tkinter import *
from tkinter import ttk

#Root
root = tk.Tk()
root.geometry('900x600')
root.title("Daycare Expense Tracker")

#Create Notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

#Create Tabs
tab1 = ttk.Frame(notebook, width=800, height=600)
tab2 = ttk.Frame(notebook, width=800, height=600)
tab3 = ttk.Frame(notebook, width=800, height=600)
tab4 = ttk.Frame(notebook, width=800, height=600)
tab5 = ttk.Frame(notebook, width=800, height=600)
tab6 = ttk.Frame(notebook, width=800, height=600)
tab7 = ttk.Frame(notebook, width=800, height=600)
tab8 = ttk.Frame(notebook, width=800, height=600)
tab9 = ttk.Frame(notebook, width=800, height=600)


#Naming the Tabs
notebook.add(tab1, text = 'Time Space')
notebook.add(tab2, text = 'Child Related Supplies')
notebook.add(tab3, text = 'Home Supplies')
notebook.add(tab4, text = 'Improvements & Repairs')
notebook.add(tab5, text = 'Furniture & Appliances')
notebook.add(tab6, text = 'Office Supplies')
notebook.add(tab7, text = 'Mileage')
notebook.add(tab8, text = 'Food Deduction')
notebook.add(tab9, text = 'Misc')


#Tab 1 Time Space
go_button = Button(tab1, text = "Calculate").pack






root.mainloop()

