#https://youtu.be/XTTwSkIPZIw?si=LyLuGmsBFVPmYbOm

#INIT
#Inicializamos el objeto lapiz_generico de la clase Lapiz
# y llamamos al metodo escribir

class Lapiz: #Definimos la clase Lapiz
    #Atributos de la clase  definiremos estos atributos en el constructor
    
    def __init__(self, color = "negro", marca ='Ni_idea', contiene_borrador = False, usa_grafito = True, tamano = 'normal', dureza = 'HB'): #Constructor de la clase, con los atributos que definimos y valores defaults, estos son opcionales pueden o no ponerse
        self.color = color
        self.marca = marca
        self.contiene_borra = contiene_borrador
        self.usa_grafito = usa_grafito
        self.tamano = tamano
        self.dureza = dureza
        
        
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

lapiz_generico = Lapiz('rojo', 'FaberCaster',True, True, 'normal', 'H2')  

lapiz_generico.escribir() #Llamamos al metodo escribir
lapiz_generico.borrar() #Llamamos al metodo borrar