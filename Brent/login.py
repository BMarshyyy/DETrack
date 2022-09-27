from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy import clock
Window.size = (350, 500)

#https://icons8.com/icons/set/chevron-left - icons

class Splash(Screen):
	pass

class Login(Screen):
	pass

sm = ScreenManager()
sm.add_widget(Splash(name="splash"))
sm.add_widget(Login(name="login"))

class DemoApp(MDApp):
	def build(self):
		screen = Builder.load_string("main.kv")
		return screen









#///class LoginPage(MDApp):
#	def build(self):
#		global screen_manager
#		screen_manager = ScreenManager()
#		screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
#		screen_manager.add_widget(Builder.load_file("login.kv"))
#		screen_manager.add_widget(Builder.load_file("main.kv"))
#		return screen_manager
#
#	def on_start(self):
#		clock.Clock.schedule_once(self.login_screen, 5)
#
#	def login_screen(self, *args):
#		screen_manager.current = "login"
#
#	def change_window_to(self, screen):
#		screen_manager.current = screen
#
#if __name__ == "__main__":
#	LoginPage().run()