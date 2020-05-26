# -*- coding: utf-8 -*-

print("Calcular taxa IMC \n\n")

print("Vamos calcular o seu IMC com base nas seguitens informações: ")
altura = float(input("CM: "))
peso = float(input("KG: "))

imc = peso/altura**2

print(" \n")
print('IMC é igual á '+str(imc)+"\n")

if imc < 18.5:

	print("MAGREZA")

elif imc >= 18.5 and imc<=24.9:

	print("NORMAL")

elif imc >=25 and imc<29.9:

	print("SOBREPESO")
	print("OBESIDADE NIVEL I")

elif imc>=30 and imc<=39.9:

	print("OBESIDADE - NIVEL II")

elif imc>=40:

	print("OBESIDADE GRAVE - NIVEL III")

else:
	print("Não foi possível calcular a sua Taxa do IMC")

print(" \n")
