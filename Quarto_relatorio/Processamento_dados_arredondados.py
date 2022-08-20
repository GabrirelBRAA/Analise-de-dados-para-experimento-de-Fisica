import pandas as pd
import math
df3 = pd.read_csv("Dados_arredondados.csv")
Tr_medio = 22
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