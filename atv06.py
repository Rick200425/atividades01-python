usuario = "Henrique"
senha = "Helloworld"

loginusuario = input("Digite seu usuario: ")
loginsenha = input("Digite sua senha: ")

if loginusuario == usuario and loginsenha == senha:
    print("Login realizado com sucesso!")
else:
    print("Usuario ou senha estão incorretos")
