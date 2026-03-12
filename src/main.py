from Personaje import Personaje
from Mago import Mago
from Guerrero import Guerrero


# polimorfismo
# def mostrar_ataque(personaje):
#     print(personaje.atacar())
def main():

    personajes = [
        Guerrero("Ares", 120, 20,10),
        Mago("Merlin", 80, 50,20),
        Guerrero("Alan", 100, 20,10),
        Mago("Harry", 70, 30,5)
    ]

    for personaje in personajes:
        print(personaje.atacar())

if __name__ == "__main__":
    main()