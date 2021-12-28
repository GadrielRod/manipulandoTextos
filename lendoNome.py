nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
nJunto = nome.replace(' ','')
#forma alternativa
#print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu nome tem {} letras'.format(len(nJunto)))
pNome = nome.split()
#forma alternativa
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(pNome[0],len(pNome[0])))