import pandas
from math import sqrt
df=pandas.read_csv('Dados_arredondados_9.csv')
#df=pandas.read_csv('Dados8.csv')

soma=0
index=0
for n in df['PV_joule']:
    index+=1
    soma+=n

media=soma/index
print(media)

soma=0
index=0
for n in df['PV_joule']:
    index+=1
    soma+=(n-media)**2

desvio_da_media = sqrt((1/((index-1)*index))*soma)

print(desvio_da_media)



