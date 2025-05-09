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