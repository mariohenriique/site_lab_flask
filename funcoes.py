import csv
import pandas as pd
from flask import request
from datetime import datetime

#funcao que dá o nome para a variável do input
def itens(name):
    output = request.form.to_dict()
    variavel = output[name]
    return variavel

def escrever_dados():
    df = pd.read_csv('modelo.csv')
    df = pd.DataFrame(df)

    lista = []
    cont = 0
    output = request.form.to_dict()
    for e in df.loc[0]:
        if cont+1 == len(df.columns):
            globals()[str(e)] = datetime.today().strftime('%Y-%m-%d')
            lista.append(globals()[str(e)])
        
        elif e == 'latitude':
            latitude = str.strip(output[e]).lower()
            #mudar latitude pro formato decimal
            globals()[str(e)] = latitude
            lista.append(globals()[str(e)])

        elif e == 'longitude':
            longitude = str.strip(output[e]).lower()
            #mudar a longitude pro formato decimal
            globals()[str(e)] = longitude
            lista.append(globals()[str(e)])

        else:
            globals()[str(e)] = str.strip(output[e]).lower()
            lista.append(globals()[str(e)])
        cont +=1
    
    with open('tabela/colecao_darwin_core.csv','a',newline='') as csvfile:
        escreve = csv.writer(csvfile)
        escreve.writerow(lista)
    
    df = pd.read_csv('tabela/colecao_darwin_core.csv')
    df = pd.DataFrame(df)
    df.to_html('tabela/colecao_darwin_core.html')
    df.to_csv('static/colecao_darwin_core.csv')