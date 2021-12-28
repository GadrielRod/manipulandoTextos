#forma (caso tenha santo em algum lugar do nome)
cidade = str(input('Digite o nome de uma cidade qualquer: ')).strip()
print('Essa cidade tem santo no nome? {}'.format('santo' in cidade.lower()))

#forma alternativa (caso tenha santo somente no começo)
print('essa cidade começa com santo? {}'.format(cidade[:5].lower() == 'santo'))

