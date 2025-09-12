while True:
    # Entrada e validação da população A
    popA = 0
    while popA <= 0:
        popA = int(input("Digite a população inicial da cidade A: "))
        if popA <= 0:
            print("Valor inválido! Digite um número positivo.")
    
    # Entrada e validação da população B
    popB = 0
    while popB <= 0:
        popB = int(input("Digite a população inicial da cidade B: "))
        if popB <= 0:
            print("Valor inválido! Digite um número positivo.")
    
    # Entrada e validação da taxa de crescimento A
    cres_a = 0
    while cres_a <= 0:
        cres_a = float(input("Digite o percentual de crescimento da cidade A (%): "))
        if cres_a <= 0:
            print("Valor inválido! Digite um número positivo.")
    
    # Entrada e validação da taxa de crescimento B
    cres_b = 0
    while cres_b <= 0:
        cres_b = float(input("Digite o percentual de crescimento da cidade B (%): "))
        if cres_b <= 0:
            print("Valor inválido! Digite um número positivo.")
    
    # Transformar as taxas em multiplicadores (ex.: 3,5% -> 1.035)
    cres_a = 1 + (cres_a / 100)
    cres_b = 1 + (cres_b / 100)

    # Cálculo do crescimento ano a ano
    anos = 0
    while popA <= popB:
        popA *= cres_a
        popB *= cres_b
        anos += 1
    
    print(f"\nSerão necessários {anos} anos para que a população da cidade A ultrapasse a de B.")
    print(f"População final de A: {int(popA)}")
    print(f"População final de B: {int(popB)}\n")
    
    # Perguntar se o usuário quer repetir
    repetir = input("Deseja realizar outro cálculo? (s/n): ").strip().lower()
    if repetir != "s":
        print("Programa encerrado.")
        
