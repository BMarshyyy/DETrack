from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.floatlayout import MDFloatLayout

#https://icons8.com/icons/set/chevron-left - icons

# CHANGING DEFAULT INDOW SIZE
Window.size = (350, 500)

# INITIALIZING JSON STORE
clients_store = JsonStore('clients.json')
expense_store = JsonStore('expenses.json')
payment_store = JsonStore('payments.json')
checked_data = []

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

class View_Expenses(Screen):
	pass

# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~=~=~=~=~    Kivy Screens    =~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=

class View_Clients(Screen):

	def load_table(self):
			# Moves row data that has been checked
		def on_check_press(self, instance_cell_row):
				json_key = instance_cell_row[0] + instance_cell_row[1]
				if json_key in checked_data:
					checked_data.remove(json_key)
				else:
					checked_data.append(json_key)


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
		data_tables = MDDataTable(
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
		data_tables.bind(on_check_press = on_check_press)
		self.add_widget(data_tables)
		return layout

		# Loads table upon entry 
	def on_enter(self):
		self.load_table()

class View_Payments(Screen):
	pass

class WindowManager(ScreenManager):
	pass	

class CPBuddy(MDApp):
	sm = ScreenManager()
	sm.add_widget(Screen(name='splash'))
	sm.add_widget(Screen(name='login'))
	sm.add_widget(Screen(name='home'))
	sm.add_widget(Screen(name='new account'))
	sm.add_widget(Screen(name='add client'))
	sm.add_widget(Screen(name='view clients'))

	def build(self):
		self.root_widget = Builder.load_file("main.kv")
		return self.root_widget 	

			# DELETES CHECKED ITEMS FROM JSONSTORE
	def delete_selections(self, *args):
		list_size = len(checked_data)

		amt_removed = 0
		for x in range(0, list_size): # for item loop stops after 1 run
			clients_store.delete(checked_data[x-amt_removed])
			checked_data.remove(checked_data[x-amt_removed])
			amt_removed += 1

	def print_entry(self, *args):
		client_id_name = str(args[0]) + str(args[1])
		clients_store.put(str(client_id_name), first_name = args[0], last_name = args[1], dob = args[2])

# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~=~=~=~=~     Run The App    =~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=

if __name__ == '__main__':
    CPBuddy().run()



