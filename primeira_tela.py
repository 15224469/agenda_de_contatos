from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.utils import get_color_from_hex 
from kivy.core.window import Window



class BemVindo(FloatLayout):
      def __init__(self, **kwargs):
         super(BemVindo, self).__init__(**kwargs)
         self.orientation='horizontal'
         self.spacing= 5
         self.padding=[20, 10]
         Window.clearcolor = get_color_from_hex('#620096') 

         self.nota = Label(
             text='Seja Bem Vindo(a) a Agenda de Contatos!',
             font_size= 30,
             font_name= 'Georgia',
             size_hint_y=None,
             pos_hint= {'x': .013, "y": .7}
             )
         self.add_widget(self.nota)
         
         self.but1 = Button(
             text='Ver Lista de Contatos',
             size_hint = (.4, .1),
             pos_hint = {'x': .3, "y": .5} ,
             background_color = get_color_from_hex('#560CAD'))
         self.but1.bind(on_press=self.Lista)
         self.add_widget(self.but1)
             

         self.but2 = Button(
             text='Adicionar Contato',
             size_hint=(.4, .1),
             pos_hint= {'x': .3, "y": .3},
             background_color = get_color_from_hex('#560CAD')
            )
         self.add_widget(self.but2)

class MyApp(App):
     def build(self):
          return BemVindo()
     
MyApp().run()     

