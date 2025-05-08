#https://www.youtube.com/watch?v=vMTV0hY2jio&t=13s

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

def suma (valor_uno, valor_dos, valor_tres):
    """
    Suma dos o tres números.
    
    :param valor_uno: Primer número a sumar.
    :param valor_dos: Segundo número a sumar.
    :param valor_tres: Tercer número a sumar (opcional, por defecto es 0).
    :return: La suma de los números.
    """
    return valor_uno + valor_dos + valor_tres
# Ejemplo de uso de la función suma
resultado = suma(10, 20,30)
print(f"La suma de 10, 20 y 30 es: {resultado}")

def division (valor_uno, valor_dos):
    """
    Divide dos números.
    
    :param valor_uno: Numerador.
    :param valor_dos: Denominador.
    :return: El resultado de la división.
    """
    return valor_uno / valor_dos
# Ejemplo de uso de la función division
resultado = division(10, 20)
print(f"La división de 10 entre 20 es: {resultado}")

def multiplicacion (valor_uno, valor_dos):
    """
    Multiplica dos números.
    
    :param valor_uno: Primer número a multiplicar.
    :param valor_dos: Segundo número a multiplicar.
    :return: El resultado de la multiplicación.
    """
    return valor_uno * valor_dos
# Ejemplo de uso de la función multiplicacion
resultado = multiplicacion(10, 20)
print(f"La multiplicación de 10 por 20 es: {resultado}")

def resta (valor_uno, valor_dos):
    """
    Resta dos números.
    
    :param valor_uno: Minuendo.
    :param valor_dos: Sustraendo.
    :return: El resultado de la resta.
    """
    return valor_uno - valor_dos
# Ejemplo de uso de la función resta
resultado = resta(10, 20)
print(f"La resta de 10 menos 20 es: {resultado}")

def potencia (valor_uno, valor_dos):
    """
    Calcula la potencia de un número.
    
    :param valor_uno: Base.
    :param valor_dos: Exponente.
    :return: El resultado de la potencia.
    """
    return valor_uno ** valor_dos
# Ejemplo de uso de la función potencia
resultado = potencia(10, 20)
print(f"La potencia de 10 elevado a 20 es: {resultado}")

def raiz (valor_uno):
    """
    Calcula la raíz cuadrada de un número.
    
    :param valor_uno: Número del cual se desea calcular la raíz cuadrada.
    :return: La raíz cuadrada del número.
    """
    return valor_uno ** 0.5
# Ejemplo de uso de la función raiz
resultado = raiz(10)
print(f"La raíz cuadrada de 10 es: {resultado}")

def factorial (valor_uno):
    """
    Calcula el factorial de un número.
    
    :param valor_uno: Número del cual se desea calcular el factorial.
    :return: El factorial del número.
    """
    if valor_uno == 0:
        return 1
    else:
        return valor_uno * factorial(valor_uno - 1)
# Ejemplo de uso de la función factorial
resultado = factorial(10)
print(f"El factorial de 10 es: {resultado}")

def fibonacci (valor_uno):
    """
    Calcula el número de Fibonacci en la posición dada.
    
    :param valor_uno: Posición del número de Fibonacci.
    :return: El número de Fibonacci en la posición dada.
    """
    if valor_uno == 0:
        return 0
    elif valor_uno == 1:
        return 1
    else:
        return fibonacci(valor_uno - 1) + fibonacci(valor_uno - 2)
# Ejemplo de uso de la función fibonacci
resultado = fibonacci(10)
print(f"El número de Fibonacci en la posición 10 es: {resultado}")

def primo (valor_uno):
    """
    Verifica si un número es primo.
    
    :param valor_uno: Número a verificar.
    :return: True si el número es primo, False en caso contrario.
    """
    if valor_uno < 2:
        return False
    for i in range(2, int(valor_uno ** 0.5) + 1):
        if valor_uno % i == 0:
            return False
    return True
# Ejemplo de uso de la función primo
resultado = primo(10)
print(f"El número 10 es primo: {resultado}")

def maximo (valor_uno, valor_dos):
    """
    Devuelve el número máximo entre dos números.
    
    :param valor_uno: Primer número.
    :param valor_dos: Segundo número.
    :return: El número máximo entre los dos.
    """
    return max(valor_uno, valor_dos)
# Ejemplo de uso de la función maximo
resultado = maximo(10, 20)
print(f"El número máximo entre 10 y 20 es: {resultado}")

def minimo (valor_uno, valor_dos):
    """
    Devuelve el número mínimo entre dos números.
    
    :param valor_uno: Primer número.
    :param valor_dos: Segundo número.
    :return: El número mínimo entre los dos.
    """
    return min(valor_uno, valor_dos)
# Ejemplo de uso de la función minimo
resultado = minimo(10, 20)
print(f"El número mínimo entre 10 y 20 es: {resultado}")

def suma_lista (lista):
    """
    Suma todos los números en una lista.
    
    :param lista: Lista de números a sumar.
    :return: La suma de los números en la lista.
    """
    return sum(lista)
# Ejemplo de uso de la función suma_lista
resultado = suma_lista([10, 20, 30])
print(f"La suma de la lista [10, 20, 30] es: {resultado}")

def promedio_lista (lista):
    """
    Calcula el promedio de los números en una lista.
    
    :param lista: Lista de números a promediar.
    :return: El promedio de los números en la lista.
    """
    return sum(lista) / len(lista)
# Ejemplo de uso de la función promedio_lista
resultado = promedio_lista([10, 20, 30])   

def multiples_valores():
    """
    Devuelve múltiples valores.
    
    :return: Cuatro valores diferentes .
    """
    return "String", 1, True, 25.6
# Ejemplo de uso de la función multiples_valores
strig, entero, booleano, flotante = multiples_valores()
print(f"El string es: {strig}")
print(f"El entero es: {entero}")
print(f"El booleano es: {booleano}")
print(f"El flotante es: {flotante}")

     