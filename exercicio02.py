nome = ""
idade =-1
salario =-1
genero = ""
situacao = ""


while len(nome) < 4:
    nome = str(input("Digite o seu nome: "))
   
while idade < 0 or idade > 100:
    idade = int(input("Digite sua idade: "))

while salario < 0:
    salario = float(input("Qual seu sálario: "))

while genero not in ['F', 'M', 'O']:
    genero = input("Digite seu gênero ('F' - feminino, 'M' - masculino, 'O' - outro): ").upper()

while situacao not in ['E', 'D', 'A']:
    situacao = input("Digite sua situação ('E' - empregado, 'D' - desempregado, 'A' - autônomo): ").upper()


print("\nDados validados:")
print("Nome:", nome)
print("Idade:", idade)
print("Salário:", salario)
print("Gênero:", genero)
print("Situação:", situacao)




    
