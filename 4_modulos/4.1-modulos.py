#https://www.youtube.com/watch?v=_4QUMUlI2S8

#Modulos
#Los módulos son archivos de Python que contienen definiciones y declaraciones de Python.
#Los módulos permiten organizar el código en diferentes archivos y reutilizarlo en diferentes programas.
#Los módulos se importan utilizando la palabra clave import, seguida del nombre del módulo.
#Los módulos pueden contener funciones, clases y variables.
#Los módulos pueden ser importados de diferentes maneras, por ejemplo, importando todo el módulo o solo una parte de él.
#Los módulos pueden ser importados utilizando alias, es decir, un nombre diferente al original.
#Los módulos pueden ser importados desde una ruta específica utilizando la palabra clave from.
#Los módulos pueden ser importados desde un paquete, es decir, un directorio que contiene un archivo __init__.py.
#Los módulos pueden ser importados desde un paquete utilizando la palabra clave from.
#Los módulos pueden ser importados desde un paquete utilizando alias, es decir, un nombre diferente al original.
#Los módulos pueden ser importados desde un paquete utilizando la palabra clave from y un alias.
#Los módulos pueden ser importados desde un paquete utilizando la palabra clave from y un alias, y se pueden importar varias partes del módulo utilizando comas.

# Este es un ejemplo de un módulo llamado "calculadora.py"
# Este módulo contiene funciones para realizar operaciones matemáticas básicas
# Definición de funciones
#calculadora.py y main.py

import sys
sys.path.append('./4_modulos/calculadora')  # Asegúrate de que la ruta sea correcta

import calculadora

resultado = calculadora.sumar(5, 3)
print(f"El resultado de la suma es: {resultado}")

#esto no dará error, porque aunque el modulo calculadora no esta en el mismo directorio que el archivo 4.1-modulos.py, con la funcion sys.path hemos incluido la ruta
# desde el cual se esta invocando.