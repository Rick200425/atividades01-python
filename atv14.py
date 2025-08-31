idades = []

while True:
    idade = int(input("Digite uma idade (-1 para sair): "))
    if idade == -1:
        break
    idades.append(idade)

    maiores_idade = 0
    for idade in idades:
        if idade >= 18:
            maiores_idade += 1


    print(f"Total de pessoa maiores de idade: {maiores_idade}")
