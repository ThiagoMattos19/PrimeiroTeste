import os
#Progama para calcular o IMC de uma Pessoa
altura = float(input('Digite a sua altura'))
peso = float(input('Digite o seu peso'))

imc = peso / altura**2

print(f'Seu imc é {imc:.2f}')

if imc < 16:
	print("Magreza grave")
elif imc < 17:
	print("Magreza moderada")
elif imc < 18.5:
	print("Magreza leve")
elif imc < 25:
	print("Saudável")
elif imc < 30:
	print("Sobrepeso")
elif imc < 35:
	print("Obesidade Grau I")
elif imc < 40:
	print("Obesidade Grau II (severa)")
else:
	print("Obesidade Grau III (mórbida)")
	
os.system('pause')