import pandas as pd
import math
erro_massa=0.1
erro_temperatura=0.5

m_calorimetro=147.9
erro_calorimetro=0.1
df = pd.read_csv("Dados_experimento_1.csv")

lista_ma=[]
for n in df["m1"]:
    m = n - m_calorimetro
    lista_ma.append(m)
MA=pd.Series(lista_ma)

erro_ma=math.sqrt(0.1**2+0.1**2)

df2 = df.assign(ma=MA.values)


lista_mb=[]
for n,i in zip(df2["m2"],df2["ma"]):
    m = n - m_calorimetro - i
    lista_mb.append(m)

MB = pd.Series(lista_mb)

erro_mb=math.sqrt(0.1**2+erro_calorimetro**2+erro_ma**2)

df3 = df2.assign(mb=MB.values)

lista_delta_ta=[]
lista_delta_tq=[]

for a,q,f in zip(df3["Ta"],df3["Tq"],df3["Tf"]):
    delta_ta=f-a
    delta_tq=f-q
    lista_delta_ta.append(delta_ta)
    lista_delta_tq.append(delta_tq)

TA=pd.Series(lista_delta_ta)
TQ=pd.Series(lista_delta_tq)

erro_delta_tq=math.sqrt(0.5**2+0.5**2)
erro_delta_ta=math.sqrt(0.5**2+0.5**2)

df4 = df3.assign(delta_Tq=TQ.values, delta_Ta=TA.values)


calor_especifico_agua=4.186
lista_C=[]
lista_erro_c=[]
for ma,mb,ta,tq in zip(df4["ma"],df4["mb"],df4["delta_Ta"],df4["delta_Tq"]):
    c=(-calor_especifico_agua*ma*ta-calor_especifico_agua*mb*tq)/(ta)
    lista_C.append(c)

    a=(((calor_especifico_agua*mb*tq)/(ta**2))**2)*(erro_delta_ta**2)
    b=(((-calor_especifico_agua*mb)/ta)**2)*(erro_delta_tq**2)
    c=(((-calor_especifico_agua*ta)/(ta))**2)*(erro_ma**2)
    d=(((-calor_especifico_agua*tq)/(ta))**2)*(erro_mb**2)
    erro_c=math.sqrt(a+b+c+d)
    lista_erro_c.append(erro_c)

C=pd.Series(lista_C)
ERRO_C=pd.Series(lista_erro_c)
df5=df4.assign(Calorimetro=C.values,Erro_C=ERRO_C.values)
print(df5)
soma = 0
for n in df5["Calorimetro"]:
    soma+=n

media_c=soma/3
print(media_c)
soma=0
for n in df5["Calorimetro"]:
    soma+=(n-media_c)**2

desvio_da_media=math.sqrt(soma/6)

print(desvio_da_media)