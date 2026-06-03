# Crie um programa que receba um número inteiro e dia qual é o dia da semana correspondente a este número
# Os dias são:
# 1 - domingo
# 2 - Segunda
# 3 - Terça
# 4 - Quarta
# 5 - Quinta
# 6 - Sexta
# 7 - Sábado

# OUTPUT ESPERADO

# Digite um número: 1
# Domingo

# Digite um número: 2
# Segunda

# Digite um número: 8
# Número errado

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

dias = int(input("Digite um número de 1 até 8 para inforar o dia da semana: "))

if dias == 1:
    print("Domingo")
elif dias == 2:
    print("Segunda")
elif dias == 3:
    print("Terça")
elif dias == 4:
    print("Quarta")
elif dias == 5:
    print("Quinta")
elif dias == 6:
    print("Sexta")
elif dias == 7:
    print("Sábado")
else:
    print("Número errado")
