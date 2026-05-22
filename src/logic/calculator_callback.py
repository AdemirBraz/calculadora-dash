from dash import Dash, html, dcc, callback, Output, Input, State, ALL,ctx
import dash_bootstrap_components as dbc
from layout.case import estrutura
from layout.buttons import create_buttons
@callback(
    Output("text", "value"),
    Input({"type": "btn", "index": ALL}, "n_clicks"),
    Input({"type": "operador", "index": ALL}, "n_clicks"),
    Input("clear", "n_clicks"),
    State('text','value'),
    prevent_initial_call=True
)

def update_display(btn_clicks,operador_clicks,clear_clicks ,valor_input):    
    trigger=ctx.triggered_id
    if trigger=='clear':
        return " "
    valor=str(trigger['index'])
    if valor_input is None:
        valor_input = ''
    else:
        valor_input=str(valor_input)
    if valor == '=':
        try:
            resultado = eval(valor_input)
            return str(resultado)
        except:
            print('ERRO')
    
    valor_input += valor
    return valor_input