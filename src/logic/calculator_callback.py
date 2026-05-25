from dash import  callback, Output, Input, State, ALL,ctx
from validation import operation
@callback(
    Output("text", "value"),
    Input({"type": "btn", "index": ALL}, "n_clicks"),
    Input({"type": "operador", "index": ALL}, "n_clicks"),
    Input("clear", "n_clicks"),
    State('text','value'),
    prevent_initial_call=True
)
def update_display(btn_clicks,operador_clicks,clear_clicks ,valor_input):
    return operation.bugs(operador_clicks,valor_input)
    
    