#https://www.youtube.com/watch?v=PeWKpuFpGZA&t=10s

#Argumentos
#Los argumentos son valores que se pasan a una función cuando se llama.
#Los argumentos se definen en la declaración de la función y se utilizan dentro de la función.
#Los argumentos pueden ser de cualquier tipo de dato, como enteros, flotantes, cadenas, listas, diccionarios, etc.
#Los argumentos pueden ser obligatorios o opcionales.
#Los argumentos obligatorios deben ser proporcionados al llamar a la función, mientras que los argumentos opcionales tienen un valor predeterminado.
#Los argumentos opcionales se definen utilizando el signo igual (=) seguido del valor predeterminado.
#Los argumentos se pueden pasar por posición o por nombre.
#Los argumentos por posición se pasan en el mismo orden en que se definen en la declaración de la función.
#Los argumentos por nombre se pasan utilizando el nombre del argumento seguido del signo igual (=) y el valor.
#Los argumentos por nombre se pueden pasar en cualquier orden, pero deben ser proporcionados con su nombre.
#Los argumentos se pueden pasar como listas o diccionarios utilizando el operador * o ** respectivamente.
#Los argumentos se pueden pasar como listas utilizando el operador *.
#Los argumentos se pueden pasar como diccionarios utilizando el operador **.

def suma (valor_uno, valor_dos):
    """
    Suma dos valores.
    
    :param valor_uno: El primer valor a sumar. Argumento obligatorio UNO.
    :param valor_dos: El segundo valor a sumar. Argumento obligatorio DOS.
    :return: La suma de los dos valores.
    """
    return valor_uno + valor_dos
# Ejemplo de uso de la función suma
resultado = suma(5, 10) #Llamada a la función con argumentos posicionales
print(f"La suma de 5 y 10 es: {resultado}") #Salida: La suma de 5 y 10 es: 15


def suma_tres_valores(valor_uno, valor_dos, valor_tres):
    """
    Suma tres valores.
    
    :param valor_uno: El primer valor a sumar. Argumento obligatorio UNO.
    :param valor_dos: El segundo valor a sumar. Argumento obligatorio DOS.
    :param valor_tres: El tercer valor a sumar. Argumento opcional TRES (valor predeterminado es 0).
    :return: La suma de los tres valores.
    """
    return valor_uno + valor_dos + valor_tres
# Ejemplo de uso de la función suma_tres_valores
resultado = suma_tres_valores(5, 10, 15) #Llamada a la función con argumentos posicionales
print(f"La suma de 5, 10 y 15 es: {resultado}") #Salida: La suma de 5, 10 y 15 es: 30

def suma (*args):
    """
    Suma varios valores.
    
    :param *argumentos: Los valores a sumar. Argumento opcional (valor predeterminado es 0).
    :return: La suma de los valores.
    """
    return sum(args) #Suma todos los valores en la tupla
# Ejemplo de uso de la función suma
resultado = suma(5, 10, 15, 20) #Llamada a la función con argumentos posicionales
print(f"La suma de 5, 10, 15 y 20 es: {resultado}") #Salida: La suma de 5, 10, 15 y 20 es: 50

def suma (**kwargs):
    """
    Suma varios valores.
    
    :param **argumentos: Los valores a sumar. Argumento opcional (valor predeterminado es 0).
    :return: La suma de los valores.
    """
    return sum(kwargs.values()) #Suma todos los valores en el diccionario
# Ejemplo de uso de la función suma
resultado = suma(valor_uno=15, valor_dos=100, valor_tres=150, valor_cuatro=1000) #Llamada a la función con argumentos por nombre
print(f"La suma de 15, 100, 150 y 1000 es: {resultado}") #Salida: La suma de 5, 10 y 15 es: 30