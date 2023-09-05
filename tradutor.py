# Biblioteca Google Translator API
from googletrans import Translator
import pandas as pd
import numpy as np
from func import tradutor
while True:
    lista_idiomas = ['Português','Inglês','Japonês','Alemão','Espanhol','Russo','Híndi','Francês','Chinês','Árabe'] #Lista de idiomas disponíveis
    indice = [1,2,3,4,5,6,7,8,9,10]
    print('\nBem-vindo ao Tradutor de idiomas, a seguir mostraremos a lista com os idiomas disponíveis, escolha o do seu interesse e seja feliz!\n')
    print('Temos os seguintes idiomas a seu dispor:', lista_idiomas)
    df = pd.DataFrame({
        'Idiomas': ['Português','Inglês','Japones','Alemão','Espanhol','Russo','Híndi','Francês','Chinês','Árabe'],
        'Nº': [1,2,3,4,5,6,7,8,9,10]
    })
    df.index = ['','', '','','','','','','','']
    print('\n',df)
    tradutor()
    next = input('\nQuer continuar traduzindo [s]/[n] ? ')
    if next == 'n':
      print('\nObrigado por utilizar nosso tradutor!')
      break
    elif next != 's':
      print('Houve algum erro na Tradução, favor tente novamente e contate os desenvolvedores')
      break