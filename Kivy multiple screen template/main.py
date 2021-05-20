from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

# No stack
class MyWindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")
class MyMainMApp(App):
    def build(self):
        return kv



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MyMainMApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
