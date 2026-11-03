# Exercício 4 – Geração de saudação com Mock - Testes unitários
from unittest.mock import patch
from exercicio_4 import gerar_saudacao


def test_1_saudacao_gerada_corretamente():
    assert gerar_saudacao(1) == "Olá, Carlos! Seja bem-vindo."


@patch("exercicio_4.buscar_nome")
def test_2_buscar_nome_foi_chamada(mock_buscar_nome):
    mock_buscar_nome.return_value = "Carlos"
    gerar_saudacao(1)
    mock_buscar_nome.assert_called()


@patch("exercicio_4.buscar_nome")
def test_3_chamada_com_id_correto(mock_buscar_nome):
    mock_buscar_nome.return_value = "Carlos"
    gerar_saudacao(5)
    mock_buscar_nome.assert_called_with(5)


@patch("exercicio_4.buscar_nome")
def test_4_mock_simula_nomes_diferentes(mock_buscar_nome):
    mock_buscar_nome.return_value = "Ana"
    assert gerar_saudacao(2) == "Olá, Ana! Seja bem-vindo."

    mock_buscar_nome.return_value = "Pedro"
    assert gerar_saudacao(3) == "Olá, Pedro! Seja bem-vindo."
