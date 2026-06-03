# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome = input("Informe o nome do produto: ")
valor = float(input("Informe quanto é o valor do produto: "))
desc = int(input("Informe o valor de desconto que você irá receber: "))

desconto = valor * (desc / 100)
final = valor - desconto

print("Qual o preço do produto?", valor)
print("Qual o valor do desconto?", desc)
print(f"O {nome} com {desconto}% de desconto cutará R$ {final}.")
