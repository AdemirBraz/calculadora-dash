from layout.buttons import create_buttons
from dash import Dash, html, dcc, callback, Output, Input,State, ALL
from layout.case import estrutura
import dash_bootstrap_components  as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

botoes = create_buttons

app.layout = html.Div([
    html.Div(children=estrutura(), id='my-div'),
    dcc.Button(id='btn-1',n_clicks=0),
    html.Div(id="btn",),
            
    ])

@app.callback(
   Output("btn","children"),
   Input({"type": "btn", "index": ALL}, "n_clicks"),
   Input({"type": "operador", "index": ALL}, "n_clicks"),

)
def update_display(btn_clicks, operador_clicks):
    if not btn_clicks and not operador_clicks:
        return
    return btn_clicks or operador_clicks

if __name__ == "__main__":
    app.run(debug=True)