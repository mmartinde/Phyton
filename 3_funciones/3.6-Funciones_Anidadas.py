#https://www.youtube.com/watch?v=S0Lfm_rEQ2A&t=21s

# Funciones Anidadas
# Una función anidada es una función definida dentro de otra función.
# Las funciones anidadas pueden acceder a las variables de la función externa.
# Las funciones anidadas son útiles cuando se necesita una función que solo se utilizará dentro de otra función.
# Las funciones anidadas pueden ayudar a organizar el código y hacerlo más legible.
# Las funciones anidadas pueden ser útiles para crear funciones de orden superior, que son funciones que toman otras funciones como argumentos o devuelven funciones como resultados.

# Definición de la función externa
def funcion_externa(valor_uno, valor_dos):
    """
    Función externa que suma dos valores utilizando una función anidada.
    
    :param valor_uno: El primer valor a sumar.
    :param valor_dos: El segundo valor a sumar.
    :return: La suma de los dos valores.
    """
    
    # Definición de la función anidada
    def funcion_interna(valor_uno, valor_dos):
        return valor_uno + valor_dos
    
    # Llamada a la función anidada
    return funcion_interna(valor_uno, valor_dos)
# Ejemplo de uso de la función externa
resultado = funcion_externa(5, 10) #Llamada a la función con argumentos posicionales
print(f"La suma de 5 y 10 es: {resultado}") #Salida: La suma de 5 y 10 es: 15

def division (num_uno, num_dos):
    """
    Función division con funcion anidada que valida si el primer número es mayor 0 y que el segundo número sea mayor que 0.
    
    :param num_uno: El primer número a validar.
    :param num_dos: El segundo número a validar.
    :return: True si el primer y segundo número es mayor que 0, False en caso contrario.
    """
    # Definición de la función anidada
    def validacion ():
        return num_uno > 0 and num_dos > 0
        
    if validacion():
        return num_uno / num_dos
    else:
        return "No se puede dividir por cero"   
    
# Llamada a la función anidada
resultado = division(10, 0)  
print(resultado) #Salida: No se puede dividir por cero
resultado = division(10, 5)
print(f"La división de 10 entre 5 es:{resultado}") #Salida: 2.0


#Closure
# Un closure es una función anidada que recuerda el entorno en el que fue creada, incluso después de que la función externa haya terminado de ejecutarse.
# Esto significa que la función anidada puede acceder a las variables de la función externa, incluso si la función externa ya ha terminado de ejecutarse.
# Los closures son útiles para crear funciones que necesitan recordar el estado entre llamadas.
# Un closure se crea cuando una función anidada utiliza variables de la función externa.
# Un closure es una función que recuerda el entorno en el que fue creada, incluso después de que la función externa haya terminado de ejecutarse.

# Definición de la función externa
def funcion_externa(valor_uno):
    """
    Función externa que devuelve una función anidada (closure) que suma un valor fijo al valor dado.
    
    :param valor_uno: El valor al que se le sumará el valor fijo.
    :return: Una función anidada que suma un valor fijo al valor dado.
    """
    
    # Definición de la función anidada (closure)
    def funcion_interna(valor_dos):
        return valor_uno + valor_dos
    
    # Devolver la función anidada
    return funcion_interna
# Ejemplo de uso de la función externa
closure = funcion_externa(7) # Llamada a la función externa
resultado = closure(3) # Llamada a la función anidada (closure)
print(f"La suma de 7 y 3 es: {resultado}") #Salida: La suma de 5 y 10 es: 15