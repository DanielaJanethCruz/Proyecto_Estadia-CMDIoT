"""
Objetivos
- Familiarizarse con la entrada y salida de datos en Python.
- Evaluar expresiones simples.

Escenario
La tarea es completar el código para evaluar y mostrar el resultado de cuatro operaciones aritméticas básicas.

El resultado debe ser mostrado en consola.

Quizá no podrás proteger el código de un usuario que intente dividir entre cero. Por ahora, no hay que preocuparse 
por ello.

Prueba tu código - ¿Produce los resultados esperados?

No te mostraremos ningún dato de prueba, eso sería demasiado sencillo.


"""
x = float(input("Ingresa un numero:"))# ingresa un valor flotante para la variable a aquí
y = float(input("Ingresa un segundo numero: "))# ingresa un valor flotante para la variable b aquí

print("Suma: ",str(x+y))# muestra el resultado de la suma aquí 
print("Resta: ",str(x-y))# muestra el resultado de la resta aquí
print("Multiplicación: ",str(x*y))# muestra el resultado de la multiplicación aquí
print("División: ",str(x/y))# muestra el resultado de la división aquí

print("\n¡Eso es todo, amigos!")