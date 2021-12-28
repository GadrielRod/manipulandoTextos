frase = 'Aprendendo o fatiamento de strings'

print(f'a frase dita foi: {frase}')
print(f'O 11º caracter da frase é: {frase[11]}')
print(frase[13:23])
print(frase[:10])
print(frase[27:])
print(frase[12:23:2])
print(frase[12::2])
print(frase[::2])

print()
print(""" Aqui eu estou escrevendo, um baita texto 
para ser printado na sua tela e vermos o uso de aspas triplas
e como funciona""")

print()
frase2 = 'Aprendendo a análise de strigs'

print(len(frase2))
print(frase2.count('e'))
print(frase2.count('e',0,10))
print(frase2.upper().count('A'))
print(frase2.find('den'))
print(frase2.find('python'))
print('Curso' in frase2)
print('análise' in frase2)

print()
frase3 = 'Aprendendo a transformação de strings'

print(frase3.replace('transformação','alquimia'))
#fraseTransmutada = frase3.replace('tranformação','alquimia')
print(frase3.replace(' ','-'))
print(frase3.upper())
print(frase3.lower())
print(frase3.capitalize())
print(frase3.title())

print()
frase4 = '   Deixando uns espaços na memória  '

print(frase4.strip())
print(len(frase4))
print(len(frase4.strip()))
print(frase4.rstrip())
print(frase4.lstrip())

print()
frase5 = 'Aprendendo a divisão e junção de strings'

print(frase5.split())
divido = frase5.split()
print(divido[2])
print('-'.join(frase5))