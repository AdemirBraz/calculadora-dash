from dash import ctx
import re

def normalizar_numeros(expressao):
    def remover_zeros_esquerda(match):
        num = match.group(0)
        num_limpo = str(int(num))
        return num_limpo

    return re.sub(r'\d+', remover_zeros_esquerda, expressao)

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
            expressao_normalizada = normalizar_numeros(valor_input)
            resultado = eval(expressao_normalizada)
            return str(resultado)
        except ZeroDivisionError:
            return 'erro nao pode dividir por zero'
        except Exception:
            print('ERRO')
            return 'erro'
    else:
        if valor == '0':
            valor_input_limpo = valor_input.strip()
            last_operador_index = -1
            for i in range(len(valor_input_limpo) - 1, -1, -1):
                if valor_input_limpo[i] in operador:
                    last_operador_index = i
                    break
            numero_atual = valor_input_limpo[last_operador_index + 1:]
            if numero_atual.startswith('0') and '.' not in numero_atual and numero_atual != '':
                return valor_input
        valor_input += valor
    return valor_input