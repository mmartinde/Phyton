#https://www.youtube.com/watch?v=yTvw1dVcER8

#Name
#Atributo __name__
#El atributo __name__ es una variable especial en Python que se utiliza para determinar si un módulo está siendo

import sys
sys.path.append('./4_modulos/calculadora')  # Asegúrate de que la ruta sea correcta

from calculadora import __name__ as __name__modulo__

print(f"El nombre del script principal es: {__name__}")
print(f"El nombre del módulo calculadora es: {__name__modulo__}")


if __name__ == "__main__":#Es este el script principal?
    print("Este es el script principal")

#Esto significa que si ejecutas este script directamente, el valor de __name__ será "__main__".
#Si importas este script desde otro módulo, el valor de __name__ será el nombre del módulo. Y por lo tanto, no se ejecutará el bloque de código dentro del if.
#Ejemplo de uso:
#Si guardas el código anterior en un archivo llamado script_principal.py y lo ejecutas directamente, verás que imprime "Este es el script principal".
#Pero si importas este script desde otro archivo, como por ejemplo otro_script.py, no verás ese mensaje.
#Esto es útil para evitar que ciertas partes del código se ejecuten cuando el módulo es importado, pero sí se ejecuten cuando el módulo es ejecutado directamente.