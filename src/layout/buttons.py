import dash_bootstrap_components as dbc
from dash import html
from logic.constant import operador
# def create_buttons():
#     numeros = []
#     for num in range(0, 10):
#         numeros.append(dbc.Button(num, id= {"type":"btn", "index":num}, color = "dark"))

ultima_linha = [0, ".", "="]

def create_buttons():
    numeros = [dbc.Button(num, id= {"type":"btn", "index":num}, color = "dark", class_name="w-25 m-1") for num in range(9, 0, -1)]
    operadores = [dbc.Button(opr,id= {"type":"operador","index":opr}, color='warning', class_name='w-100 m-1' )for opr in operador]
    last_row = [dbc.Button(symbol, id= {"type":"btn", "index":symbol}, color = "dark", class_name="w-25 m-1") for symbol in ultima_linha]
    return dbc.Row([
        dbc.Col([
            dbc.Row(
                numeros
            ),
            dbc.Row(
                last_row
            )
        ], width=8),
        dbc.Col(
            operadores,
        width=4 ,class_name='d=flex justify-content-left')
    ], class_name="px-1 mt-2")

