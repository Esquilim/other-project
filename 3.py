3. # Lendo as 4 notas do usuário
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota: "))

# Calculando a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibindo as notas e a média
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print(f"Nota 4: {nota4}")
print(f"Média: {media:.2f}")