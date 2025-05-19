#https://youtu.be/xN70bAjbjhs?si=JzB1Toxcwlaxle_R

#Override
# # En Python, el método `__str__` se utiliza para definir cómo se debe representar un objeto como una cadena de texto.
# # Este método se llama automáticamente cuando se utiliza la función `str()` o `print()` en un objeto.
# # Al sobrescribir este método, puedes personalizar la representación en cadena de tus objetos.

# # En este ejemplo, la clase `Persona` tiene un método `__str__` que devuelve una representación en cadena del objeto.
# # La clase `Empleado` hereda de la clase `Persona` y también sobrescribe el método `__str__` para incluir información adicional.
# # La clase `Gerente` hereda de la clase `Empleado` y también sobrescribe el método `__str__` para incluir información adicional.
# # La salida muestra cómo se puede personalizar la representación en cadena de los objetos utilizando el método `__str__`.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario
    def __str__(self):
        return f"{super().__str__()}, Salario: {self.salario}"
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento
    def __str__(self):
        return f"{super().__str__()}, Departamento: {self.departamento}"
# Crear instancias de las clases
persona = Persona("Juan", 30)
empleado = Empleado("Ana", 25, 50000)
gerente = Gerente("Luis", 40, 80000, "Ventas")
# Imprimir las representaciones en cadena de los objetos
print(persona)  # Salida: Nombre: Juan, Edad: 30
print(empleado)  # Salida: Nombre: Ana, Edad: 25, Salario: 50000
print(gerente)  # Salida: Nombre: Luis, Edad: 40, Salario: 80000, Departamento: Ventas
# En este ejemplo, la clase `Persona` tiene un método `__str__` que devuelve una representación en cadena del objeto.
# La clase `Empleado` hereda de la clase `Persona` y también sobrescribe el método `__str__` para incluir información adicional.
# La clase `Gerente` hereda de la clase `Empleado` y también sobrescribe el método `__str__` para incluir información adicional.
# La salida muestra cómo se puede personalizar la representación en cadena de los objetos utilizando el método `__str__`.


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
    def __init__(self, nombre):
        self.nombre = nombre # inicializa el objeto y establece el nombre de la mascota
# La clase `Mascota` tiene un atributo `nombre` que se inicializa en el constructor `__init__`.
# El método `__init__` se utiliza para inicializar el objeto y establecer el nombre de la mascota.
# En este ejemplo, el método `__init__` se utiliza para inicializar el objeto y establecer el nombre de la mascota.
# El método `mostrar_nombre` se define en la clase `Mascota` y se puede sobrescribir en las clases que heredan de ella.
    def mostrar_nombre(self):
        print (f"El nombre de la mascota es: {self.nombre}")
        
    def domestico(self):
        return True
    
    def jugar(self):
        return "La mascota esta jugando"
    
# La clase Gato hereda de las clases Felino y Mascota
# En este ejemplo, la clase `Gato` hereda de las clases `Felino` y `Mascota`, y sobrescribe el método `mostrar_nombre` para incluir información adicional.
class Gato (Felino, Mascota):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre_gato = nombre # inicializa el objeto y establece el nombre del gato
    # El método `__init__` se utiliza para inicializar el objeto y establecer el nombre del gato.
    @property
    def domestico(self):
        return True
    
    def maullar(self):
        print ("El gato esta maullando")
    
    def mostrar_nombre(self):
        Mascota.mostrar_nombre(self) # Llama al método `mostrar_nombre` de la clase `Mascota`
        #super().mostrar_nombre() # Llama al método `mostrar_nombre` de la clase `Mascota`
        print(f"{self.jugar()} y se llama {self.nombre} ")   


        
gato  = Gato("Michi")
#gato.nombre = "Michi" # gato.mostrar_nombre() le asigna el nombre "Michi" a la mascota cuando se crea la instancia de la clase `Gato`. Pero al estar inicializada la 
gato.mostrar_nombre()