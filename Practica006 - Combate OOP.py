"""
Si te parece bien, me gustaría colaborar en tu proyecto para poder aprender mutuamente tanto a colaborar
como a utilizar github correctamente, ya que necesito practicar.
Voy a tratar de sugerir algún cambio en el código.
1- El primer cambio que te sugiero es utilizar Clases y Objetos para poder ir escalando poco a poco.
2- El segundo cambio es utilizar los fstrings en vez del .format() para pasar variables a Strings
"""

# Importamos la funcion random para el ataque del Pokemon Oponente
# Pikachu en este caso
import random

# Creamos la clase Ataque con los atributos nombre que guardará el nombre del ataque
# y poder que guardará los puntos de daño de los ataques
class Ataque:
    def __init__(self, nombre: str, poder: int) -> None:
        self.nombre = nombre
        self.poder = poder

# Creamos la clase Pokemon con los atributos nombre, vida y ataques
# y los métodos para agregar, elegir y recibir ataques
class Pokemon:
    def __init__(self, nombre: str, vida: int) -> None:
        self.nombre = nombre
        self.vida = vida
        self.ataques = {}

    def agregar_ataque(self, nombre: str, poder: int):
        self.ataques[nombre] = Ataque(nombre, poder)

    def elegir_ataque(self, nombre_ataque: str):
        return self.ataques.get(nombre_ataque)

    def recibir_ataque(self, ataque: Ataque):
        self.vida -= ataque.poder
        if self.vida < 0:
            self.vida = 0

# Creamos la clase Combate que contendrá el Pokemon del jugador y del oponente
# y los turnos de ataque de jugador y oponente. Empezará atacando el oponente.
class Combate:
    def __init__(self, jugador: Pokemon, oponente: Pokemon) -> None:
        self.jugador = jugador
        self.oponente = oponente
        self.historico = []
        self.pulsa_para_continuar = "\nPulsa ENTER/INTRO para continuar...\n"

    def turno_atacar_oponente(self):
        ataque_oponente = random.choice(list(self.oponente.ataques.values()))
        print(f"{self.oponente.nombre} usa {ataque_oponente.nombre} y causa {ataque_oponente.poder} puntos de daño.")
        self.jugador.recibir_ataque(ataque_oponente)
        print(f"Te quedan {self.jugador.vida} puntos de vida.")

    def turno_atacar_jugador(self):
        print("\nAhora es tu turno para atacar. Puedes elegir entre los 3 ataques que tienes disponibles.")
        elegir_ataque = int(input("Elige que ataque quieres hacer\n"
                                  "1- Placaje\n"
                                  "2- Pistola de agua\n"
                                  "3- Burbuja\n"
                                  "Tu opción --> "))
        ataques_posibles = list(self.jugador.ataques.values())
        if 1 <= elegir_ataque <= len(ataques_posibles):
            ataque_jugador = ataques_posibles[elegir_ataque - 1]
            print(f"¡Lanzas un ataque {ataque_jugador.nombre} y causas {ataque_jugador.poder} puntos de daño a {self.oponente.nombre}.")
            self.oponente.recibir_ataque(ataque_jugador)
            print(f"A {self.oponente.nombre} le quedan {self.oponente.vida} puntos de vida.")
        else:
            print("¡Has perdido el turno! No elegiste un ataque válido.")

# Explicación del juego, componentes y dinámica
    def jugar(self):
        print("** COMBATE POKEMON -- Pikachu contra Squirtle **")
        print("Te reto a un combate entre personajes Pokemon. Yo controlo a Pikachu y tú a Squirtle.")
        print("Combatimos mientras ambos tengamos vida.\n")
        input(self.pulsa_para_continuar)

        while self.jugador.vida > 0 and self.oponente.vida > 0:
            self.turno_atacar_oponente()

            if self.jugador.vida == 0:
                break

            input(self.pulsa_para_continuar)
            self.turno_atacar_jugador()

            if self.oponente.vida == 0:
                break

            input(self.pulsa_para_continuar)

            print("\nResumen del combate:")
            print(f"Te quedan {self.jugador.vida} puntos de vida.")
            print(f"A {self.oponente.nombre} le quedan {self.oponente.vida} puntos de vida.")
        
        if self.jugador.vida == 0:
            print("\nLo siento, pero Pikachu te ha ganado.")
        if self.oponente.vida == 0:
            print("\n¡ENHORABUENA! Has derrotado a Pikachu.")

        print("\nEspero volver a verte pronto.")

# Creamos ambos Pokémon
pikachu = Pokemon("Pikachu", 80)
pikachu.agregar_ataque("Bola Voltio", 10)
pikachu.agregar_ataque("Onda Trueno", 11)

squirtle = Pokemon("Squirtle", 90)
squirtle.agregar_ataque("Placaje", 10)
squirtle.agregar_ataque("Pistola de agua", 12)
squirtle.agregar_ataque("Burbuja", 9)

# Creamos el Combate:
# El primer Pokemon que pasamos como argumento es el del jugador y el segundo el del oponente
combate = Combate(squirtle, pikachu)
combate.jugar()

"""
Como primera aportación creo que es suficiente para ver si te parece bien continuar por esta línea de colaboración.

Como siguientes pasos sugiero:
1- Cambiar los sitios donde aparecen Pikachu y Squirtle escritos "a mano" por una llamada al Pokemon.nombre que corresponda
    por ejemplo en las líneas 72, 73, 96, 98
2- Cambiar los valores escritos "a mano" en la función turno_atacar_jugador() por una llamada a los mismos
"""