import dash_bootstrap_components as dbc
from dash import html
from logic.constant import operador
# def create_buttons():
#     numeros = []
#     for num in range(0, 10):
#         numeros.append(dbc.Button(num, id= {"type":"btn", "index":num}, color = "dark"))

def create_buttons():
    numeros = [dbc.Button(num, id= {"type":"btn", "index":num}, color = "dark") for num in range(9, 0, -1)]
    operadores = [dbc.Button(opr,id= {"type":"operador","index":opr})for opr in operador]
    return dbc.Row([
        dbc.Col([
            dbc.Row(
                numeros,class_name='w-50 p-1 justify-content-left'
            ),
            dbc.Row(
                dbc.Button(0, id= {"type":"btn", "index":"0"}, color = "dark")
            )
        ]),
        dbc.Col(
            operadores
        )
    ])
    return 

    return dbc.Col([
        dbc.Col(
            dbc.ButtonGroup([
                dbc.Button(7, id={"type": "btn", "index": 7},color='dark'),
                dbc.Button('8', id={"type": "btn", "index": 8},color='dark'),
                dbc.Button('9', id={"type": "btn", "index": 9},color='dark'),
                dbc.Button('x', id={"type": "operador", "index": '*'},color='dark'),
            ], class_name='w-100 p-1 ')),
        dbc.Col(
            dbc.ButtonGroup([
                dbc.Button('4', id={"type": "btn", "index": 4},color='dark'),
                dbc.Button('5', id={"type": "btn", "index": 5},color='dark'),
                dbc.Button('6', id={"type": "btn", "index": 6},color='dark'),
                dbc.Button('-', id={"type": "operador", "index":'-'},color='dark'),
            ], class_name='w-100 p-1 ')),
        dbc.Col(
            dbc.ButtonGroup([
                dbc.Button('1', id={"type": "btn", "index": 1},color='dark'),
                dbc.Button('2', id={"type": "btn", "index": 2},color='dark'),
                dbc.Button('3', id={"type": "btn", "index": 3},color='dark'),
                dbc.Button('+', id={"type": "operador", "index": '+'},color='dark'),
            ], class_name='w-100 p-1 ')),
        dbc.Col(
            dbc.ButtonGroup([
                dbc.Button('0', id={"type": "btn", "index": 0},color='dark'),
                dbc.Button('.', id={"type": "operador", "index": '.'},color='dark'),
                dbc.Button('÷', id={"type": "operador", "index": '/'},color='dark'),
                dbc.Button('=', id={"type": "operador", "index": '='},color='warning'),
            ], class_name='w-100 p-1 '))
    ], className='g-2')
