#https://youtu.be/RFGXxnEAejo?si=kPxJMfjctTK2rKIg

# Métodos de clase
# Un método de clase es un método que pertenece a la clase y no a la instancia.
# Se define con el decorador @classmethod y recibe como primer parámetro cls, que hace referencia a la clase.
# Se utiliza para crear métodos que afectan a la clase en su conjunto, en lugar de a una instancia específica.
# Se puede utilizar para crear métodos de fábrica, que son métodos que crean instancias de la clase.


class Animal:
    volador = True
    
class Cocodrilo(Animal):

    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def new(cls, nombre):
        cls.volador = False
        # Cambia el atributo de clase volador a False
        # y crea una nueva instancia de la clase
        return Cocodrilo(nombre)
    
cocodrilo = Cocodrilo.new("Cocodrilo")
print(cocodrilo.nombre)  # Salida: Cocodrilo
print(cocodrilo.volador)  # Salida: True