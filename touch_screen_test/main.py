import sys
from kivy.app import App
from kivy.properties import ObjectProperty
from navigation_screen_manager import NavigationScreenManager
from kivy.uix.widget import Widget



class AppScreenManager(NavigationScreenManager):
    pass

class TouchScreenTest(App, Widget):



    manager = ObjectProperty(None)


    touch_point = {"1": "normal",
                   "2": "normal",
                   "3": "normal",
                   "4": "normal",
                   "5": "normal",
                   "6": "normal",
                   "7": "normal",
                   "8": "normal",
                   "9": "normal"}

    def build(self):
        self.manager = AppScreenManager()
        return self.manager

    def selection_set(self):
        self.manager.push("Screen 1")


    def validate_touchPoint(self):
        check_points = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for check_point in check_points:
            if self.touch_point[check_point] != "down":
                print("FAIL")
                self.manager.push("Screen 2")
                return None

        print("PASS")
        self.manager.push("Screen 2")

    def toggle_state_change(self, widget):
        state = widget.state
        button_text = widget.text
        # print(button_text + " : " + state)
        self.touch_point[button_text] = state
        # print(self.touch_point)

    def on_touch_down(self, touch):
        print(touch)

    def on_touch_move(self, touch):
        print(touch)

    def on_touch_up(self, touch):
        print("RELEASED!", touch)



def Main():
    TouchScreenTest().run()

if __name__ == '__main__':
    Main()

