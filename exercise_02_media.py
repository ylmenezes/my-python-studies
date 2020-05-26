# -*- coding: utf-8 -*-*

x = float(input("Qual é a sua primeira nota: "))
y = float(input("Qual é a sua segunda nota: "))

total = x+y/2

if total < 6:
	print("Você foi reprovado!")
elif total >= 6:
	print("Você foi aprovado!! Uhuuu!!!")
else:
	print("Não foi possível calcular sua média")
