# Exercício 5 – Validação de senha com Mock


def verificar_senha(senha):
    tem_numero = False
    tem_letra = False

    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
        if caractere.isalpha():
            tem_letra = True

    return len(senha) >= 8 and tem_numero and tem_letra


def criar_conta(nome, senha):
    if verificar_senha(senha):
        return "Conta criada com sucesso"
    else:
        return "Senha inválida"
