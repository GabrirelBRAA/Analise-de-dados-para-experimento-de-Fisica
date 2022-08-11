import pandas
from math import pi

df = pandas.read_csv('Dados.csv')
print(df)
a=0
soma=0
lista_volume=[]
lista_index=[]
for n in df['L(cm)']:
    lista_index.append(a)
    a+=1
    v=pi*(3.481**2)*n
    print(v)
    lista_volume.append(v)
vol=pandas.Series(lista_volume,index=lista_index)
print(lista_index)
print(lista_volume)
df2=df.assign(Volume=vol.values)
print(df2)
df2.to_csv('Dados_processados.csv', index=False)
