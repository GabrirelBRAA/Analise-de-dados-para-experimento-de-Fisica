from constante_x import constante_x
from constante_de_erro import constante_de_incerteza
from constante_x_aoquadrado import constante_x_ao_quadrado
from constante_y import constante_y
from constante_yx import constante_yx
from math import sqrt

a_f=((constante_x*constante_y)-constante_yx)/(constante_x**2-constante_x_ao_quadrado)

b_f=constante_y-a_f*constante_x

delta_a_f=sqrt((1/constante_de_incerteza)/(constante_x_ao_quadrado-(constante_x)**2))

delta_b_f=sqrt((constante_x_ao_quadrado/constante_de_incerteza)/(constante_x_ao_quadrado-constante_x**2))

a=round(a_f,1)
b=round(b_f,1)
delta_a=round(delta_a_f,1)
delta_b=round(delta_b_f,1)

#print(a)
#print(delta_a)
#print(b)
#print(delta_b)
