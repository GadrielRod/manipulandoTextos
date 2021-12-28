num = input('Digite um numero de 0 a 9999: ')
numTotal = num.zfill(4)

print(f'{numTotal[0]} Milhar')
print(f'{numTotal[1]} Centenas')
print(f'{numTotal[2]} Dezenas')
print(f'{numTotal[3]} Unidades')

'''print('milhar: {}\n'
      'centena: {}\n'
      'dezena: {}\n'
      'unidade: {}'.format(numTotal[0],numTotal[1],numTotal[2],numTotal[3]))'''