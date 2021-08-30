""" Faça um programa para calcular a quantidade de latas de tintas para pintar uma
parede. O programa deverá solicitar ao usuário, a altura e o comprimento da
parede. Considere que a cobertura da tinta é de 1 litro para cada 3 metros
quadrados e que a tinta é vendida em latas de 3,6 litros, que custam R$ 107,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço
total. """

largura = float(input("Informe a largura da parede: "))

altura = float(input("Informe a altura da parede: "))

area = (largura*altura)

litros = (area/3)
litrosV = litros / 3.6
preco = litrosV * 107
print("A área é{}".format(area))
print("A quantidade de latas de tintas para serem compradas é {:.3f}\nE o preço total é: {:.3f}".format(litros,preco))
