# Exercício 1 – Classificação de notas - Testes unitários
from exercicio_1 import classificar_nota


def test_1_nota_8_aprovado():
    assert classificar_nota(8) == "Aprovado"


def test_2_nota_6_recuperacao():
    assert classificar_nota(6) == "Recuperação"


def test_3_nota_4_reprovado():
    assert classificar_nota(4) == "Reprovado"


def test_4_nota_10_aprovado():
    assert classificar_nota(10) == "Aprovado"


def test_5_nota_menos_1_invalida():
    assert classificar_nota(-1) == "Nota inválida"


def test_6_nota_11_invalida():
    assert classificar_nota(11) == "Nota inválida"
