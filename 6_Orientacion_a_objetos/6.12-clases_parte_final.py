#https://youtu.be/y-ZzTGHFEhI?si=O4UmItkTyb7yoOCx

# Métodos parte Final

#Como crear atributos a una instancia de una clase
# En Python, las instancias de una clase pueden tener atributos que se crean dinámicamente.
# Esto significa que puedes agregar atributos a una instancia de una clase en cualquier momento, incluso después de que la instancia ha sido creada.
# Esto es diferente de otros lenguajes de programación orientada a objetos, donde los atributos de una instancia deben ser definidos en la clase antes de que la instancia sea creada.
# En Python, puedes crear atributos de instancia simplemente asignando un valor a un nombre de atributo en la instancia.
# Esto se hace utilizando la sintaxis: instancia.nombre_atributo = valor.
# Esto crea un nuevo atributo en la instancia y le asigna el valor especificado.
# En el siguiente ejemplo, se crea una clase Usuario y luego se crea una instancia de la clase.
# Luego, se agrega un atributo nombre a la instancia y se imprime el valor del atributo.
# En este caso, el atributo nombre no está definido en la clase Usuario, pero se puede agregar a la instancia de la clase.
"""class Usuario:
    pass

usuario = Usuario()
print (usuario.__dict__) #No se ha creado ningún atributo
usuario.nombre = "Juan"
print(usuario.nombre)  
print (usuario.__dict__)# Salida: aparece el atributo nombre en el diccionario de atributos de la instancia

"""

class Usuario:
    def __new__(cls):
        print("Este es el método __new__ es el primero que se ejecuta")
        return super().__new__(cls)
    
    def __init__(self):
        print ("Este método es el segundo que se ejecuta")
        
    def __str__(self):
        return "Este es el método __str__ que se imprime al imprimir la instancia"
    
    def __getattr__(self, name):
        return "No se encuentra el atributo " + name    
    
usuario = Usuario()
print(usuario) # Salida: Este es el método __str__ que se imprime al imprimir la instancia

print (usuario.apellido) # Salida: Este es el método __getattribute__ lanza el mensaje que NO se encuentra el atributo apellido