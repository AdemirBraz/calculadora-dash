from dash import  callback, Output, Input, State, ALL,ctx, no_update
from validation.operation import validar
from logic.constant import operador

@callback(
    Output("text", "value"),
    Input({"type": "btn", "index": ALL}, "n_clicks"),
    Input({"type": "operador", "index": ALL}, "n_clicks"),
    Input("clear", "n_clicks"),
    State('text','value'),
    prevent_initial_call=True
)
def update_display( _, operador_clicks,__ , valor_input):
    trigger=ctx.triggered_id
    last_operador_index = -1
    if trigger=='clear':
        return " "
    valor=str(trigger['index'])

    "" if valor_input else str(valor_input)

    if valor == '.':
        if valor_input == "":
            print("dmsamdmasd")
            return no_update
        if valor_input[-1] in operador:
            print("dasdasdasdasdsadasd")
            return no_update

        for i in range(len(valor_input) - 1, -1, -1):
            print(f" isso aquiiii {i}")
            if valor_input[i] in operador:
                print(f" isso aquiiii222222222 {i}")
                last_operador_index = i
                break
        if '.' in valor_input[last_operador_index + 1:]: 
            return valor_input

    elif valor in operador:
        if valor_input == "":
            return no_update
        if valor_input[-1] in operador:
            return no_update

    else:
        if valor == '0':
            valor_input_limpo = valor_input.strip()
            for i in range(len(valor_input_limpo) - 1, -1, -1):
                if valor_input_limpo[i] in operador:
                    last_operador_index = i
                    break
            numero_atual = valor_input_limpo[last_operador_index + 1:]
            if numero_atual.startswith('0') and '.' not in numero_atual and numero_atual != '':
                return valor_input

    if valor == '=':
        valor_input = validar(operador_clicks,valor_input)
    else:
        valor_input += valor # concatena os valores

    return valor_input
    
    