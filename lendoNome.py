nome = str(input('Digite seu nome completo: '))

print(nome.upper())
print(nome.lower())
nJunto = nome.replace(' ','')
print('Seu nome tem {} letras no totais'.format(len(nJunto)))

pNome = nome.split()

print('Seu primeiro nome tem {} letras'.format(len(pNome[0])))