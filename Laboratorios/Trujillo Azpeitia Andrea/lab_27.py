"""
Escenario
Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el 
día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba 
es solo el comienzo.
"""

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    meses=[1,2,3,4,5,6,7,8,9,10,11,12]
    is_year_b = is_year_leap(year)
    if month in meses:
        if month == 2 and is_year_b == True:
            return 29
        elif month == 2 and is_year_b== False:
            return 28
        elif month in [1,3,5,7,8,10,12]:
            return 31
        else:
            return 30
    else:
        return

def day_of_year(year, month, day):
    yb=is_year_leap(year)
    dm=days_in_month(year,month)
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day > dm:
        return
    else:
        if yb == True:
            dias_por_mes[2] = 29
        num_dia = sum(dias_por_mes[:month])+day
        return num_dia
            

print(day_of_year(2000, 12, 31))
