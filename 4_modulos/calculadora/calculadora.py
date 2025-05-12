#!/usr/bin/python3

"""
NAME
Calculadora

DESCRIPTION
    Esta es una calculadora que permite realizar operaciones matematicas basicas como suma, resta, multiplicacion y division.
    
FUNCTIONS
    division(num1, num2)
        Regresa la division de dos numeros enteros.
        Esta funcion verifica si el divisor es cero y devuelve un mensaje de error en caso de que lo sea.
    
    multiplicacion(num1, num2)
        Regresa la multiplicacion de dos numeros enteros.
        Esta funcion verifica si el divisor es cero y devuelve un mensaje de error en caso de que lo sea.
        
    suma(num1, num2)
        Regresa la suma de dos numeros enteros.
        Esta funcion verifica si el divisor es cero y devuelve un mensaje de error en caso de que lo sea.
        
    resta(num1, num2)
        Regresa la resta de dos numeros enteros.
        Esta funcion verifica si el divisor es cero y devuelve un mensaje de error en caso de que lo sea.
        
    potencia(num1, num2)
        Regresa la potencia de dos numeros enteros.
        Esta funcion verifica si el divisor es cero y devuelve un mensaje de error en caso de que lo sea.
        
    raiz(num1)
        Regresa la raiz cuadrada de un numero entero.
        Esta funcion verifica si el divisor es cero y devuelve un mensaje de error en caso de que lo sea.impo
        
    factorial(num1)
        Regresa el factorial de un numero entero.
        Esta funcion verifica si el divisor es cero y devuelve un mensaje de error en caso de que lo sea.
"""
___author__ = "Manu Martin"
___copyright__ = "Copyright 2025 Manu Martin"
___credits__ = ["Código facilito"]

___license__ = "GPL"
___version__ = "1.0.0"
___maintainer__ = "Manu Martin"
___email__ = "manu1574@hotmail.com"
___status__ = "Development"

def sumar (num1, num2):
    """Suma de dos numeros enteros
    Esta funcion recibe dos numeros enteros y devuelve la suma de ellos.

    Args:
        num1 (integer): sumando uno
        num2 (integer): sumando dos

    Returns:
        integer: suma de los dos numeros
    """
    return num1 + num2

def restar (num1, num2):
    """Resta de dos numeros enteros
    Esta funcion recibe dos numeros enteros y devuelve la resta de ellos.

    Args:
        num1 (integer): operador uno
        num2 (integer): operador dos

    Returns:
        integer: resultado de la resta
    """
    return num1 - num2

def multiplicacion (num1, num2):
    """Multiplicacion de dos numeros enteros
    Esta funcion recibe dos numeros enteros y devuelve la multiplicacion de ellos.

    Args:
        num1 (integer): operador uno
        num2 (integer): operador dos

    Returns:
        integer: resultado de la multiplicacion
    """
    return num1 * num2

def division (num1, num2):
    """Division de dos numeros enteros
    Esta funcion recibe dos numeros enteros y devuelve la division de ellos.
    Esta funcion verifica si el divisor es cero y devuelve un mensaje de error en caso de que lo sea.

    Args:
        num1 (integer): dividendo
        num2 (integer): divisor

    Returns:
        integer: delvuelve la division de los dos numeros
    """
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return num1 / num2

def potencia (num1, num2):
    """Potencia de dos numeros enteros
    Esta funcion recibe dos numeros enteros y devuelve la potencia de ellos.
    Args:
        num1 (integer): base
        num2 (integer): exponente
    Returns:
        integer: resultado de la potencia
    """
    return num1 ** num2

def raiz (num1):
    """Raiz cuadrada de un numero entero
    Esta funcion recibe un numero entero y devuelve la raiz cuadrada de el.
    Args:
        num1 (integer): numero al que se le quiere calcular la raiz cuadrada
    Returns:
        integer: resultado de la raiz cuadrada
    """
    if num1 < 0:
        return "Error: Cannot calculate the square root of a negative number."
    else:
        return num1 ** 0.5

def factorial (num1):
    """Factorial de un numero entero
    Esta funcion recibe un numero entero y devuelve el factorial de el.
    Args:
        num1 (integer): numero al que se le quiere calcular el factorial
    Returns:
        integer: resultado del factorial
    """
    if num1 < 0:
        return "Error: Factorial of a negative number is not defined."
    elif num1 == 0 or num1 == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, num1 + 1):
            resultado *= i
        return resultado
    
if __name__ == "__main__":
    print ("Este es el script principal")
    
    
#Esto significa que si ejecutas este script directamente, el valor de __name__ será "__main__".
#Si importas este script desde otro módulo, el valor de __name__ será el nombre del módulo. Y por lo tanto, no se ejecutará el bloque de código dentro del if.
#Ejemplo de uso:
#Si guardas el código anterior en un archivo llamado script_principal.py y lo ejecutas directamente, verás que imprime "Este es el script principal".
#Pero si importas este script desde otro archivo, como por ejemplo otro_script.py, no verás ese mensaje.
#Esto es útil para evitar que ciertas partes del código se ejecuten cuando el módulo es importado, pero sí se ejecuten cuando el módulo es ejecutado directamente.