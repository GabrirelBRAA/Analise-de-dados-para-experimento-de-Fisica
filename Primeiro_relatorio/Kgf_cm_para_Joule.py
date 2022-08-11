import pandas

df=pandas.read_csv('Dados_arredondados_8.csv')

def to_Joule(x):
    return x*9.80665/100

lista_PV=[]
lista_erros=[]
for n , i in zip(df['Pressao_x_Volume'],df['Erros_de_PV']):
    pv=round(to_Joule(n))
    erro=round(to_Joule(i))
    lista_PV.append(pv)
    lista_erros.append(erro)

print(lista_PV)
print(lista_erros)

PV=pandas.Series(lista_PV)
ERROS=pandas.Series(lista_erros)

df2=df.assign(PV_joule=PV.values,PV_erro_joule=ERROS.values)
print(df2)

df2.to_csv('Dados_arredondados_9.csv',index=False)