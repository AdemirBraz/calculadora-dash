from dash import ctx
import re
from logic.constant import operador

def last_op_index(s):
    return max((i for i, c in enumerate(s) if c in operador), default=-1)


def normalizar_numeros(expressao):
    def remover_zeros_esquerda(match):
        num = match.group(0)
        num_limpo = str(int(num))
        return num_limpo

    return re.sub(r'\d+', remover_zeros_esquerda, expressao)

def validar(valor_input):
    try:
        expressao_normalizada = normalizar_numeros(valor_input)
        resultado = eval(expressao_normalizada)
        return str(resultado)
    except ZeroDivisionError:
        return 'erro nao pode dividir por zero'
    except Exception:
        return 'erro'
    
def bloquear(valor, valor_input):
    valor_input = (valor_input or "").strip()
    if not valor_input:
        if valor in operador or valor == '.':
            return True
        return False

    if valor == '.':
        if valor_input[-1] in operador:
            return True
        if '.' in valor_input[last_op_index(valor_input) + 1:]:
            return True

    elif valor in operador:
        pass

    elif valor == '0':
        idx = last_op_index(valor_input.strip())
        numero_atual = valor_input.strip()[idx + 1:]
        if numero_atual.startswith('0') and '.' not in numero_atual:
            return True

    return False