class Personaje:

    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self._vida = vida  # privado
        self.ataque = ataque

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self._vida = 0  # evita vida negativa
        else:
            self._vida = valor


    def mostrar(self):
        print(f"{self.nombre} vida: {self._vida}")

    def atacar(self):
        if self._vida > 0:
            danio = self.ataque
    
    def recibir_danio(self,_vida, danio):
        self._vida = _vida - danio
        if self._vida <= 0:
            self.morir() 

    def estoy_vivo(self):
        if self._vida <= 0:
            print("estoy muerto")
        else:
            print(f"estoy vivo, {self._vida} vida")

    def morir(self):
        self._vida = 0
        print(f"{self.nombre} mori")