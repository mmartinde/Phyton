#https://youtu.be/vdz9HGfFguc?si=kGZIGe-dmU_VOHEd

#Clases y objetos
#las clases son plantillas para crear objetos. Un objeto es una instancia de una clase. Las clases pueden contener atributos (variables) y métodos (funciones) que definen el comportamiento y las propiedades de los objetos.
#Las clases son una forma de organizar y estructurar el código, lo que facilita la reutilización y el mantenimiento.
#Las clases se definen utilizando la palabra clave class, seguida del nombre de la clase y dos puntos. El cuerpo de la clase contiene los atributos y métodos.
#Los atributos se definen dentro de la clase y se inicializan en el método especial __init__, que se llama automáticamente cuando se crea un nuevo objeto de la clase. Los métodos se definen como funciones dentro de la clase y pueden acceder a los atributos de la clase utilizando la palabra clave self.
#Los objetos se crean instanciando la clase, lo que significa que se llama al constructor de la clase (el método __init__) para crear una nueva instancia de la clase.
#Los objetos pueden tener diferentes valores para sus atributos, lo que permite crear múltiples instancias de la misma clase con diferentes propiedades.
#Las clases pueden heredar de otras clases, lo que significa que pueden heredar atributos y métodos de una clase base. Esto permite crear jerarquías de clases y reutilizar código.
#La herencia se define utilizando la sintaxis class NombreClase(Herencia), donde Herencia es la clase base de la que se hereda.
#La encapsulación es el proceso de ocultar los detalles internos de una clase y exponer solo lo necesario. Esto se logra utilizando modificadores de acceso, como público, protegido y privado.
#La encapsulación ayuda a proteger los datos y a mantener la integridad de los objetos.
#La polimorfismo es la capacidad de un objeto de tomar muchas formas. En Python, esto se logra mediante la sobrecarga de métodos y la sobrecarga de operadores.
#El polimorfismo permite que diferentes clases implementen el mismo método de diferentes maneras, lo que facilita la reutilización del código y la creación de interfaces comunes.
#La modularidad es el proceso de dividir un programa en módulos o componentes más pequeños y manejables. Esto facilita la organización y el mantenimiento del código.
#La modularidad se logra utilizando funciones, clases y módulos. Los módulos son archivos de Python que contienen definiciones de funciones, clases y variables. Se pueden importar en otros módulos o scripts para reutilizar el código.
#La modularidad permite crear programas más grandes y complejos sin perder la claridad y la organización del código.
#La programación orientada a objetos es un paradigma de programación que utiliza clases y objetos para organizar el código. Permite crear programas más estructurados, reutilizables y mantenibles.
#La programación orientada a objetos se basa en cuatro principios fundamentales: encapsulación, herencia, polimorfismo y modularidad.
#La programación orientada a objetos es un enfoque poderoso y flexible para la programación, y es ampliamente utilizado en el desarrollo de software moderno.
#La programación orientada a objetos es un paradigma de programación que utiliza clases y objetos para organizar el código. Permite crear programas más estructurados, reutilizables y mantenibles.
#La programación orientada a objetos se basa en cuatro principios fundamentales: encapsulación, herencia, polimorfismo y modularidad.
#La programación orientada a objetos es un enfoque poderoso y flexible para la programación, y es ampliamente utilizado en el desarrollo de software moderno.
#La programación orientada a objetos es un paradigma de programación que utiliza clases y objetos para organizar el código. Permite crear programas más estructurados, reutilizables y mantenibles.
#La programación orientada a objetos se basa en cuatro principios fundamentales: encapsulación, herencia, polimorfismo y modularidad.
#La programación orientada a objetos es un enfoque poderoso y flexible para la programación, y es ampliamente utilizado en el desarrollo de software moderno.
#La programación orientada a objetos es un paradigma de programación que utiliza clases y objetos para organizar el código. Permite crear programas más estructurados, reutilizables y mantenibles.

class Lapiz: #Definimos la clase Lapiz
    #Atributos de la clase  
    color = 'Violeta'
    marca = 'Faber Castell'
    contiene_borra = False
    usa_grafito = True
    
lapiz_generico = Lapiz() #Este es un objeto de la clase Lapiz
print(lapiz_generico.color)
print(lapiz_generico.marca)
print(lapiz_generico.contiene_borra)
print(lapiz_generico.usa_grafito)
print(lapiz_generico.__dict__) #muestra los atributos del objeto
print(lapiz_generico.__class__) #muestra