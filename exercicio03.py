

while True:

    usuario = str(input('Digite seu usuario: '))
    senha = str(input('Digite sua senha: '))

    if usuario in senha:
        print('A senha não pode conter partes do usuário')
    else:
        print('Login realizado com sucesso!')
        break
