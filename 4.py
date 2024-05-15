def ler_vetor() -> [str]:
    caracteres = [input("Digite um caractere: ") for _ in range(10)]
    return caracteres

def verificar_consoantes(caracteres: [str]):
    vogais = {'A', 'E', 'I', 'O', 'U'}
    consoantes = []

    for caractere in caracteres:
        if caractere.upper() not in vogais:
            consoantes.append(caractere)

    print(f"As consoantes digitadas foram: {consoantes}")

if _name_ == "_main_":
    vetor_caracteres = ler_vetor()
    verificar_consoantes(vetor_caracteres)