import pandas
from math import pi,sqrt

df = pandas.read_csv('Dados_arredondados_2')
Volume_inverso=[]
index=[]
a=0
for n in df['Volume']:
    index.append(a)
    a+=1
    novo_dado=round((1/n)*100,3)
    Volume_inverso.append(novo_dado)

v=pandas.Series(Volume_inverso,index=index)

df2=df.assign(Volume_inverso=v.values)
print(df2)
#df2.to_csv("Dados_arredondados_3.csv",index=False)