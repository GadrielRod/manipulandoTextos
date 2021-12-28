num = int(input('Digite um numero de 0 a 9999: '))
n = str(num)
numTotal = n.zfill(4)

print(f'{numTotal[0]} Milhar')
print(f'{numTotal[1]} Centenas')
print(f'{numTotal[2]} Dezenas')
print(f'{numTotal[3]} Unidades')

'''print('milhar: {}\n'
      'centena: {}\n'
      'dezena: {}\n'
      'unidade: {}'.format(numTotal[0],numTotal[1],numTotal[2],numTotal[3]))'''

#forma alternativa

'''
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
'''