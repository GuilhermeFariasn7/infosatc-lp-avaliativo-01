print('\033[4;33mDigite 4 notas\033[m ')
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

print("Sua média será: {:.1f}".format((n1+n2+n3+n4)/4))