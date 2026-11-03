# Exercício 6 – Sistema de reserva de assentos com Mock - Testes unitários
from unittest.mock import patch
from exercicio_6 import confirmar_reserva


def test_1_reserva_realizada_com_sucesso():
    assert confirmar_reserva(1) == "Assento reservado"


def test_2_assento_indisponivel():
    assert confirmar_reserva(3) == "Assento indisponível"


@patch("exercicio_6.verificar_assento")
def test_3_verificar_assento_foi_chamada(mock_verificar):
    mock_verificar.return_value = True
    confirmar_reserva(1)
    mock_verificar.assert_called_with(1)


@patch("exercicio_6.reservar_assento")
@patch("exercicio_6.verificar_assento")
def test_4_reservar_chamada_quando_disponivel(mock_verificar, mock_reservar):
    mock_verificar.return_value = True
    confirmar_reserva(1)
    mock_reservar.assert_called_with(1)


@patch("exercicio_6.reservar_assento")
@patch("exercicio_6.verificar_assento")
def test_5_reservar_nao_chamada_quando_indisponivel(mock_verificar, mock_reservar):
    mock_verificar.return_value = False
    confirmar_reserva(1)
    mock_reservar.assert_not_called()


@patch("exercicio_6.reservar_assento")
@patch("exercicio_6.verificar_assento")
def test_6_mock_simula_cenarios(mock_verificar, mock_reservar):
    mock_reservar.return_value = "Assento reservado"

    mock_verificar.return_value = True
    assert confirmar_reserva(5) == "Assento reservado"

    mock_verificar.return_value = False
    assert confirmar_reserva(5) == "Assento indisponível"
