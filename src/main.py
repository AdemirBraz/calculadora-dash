from layout.buttons import create_buttons
from dash import Dash, html, dcc, callback, Output, Input, State, ALL,ctx
from layout.case import estrutura
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

botoes = create_buttons

app.layout = html.Div([
    html.Div(children=estrutura(), id='my-div'),
    dcc.Button(id='btn-1', n_clicks=0),
    html.Div(id="btn",)
])

@app.callback(
    Output("text", "value"),
    Input({"type": "btn", "index": ALL}, "n_clicks"),
    Input({"type": "operador", "index": ALL}, "n_clicks"),
    Input("clear", "n_clicks"),
    State('text','value'),
    prevent_initial_call=True
)

def update_display(btn_clicks, operador_clicks, clear_clicks,valor_input):    
   trigger=ctx.triggered_id
   print(trigger['index'])
   valor_input+=1
   return trigger['index']
if __name__ == "__main__":
    app.run(debug=True)
