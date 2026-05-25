from layout.buttons import create_buttons
from dash import Dash, html, dcc, callback, Output, Input, State, ALL,ctx
from layout.case import estrutura
import dash_bootstrap_components as dbc
import logic.calculator_callback
import validation.operation
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

botoes = create_buttons

app.layout = html.Div([
    html.Div(children=estrutura(), id='my-div'),
    dcc.Button(id='btn-1', n_clicks=0),
    html.Div(id="btn",)
])

if __name__ == "__main__":
    app.run(debug=True)
