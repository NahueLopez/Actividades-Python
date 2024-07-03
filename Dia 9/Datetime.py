import datetime
from datetime import datetime
from datetime import date
"""
mi_hora = datetime.time(17,5)
print(mi_hora)


mi_dia = datetime.date(2025 , 10 ,17)
print(mi_dia.today()) #Para mostrar el dia de hoy.

mi_fecha = datetime(2025 , 5, 15 ,22, 10, 15 , 2500)
mi_fecha = mi_fecha.replace(month= 11) #Cambiamos la fecha
print(mi_fecha)
"""
#De esta forma hacemos una resta de fechas.
"""
nacimiento = date(1995,3,5)
defuncion = date(2095,6,19)

vida = defuncion - nacimiento

print(vida.days)
"""

#Hacemos una cuenta con las horas que estuvo despierto
despierta = datetime(2022 , 10 ,5 , 7, 30)
duerme = datetime(2022, 10, 5 , 23, 45)

vigilia = duerme - despierta

print(vigilia)
"""
#Fecha de hoy
mi_fecha = datetime.date(1999, 2, 3)
print(mi_fecha)

hoy = datetime.date(2025 , 10 ,17)
print(hoy.today()) #Para mostrar el dia de hoy.
"""
hora = datetime.today()
minutos= hora.minute
print(minutos)

hora = datetime.minute
print(hora)