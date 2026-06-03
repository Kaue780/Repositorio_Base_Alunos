# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota da prova: "))
nota2 = float(input("Digite sua primeira nota da prova: "))
nota3 = float(input("Digite sua primeira nota da prova: "))
soma = nota1 + nota2 + nota3


media = soma / 3
print("Nome do Aluno: ", nome)
print(f"A média da nota das suas provas é: ", media)
if soma == 10:
    print("Aprovado com perfeição")
elif soma < 6:
    print("Reprovado")
else:
    print("Aprovado")