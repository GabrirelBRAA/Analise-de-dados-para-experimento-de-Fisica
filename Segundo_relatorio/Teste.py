import pandas as pd
import math

Erro_de_K=7
df = pd.read_csv('Dados.csv')


Kelvin_lista=[]
for n in df['Celcius']:
    Kelvin_lista.append((n+273))

dados = pd.Series(Kelvin_lista)

df2 = df.assign(Kelvin=dados.values)

inverse_kelvin=[]
for n in df2['Kelvin']:
    a=1/n
    inverse_kelvin.append(a)

dados2=pd.Series(inverse_kelvin)



erro_inkelvin=[]
for n in df2['Kelvin']:
    erro=math.sqrt(((-1/(n**2))**2)*(7**2))
    erro_inkelvin.append(erro)
dados3 = pd.Series(erro_inkelvin)

df3 = df2.assign(y=dados2.values, y_erro=dados3.values)

x_lista=[]
r_0=58.50
for n in df['R']:
    x_atual = math.log(n/r_0)
    x_lista.append(x_atual)

dados4=pd.Series(x_lista)

erro_x_lista=[]
for n,i in zip(df3['R'],df3['Erro_R']):
    erro_x=math.sqrt(((1/n)**2)*i**2)
    erro_x_lista.append(erro_x)

dados5=pd.Series(erro_x_lista)
df4 = df3.assign(x=dados4.values,Erro_x=dados5.values)


print(df4)
#Constante de erro
#flag_erro=True
constante_de_erro=0
for n in df4['y_erro']:
    #if flag_erro:
    #    flag_erro=False
   #     continue
    constante_de_erro += 1/(n**2)
#Constante x
#flag_x=True
constante_x=0
for n,i in zip(df4['x'],df4['y_erro']):
    #if flag_x:
    #    flag_x=False
    #    continue
    constante_x+=n/(i**2)
constante_x = constante_x/constante_de_erro
#flag_x_quadrado=True
#Constante x^2
constante_x_quadrado=0
for n,i in zip(df4['x'],df4['y_erro']):
    #if flag_x_quadrado:
    #    flag_x_quadrado=False
    #    continue
    constante_x_quadrado+=(n**2)/(i**2)
constante_x_quadrado=constante_x_quadrado/constante_de_erro
#Constante y
#flag_y=True
constante_y=0
for n,i in zip(df4['y'],df4['y_erro']):
    #if flag_y:
    #    flag_y=False
    #    continue
    constante_y+=n/(i**2)
constante_y = constante_y/constante_de_erro
#Constante xy
#flag_xy=True
constante_xy=0
for n,i,o in zip(df4['x'],df4['y_erro'],df4['y']):
    #if flag_xy:
    #    flag_xy=False
    #    continue
    constante_xy+=(n*o)/(i**2)
constante_xy = constante_xy/constante_de_erro

#A
valor_a =(constante_x*constante_y-constante_xy)/(constante_x**2-constante_x_quadrado)

valor_b =constante_y -valor_a*constante_x

print("A :" + str(valor_a))
print("B :" + str(valor_b))


delta_a=math.sqrt((1/constante_de_erro)/(constante_x_quadrado-constante_x**2))
delta_b=math.sqrt((constante_x_quadrado/constante_de_erro)/(constante_x_quadrado-constante_x**2))
print("DeltaA :" + str(delta_a))
print("DeltaB :" + str(delta_b))
