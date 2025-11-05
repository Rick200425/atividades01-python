class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print(f'O nome é {self.nome} e sua idade é {self.idade} anos.')


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        
        super().__init__(nome, idade)
        self.matricula = matricula

    def exibir_dados(self):
       
        super().exibir_dados()
        print(f'Matrícula: {self.matricula}')


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def exibir_dados(self):
        
        super().exibir_dados()
        print(f'Disciplina: {self.disciplina}')



print("---PAI---")
pai = Pessoa("Severino", 65)
pai.exibir_dados()

print("\n---ALUNO---")
aluno = Aluno("Henrique", 21, "2025")
aluno.exibir_dados()

print("\n---PROFESSOR---")
professor = Professor("Elvis", 35, "Matemática e Física")
professor.exibir_dados()
