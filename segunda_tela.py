from conexaobd import *
from bdcontatos import *
import sqlite3
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.label import Label



class Adicionar(FloatLayout):
    def __init__(self, **kwargs):
        super(Adicionar, self).__init__(**kwargs)
        self.orientation='horizontal'
        self.spacing=5
        self.padding=[20, 10]
        Window.clearcolor = get_color_from_hex('#620096') 

        self.label = Label(
            text= 'ADICIONE O CONTATO:', 
            font_size = 40, 
            font_name = 'Georgia',
            size_hint_y=None,
            pos_hint={'x': .013, "y": .8}
            )
        self.add_widget(self.label)

        self.nome = TextInput(
            hint_text="Nome Completo: ",
            size_hint=[.4, .1],
            multiline=False,
            pos_hint= {'x': .3, "y": .7},
            padding_y= [10, 10],
            padding_x= [10, 10],
            font_name = 'Georgia',
            background_color=get_color_from_hex('ffdde8'),  
            background_normal='',  
            border=(1, 1, 1, 1)  
        )
        self.add_widget(self.nome) 

        self.email = TextInput(
            hint_text="E-mail: ",
            size_hint=[.4, .1],
            multiline=False,
            pos_hint= {'x': .3, "y": .5},
            padding_y= [10, 10],
            padding_x= [10, 10],
            font_name = 'Georgia',
            background_color=get_color_from_hex('ffdde8'),  
            background_normal='',  
            border=(1, 1, 1, 1)  
        )
        self.add_widget(self.email)

        self.celular = TextInput(
            hint_text="Número de telefone: (DDD) ****-****",
            size_hint=[.4, .1],
            multiline=False,
            pos_hint= {'x': .3, "y": .3},
            padding_y= [10, 10],
            padding_x= [10, 10],
            font_name = 'Georgia',
            background_color=get_color_from_hex('ffdde8'),  
            background_normal='',  
            border=(1, 1, 1, 1) 
          )
        
        self.add_widget(self.celular)

        self.data = TextInput(
            hint_text="Data de nascimento: **/**/****",
            size_hint=[.4, .1],
            multiline=True,
            pos_hint= {'x': .3, "y": .1},
            padding_y= [10, 10],
            padding_x= [10, 10],
            font_name = 'Georgia',
            background_color=get_color_from_hex('ffdde8'),  
            background_normal='',  
            border=(1, 1, 1, 1) 
        )
        self.add_widget(self.data)

        self.button2 = Button(
            size_hint = (.1, .05),
            pos_hint = {'x': .45, 'y':.04} ,
            text = 'Adicionar',
             font_name = 'Georgia',
            background_color = ('8208b3')
              )
        self.button2.bind(on_press=self.adicionar_banco)
        self.add_widget(self.button2)

        def adicionar_banco(self, instance):
            conn = sqlite3.connect('contatos.db')
            cursor = conn.cursor()

            cursor.execute('''
            INSERT INTO contato (nome, email, numero, nascimento) VALUES (%s,%s,%s,%s)
                           ''')
            
            conn.commit()
            conn.close()

            print("Contato adicionado")


class TelaAdicionar(App):
    def build(self):
        return Adicionar()

TelaAdicionar().run()