# Exercício 6 – Sistema de reserva de assentos com Mock


def verificar_assento(numero_assento):
    assentos_ocupados = [3, 7, 10]
    return numero_assento not in assentos_ocupados


def reservar_assento(numero_assento):
    return "Assento reservado"


def confirmar_reserva(numero_assento):
    if verificar_assento(numero_assento):
        return reservar_assento(numero_assento)
    else:
        return "Assento indisponível"
