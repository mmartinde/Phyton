#https://youtu.be/ZD-E0EX-4KM?si=iqCsIYs0PSrQXAp7

#Atributos y métodos
#Los atributos son variables que pertenecen a una clase y representan las propiedades o características de los objetos de esa clase. Los métodos son funciones que pertenecen a una clase y representan el comportamiento o las acciones que pueden realizar los objetos de esa clase.
#Los atributos y métodos se definen dentro de la clase y se accede a ellos utilizando la palabra clave self, que hace referencia al objeto actual.
#Los atributos y métodos pueden ser públicos, protegidos o privados. Los atributos y métodos públicos son accesibles desde fuera de la clase, los protegidos son accesibles solo desde dentro de la clase y sus subclases, y los privados son accesibles solo desde dentro de la clase.
#Los atributos y métodos públicos se definen sin un guion bajo al principio, los protegidos se definen con un guion bajo al principio y los privados se definen con dos guiones bajos al principio.
#Los atributos y métodos públicos son accesibles desde fuera de la clase, los protegidos son accesibles solo desde dentro de la clase y sus subclases, y los privados son accesibles solo desde dentro de la clase.
#Los atributos y métodos públicos se definen sin un guion bajo al principio, los protegidos se definen con un guion bajo al principio y los privados se definen con dos guiones bajos al principio.


class Lapiz: #Definimos la clase Lapiz
    #Atributos de la clase  
    color = 'Violeta'
    marca = 'Faber Castell'
    contiene_borra = False
    usa_grafito = True
    
    #Metodos de la clase
    def escribir(self): #Metodo para escribir
        print('Escribiendo con el lapiz')
    
    def borrar(self): #Metodo para borrar
        if self.es_valido_para_borrar():
            print('Borrando con el lapiz')
        else:
            print('No se puede borrar con el lapiz')
    
    def afilar(self): #Metodo para afilar
        print('Afilando el lapiz')
    
    def es_valido_para_borrar(self):
        return self.contiene_borra

lapiz_generico = Lapiz() #Este es un objeto de la clase Lapiz
lapiz_generico.escribir() #Llamamos al metodo escribir
lapiz_generico.borrar() #Llamamos al metodo borrar
lapiz_generico.contiene_borra = True #Cambiamos el atributo contiene_borra
lapiz_generico.borrar() #Llamamos al metodo borrar∫