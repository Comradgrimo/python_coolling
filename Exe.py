from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from CollingStation import param


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        self.row = 1
        self.username = TextInput(multiline=True)
        self.add_widget(self.username)
        self.hello = Button(text="Получить")
        self.hello.bind(on_press=self.getparams)
        self.add_widget(self.hello)

    def getparams(self,instance):
        z=param()
        self.username.text = str('\n'.join(z))

class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()