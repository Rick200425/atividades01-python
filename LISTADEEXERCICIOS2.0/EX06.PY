while True:
    print("\n>>>> MENU DO BANCO <<<<")
    print("1. Ver Saldo")
    print("2. Fazer Depósito")
    print("3. Fazer Saque")
    print("4. Sair")
    print("0. Encerrar")

    escolha = input("Escolha uma opção: ")

    
    if not escolha.isdigit():
        print("Entrada inválida! Digite apenas números.")
        continue

    escolha = int(escolha)

    if escolha == 1:
        print("Você escolheu 'Ver Saldo'.")
    elif escolha == 2:
        print("Você escolheu 'Fazer Depósito'.")
    elif escolha == 3:
        print("Você escolheu 'Fazer Saque'.")
    elif escolha == 4 or escolha == 0:
        print("Saindo... Obrigado por usar nosso banco!")
        break
    else:
        print("Opção inválida! Tente novamente.")