nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))
nota4 = float(input("Digite a 4ª nota: "))

media = (nota1 + nota2 + nota3 + nota4)

if media >= 7.0:
    print("Aprovado(a) ✅")
elif media >= 5.0 and media < 7.0:
    print("Recuperação ⚠️")
else:
    print("Reprovado(a) ❌")


print(f"O aluno {nome} tem uma média de {media:.2f}")
