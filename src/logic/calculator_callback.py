from dash import callback, Output, Input, State, ALL, ctx, no_update
from validation.operation import validar, bloquear
from logic.constant import operador

@callback(
    Output("text", "value"),
    Input({"type": "btn", "index": ALL}, "n_clicks"),
    Input({"type": "operador", "index": ALL}, "n_clicks"),
    Input("clear", "n_clicks"),
    State('text', 'value'),
    prevent_initial_call=True
)
def update_display(_, operador_clicks, __, valor_input):
    trigger = ctx.triggered_id

    if trigger == 'clear':
        return " "

    valor = str(trigger['index'])
    valor_input = valor_input or ""

    if bloquear(valor, valor_input):
        return no_update

    if valor == '=':
        return validar(operador_clicks, valor_input)

    return valor_input + valor