from dash import callback, Output, Input, State, ALL, ctx, no_update
from validation.operation import validar, bloquear, update_operador
from logic.constant import operador

@callback(
    Output("text", "value"),
    Input({"type": "btn", "index": ALL}, "n_clicks"),
    Input({"type": "operador", "index": ALL}, "n_clicks"),
    Input("clear", "n_clicks"),
    State('text', 'value'),
    prevent_initial_call=True
)
def update_display(_, __, ___, valor_input = ""):
    trigger = ctx.triggered_id

    if trigger == 'clear':
        return ""

    valor = str(trigger['index'])

    if bloquear(valor, valor_input):
        return no_update

    if valor == '=':
        #aqui retorna o resultado formatado pela validação
        return validar(valor_input)

    #deixei um comentario na definição dessa função
    if update_operador(valor, valor_input): 
        return valor_input[:-1] + valor

    return valor_input + valor