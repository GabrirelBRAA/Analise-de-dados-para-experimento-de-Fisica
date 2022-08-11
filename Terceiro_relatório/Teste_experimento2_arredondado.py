import pandas as pd
import math

df4 = pd.read_csv("Dados_experimento2_processados.csv")
print(df4)
soma=0
for n in df4["c"]:
    soma+=n

media_c=soma/3
print(media_c)
soma=0
for n in df4["c"]:
    soma+=(n-media_c)**2

desvio_da_media=math.sqrt(soma/6)

print(desvio_da_media)