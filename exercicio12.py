n = int(input("Digite o número da tabuada: "))
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

for i in range(inicio, fim+1):
    print(f"{n} x {i} = {n*i}")
