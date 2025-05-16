#https://youtu.be/SnqNoerkx0A?si=AtYoLeXPpBBmWfbS

"""
HERENCIAS
La herencia es un mecanismo que permite crear una nueva clase a partir de una clase existente.
La nueva clase hereda los atributos y métodos de la clase existente, lo que permite reutilizar el código y crear jerarquías de clases.
La clase existente se llama clase padre o superclase, y la nueva clase se llama clase hija o subclase.
La herencia se define utilizando la palabra clave "class" seguida del nombre de la clase hija y el nombre de la clase padre entre paréntesis.
En Python, la herencia se puede utilizar para crear jerarquías de clases y reutilizar código.
La herencia se puede utilizar para crear jerarquías de clases y reutilizar código.
"""

class Animal: #Clase padre
    @property
    def terrestre(self):
        return True
            
class Felino(Animal): #Clase padre
    @property     #Propiedad que indica si el gato tiene garras retractiles
    def garras_retractiles(self):
        return True
    def cazar(self):
        print ("El felino esta cazondo")

class Gato(Felino): #Clase hija
    def gato_cazador(self):
        self.cazar() #Sobreescribimos el metodo cazar de la clase padre 


class Jaguar(Felino): #Clase hija
    pass

gato= Gato()
jaguar = Jaguar()

print(gato.garras_retractiles)
print(gato.terrestre)
print(gato.gato_cazador())

print(jaguar.garras_retractiles)
print(jaguar.terrestre)
print(jaguar.cazar())

#Dont repeat yourself
#No repitas el mismo codigo en diferentes clases
#En este caso, el gato y el jaguar tienen el mismo metodo cazar, por lo que se puede crear una clase padre que contenga ese metodo 
#y las clases hijas heredaran ese metodo    
