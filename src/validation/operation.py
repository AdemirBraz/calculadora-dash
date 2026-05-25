from dash import ctx
def bugs(operador_clicks,valor_input):
    trigger=ctx.triggered_id
    operador=['/','*','+','-']
    if trigger=='clear':
        return " "
    valor=str(trigger['index'])
    if valor_input is None:
        valor_input = ''
    else:
        valor_input=str(valor_input)
    if valor == '.':
        if valor_input == "":
            return valor_input
        if valor_input[-1] in operador:
            return valor_input
        last_operador_index = -1
        for i in range(len(valor_input) - 1, -1, -1):
            if valor_input[i] in operador:
                last_operador_index = i
                break
        if '.' in valor_input[last_operador_index + 1:]:
            return valor_input
        valor_input += valor
    elif valor in operador:
        if valor_input == "":
            return valor_input
        if valor_input[-1] in operador:
            return valor_input
        valor_input += valor
    elif valor == '=':
        try:
            resultado = eval(valor_input)
            return str(resultado)
        except ZeroDivisionError:
            return 'erro nao pode dividir por zero'
        except Exception:
            print('ERRO')
            return 'erro'
    else:
        valor_input += valor
    return valor_input