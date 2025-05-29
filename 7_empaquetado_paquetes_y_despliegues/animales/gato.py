class Gato:
    def __init__(self, nombre):
        self.nombre = nombre

    def maullar(self):
        return f"{self.nombre} dice: ¡Miau!"
    def dormir(self):
        return f"{self.nombre} está durmiendo."
    def comer(self):
        return f"{self.nombre} está comiendo."
    def jugar(self):
        return f"{self.nombre} está jugando."