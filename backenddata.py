from conexaobd import connect
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from datetime import datetime
import re


class DateInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if len(self.text) == 10:
            return
        if len(self.text) == 2 or len(self.text) == 5:
            if substring != '/':
                substring = '/' + substring
        super(DateInput, self).insert_text(substring, from_undo=from_undo)

    def on_text_validate(self):
        date_str = self.text
        try:
            date_obj = datetime.strptime(date_str, '%d/%m/%y').date()
            print("Data inserida:", date_obj)
        except ValueError:
            print("Data inválida:")
    
class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        date_input = DateInput(hint_text='DD/MM/AAAA')

        layout.add_widget(date_input)

        return layout


if __name__ == '__main__':
    MainApp().run()