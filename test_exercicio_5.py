# Exercício 5 – Validação de senha com Mock - Testes unitários
from unittest.mock import patch
from exercicio_5 import criar_conta


def test_1_senha_valida():
    assert criar_conta("Carlos", "senha123") == "Conta criada com sucesso"


def test_2_senha_invalida():
    assert criar_conta("Carlos", "abc") == "Senha inválida"


@patch("exercicio_5.verificar_senha")
def test_3_verificar_senha_foi_chamada(mock_verificar):
    mock_verificar.return_value = True
    criar_conta("Carlos", "senha123")
    mock_verificar.assert_called()


@patch("exercicio_5.verificar_senha")
def test_4_chamada_com_senha_correta(mock_verificar):
    mock_verificar.return_value = True
    criar_conta("Carlos", "senha123")
    mock_verificar.assert_called_with("senha123")


@patch("exercicio_5.verificar_senha")
def test_5_mock_senha_valida(mock_verificar):
    mock_verificar.return_value = True
    assert criar_conta("Carlos", "qualquer") == "Conta criada com sucesso"


@patch("exercicio_5.verificar_senha")
def test_6_mock_senha_invalida(mock_verificar):
    mock_verificar.return_value = False
    assert criar_conta("Carlos", "qualquer") == "Senha inválida"
