import pandas

df = pandas.read_csv('Dados_arredondados_7.csv')

lista_round=[]
for n in df['Pressao_x_Volume']:
    r=round(n)
    lista_round.append(r)

valores=pandas.Series(lista_round)

df2=df.assign(Pressao_x_Volume=valores.values)

df2.to_csv('Dados_arredondados_8.csv',index=False)