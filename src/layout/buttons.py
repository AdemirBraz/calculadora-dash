import dash_bootstrap_components as dbc
from dash import html

def create_buttons():
    return dbc.Col([
        dbc.Col(
            dbc.ButtonGroup([
                dbc.Button('C', id="clear", color="danger"),
                dbc.Button('7', id={"type": "btn", "index": 7}),
                dbc.Button('8', id={"type": "btn", "index": 8}),
                dbc.Button('9', id={"type": "btn", "index": 9}),
                dbc.Button('÷', id={"type": "operador", "index": '/'})
            ], id='botoes-1', class_name='w-100 p-1')),
        dbc.Col(
            dbc.ButtonGroup([
                dbc.Button('4', id={"type": "btn", "index": 4}),
                dbc.Button('5', id={"type": "btn", "index": 5}),
                dbc.Button('6', id={"type": "btn", "index": 6}),
                dbc.Button('x', id={"type": "operador", "index": '*'})
            ], class_name='w-100 p-1')),
        dbc.Col(
            dbc.ButtonGroup([
                dbc.Button('1', id={"type": "btn", "index": 1}),
                dbc.Button('2', id={"type": "btn", "index": 2}),
                dbc.Button('3', id={"type": "btn", "index": 3}),
                dbc.Button('-', id={"type": "operador", "index":'-'})
            ], class_name='w-100 p-1')),
        dbc.Col(
            dbc.ButtonGroup([
                dbc.Button('0', id={"type": "btn", "index": 0}),
                dbc.Button('.', id={"type": "operador", "index": '.'}),
                dbc.Button('=', id={"type": "operador", "index": '='}),
                dbc.Button('+', id={"type": "operador", "index": '+'})
            ], class_name='w-100 p-1'))
    ], className='g-2')
