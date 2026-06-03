# Escreva um código que mostre na tela um "MENU" de opções de operações matematicas (Adição, Subtração, Divisão e Multiplicação)
# O usuário deve escolher uma das opções e depois inserir dois números para serem calculados de acordo com a operação escolhida.
# No fim mostre o resultado da operação

# OUTPUT ESPERADO:

#----------------------------------------- Exemplo 1 (Soma)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 1
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 20.0

# ----------------------------------------- Exemplo 2 (Multiplicação)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 3
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 100.0

# ----------------------------------------- Exemplo 3 (Opção inválida)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 6
# | Digite o primeiro número:1
# | Digite o segundo número:2
# | ERRO. Escolha uma opção válida.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("Calculadora")
print("Selecione a opção de calculos que deseja abaixo")
opc = input("1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão")

if opc == "1":
    soma1 = int(input("Digite o valor que deseja somar: "))
    soma2 = int(input("Digite o o segundo valor que deseja somar com o primeiro: "))
    soma3 = soma1 + soma2
    print(soma3)

elif opc == "2":
    sub1 = int(input("Digite o valor que deseja subtrair: "))
    sub2 = int(input("Digite o o segundo valor que deseja subtrair com o primeiro: "))
    sub3 = sub1 - sub2
    print(sub3)

elif opc == "3":
    mult1 = int(input("Digite o valor que deseja multiplicar: "))
    mult2 = int(input("Digite o o segundo valor que deseja multiplicar com o primeiro: "))
    mult3 = mult1 * mult2
    print(mult3)

elif opc == "4":
    div1 = int(input("Digite o valor que deseja somar: "))
    div2 = int(input("Digite o o segundo valor que deseja somar com o primeiro: "))
    div3 = div1 / div2
    print(div3)

else:
    print("ERRO. Escolha uma opção válida.")