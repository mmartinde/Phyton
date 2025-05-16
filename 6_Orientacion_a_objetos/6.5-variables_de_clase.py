#https://youtu.be/0n1GSt8ZFJ8?si=ygAuUVJV-fH8xwbg

#Variables de clase
#Las variables de clase son aquellas que se definen dentro de la clase y son compartidas por todas las instancias de la clase
#Se definen fuera del constructor __init__
#En este caso la variable de clase contador es compartida por todas las instancias de la clase Usuario
#Cada vez que se crea una nueva instancia de la clase Usuario se incrementa el contador
#El contador se puede acceder desde fuera de la clase con el nombre de la clase

class Circulo:
    
    _pi = 3.1416 #Variable de clase; se define fuera del constructor __init__, por convencion se define con un guion bajo al inicio del nombre de la variable
    
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return self._pi * (self.radio ** 2)
    
    def perimetro(self):
        return 2 * self._pi * self.radio
    
    def __str__(self):
        return f'Circulo de radio {self.radio} y area {self.area()} y perimetro {self.perimetro()}'
    
    def __repr__(self):
        return f'Circulo({self.radio})'
#El __dict__ es un atributo de las clases y objetos en Python que devuelve un diccionario que contiene todos los atributos y métodos de la clase o del objeto
#El __dict__ de la clase Circulo contiene la variable de clase pi y los metodos area, perimetro, __str__ y __repr__   
        
        

circulo_uno = Circulo(4)
circulo_dos = Circulo(3)


print(f'El valor de la variable de clase pi es: {circulo_uno._pi}') #Imprime el valor de la variable de clase pi

print(f'El diccionario de la instancia cirulo uno es: {circulo_uno.__dict__}') #Imprime el diccionario de la instancia circulo_uno


print(circulo_uno) #Imprime el resultado del metodo __str__
print(circulo_dos) #Imprime el resultado del metodo __str__ 