nome = str(input('Digite seu nome completo: ')).strip()
pNome = nome.split()
print('Seu primeiro nome é: {}'.format(pNome[0]))

print('Seu ultimo nome é: {}'.format(pNome[len(pNome)-1]))
