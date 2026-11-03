# Exercício 2 – Identificação de palavras - Testes unitários
from exercicio_2 import analisar_texto


def test_1_frase_com_5_palavras():
    assert analisar_texto("Eu gosto de estudar Python") == 5


def test_2_frase_com_uma_palavra():
    assert analisar_texto("Python") == 1


def test_3_frase_vazia():
    assert analisar_texto("") == 0


def test_4_espacos_no_inicio_e_no_final():
    assert analisar_texto("   Olá mundo   ") == 2


def test_5_varios_espacos_entre_palavras():
    assert analisar_texto("Olá     mundo     Python") == 3
