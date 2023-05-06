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