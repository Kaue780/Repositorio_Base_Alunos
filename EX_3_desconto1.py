# Escreva um programa que pede ao usuário o preço de um produto e o valor de desconto em % e depois informe qual será o valor do desconto.
# Dica: 
# use a fórmula 
# desconto = preco * (porcentagem / 100) 
# para calcular o valor do desconto 

# OUTPUT ESPERADO:

# Qual o preço do produto? 300
# Qual a porcentagem de desconto? 10
# O produto que custa R$300.0 terá R$30.0 de desconto.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

valor = float(input("Informe quanto é o valor do produto: "))
desc = int(input("Informe o valor de desconto que você irá receber: "))

desconto = valor * (desc / 100)

print("Qual o preço do produto?", valor)
print("Qual o valor do desconto?", desc)
print(f"O produto que custa R$ {valor} terá {desconto}% de desconto.")
