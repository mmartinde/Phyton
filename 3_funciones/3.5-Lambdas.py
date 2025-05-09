#https://www.youtube.com/watch?v=cJ9zcR1uTt8&t=14s

#Lambdas
#Una función lambda es una función anónima que se puede definir en una sola línea de código.
#Las funciones lambda se utilizan para crear funciones pequeñas y simples que no necesitan un nombre.
#Las funciones lambda se definen utilizando la palabra clave lambda seguida de los argumentos y una expresión.
#Las funciones lambda son útiles cuando se necesita una función simple y no se quiere definir una función completa.
#Las funciones lambda se pueden utilizar como argumentos para otras funciones, como map(), filter() y reduce().
#Las funciones lambda se pueden utilizar para crear funciones de orden superior, que son funciones que toman otras funciones como argumentos o devuelven funciones como resultados.

def suma_lambda(valor_uno, valor_dos):
    """
    Suma dos valores utilizando una función lambda.
    
    :param x: El primer valor a sumar.
    :param y: El segundo valor a sumar.
    :return: La suma de los dos valores.
    """
    return (lambda valor_uno, valor_dos: valor_uno + valor_dos)(valor_uno, valor_dos)

# Ejemplo de uso de la función suma_lambda
resultado = suma_lambda(5, 10) #Llamada a la función con argumentos posicionales
print(f"La suma de 5 y 10 es: {resultado}") #Salida: La suma de 5 y 10 es: 15


#Otra forma de definir una función lambda es utilizando la palabra clave lambda seguida de los argumentos y una expresión.

mi_funcion = lambda valor_uno, valor_dos: valor_uno + valor_dos
# Ejemplo de uso de la función lambda
resultado = mi_funcion(5, 10) #Llamada a la función con argumentos posicionales
print(f"La suma de 5 y 10 es: {resultado}") #Salida: La suma de 5 y 10 es: 15

formato = lambda sentencia: '¿{}?'.format(sentencia)
# Ejemplo de uso de la función lambda
resultado = formato("Puedes hacer este 'Hola Mundo' una pregunta") #Llamada a la función con argumentos posicionales 
print(resultado) #Salida: ¿Puedes hacer este 'Hola Mundo' una pregunta?