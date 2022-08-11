from Minimos_quadrados_e_incertezas import delta_b
from math import sqrt
import pandas

incer_p=0.1**2
incer_pat=delta_b**2
incerteza_ptotal=sqrt(incer_pat+incer_p)

df = pandas.read_csv('Dados_arredondados_6.csv')

lista_erro_de_pv=[]
index=[]
q=0
for n,i in zip(df['Pressao_Total'], df['Volume']):
    index.append(q)
    q+=1
    erro=sqrt(((i**2)*incerteza_ptotal**2)+((n**2)*2**2))
    erro_round=round(erro)
    lista_erro_de_pv.append(erro_round)

valores=pandas.Series(lista_erro_de_pv,index=index)

df2=df.assign(Erros_de_PV=valores.values)
df2.to_csv('Dados_arredondados_7.csv',index=False)
print(df2)
