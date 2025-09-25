luz_acesa = False

while True:
    escolha = input("O que fazer? (1: apertar interruptor, 0: sair): ")

    if escolha == "1":
        luz_acesa = not luz_acesa
        if luz_acesa:
            print("A luz está ACESA.")
        else:
            print("A luz está APAGADA.")
    elif escolha == "0":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida, tente novamente.")
