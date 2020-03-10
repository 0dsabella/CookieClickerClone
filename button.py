import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        button = Button(text='PUSH FOR MONEY')
        return button

if __name__ == '__main__':
  TestApp().run()
