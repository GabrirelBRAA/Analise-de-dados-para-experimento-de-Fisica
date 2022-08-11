import pandas
from Minimos_quadrados_e_incertezas import b


pressao_atmosferica= -b
df = pandas.read_csv('Dados_arredondados_5.csv')

lista_pt=[]



lista_pv=[]
index=[]
z=0
for n ,i in zip(df['Volume'],df['Pressao_Total']):
    index.append(z)
    pv = n * i
    lista_pv.append(pv)
    z+=1


pressao_x_volume=pandas.Series(lista_pv)

df2 = df.assign(Pressao_x_Volume=pressao_x_volume)

df2.to_csv('Dados_arredondados_6.csv', index=False)
print(df2)
