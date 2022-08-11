from constante_de_erro import constante_de_incerteza
import pandas



df = pandas.read_csv('Dados_arredondados_3.csv')


soma=0
for n in df['Volume_inverso']:
    soma+=(n**2)/(0.1**2)

constante_x_ao_quadrado= (1/constante_de_incerteza)*soma
