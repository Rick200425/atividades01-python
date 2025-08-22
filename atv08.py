def executar():
    entrada = input("Digite um número inteiro: ").strip()
    try:
        n = int(entrada)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return
    
    if n % 2 == 0:
        print(f"{n} é PAR.")
    else:
        print(f"{n} é ÍMPAR.")
        