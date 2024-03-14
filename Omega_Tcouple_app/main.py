import kivy.uix.button
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout


class MainWidget(Widget):
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

    pass


ThermoCoupleOmegaApp().run()