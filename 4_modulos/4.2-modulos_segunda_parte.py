#https://www.youtube.com/watch?v=S0wU4tqP6Bs&t=13s

#Modulos
#Los módulos son archivos de Python que contienen definiciones y declaraciones de Python.

#Otras formas de importar las funcionalidades de los modulos de formas diferentes

import sys
sys.path.append('./4_modulos/calculadora')  # Asegúrate de que la ruta sea correcta

from calculadora import sumar, restar #Importar funciones específicas
from calculadora import multiplicacion as multiplicar, division as dividir #Importar funciones con alias

resultado_suma = sumar(5, 3)
print(f"El resultado de la suma es: {resultado_suma}")

resultado_resta = restar(5, 3)
print(f"El resultado de la resta es: {resultado_resta}")

resultado_multiplicacion = multiplicar(5, 3)
print(f"El resultado de la multiplicacion es: {resultado_multiplicacion}")

resultado_division = dividir(5, 3)
print(f"El resultado de la division es: {resultado_division}")
