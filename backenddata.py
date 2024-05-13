from conexaobd import connect
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from datetime import date
import re


class DateInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if len(self.text) == 10:
            return
        if len(self.text) == 2 or len(self.text) == 5:
            if substring != '/':
                substring = '/' + substring
        super(DateInput, self).insert_text(substring, from_undo=from_undo)


class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        date_input = DateInput(hint_text='DD/MM/AAAA')

        layout.add_widget(date_input)

        return layout


if __name__ == '__main__':
    MainApp().run()