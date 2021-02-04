lista = list()

while True:
	num = int(input('Digite o valor: '))
	if num in lista:
		print('Valor não adicionado, pois já existe!')
	else:
		lista.append(num)
		print('Valor adicionado com sucesso!')
	opc = str(input('Quer continuar? [S/N]: '))
	if opc in 'Nn':
		break
lista.sort()
print('--'*20)
print(f'Valores digitados: {lista}')
print('--'*20)