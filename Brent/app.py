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
store = JsonStore('clients.json')
checked_data = []

# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~=~=~=~=~    Kivy Screens    =~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=

class Splash_Page(Screen):
	pass

class Login_Page(Screen):
	pass

class Home_Page(Screen):
	pass

class New_Account(Screen):
	pass

class Add_Client(Screen):
	pass

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
		for item in store:
			cl_tup = []
			store_items = store.get(item)

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
				("[size=16]First[/size]", dp(25)),
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
	def delete_selections(self):
		for entry in checked_data:
			store.delete(entry)
			checked_data.remove(entry)



	def print_entry(self, *args):
		client_id_name = str(args[0]) + str(args[1])
		store.put(str(client_id_name), first_name = args[0], last_name = args[1], dob = args[2])


# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~=~=~=~=~     Run The App    =~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=

if __name__ == '__main__':
    CPBuddy().run()


