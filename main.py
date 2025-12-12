import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.9.0')

class MelangeTestApp(App):
    def build(self):
        return Label(text="APK Built Successfully via Melange TCB!")

if __name__ == '__main__':
    MelangeTestApp().run()
