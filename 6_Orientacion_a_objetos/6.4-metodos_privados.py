#https://youtu.be/ciU3D6PGN80?si=SLyBacFGuE9mjLks

#Metodos privados
#Los metodos privados son aquellos que no se pueden acceder desde fuera de la clase
#Se definen con un guion bajo al inicio del nombre del metodo
#En este caso el atributo password es privado y no se puede acceder desde fuera de la clase
#De la misma manera el metodo generar_password es privado y no se puede acceder desde fuera de la clase
#Para poder acceder al password desde fuera de la clase se define un metodo publico get_password



class Usuario:
    def __init__(self, username,password, email):
        self.username = username
        self.__password = self.__generar_password (password) #Atributo Privado; el password se genera con el metodo privado generar_password 
        self.email = email
    
    def __generar_password(self,password): #Se define el metodo privado con un guion bajo al inicio del nombre del metodo
        return password.upper()   
    
    def get_password(self): #Metodo publico para acceder al password
        return self.__password
    
    
        
eduardo = Usuario('eduardo', 'pasword1234', 'eduardo@email.com')
print(eduardo.username)
print(eduardo.get_password())
print(eduardo.email)