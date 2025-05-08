#https://www.youtube.com/watch?v=2KL-mJ4n1k4&t=14s

# Docstring
# Es una cadena de texto que se utiliza para documentar funciones, clases y módulos en Python.
# Se coloca justo después de la definición de la función, clase o módulo y se utiliza para describir su propósito, parámetros y valor de retorno.
# Se puede acceder a la docstring de una función utilizando el atributo __doc__ de la función.
# La docstring se puede utilizar para generar documentación automática utilizando herramientas como Sphinx o pydoc.

def generador(*args):
    """
    :param args: Cantidad de n números.
    :return: El número recibido además de un True o False si el número es mayor a 5.
    """
    for valor in args:
        yield valor, True if valor >5 else False


nombre = generador.__name__
print(nombre)
# Imprime el nombre de la función generador
documentacion = generador.__doc__
print(documentacion)
# Imprime la docstring de la función generador

# La docstring se puede utilizar para generar documentación automática utilizando herramientas como Sphinx o pydoc.
# Ejemplo de uso de la función generador
for valor, mayor in generador(1, 2, 3, 4, 5, 6, 7, 8, 9):
    print(f"El número {valor} es mayor a 5: {mayor}")