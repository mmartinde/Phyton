#https://youtu.be/3O3h-I9Z-4I?si=rvPqMaubAh8GC4P2

# Herencia múltiple
# En Python, una clase puede heredar de múltiples clases base.
# Esto se conoce como herencia múltiple.
# La herencia múltiple puede ser útil, pero también puede complicar el diseño de la clase y la resolución de conflictos.
# En este ejemplo, la clase `A` y la clase `B` tienen un método `saludar`.
# La clase `C` hereda de ambas clases y puede llamar a ambos métodos `saludar`.
class A:
    def saludar(self):
        print("Hola desde la clase A")
class B:
    def saludar(self):
        print("Hola desde la clase B")
class C(A, B):
    def saludar(self):
        print("Hola desde la clase C")
        A.saludar(self)
        B.saludar(self)
# Crear una instancia de la clase C
c = C()
# Llamar al método saludar de la clase C
c.saludar()
# Salida:
# Hola desde la clase C
# Hola desde la clase A
# Hola desde la clase B
# En este ejemplo, la clase `C` hereda de las clases `A` y `B`, y puede llamar a los métodos `saludar` de ambas clases.
# La salida muestra que el método `saludar` de la clase `C` se ejecuta primero, seguido por los métodos `saludar` de las clases `A` y `B`.
# La herencia múltiple puede ser útil en algunos casos, pero también puede complicar el diseño de la clase y la resolución de conflictos.
# En este ejemplo, la clase `C` tiene un método `saludar` que llama a los métodos `saludar` de las clases `A` y `B`.


# En resumen, la herencia múltiple es una característica poderosa de Python que permite a las clases heredar de múltiples clases base.
# Sin embargo, es importante usarla con precaución y asegurarse de que el diseño de la clase sea claro y fácil de entender.


class Animal:
    @property
    def terrestre(self):
        return True
    
class Felino (Animal):
    @property
    def garras_retractiles(self):
        return True
    
    def cazar(self):
        print ("El felino esta Cazando")

class Mascota:
    nombre = " " #Todas las mascotas tienen un nombre
    
    @property
    def domestico(self):
        return True
    
    def jugar(self):
        print ("La mascota esta jugando")
    
    def mostrar_nombre(self):
        print (f"El nombre de la mascota es: {self.nombre}")

# La clase Gato hereda de las clases Felino y Mascota
class Gato (Felino, Mascota):
    @property
    def domestico(self):
        return True
    
    def maullar(self):
        print ("El gato esta maullando")
# En este ejemplo, la clase Gato hereda de las clases Felino y Mascota.
# La clase Gato tiene acceso a los métodos y propiedades de ambas clases.
# La clase Gato tiene su propio método maullar, pero también puede usar los métodos cazar y jugar de las clases Felino y Mascota.
# La clase Gato también tiene su propia propiedad domestico, que sobrescribe la propiedad domestico de la clase Mascota.
# La clase Gato tiene acceso a la propiedad terrestre de la clase Animal a través de la herencia de la clase Felino.
# La clase Gato hereda de las clases Felino y Mascota, lo que significa que la clase Gato es una subclase de ambas clases.

        
gato  = Gato()
gato.nombre = "Michi"
gato.mostrar_nombre()
print (f"Mostramos la propiedad de la clase Animal del gato es 'terrestre' valor: {gato.terrestre}")