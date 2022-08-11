from constante_de_erro import constante_de_incerteza
import pandas



df = pandas.read_csv('Dados_arredondados_3.csv')


soma=0
for n,i in zip(df['Pressao'],df['Volume_inverso']):
    soma+=(n*i)/(0.1**2)

constante_yx= (1/constante_de_incerteza)*soma

