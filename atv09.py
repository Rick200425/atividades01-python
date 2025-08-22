import random

OPCOES = {"1": "pedra", "2": "papel", "3": "tesoura"}

def executar():
    print("Escolha: 1) pedra  2) papel  3) tesoura")
    escolha_usuario = input("Sua escolha: ").strip().lower()

    if escolha_usuario not in OPCOES:
        print("Opção inválida.")
        return

    jogador = OPCOES[escolha_usuario]
    computador = random.choice(list(OPCOES.values()))

    print(f"Você: {jogador} | Computador: {computador}")

    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "tesoura" and computador == "papel") or \
         (jogador == "papel" and computador == "pedra"):
        print("Você venceu!")
    else:
        print("Computador venceu!")