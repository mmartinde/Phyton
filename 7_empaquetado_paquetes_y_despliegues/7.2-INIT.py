#https://youtu.be/MZtp4ZuEcGM?si=UncwL1WRfohSwerk

# Init file
# Este archivo se ejecuta cuando se importa el paquete
# Se pueden importar módulos o subpaquetes aquí



from animales import Gato
from animales import Leon
from animales import creador_gatos
# Ejemplo de uso
leon = Leon()
print(leon.rugir())

gato = creador_gatos ("nuevo gato por paquete")

gato= Gato("Miau")
print(gato.maullar())