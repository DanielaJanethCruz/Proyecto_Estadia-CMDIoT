"""
Escenario
Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días 
del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal).

La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen 
sentido.

Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LABORATORIO 4.1.3.6). Puede ser 
muy útil. Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de la función; este truco 
acortará significativamente el código.

Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.
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
            
    

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
