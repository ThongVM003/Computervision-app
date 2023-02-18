import kivy
from kivy.app import App
from kivy.uix.label import Label
# kivy.require("1.0.1")

class meomeo(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def build(self):
        return Label(text="Dau tay time")

meomeo = meomeo()
meomeo.run()

