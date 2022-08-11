import pandas

df = pandas.read_csv('Dados8.csv')

lista_volume=[]
for n in df['Volume']:
    lista_volume.append(round(n))

df2=pandas.DataFrame()

vol=pandas.Series(lista_volume)
df3=df2.assign(Pressao=df['Pressão '],Volume=vol.values)
print(df3)
