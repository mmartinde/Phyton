#https://www.youtube.com/watch?v=munC0mVXPWk

#Variables Generales
#Las variables generales son variables que se pueden utilizar en diferentes partes de un programa.
#Se definen utilizando la palabra clave global, seguida del nombre de la variable.
#Las variables generales pueden ser de cualquier tipo de dato, como enteros, flotantes, cadenas, listas, diccionarios, etc.
#Las variables generales pueden ser modificadas en cualquier parte del programa.
#Las variables generales pueden ser utilizadas en funciones, pero deben ser declaradas como globales dentro de la función.
#Las variables generales pueden ser utilizadas en clases, pero deben ser declaradas como globales dentro de la clase.

def palindromo (frase):
    """
    Verifica si una palabra es un palíndromo.
    
    :param palabra: La palabra a verificar.
    :return: True si la palabra es un palíndromo, False en caso contrario.
    """
    frase =frase.replace(" ", "").lower() #Variable de tipo str LOCAL
    # Eliminar espacios y convertir a minúsculas
    # Comprobar si la frase es igual a su reverso
    return frase == frase[::-1]


frase = "Anita lava la tina" #Varialble de tipo str GLOBAL
if palindromo(frase):
    print(f"La frase '{frase}' es un palíndromo.")
else:
    print(f"La frase '{frase}' no es un palíndromo.")


def modificar_variable_global():
    """
    Modifica una variable global.
    
    :return: None
    """
    global variable_global #Declarar la variable como global
    variable_global = "Nueva variable global" #Modificar la variable global
    # La variable global se puede modificar dentro de la función

# Ejemplo de uso de la función modificar_variable_global
variable_global = "Variable global" #Variable de tipo str GLOBAL
print(f"Variable global antes de modificar: {variable_global}")
modificar_variable_global()
print(f"Variable global después de modificar: {variable_global}")


def crear_variable_global():
    """
    Crea una variable global.
    
    :return: None
    """
    global variable_global #Declarar la variable como global
    variable_global = "Esto es una nueva Variable global" #Crear la variable global
    # La variable global se puede crear dentro de la función
# Ejemplo de uso de la función crear_variable_global
crear_variable_global()
print(f"Variable global después de crear: {variable_global}")
