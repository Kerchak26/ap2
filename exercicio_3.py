# Exercício 3 – Verificação de números


def analisar_numero(numero):
    if numero > 0:
        sinal = "Positivo"
    elif numero < 0:
        sinal = "Negativo"
    else:
        sinal = "Zero"

    if numero % 2 == 0:
        tipo = "par"
    else:
        tipo = "ímpar"

    return sinal + " e " + tipo
