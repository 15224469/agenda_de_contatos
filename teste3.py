from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from bdcontatos import insert
from conexaobd import connect

mydb = connect()

class ListaContatos(FloatLayout):
    def __init__(self, **kwargs):
        mydb = connect()
        super(ListaContatos, self).__init__(**kwargs)
        self.spacing = 5
        self.padding = [20, 10]
        Window.clearcolor = get_color_from_hex('#620096')

        self.nota = Label(
            text='Lista de Contatos:',
            font_size=45,
            font_name='Georgia',
            size_hint_y=None,
            pos_hint={'x': .013, "y": .7}
        )
        self.add_widget(self.nota)

        texto = ""  # Inicializa a variável texto

        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM contato")
        contatos = cursor.fetchall()

        for contato in contatos:
            texto += f"Nome: {contato[0]}, Email: {contato[1]}, Número: {contato[2]}, Nascimento: {contato[3]}\n"
        
        self.list = Label(
            text=texto, font_size=16,
            font_name='Georgia',
            size_hint_y=None,
            pos_hint={'x': .016, "y": .5}
        )
        self.add_widget(self.list)  # Adiciona o widget self.list à instância de ListaContatos

        self.but1 = Button(
            text='Voltar a tela de início',
            size_hint=(.2, .1),
            pos_hint={'x': .2, "y": .1},
            background_color=get_color_from_hex('#560CAD')
        )
        self.but1.bind(on_press=self.voltar_tela_inicial)
        self.add_widget(self.but1)

        self.but2 = Button(
            text='Excluir Contato',
            size_hint=(.2, .1),
            pos_hint={'x': .6, "y": .1},
            background_color=get_color_from_hex('#560CAD')
        )
        self.but2.bind(on_press=self.excluir_contato)
        self.add_widget(self.but2)

    def voltar_tela_inicial(self, instance):
        App.get_running_app().root.switch_to(BemVindo())

    def excluir_contato(self, instance):
        self.clear_widgets()
        self.add_widget(self.nota)

        self.label_excluir = Label(
            text='Selecione o contato para excluir!',
            font_size=30,
            font_name='Georgia',
            size_hint_y=None,
            pos_hint={'x': .013, "y": .6}
        )
        self.add_widget(self.label_excluir)

class BemVindo(FloatLayout):
    def __init__(self, **kwargs):
        super(BemVindo, self).__init__(**kwargs)
        Window.clearcolor = get_color_from_hex('#620096')

        self.label = Label(
            text='Seja Bem Vindo(a) a Agenda de Contatos!',
            font_size=45,
            font_name='Georgia',
            size_hint_y=None,
            pos_hint={'x': .013, "y": .7}
        )
        self.add_widget(self.label)

        self.but1 = Button(
            text='Ir para Lista de Contatos',
            size_hint=(.2, .1),
            pos_hint={'x': .4, "y": .5},
            background_color=get_color_from_hex('#560CAD')
        )
        self.but1.bind(on_press=self.lista_contatos)
        self.add_widget(self.but1)

        self.but2 = Button(
            text='Adicionar Contato',
            size_hint=(.2, .1),
            pos_hint={'x': .4, "y": .3},
            background_color=get_color_from_hex('#560CAD')
        )
        self.but2.bind(on_press=self.adicionar_contato)
        self.add_widget(self.but2)

    def lista_contatos(self, instance):
        App.get_running_app().root.switch_to(ListaContatos())

    def adicionar_contato(self, instance):
        App.get_running_app().root.switch_to(Adicionar())

class Adicionar(FloatLayout):
    def __init__(self, **kwargs):
        super(Adicionar, self).__init__(**kwargs)
        self.spacing = 5
        self.padding = [20, 10]
        Window.clearcolor = get_color_from_hex('#620096')

        self.label = Label(
            text='ADICIONE O CONTATO:',
            font_size=40,
            font_name='Georgia',
            size_hint_y=None,
            pos_hint={'x': .013, "y": .8}
        )
        self.add_widget(self.label)

        self.nome = TextInput(
            hint_text="Nome Completo: ",
            size_hint=[.4, .1],
            multiline=False,
            pos_hint={'x': .3, "y": .7},
            font_name='Georgia',
            background_color=get_color_from_hex('ffdde8'),
            background_normal='',
            border=(1, 1, 1, 1)
        )
        self.add_widget(self.nome)

        self.email = TextInput(
            hint_text="E-mail: ",
            size_hint=[.4, .1],
            multiline=False,
            pos_hint={'x': .3, "y": .5},
            font_name='Georgia',
            background_color=get_color_from_hex('ffdde8'),
            background_normal='',
            border=(1, 1, 1, 1)
        )
        self.add_widget(self.email)

        self.celular = TextInput(
            hint_text="Número de telefone: (DDD) ****-****",
            size_hint=[.4, .1],
            multiline=False,
            pos_hint={'x': .3, "y": .3},
            font_name='Georgia',
            background_color=get_color_from_hex('ffdde8'),
            background_normal='',
            border=(1, 1, 1, 1)
        )
        self.add_widget(self.celular)

        self.data = TextInput(
            hint_text="Data de nascimento: ano-mês-dia",
            size_hint=[.4, .1],
            multiline=True,
            pos_hint={'x': .3, "y": .1},
            font_name='Georgia',
            background_color=get_color_from_hex('ffdde8'),
            background_normal='',
            border=(1, 1, 1, 1)
        )
        self.add_widget(self.data)

        self.button2 = Button(
            size_hint=(.1, .05),
            pos_hint={'x': .45, 'y': .04},
            text='Adicionar',
            font_name='Georgia',
            background_color=get_color_from_hex('8208b3')
        )
        self.button2.bind(on_press=self.register_contato)
        self.add_widget(self.button2)

    def register_contato(self, instance):
        name = self.nome.text
        email = self.email.text
        celular = self.celular.text
        data = self.data.text
        if name and email and celular and data:
            contato = insert(mydb, name, email, celular, data)
            self.limpar_campos()
            self.lista(instance)

    def limpar_campos(self):
        self.nome.text = ''
        self.email.text = ''
        self.celular.text = ''
        self.data.text = ''

    def lista(self, instance):
        App.get_running_app().root.switch_to(ListaContatos())

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