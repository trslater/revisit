from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Main(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        return Main()
