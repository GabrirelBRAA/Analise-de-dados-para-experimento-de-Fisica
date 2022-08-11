import pandas as pd
import math

df = pd.read_csv("Dados_experimento_2.csv")

erro_temperatura=0.5
erro_massa=0.1

m_peca=200.1
m_calorimetro=147.91
C_calorimetro=61.52780789452812
C_erro=4.7453174204293

lista_ma=[]
for n in df["m1"]:
    m=n-m_calorimetro
    lista_ma.append(m)
MA= pd.Series(lista_ma)

erro_ma=math.sqrt(0.1**2+0.1**2)

df2 = df.assign(ma=MA.values)

lista_delta_ta=[]
lista_delta_tq=[]
for a,q,f in zip(df["Ta"],df["Tq"],df["Tf"]):
    delta_ta=f-a
    delta_tq=f-q

    lista_delta_ta.append(delta_ta)
    lista_delta_tq.append(delta_tq)

TA=pd.Series(lista_delta_ta)
TQ=pd.Series(lista_delta_tq)

erro_delta_ta=math.sqrt(0.5**2+0.5**2)
erro_delta_tq=math.sqrt(0.5**2+0.5**2)

df3=df2.assign(Delta_Ta=TA.values,Delta_Tq=TQ.values)

calor_especifico_da_agua=4.186
calor_especifico_da_agua2=4186



lista_c=[]
lista_c_erro=[]
for ma,ta,tq in zip(df3["ma"],df3["Delta_Ta"],df3["Delta_Tq"]):
    c = (-ta*(calor_especifico_da_agua*ma+C_calorimetro))/(m_peca*tq)*1000
    lista_c.append(c)

    #ma=ma/1000
    #m_peca=m_peca/1000
    a = (((-calor_especifico_da_agua*ma+C_calorimetro) / (m_peca*ta)) ** 2) * (erro_delta_ta) ** 2
    b = (((-ta*calor_especifico_da_agua) / (m_peca*tq)) ** 2) * (erro_ma) ** 2
    c = (((ta*(calor_especifico_da_agua*ma+C_calorimetro)) / (m_peca*(tq**2))) ** 2) * (erro_delta_tq) ** 2
    d = (((ta*(calor_especifico_da_agua*ma+C_calorimetro)) / ((m_peca**2)*tq)) ** 2) * (erro_massa) ** 2
    e = (((-ta) / (m_peca*tq)) ** 2) * (C_erro) ** 2
    erro_c=math.sqrt(a+b+c+d+e)
    lista_c_erro.append(erro_c*1000)
    #m_peca=m_peca*1000



VALORC=pd.Series(lista_c)
ERROC=pd.Series(lista_c_erro)

df4=df3.assign(c=VALORC.values,erro_c=ERROC.values)


print(df4)
print(erro_delta_tq)
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






