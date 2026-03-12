from Personaje import Personaje

# hereda de Personaje
class Guerrero(Personaje):

    def __init__(self, nombre, vida, ataque, fuerza):
        super().__init__(nombre, vida, ataque)
        self.fuerza = fuerza

    # sobrescribe el metodo atacar
    def atacar(self):
        if self._vida > 0:
            danio = self.ataque + self.fuerza
            return f"{self.nombre} ataca con espada y causa {danio} de daño"
