#https://www.youtube.com/watch?v=l7Aj6RhJx8g

#ARGV
#La función sys.argv es una lista que contiene los argumentos de la línea de comandos pasados al script de Python.
#El primer elemento de la lista (sys.argv[0]) es siempre el nombre del script en sí, y los siguientes elementos son los argumentos proporcionados por el usuario.
#Esto es útil para permitir que los usuarios pasen información al script al ejecutarlo desde la línea de comandos.
#Ejemplo:
import sys

# sys.argv es una lista que contiene los argumentos de la línea de comandos pasados al script.
# El primer elemento de la lista (sys.argv[0]) es siempre el nombre del script en sí, y los siguientes elementos son los argumentos proporcionados por el usuario.
# En este caso, estamos imprimiendo todos los argumentos pasados al script.
if __name__ == "__main__":
    # Comprobamos si se han pasado argumentos al script
    if len(sys.argv) > 1:
        # Si el primer argumento es 'help', imprimimos un mensaje de ayuda
        if sys.argv[1] == 'help':
            print("Este script acepta los siguientes argumentos:")
            print("1. help: Muestra este mensaje de ayuda.")
            print("2. [cualquier otro argumento]: Se imprimirá en la consola.")
        else:
            # Imprimimos los argumentos pasados al script
            for arg in sys.argv[1:]:
                print(arg)
    else:
        # Si no se han pasado argumentos, imprimimos un mensaje
        print("No se han pasado argumentos al script.")
