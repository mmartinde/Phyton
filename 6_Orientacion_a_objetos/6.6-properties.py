#https://youtu.be/CIhs2XSM66U?si=aapgsV0ISFTNAg0l

#Properties
#Las propiedades son una forma de acceder a los atributos de una clase de forma controlada
#Se definen con el decorador @property
#Se pueden definir propiedades de solo lectura, de solo escritura o de lectura y escritura
#Las propiedades de solo lectura se definen con el decorador @property
#Las propiedades de solo escritura se definen con el decorador @nombre_propiedad.setter
#Las propiedades de lectura y escritura se definen con el decorador @nombre_propiedad.setter y @property
#Las propiedades son una forma de encapsular los atributos de una clase y controlar su acceso

class Usuario:
    
    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generar_password(password) #El __password es un atributo privado, no se puede acceder desde fuera de la clase
        self.email = email
        
    def __generar_password(self, password): #Es un metodo privado, no se puede acceder desde fuera de la clase
        return password[::-1] #Devuelve el password al reves, para simular un hash
    
    def get_password(self):
        return self.__password
    
    @property #Decorador para definir una propiedad de solo lectura
    def password(self):
        return self.__password    
    
    @password.setter #Decorador para definir una propiedad de solo escritura
    def password(self, nuevo_password):
        self.__password = self.__generar_password(nuevo_password) #Genera un nuevo password al reves:
        
        
maguila = Usuario('Gorila', 'Gorila1234', 'maguila@gorila.es')

print(f'El password antes modificar es {maguila.password}') #Imprime el password al reves
maguila.password = 'NuevoGorila1234' #Cambia el password 
print(f'El password modificado es {maguila.password}')     #Imprime el password modificado al reves