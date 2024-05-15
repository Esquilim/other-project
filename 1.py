# Projeto para ler todos os numeros inteiros
vetor = []
#  Inserindo os numeros de 1 a 5
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)

# Numeros lidos
print("Números lidos:")
for numero in vetor:
# Executando em print
    print(numero)