import pandas
from Minimos_quadrados_e_incertezas import b

df = pandas.read_csv('Dados_arredondados_9.csv')

for n ,i in zip(df['Pressao'],df['Volume']):
    print(((n+(-b))*i))