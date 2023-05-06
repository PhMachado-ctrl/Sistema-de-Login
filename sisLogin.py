'''Módulos'''
import PySimpleGUI as sg #Biblioteca da Interface

'''Váriavel para armazenar o designer'''
layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('',key='mensagem')],
]

'''Janela para ser mostrada na Tela'''
window = sg.Window('Login',layout=layout)

'''Loop de Eventos'''
while True:
    event, values = window.read() #Lê os valores dos eventos que estão na Tela
    
    if event == sg.WIN_CLOSED: #Quando a tela for fechada pare a execução
        break
    elif event == 'login': #se acontecer o evento de apertar o botão de login
        senha_correta = '12345'
        usuario_correto = 'jonathan'
        usuario = values['usuario']
        senha = values['senha']

        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login feito com Sucesso')
        else:
            window['mensagem'].update('Senha ou Usuario incorreto')
