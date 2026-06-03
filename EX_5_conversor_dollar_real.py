# Escreva um programa que pede ao usuário o valor atual da cotação do dollar e a quantidade de dólares para ser convertido em reais. 
# Depois mostre na tela a conversão.

# OUTPUT ESPERADO:

# Digite a cotação do dollar: 5.60
# Digite o valor em dollar a ser convetido para real: 100
# O valor em reais é:  560.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

dollar = float(input("Digite a cotação atual do dollar: "))
qntde = float(input("Digite a quantidade que você quer converter em reais: "))

final = dollar * qntde
print(f"O valor de dollares convertidos em reais é de R$:", final)
