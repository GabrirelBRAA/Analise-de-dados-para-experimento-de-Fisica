import pandas
from math import pi,sqrt

df=pandas.read_csv('Dados_arrendodados_1.csv')

def error_inverse_volume(volume,volume_error):
    return sqrt(((-100/(volume**2))**2)*volume_error**2)

lista_erro=[]
index=[]
a=0


#for n , i in zip(df['Volume'],df['Erro_de_volume']):
for n in df['Volume']:
    index.append(a)
    a+=1
    erro=round(error_inverse_volume(n,1.9),3)

    lista_erro.append(erro)





valores=pandas.Series(lista_erro,index=index)

df2=df.assign(Erro_volume_inverso=valores.values)
print(df2)
