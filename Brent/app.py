from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.uix.screenmanager import NoTransition
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp

#https://icons8.com/icons/set/chevron-left - icons

# CHANGING DEFAULT INDOW SIZE
Window.size = (350, 500)

# INITIALIZING JSON STORE
store = JsonStore('clients.json')

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
		layout = AnchorLayout()
		data_tables = MDDataTable(
			size_hint=(1, 1),
			use_pagination=True,
			check=True,
			column_data=[
				("First Name", dp(30)),
				("Last Name", dp(20)),
				("DoB", dp(20)),],
			row_data=[
				(f"{i + 1}", "2.23", "3.65", "44.1", "0.45", "62.5")
				for i in range(50)],)
		self.add_widget(data_tables)
		return layout
	
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

	def print_entry(self, *args):
		client_id_name = str(args[0]) + str(args[1])
		store.put(str(client_id_name), first_name = args[0], last_name = args[1], dob = args[2])

		print(store.get(client_id_name))

	

# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~=~=~=~=~     Run The App    =~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=

if __name__ == '__main__':
    CPBuddy().run()





























	#def splash_switch(self, dt):
	#	self.root_widget.current = 'splash'

	#def login_switch(self, dt):
	#	self.root_widget.current = 'login'

	#def home_switch(self, dt):
	#	self.root_widget.current = 'home'

	#def home_switch(self, dt):
	#	self.root_widget.current = 'new account'