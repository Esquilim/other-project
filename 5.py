NUMEROS = 20
inteiros = []
pares = []
impares = []

for i in range(NUMEROS):
    while True:
        try:
            numero = int(input(f"Digite o {i+1}° número inteiro: "))
            break  # Se o usuário digitou um inteiro, saímos do loop
        except ValueError:
            print("Número inválido. Por favor, tente novamente.")

    inteiros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\nInteiros:")
for numero in inteiros:
    print(f"{numero}", end=" ")

print("\nPares:")
for numero in pares:
    print(f"{numero}", end=" ")

print("\nÍmpares:")
for numero in impares:
    print(f"{numero}", end=" ")