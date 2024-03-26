from time import sleep

import kivy.uix.button
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_file("UI_1.kv")
class MainWidget(Widget):
    def press_OK(self):
        print("OK")
    pass

class TopGrid(GridLayout):
    pass
# class GridLayout(GridLayout):
#     pass
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)"""

# name the .kv file with same name without app. (Ex: ThermoCoupleOmega.kv)
class ThermoCoupleOmegaApp(App):
    def build(self):
        return MainWidget()
    pass


ThermoCoupleOmegaApp().run()