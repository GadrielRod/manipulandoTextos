frase = input('Escreva uma frase qualquer: ')

print('Essa frase tem: {} as'.format(frase.lower().count('a')))
print('A primeira letra "a" aparece na posição: {}'.format(frase.lower().find('a')))
print('A ultima letra "a" aperece na posição: {}'.format(frase.lower().rfind('a')))