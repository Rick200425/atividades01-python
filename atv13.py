notas = [8.5, 9.0, 6.5, 10.0, 7.5]
soma = 0


for nota in notas:
    soma += nota


media = soma / len(notas)
print(f"A nota média da turma é: {media:.2f}")
