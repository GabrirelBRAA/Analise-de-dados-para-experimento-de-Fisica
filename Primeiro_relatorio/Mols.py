from math import sqrt
from Media_desvio import media,desvio_da_media
t=292.95
#t=19.8

def calcular_erro(temperatura,R,erro_PV,erro_T,PV):
    return sqrt((((1/(R*temperatura))**2))*erro_PV**2 + ((-PV/(R*temperatura**2))**2)*erro_T**2)

print(calcular_erro(t,8.31,desvio_da_media,0.5,media))

print((media/(8.31*t)))