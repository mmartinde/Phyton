#https://youtu.be/GnORUc5SeHc?si=CIKTQHCxc_bOJ9J-

# Paquete de Python
# Paquete de Python es una carpeta que contiene un archivo __init__.py
# Este archivo puede estar vacío o contener código de inicialización para el paquete
# La carpeta del paquete puede contener subcarpetas que también son paquetes
# La estructura de un paquete de Python es la siguiente:
# paquete/
# ├── __init__.py
# ├── modulo1.py
# ├── modulo2.py
# └── subpaquete/
#     ├── __init__.py
#     └── modulo3.py
# El archivo __init__.py se ejecuta cuando se importa el paquete
# El archivo __init__.py puede contener código de inicialización para el paquete
# El archivo __init__.py puede estar vacío


#Desde este archivo se importan los módulos, se podría llamar main.py o de cualquier otra manera.
from animales.gato import Gato

# Se crea una instancia de la clase Gato
gato = Gato("Misifus")
print(gato.maullar())

