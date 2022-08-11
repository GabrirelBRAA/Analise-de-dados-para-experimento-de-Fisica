import pandas

df = pandas.read_csv('Dados_arredondados_4.csv')

index= 0
lista_dados=[]
for n in df['Pressao_Total']:
    r=round(n,1)
    lista_dados.append(r)

valores=pandas.Series(lista_dados)
df2=df.assign(Pressao_Total=lista_dados)

df2.to_csv('Dados_arredondados_5.csv', index=False)