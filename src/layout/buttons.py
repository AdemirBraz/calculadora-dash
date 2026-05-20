import dash_bootstrap_components  as dbc
from dash import html

lista = []
simbolos = ["/", "x", ...]

def btnss():
        for i in range(0, 10):
                lista.append(dbc.Button(i, id={"type": "btn", "index": i}))

        for pos, simbolo in enumerate(simbolos):
                dbc.Button(simbolo, id={"type": "operador", "index": pos})
        return lista # [ botao1, botao2 ...]

def create_buttons():
        return dbc.Col([
                dbc.Col(
                        dbc.ButtonGroup([
                                dbc.Button('7', id={"type": "btn", "index": 0}),
                                dbc.Button('8', id={"type": "btn", "index": 1}),
                                dbc.Button('9'),
                                dbc.Button('/')
                        ], id='botoes-1',class_name='w-100 p-1')),
                dbc.Col(
                        dbc.ButtonGroup([
                                dbc.Button('4'),
                                dbc.Button('5'),
                                dbc.Button('6'),
                                dbc.Button('*')
                        ],class_name='w-100 p-1')),
                dbc.Col(
                        dbc.ButtonGroup([
                                dbc.Button('1'),
                                dbc.Button('2'),
                                dbc.Button('3'),
                                dbc.Button('-')
                        ],class_name='w-100 p-1')),
                dbc.Col(
                        dbc.ButtonGroup([
                                dbc.Button('0'),
                                dbc.Button('.'),
                                dbc.Button('='),
                                dbc.Button('+')
                        ],class_name='w-100 p-1')),
        ], className='g-2')      