from googletrans import Translator


def tradutor():
  try:
    idiomas=['','portuguese','english','japanese','german','spanish','russian','hindi','french','chinese (simplified)','arabic']
    idioma_dest=int(input('\nDigite o numero do idioma: '))
    if idioma_dest not in [1,2,3,4,5,6,7,8,9,10]:
        print('Por favor digite um valor valido')
        return
    tradutor = Translator()
    frase = input('\nTexto original: ')
    texto = tradutor.detect(frase) #Função que detecta o idioma do texto digitado
    traduzido = tradutor.translate(frase, dest=idiomas[idioma_dest]) #Função que traduz para o idioma desejado
    print('Tradução:', traduzido.text)
  except ValueError as error:
    print("Houve algum erro na Tradução, favor tente novamente e contate os desenvolvedores")
  