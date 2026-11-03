# Exercício 4 – Geração de saudação com Mock


def buscar_nome(usuario_id):
    return "Carlos"


def gerar_saudacao(usuario_id):
    nome = buscar_nome(usuario_id)
    return "Olá, " + nome + "! Seja bem-vindo."
