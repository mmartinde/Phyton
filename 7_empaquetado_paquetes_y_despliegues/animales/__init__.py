from .felinos import Gato
from .felinos import Leon

def creador_gatos(nombre):
    return Gato(nombre)

def creador_leones():
    return Leon()

#singleton
# Un singleton es una clase que solo puede tener una instancia.
# En Python, se puede implementar un singleton utilizando el patrón de diseño Singleton.
# Esto se puede hacer utilizando un decorador o una metaclase.
# Un singleton es útil cuando se necesita garantizar que una clase tenga solo una instancia y proporcionar un punto de acceso global a esa instancia.
# Un ejemplo de singleton en Python es la clase `Logger`, que se utiliza para registrar mensajes en un archivo de registro.


