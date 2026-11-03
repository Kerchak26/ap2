# Exercício 3 – Verificação de números - Testes unitários
from exercicio_3 import analisar_numero


def test_1_positivo_e_par():
    assert analisar_numero(10) == "Positivo e par"


def test_2_positivo_e_impar():
    assert analisar_numero(7) == "Positivo e ímpar"


def test_3_negativo_e_par():
    assert analisar_numero(-4) == "Negativo e par"


def test_4_negativo_e_impar():
    assert analisar_numero(-3) == "Negativo e ímpar"


def test_5_zero():
    assert analisar_numero(0) == "Zero e par"
