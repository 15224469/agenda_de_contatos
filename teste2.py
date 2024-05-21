from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
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
        self.but1.bind(on_press=self.abrir_lista_contatos)
        self.add_widget(self.but1)

        self.but2 = Button(
            text='Adicionar Contato',
            size_hint=(.4, .1),
            pos_hint= {'x': .3, "y": .3},
            background_color = get_color_from_hex('#560CAD')
        )
        self.add_widget(self.but2)

    def abrir_lista_contatos(self, instance):
        App.get_running_app().root.switch_to(ListaContatos())

class ListaContatos(FloatLayout):
    def __init__(self, **kwargs):
        super(ListaContatos, self).__init__(**kwargs)
        self.orientation='horizontal'
        self.spacing= 5
        self.padding=[20, 10]
        Window.clearcolor = get_color_from_hex('#620096') 

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
        self.but1.bind(on_press=self.voltar_tela_inicial)
        self.add_widget(self.but1)

    def voltar_tela_inicial(self, instance):
        App.get_running_app().root.switch_to(BemVindo())

class GerenciadorTelas(FloatLayout):
    def __init__(self, **kwargs):
        super(GerenciadorTelas, self).__init__(**kwargs)
        self.bem_vindo = BemVindo()
        self.add_widget(self.bem_vindo)

    def switch_to(self, tela):
        self.clear_widgets()
        self.add_widget(tela)

class MinhaApp(App):
    def build(self):
        return GerenciadorTelas()
     
if __name__ == '__main__':
    MinhaApp().run() 
