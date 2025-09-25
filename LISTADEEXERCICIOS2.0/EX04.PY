
soma = 0
alunos = int(input("Digite quantos alunos existem na turma: "))


for i in range(alunos):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    while nota < 0 or nota > 10:
        print("Nota inválida! Digite novamente.")
        nota = float(input(f"Digite a nota do aluno {i+1} (0 a 10): "))
    soma += nota
 

media = soma / alunos
print(f"A nota média da turma é: {media:.2f}")
