from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    touch_point = {"1": "normal",
                   "2": "normal",
                   "3": "normal",
                   "4": "normal",
                   "5": "normal",
                   "6": "normal",
                   "7": "normal",
                   "8": "normal",
                   "9": "normal"}

    def validate_touchPoint(self):
        check_points = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for check_point in check_points:
            if self.touch_point[check_point] != "down":
                print("FAIL")
                self.parent.current = 'Screen 3'
                return None

        print("PASS")
        self.parent.current = 'Screen 3'

    def toggle_state_change(self, widget):
        state = widget.state
        button_text = widget.text
        # print(button_text + " : " + state)
        self.touch_point[button_text] = state
        # print(self.touch_point)


class ThirdScreen(Screen):

    mouse_position = []
    Y_THRESHOLD = 10
    y_range_center = None


    def on_touch_down(self, touch):
        self.y_range_center = touch.pos[1]
        print("down", touch)

    def on_touch_move(self, touch):
        self.mouse_position.append(touch.pos)
        print(touch)

    def on_touch_up(self, touch):
        print("RELEASED!", touch)

        print(self.y_range_center)
        for x, y in self.mouse_position:
            if y < self.y_range_center - self.Y_THRESHOLD or y > self.y_range_center + self.Y_THRESHOLD:
                print("FAIL")
                self.mouse_position = []
                return

        print("PASS")
        self.mouse_position = []

class TouchInput(App, Widget):



    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='First Screen'))
        sm.add_widget(SecondScreen(name='Screen 1'))
        sm.add_widget(ThirdScreen(name='Screen 3'))

        return sm



if __name__ == "__main__":
    TouchInput().run()