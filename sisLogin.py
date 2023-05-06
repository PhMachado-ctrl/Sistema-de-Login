'''Módulos'''
import PySimpleGUI as sg #Biblioteca da Interface

'''Váriavel para armazenar o designer'''
layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('Login')],
    [sg.Text('',key='mensagem')],
]

'''Janela para ser mostrada na Tela'''
window = sg.Window('Login',layout=layout)

'''Loop de Eventos'''
while True:
    event, values = window.read() #Lê os valores dos eventos que estão na Tela
    #Quando a tela for fechada pare a execução
    if event == sg.WIN_CLOSED:
        break