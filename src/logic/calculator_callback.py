from dash import callback, Output, Input, State, ALL, ctx, no_update
from validation.operation import validar, bloquear
from logic.constant import operador
from validation.operation import normalizar_numeros

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
        return ""

    valor = str(trigger['index'])
    valor_input = valor_input or ""

    if bloquear(valor, valor_input):
        return no_update

    if valor == '=':
        try:
            expressao_normalizada = normalizar_numeros(valor_input)
            resultado = eval(expressao_normalizada)
            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)
            return str(resultado)
        except Exception:
            return no_update

    if valor in operador and valor_input and valor_input[-1] in operador:
        return valor_input[:-1] + valor

    return valor_input + valor