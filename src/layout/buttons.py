import dash_bootstrap_components as dbc
from logic.constant import operador, ultima_linha

def create_buttons():
    numeros = [dbc.Button(num, id= {"type":"btn", "index":num}, color = "dark", class_name="w-25 m-1") for num in range(9, 0, -1)]
    operadores = [dbc.Button(opr,id= {"type":"operador","index":opr}, color='warning', class_name='w-100 m-1' )for opr in operador]
    last_row = [dbc.Button(symbol, id= {"type":"btn", "index":symbol}, color = "dark", class_name="w-25 m-1") for symbol in ultima_linha]

    left_column = [dbc.Row(numeros), dbc.Row(last_row)] # botei a lista numa variavel pra ficar mais curto embaixo

    return dbc.Row([
        dbc.Col(left_column, width=8), # já que vai ficar curto pode deixar em uma linha só
        dbc.Col(operadores, width=4)
    ], class_name="px-1 mt-2")
