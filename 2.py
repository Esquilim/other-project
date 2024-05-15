vetor = []

for i in range(10):
    numero = float(input(f'Digite o {i+1} numero reais: '))
    vetor.append(numero)

for numero in reversed(vetor):
    print(numero)