#Questão 30 - Descobrir quantos o valor em reais irá ficar convertido para dolar
C = float(input("Digite a cotação do dólar: "))
R = float(input("Digite o valor desejado a ser convertido em dolar: "))

D = (R/C)

print("O valor convertido de reais para dolar: {:.2f}".format(D))

