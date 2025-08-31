CARDAPIO = {
    1: {"nome": "Coxinha", "preço": 4.00},
    2: {"nome": "Pastel", "preço": 6.00},
    3: {"nome": "Risole", "preço": 5.00},
}

def executar():
    print("\n--- Cardápio ---")
    for codigo, item in CARDAPIO.items():
        print(f"{codigo} - {item['nome']} - R$ {item['preço']:.2f}")

        entrada = input("Digite o código do item desejado: ").strip()
        try:
            codigo = int(entrada)
        except ValueError:
            print("Opção inválida (não é número).")
            return

        if codigo in CARDAPIO:
            item = CARDAPIO[codigo]
            print(f"Você escolheu: {item['nome']} - R$ {item['preço']:.2f}")
        else:
            print("Opção inválida.")



if __name__ == "__main__":
    executar()
                
