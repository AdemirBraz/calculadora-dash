from layout.buttons import create_buttons
from dash import Dash, html, dcc, callback, Output, Input,State,dash
from layout.case import estrutura
import dash_bootstrap_components  as dbc

app = Dash(__name__,
           external_stylesheets=[dbc.themes.BOOTSTRAP])

botoes = create_buttons

app.layout = html.Div([
    html.Div(children=estrutura(), id='my-div'),
    dcc.Button(id='botoes',n_clicks=0),
    html.Div(id=f"btn-{botoes}"),
            
    ])
app.callback(
   Output("my-div", "children"),
   Input('btn-7','n_clicks'),
)
def update_display(value):
    return value

if __name__ == "__main__":
    app.run(debug=True)