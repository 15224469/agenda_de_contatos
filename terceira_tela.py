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
         Window.clearcolor = get_color_from_hex('#380659') 

         self.nota = Label(
             text='Lista de Contatos:',
             font_size= 45,
             font_name= 'Georgia',
             size_hint_y=None,
             pos_hint= {'x': .013, "y": .7}
             )
         self.add_widget(self.nota)
         
         self.but1 = Button(
             text='Voltar a tela de início',
             size_hint = (.2, .1),
             pos_hint = {'x': .4, "y": .1} ,
             background_color = get_color_from_hex('#560CAD'))
             
         self.add_widget(self.but1)

         

class MyApp(App):
     def build(self):
          return BemVindo()
     
MyApp().run()     

