alguem_reprovou = False

for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i+1} (0 a 10): "))

    while nota < 0 or nota > 10:
        print("Nota inválida, digite entre 0 e 10.")
        nota = float(input(f"Digite a nota do aluno {i+1} (0 a 10): "))

    if nota < 5:
        alguem_reprovou = True

print("===== RESULTADO =====")
if alguem_reprovou:
    print("A turma possui pelo menos um aluno reprovado.")
else:
    print("Parabéns! Todos na turma foram aprovados.")
