import pandas as pd
import math

incerteza_Tv = 4

Tr_inicial = 21
Tr_final = 23
incerteza_Tr = 4

Resistencia_inicial = 7.2
Resistencia_final = 12.8
incerteza_resistencia = 0.6

Tamb_inicial = 24
Tamb_final = 21
Incerteza_Tamb = 4

df = pd.read_csv("Dados.csv")

Tr_medio = (Tr_inicial+Tr_final)/2
Resistencia_media = (Resistencia_final+Resistencia_inicial)/2


lista_potencia=[]
lista_erro_p=[]
lista_carnot=[]
lista_erro_carnot = []

for v,v_erro,tv in zip(df["V"],df["erro_V"],df["Tv"]):
    potencia = ((v/1000)**2)/Resistencia_media
    potencia = potencia * 10**9
    lista_potencia.append(potencia)
    Erro_p = math.sqrt(((2*(v/1000)*(v_erro/1000))/Resistencia_media)**2 + ((-(v/1000)**2*incerteza_resistencia)/(Resistencia_media**2))**2)
    Erro_p = Erro_p * 10**9
    lista_erro_p.append(Erro_p)
    if (Tr_medio > tv):
        T_maior = Tr_medio + 273.15
        T_menor = tv + 273.15
        Erro_maior=incerteza_Tr
        Erro_menor = incerteza_Tv
    else:
        T_maior = tv + 273.15
        T_menor = Tr_medio + 273.15
        Erro_maior = incerteza_Tv
        Erro_menor = incerteza_Tr
    carnot = 1 - (T_menor/T_maior)
    lista_carnot.append(carnot)
    erro_carnot = math.sqrt(((-T_menor*Erro_maior)/T_maior**2)**2 + (-Erro_menor/T_maior)**2)
    lista_erro_carnot.append(erro_carnot)

SP=pd.Series(lista_potencia)
SEP=pd.Series(lista_erro_p)
SC=pd.Series(lista_carnot)
SEC=pd.Series(lista_erro_carnot)

df2 = df.assign(P=SP.values,Erro_P=SEP.values,Carnot=SC.values,Erro_Carnot=SEC.values)

print(df2)
lista_potencia_carnot=[]
lista_erro_potencia_carnot=[]
for p,c,erro_p,erro_c in zip(df2["P"],df2["Carnot"],df2["Erro_P"],df2["Erro_Carnot"]):
    if c==0:
        potencia_carnot = 0
        Erro_PQ=0
    else:
        potencia_carnot = p/c
        Erro_PQ = math.sqrt((erro_p / c) ** 2 + ((-p * erro_c )/ (c ** 2)) ** 2)
    lista_potencia_carnot.append(potencia_carnot)

    lista_erro_potencia_carnot.append(Erro_PQ)

SPQ = pd.Series(lista_potencia_carnot)
SEPQ = pd.Series(lista_erro_potencia_carnot)

df3 = df2.assign(PQ = SPQ.values, Erro_PQ = SEPQ.values)

print(df3)


M_erro = 0
for v_erro in df3["erro_V"]:
    M_erro += 1/(v_erro**2)

M_x_sobre_erro=0
for v_erro,tv in zip(df3["erro_V"],df3["Tv"]):
    M_x_sobre_erro += (tv-Tr_medio)/((v_erro)**2)
M_x = M_x_sobre_erro/M_erro

M_y_sobre_erro=0
for v_erro,v in zip(df3["erro_V"],df3["V"]):
    M_y_sobre_erro += (v)/((v_erro)**2)
M_y = M_y_sobre_erro/M_erro

M_xy_sobre_erro=0
for v_erro,v,tv in zip(df3["erro_V"],df3["V"],df3["Tv"]):
    M_xy_sobre_erro += (v*(tv-Tr_medio))/((v_erro)**2)
M_xy = M_xy_sobre_erro/M_erro

M_xquadrado_sobre_erro=0
for v_erro,tv in zip(df3["erro_V"],df3["Tv"]):
    M_xquadrado_sobre_erro += ((tv-Tr_medio)**2)/((v_erro)**2)
M_xquadrado = M_xquadrado_sobre_erro/M_erro

a = (M_x*M_y-M_xy)/(M_x**2-M_xquadrado)
b = M_y-a*M_x
delta_a = math.sqrt((1/M_erro)/(M_xquadrado-M_x**2))
delta_b = math.sqrt((M_xquadrado/M_erro)/(M_xquadrado-M_x**2))
print(a)
print(b)
print(delta_a)
print(delta_b)

print(df3["PQ"])
print(df3["Erro_PQ"])



