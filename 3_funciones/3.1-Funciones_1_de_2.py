#https://www.youtube.com/watch?v=hF85etcCghY&t=17s

#Funciones
#Las funciones son bloques de código que se pueden reutilizar en diferentes partes de un programa.
#Se definen utilizando la palabra clave def, seguida del nombre de la función y los parámetros entre paréntesis.
#Las funciones pueden devolver valores utilizando la palabra clave return.
#Las funciones pueden tener parámetros opcionales, que se definen utilizando un valor por defecto.
#Las funciones pueden tener un número variable de argumentos utilizando el operador *args o **kwargs.
#Las funciones pueden ser anidadas, es decir, una función puede contener otra función dentro de su cuerpo.
#Las funciones pueden ser lambda, es decir, funciones anónimas que se definen utilizando la palabra clave lambda.
#Las funciones pueden ser generadores, es decir, funciones que utilizan la palabra clave yield para devolver un valor y pausar su ejecución.
#Las funciones pueden ser decoradores, es decir, funciones que modifican el comportamiento de otras funciones.
#Las funciones pueden ser métodos, es decir, funciones que pertenecen a una clase y se definen dentro de la clase.
#Las funciones pueden ser recursivas, es decir, funciones que se llaman a sí mismas

def factorial_numero(numero):
    """
    Calcula el factorial de un número entero positivo.
    
    :param numero: Número entero positivo del cual se desea calcular el factorial.
    :return: El factorial del número.
    """
    if numero < 0:
        raise ValueError("El número debe ser un entero positivo.")
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

# Ejemplo de uso de la función factorial_numero

factorial = factorial_numero(4)
print(f"El factorial de 4 es: {factorial}")

factorial = factorial_numero(5)
print(f"El factorial de 5 es: {factorial}")

factorial = factorial_numero(6)
print(f"El factorial de 6 es: {factorial}")