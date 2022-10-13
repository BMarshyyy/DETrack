from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.floatlayout import MDFloatLayout
from datetime import datetime


# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~~=~=~~=~==~=   To Do List   ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# 1.) See if global can be removed 
# 2.) Feedback upon completion (ex. add client)
#
#
#
#
# 
# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~==~=~=   Easy Access Obj   ~=~=~=~=~=~=~=~=~=~=~=~==~=~=~
# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=

#https://icons8.com/icons/set/chevron-left - icons

# CHANGING DEFAULT INDOW SIZE
Window.size = (350, 500)

# INITIALIZING JSON STORE
clients_store = JsonStore('clients.json')
payment_store = JsonStore('payments.json')
expense_store = JsonStore('expenses.json')

checked_data = []
checked_payments = []
checked_expenses = []


# GLOBALS
client_table_refresh = False
payment_table_refresh = False
expense_table_refresh = False

# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~=   Kivy Screens - (Py Unused)   ~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=

class Add_Client(Screen):
	pass

class Add_Expense(Screen):
	pass

class Home_Page(Screen):
	pass

class Loading_Page(Screen):
	pass

class Login_Page(Screen):
	pass

class Log_Expense(Screen):
	pass

class Log_Payments(Screen):
	pass

class New_Account(Screen):
	pass

class Splash_Page(Screen):
	pass

class WindowManager(ScreenManager):
	pass

# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~=~=~=~=~    Kivy Screens    =~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=

class View_Clients(Screen):
	def load_table(self):
		global client_table_refresh

			# Moves row data that has been checked
		def on_check_press(self, instance_cell_row):
				json_key = instance_cell_row[0] + instance_cell_row[1]
				if json_key in checked_data:
					checked_data.remove(json_key)
				else:
					checked_data.append(json_key)

			# Deletes the data table if it exists 
		if client_table_refresh == True:
			self.data_tables.clear_widgets()

			# Displaying screen layout
		layout = MDFloatLayout()
		
			# Generating tuple for table to display
		json_client_list = []
		for item in clients_store:
			cl_tup = []
			store_items = clients_store.get(item)

			for details in store_items.values():
				cl_tup.append(details)
			json_client_list.append(tuple(cl_tup))
			
			# Generates kivy table
		self.data_tables = MDDataTable(
			size_hint=(1, .8),
			pos_hint={"center_y": 0.5, "center_x": 0.5},
			background_color_header = "#AEAEAE",
			use_pagination=True,
			check=True,
			
			column_data=[
				("[size=16]First[/size]", dp(32)),
				("[size=16]Last[/size]", dp(20)),
				("[size=16]DoB[/size]", dp(20)),],
			row_data=json_client_list)
						
		# Adding widget and binding check capabilities
		self.data_tables.bind(on_check_press = on_check_press)
		self.add_widget(self.data_tables)
		client_table_refresh = True
		return layout

		# Loads table upon entry 
	def on_enter(self):
		self.load_table()

class View_Expenses(Screen):
	def load_table(self):
		global expense_table_refresh

			# Moves row data that has been checked
		def on_check_press(self, instance_cell_row):
				rem_dollar = instance_cell_row[2].replace("$", "")
				json_key = instance_cell_row[0] + rem_dollar + instance_cell_row[3]

				if json_key in checked_expenses:
					checked_expenses.remove(json_key)
				else:
					checked_expenses.append(json_key)

			# Deletes the data table if it exists 
		if expense_table_refresh == True:
			self.expense_data_table.clear_widgets()

			# Displaying screen layout
		layout = MDFloatLayout()
		
			# Generating tuple for table to display
		json_client_list = []
		for item in expense_store:
			cl_tup = []
			store_items = expense_store.get(item)

			for details in store_items.values():
				cl_tup.append(details)
			json_client_list.append(tuple(cl_tup))
			
			# Generates kivy table
		self.expense_data_table = MDDataTable(
			size_hint=(1, .8),
			pos_hint={"center_y": 0.5, "center_x": 0.5},
			background_color_header = "#AEAEAE",
			use_pagination=True,
			check=True,
			
			column_data=[
				("[size=16]Expense[/size]", dp(32)),
				("[size=16]Location[/size]", dp(20)),
				("[size=16]Amount[/size]", dp(20)),
				("[size=16]Date[/size]", dp(20)),
				("[size=16]Category[/size]", dp(30)),],
			row_data=json_client_list)
						
		# Adding widget and binding check capabilities
		self.expense_data_table.bind(on_check_press = on_check_press)
		self.add_widget(self.expense_data_table)
		expense_table_refresh = True
		return layout

		# Loads table upon entry 
	def on_enter(self):
		self.load_table()

class View_Payments(Screen):
	def load_table(self):
		global payment_table_refresh

			# Moves row data that has been checked
		def on_check_press(self, instance_cell_row):
				json_key = instance_cell_row[0] + instance_cell_row[1]
				if json_key in checked_payments:
					checked_payments.remove(json_key)
				else:
					checked_payments.append(json_key)

			# Deletes the data table if it exists 
		if payment_table_refresh == True:
			self.payment_table.clear_widgets()

			# Displaying screen layout
		layout = MDFloatLayout()
		
			# Generating tuple for table to display
		json_expense_list = []
		for item in payment_store:
			cl_tup = []
			store_items = payment_store.get(item)

			for details in store_items.values():
				cl_tup.append(details)
			json_expense_list.append(tuple(cl_tup))
			
			# Generates kivy table
		self.payment_table = MDDataTable(
			size_hint=(1, .8),
			pos_hint={"center_y": 0.5, "center_x": 0.5},
			background_color_header = "#AEAEAE",
			use_pagination=True,
			check=True,
			
			column_data=[
				("[size=16]Child[/size]", dp(32)),
				("[size=16]Payee[/size]", dp(20)),
				("[size=16]Amount[/size]", dp(20)),
				("[size=16]Date[/size]", dp(20)),
				("[size=16]Memo[/size]", dp(100)),],
			row_data=json_expense_list)
						
		# Adding widget and binding check capabilities
		self.payment_table.bind(on_check_press = on_check_press)
		self.add_widget(self.payment_table)
		payment_table_refresh = True
		return layout

			# Loads table upon entry 
	def on_enter(self):
		self.load_table()

class CPBuddy(MDApp):
	sm = ScreenManager()
	sm.add_widget(Screen(name='splash'))
	sm.add_widget(Screen(name='login'))
	sm.add_widget(Screen(name='home'))
	sm.add_widget(Screen(name='loading'))
	sm.add_widget(Screen(name='new account'))
	sm.add_widget(Screen(name='add client'))
	sm.add_widget(Screen(name='view clients'))
	sm.add_widget(Screen(name='log payments'))
	sm.add_widget(Screen(name='view payments'))
	sm.add_widget(Screen(name='add expense'))
	sm.add_widget(Screen(name='view expenses'))
		
		# PRIMARY BUILD
	def build(self):
		self.root_widget = Builder.load_file("main.kv")
		return self.root_widget 	

	######################### DELETES CHECKED ITEMS FROM JSONSTORE ################################
		# Clients
	def delete_selections_clients(self, *args):
		list_size = len(checked_data)

		for x in range(0, list_size):
			clients_store.delete(checked_data[x]) 
		checked_data.clear() 

		# Payments
	def delete_selections_payments(self, *args):
		list_size = len(checked_payments)

		for x in range(0, list_size):
			payment_store.delete(checked_payments[x]) 
		checked_payments.clear() 

		# Expenses
	def delete_selections_expenses(self, *args):
		list_size = len(checked_expenses)

		for x in range(0, list_size):
			expense_store.delete(checked_expenses[x]) 
		checked_expenses.clear() 

	############################# ADDING CLIENTS TO JSON STORE ########################################
		
	def add_client_entry(self, *args):
		client_id_name = str(args[0]) + str(args[1])
		clients_store.put(str(client_id_name), first_name = args[0], last_name = args[1], dob = args[2])

	def add_expense_entry(self, *args):
		# Creating expense ID
		log_id = args[0] + args[2] + args[3]

		#expense_id_name = str(args[0]) + str(args[1])
		try:
			cat = args[4]
		except:
			cat = ""
		expense_store.put(str(log_id), Expense = args[0], Location = args[1], Amount = "$" + str(args[2]), Date = args[3], Category = cat)

	def add_payment_entry(self, *args):
		payment_id_name = str(args[0]) + str(args[1])
		payment_store.put(str(payment_id_name), child = args[0], payee = args[1], amount = "$" + str(args[2]), pay_date = args[3], memo = args[4])

# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~=~=~=~=~     Run The App    =~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=

if __name__ == '__main__':
    CPBuddy().run()













