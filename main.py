from re import L
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

Config.set("graphics", "width", "1280")
Config.set("graphics", "height", "800")
Config.set("graphics", "resizable", False)
Config.set("graphics", "fullscreen", "false")
Config.set("input", "mouse", "mouse,disable_on_activity")
Config.set("kivy", "keyboard_mode", "systemanddock")

Builder.load_string("""
<DemoApp>:
    orientation: "vertical"
    Image:
        source: "assets/pumpkin.png"
        allow_stretch: True
    Button:
        id: btnExit
        text: "exit"
        on_release: app.stop()
""")

class DemoApp(App, BoxLayout):
    def build(self):
        return self

if __name__ == "__main__":
    DemoApp().run()