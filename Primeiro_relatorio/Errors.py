import pandas
from math import pi,sqrt

df = pandas.read_csv('Dados_arredondados_3.csv')
r=3.481

def find_error(l, error_r, error_l,radius=r):
    return sqrt( ((2*pi*radius*l)**2)*error_r**2 + ((pi*radius**2)**2)*error_l**2)
list_error=[]
index=[]
a=0
for n in df['L(cm)']:
    index.append(a)
    a+=1
    error=find_error(n,0.001,0.05)
    list_error.append(error)
    print(error)

print(list_error)

s=pandas.Series(list_error, index=index)
df3=df.assign(Erro_de_volume=s.values)

df3.to_csv('Dados_pros_erros.csv',index=False)