""" Um determinado prêmio de loteria saiu para um bolão de três amigos. Uma lei
garante que todo prêmio de loteria deva pagar um imposto de 7% para os
cofres estaduais. Do total descontado o imposto, os amigos irão dividir o prêmio
da seguinte maneira:
O primeiro ganhador recebera 46%;
O segundo recebera 32%;
O terceiro recebera o restante;
Faça um programa que leia o valor total do prêmio, calcule o desconto, o valor
que cada um tem direito e imprima o total do prêmio, o premio descontado o
imposto e a quantia recebida por cada um dos ganhadores. """

tt = float(input("Informe o valor total do prêmio: "))

ttimposto = (tt*0.93)

primeiro = (ttimposto*0.54)
segundo = (ttimposto*0.68)
terceiro = (ttimposto*0.85)

print("o prêmio total foi de {:.3f}, mas com imposto ficará{:.3f}: o primeiro ganhador ganhará {:.3f} reais\nO segundo ganhará {:.3f} reais\nO terceiro ganhará {:.3f} reais".format(tt,ttimposto,primeiro,segundo,terceiro))