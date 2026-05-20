import dash_bootstrap_components  as dbc
from dash import html

def create_buttons():
        return dbc.Col([
                dbc.Col(dbc.ButtonGroup([dbc.Button('7',id='btn-7'),dbc.Button('8'),dbc.Button('9'),dbc.Button('/')],id='botoes',class_name='w-100 p-1')),
                dbc.Col(dbc.ButtonGroup([dbc.Button('4'),dbc.Button('5'),dbc.Button('6'),dbc.Button('*')],id='botoes',class_name='w-100 p-1')),
                dbc.Col(dbc.ButtonGroup([dbc.Button('1'),dbc.Button('2'),dbc.Button('3'),dbc.Button('-')],id='botoes',class_name='w-100 p-1')),
                dbc.Col(dbc.ButtonGroup([dbc.Button('0'),dbc.Button('.'),dbc.Button('='),dbc.Button('+')],id='botoes',class_name='w-100 p-1')),
        ], className='g-2')      