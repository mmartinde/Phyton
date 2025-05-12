#https://www.youtube.com/watch?v=44D-QCg-YEw

#Librerias
#Las librerías son colecciones de módulos que proporcionan funcionalidades adicionales a Python. Puedes crear tus propias librerías o utilizar librerías de terceros.
#Las librerías son útiles para organizar y reutilizar código, y pueden contener funciones, clases y variables que puedes importar en tus scripts.

import random
import datetime
import sys
import time

valor = random.randint(1, 10)
print(f"El valor aleatorio es: {valor}")
#El módulo random es una librería estándar de Python que proporciona funciones para generar números aleatorios.
#En este caso, estamos utilizando la función randint para generar un número entero aleatorio entre 1 y 10.
#La función randint toma dos argumentos: el límite inferior y el límite superior (ambos inclusivos).
#Por lo tanto, el valor aleatorio generado puede ser cualquier número entre 1 y 10, incluyendo ambos extremos.
#La función random.randint() es útil en una variedad de aplicaciones, como juegos, simulaciones y pruebas, donde se requiere la generación de números aleatorios.

lista=[True,"String", 23, False]
valor=random.choice(lista)
print(f"El valor aleatorio es: {valor}")

#que pasa si quiero desordenar la lista?
#La función random.shuffle() se utiliza para mezclar los elementos de una lista en su lugar, es decir, modifica la lista original y no devuelve una nueva lista.
#Esto es útil cuando deseas obtener una secuencia aleatoria de elementos de una lista sin crear una copia adicional.
#Ejemplo:
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(f"Lista desordenada: {lista}")
#En este caso, la lista original se ha modificado y ahora contiene los elementos en un orden aleatorio.
#La función random.sample() se utiliza para obtener una muestra aleatoria de elementos de una lista sin reemplazo.
#Esto significa que no se repiten elementos en la muestra y la lista original no se modifica.


#La función datetime.now() se utiliza para obtener la fecha y hora actuales en el formato de un objeto datetime.
#Este objeto contiene información sobre el año, mes, día, hora, minuto, segundo y microsegundo actuales.
#La función datetime.now() es útil para registrar la fecha y hora en que se ejecuta un programa, realizar cálculos de tiempo y trabajar con fechas y horas en general.
#Ejemplo:
fecha_hora_actual = datetime.datetime.now()
print(f"Fecha y hora actuales: {fecha_hora_actual}")


#La función sys.argv es una lista que contiene los argumentos de la línea de comandos pasados al script de Python.
#El primer elemento de la lista (sys.argv[0]) es siempre el nombre del script en sí, y los siguientes elementos son los argumentos proporcionados por el usuario.
#Esto es útil para permitir que los usuarios pasen información al script al ejecutarlo desde la línea de comandos.
#Ejemplo:


for i in range(100):
    time.sleep(0.1)
    sys.stdout.flush()
    sys.stdout.write("\r%d%%" % i)
