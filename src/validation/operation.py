from dash import ctx
import re

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