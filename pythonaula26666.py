# Programa 1: Verificar se o aluno passou de ano
print("--- SISTEMA DE NOTAS DO 1º ANO ---")

nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do primeiro trimestre: "))

# A média mínima é 6
if nota >= 6.0:
    print(f"Parabéns, {nome}! Você está APROVADO(A) com nota {nota}.")
else:
    print(f"Que pena, {nome}. Você está REPROVADO(A) com nota {nota}. converse com seu professor(a)!")
# Programa 2: Descobrir a idade em 2026
print("--- CALCULADORA DE IDADE ---")

ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = 2026

idade = ano_atual - ano_nascimento

print(f"Em {ano_atual}, você tem (ou fará) {idade} anos!")
# Programa 3: Somar dois números
print("--- SOMADOR SIMPLES ---")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2

print(f"O resultado da soma entre {num1} e {num2} é: {soma}")