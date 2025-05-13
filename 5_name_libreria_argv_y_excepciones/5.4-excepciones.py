#https://www.youtube.com/watch?v=l7Aj6RhJx8g

#excepciones
# Las excepciones son eventos que pueden alterar el flujo normal de un programa.
# En Python, las excepciones se utilizan para manejar errores y situaciones inesperadas que pueden ocurrir durante la ejecución de un programa.
# Cuando ocurre una excepción, Python detiene la ejecución del programa y busca un bloque de código que pueda manejar la excepción.
# Si no se encuentra un bloque de manejo de excepciones adecuado, el programa se detiene y muestra un mensaje de error.
# Las excepciones se pueden manejar utilizando bloques try y except.
# El bloque try contiene el código que puede generar una excepción, y el bloque except contiene el código que se ejecutará si se produce una excepción.
# También se pueden utilizar bloques finally para ejecutar código que debe ejecutarse independientemente de si se produce una excepción o no.


# Ejemplo de manejo de excepciones en Python
try:
    # Intentamos dividir 2 entre 0, lo que generará una excepción ZeroDivisionError
    print(2/0)
except ZeroDivisionError:
    # Si se produce una excepción ZeroDivisionError, se ejecuta este bloque
    print("Error: No se puede dividir entre cero.")
finally:
    # Este bloque se ejecuta independientemente de si se produjo una excepción o no
    print("Este bloque se ejecuta siempre.")
    print  ("--------------------------------------------------")
    

# Ejemplo de manejo de excepciones con múltiples tipos de excepciones
try:
    # Intentamos convertir una cadena no numérica a un número entero, lo que generará una excepción ValueError
    print(int("Hola"))
except (ZeroDivisionError, ValueError) as e:
    # Si se produce una excepción ZeroDivisionError o ValueError, se ejecuta este bloque
    print(f"Error: {e}")
finally:
    # Este bloque se ejecuta independientemente de si se produjo una excepción o no
    print("Este bloque se ejecuta siempre.")
    print  ("--------------------------------------------------")
# Ejemplo de manejo de excepciones con múltiples bloques except
try:
    # Intentamos dividir 2 entre 0, lo que generará una excepción ZeroDivisionError
    print(2/0)
except ZeroDivisionError:
    # Si se produce una excepción ZeroDivisionError, se ejecuta este bloque
    print("Error: No se puede dividir entre cero.")
except ValueError:
    # Si se produce una excepción ValueError, se ejecuta este bloque
    print("Error: Valor no válido.")
finally:
    # Este bloque se ejecuta independientemente de si se produjo una excepción o no
    print("Este bloque se ejecuta siempre.")
    print  ("--------------------------------------------------")


# Ejemplo de manejo de excepciones con bloques try anidados
try:
    # Intentamos dividir 2 entre 0, lo que generará una excepción ZeroDivisionError
    print(2/0)
except ZeroDivisionError:
    # Si se produce una excepción ZeroDivisionError, se ejecuta este bloque
    print("Error: No se puede dividir entre cero.")
    try:
        # Intentamos convertir una cadena no numérica a un número entero, lo que generará una excepción ValueError
        print(int("Hola"))
    except ValueError:
        # Si se produce una excepción ValueError, se ejecuta este bloque
        print("Error: Valor no válido.")
    finally:
        # Este bloque se ejecuta independientemente de si se produjo una excepción o no
        print("Este bloque se ejecuta siempre.")
        print  ("--------------------------------------------------")
# Ejemplo de manejo de excepciones con bloques try anidados y múltiples bloques except
