from Personaje import Personaje

# hereda de Personaje
class Mago(Personaje):

    def __init__(self, nombre, vida, ataque, mana):
        super().__init__(nombre, vida,ataque)
        self.mana = mana

    # sobrescribe el metodo atacar
    def atacar(self):
        if self._vida > 0:
            danio = self.ataque + self.mana
        return f"{self.nombre} ataca con mana y causa {danio} de daño"