#https://youtu.be/QP4vJg8q-ZA?si=revx5p6OmfHR5uWw

#Metodos estaticos
#Los metodos estaticos son metodos que no necesitan acceder a la instancia de la clase
#Se definen con el decorador @staticmethod
#Se pueden llamar sin necesidad de crear una instancia de la clase
#Los metodos estaticos son utiles para definir metodos que no necesitan acceder a la instancia de la clase
#Los metodos estaticos no pueden acceder a los atributos de la clase ni a los metodos de la clase


class Circulo:
    
    _pi = 3.1416 #Atributo de clase, se puede acceder desde la instancia de la clase o desde la clase
    
    def __init__(self, radio):
        self.radio = radio #Atributo de instancia, se accede desde la instancia de la clase
    
    @staticmethod
    def area(radio): #Metodo estatico, no necesita acceder a la instancia de la clase
        return Circulo._pi * (radio ** 2) #Devuelve el area del circulo
    
    @classmethod
    def area_clase(cls, radio): #Metodo de clase, necesita acceder a la clase
        return cls._pi * (radio ** 2) #Devuelve el area del circulo
    
    def area_instancia(self): #Metodo de instancia, necesita acceder a la instancia de la clase
        return self._pi * (self.radio ** 2) #Devuelve el area del circulo
    
circulo_uno = Circulo(5) #Crea una instancia de la clase Circulo
print(f'El area del circulo es {circulo_uno.area_instancia()}') #Imprime el area del circulo
print(f'El area del circulo es {Circulo.area(5)}') #Imprime el area del circulo
print(f'El area del circulo es {Circulo.area_clase(5)}') #Imprime el area del circulo