# Exercício 1 – Classificação de notas


def classificar_nota(nota):
    if nota < 0 or nota > 10:
        return "Nota inválida"
    elif nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
