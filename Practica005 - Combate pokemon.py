#vamos a representar un combate entre 2 peronajes de Pokemon. Por un lado el ordenador controla a Pikachu y el jugador
#controla a Squirtle

#creamos variable ocn el titulo para darle formato
titulo = "** COMBATE POKEMON -- Pikachu contra Squirtle **"
#imprimo el título con formato
print("\n" + "*" * len(titulo) + "\n" + titulo + "\n" + "*" * len(titulo)+ "\n")

#importo la funcion random para el ataque de pikachu
import random

#creo variable para no repetir el texto de pulse para continuar
pulsa_para_continuar = "\nPulsa una ENTER/INTRO para continuar...\n"

#creo una variable para la vida de cada personaje
vida_pikachu = 80
vida_squirtle = 90

#creo variables para los puntos de daño de los ataques de pikachu y squirtle
#De esta forma si en un futuro modifico puntos de daño lo hago en la variable y no busco las fórmualas
p_bola_voltio = 10
p_onda_trueno = 11
s_placaje = 10
s_pistola_agua = 12
s_burbuja = 9

#Explico el juego, componentes y dinámica
print("Te reto a un combate entre personajes Pokemon. "
      "En este caso yo controlo a Pikachu y tu vas a controla a Squirtle.\n"
      "Haremos 1 turno de ataque cada uno."
      "Mis ataques de Pikachu son Bola Voltio y Onda Trueno. Tus ataques serán Placaje, Pistola de Agua y Burbuja\n"
      "\nComo el juego es mío, empiezo atacando yo\n")
print("Combatimos mientras los dos tengamos vida")
input(pulsa_para_continuar)

while vida_pikachu > 0 and vida_squirtle > 0:

    #ataca pikachu
    ataque_pikachu = int(random.randint(1,2))

    #compruebo el ataque que ha salido con el número aleatorio
    if ataque_pikachu == 1:
        # si el número aleatorio es 1 infringe ataque bola voltio
        print("Pikachu te lanza un ataque Bola Voltio y te infringe {} puntos de daño".format(p_bola_voltio))
        vida_squirtle -= p_bola_voltio
    else:
        # si el número aleatorio es 1 infringe ataque bonda trueno
        print("Pikachu te lanza un ataque ONDA TRUENO y te infringe {} puntos de daño".format(p_onda_trueno))
        vida_squirtle -= p_onda_trueno

    #Compruebo si la vida ha salido negativo. en ese caso la pongo a 0, porque menos de cero vida no puede tener
    if vida_squirtle <0:
        vida_squirtle=0

    #muestro la vida que le queda al jugador
    print("Te quedan {} de puntos de vida".format(vida_squirtle))

    #le pido que pulse enter para continuar para que le de tiempo a leer.
    #Seguro que hay mejor manera de hacerlo, pero no se como.
    input(pulsa_para_continuar)

    #compruebo si ya ha ganado pikachu y me ha quitado toda la vida, termino el bucle while para que no me vuelva
    # a pedir que ataque el jugador
    if vida_squirtle == 0:
        break

    #le cuento que le toca y si no pone opción correcta, pierde el turno
    print("\nAhora es tu turno para atacar. Puedes elegir entre los 3 ataques que tienes disponibles.\n"
          "Si no pones un número correcto, pierdes tu ataque, por lo que ten cuidado y afina el tiro\n")
    elegir_ataque_squirtle = int(input("Elige que ataque quires hacer\n"
                                       "1- Placaje\n"
                                       "2- Pistola de agua\n"
                                       "3- Burbuja\n"
                                       "Tu opción --> "))
    if elegir_ataque_squirtle == 1:
        print("Perfecto!!!! Le lanzas un ataque PLACAJE y le infringes {} puntos de daño a Pikachu".format(s_placaje))
        vida_pikachu -=s_placaje
    elif elegir_ataque_squirtle == 2:
        print("Maravilloso!!!! Ataque PISTOLA DE AGUA e infringes {} puntos de daño a Pikachu".format(s_pistola_agua))
        vida_pikachu -=s_pistola_agua
    elif elegir_ataque_squirtle == 3:
        print("No está mal. Le lanzas un ataque Burbuja y le infringes {} puntos de daño a Pikachu".format(s_burbuja))
        vida_pikachu -=s_burbuja
    else:
        print("pierdes el turno")
    #Compruebo si la vida ha salido negativo. en ese caso la pongo a 0, porque menos de cero vida no puede tener
    if vida_pikachu <0:
        vida_pikachu=0
    print("Le quedan a Pikachu {} puntos de vida\n".format(vida_pikachu))

    print("Resumiendo como va la partida:\n"
          "Te quedan {} puntos de vida".format(vida_squirtle))
    print("Le quedan a pikachu {} puntos de vida".format(vida_pikachu))

    #le pido que pulse enter para continuar para que le de tiempo a leer.
    #Seguro que hay mejor manera de hacerlo, pero no se como.
    input(pulsa_para_continuar)

if vida_pikachu == 0:
    print("ENHORABUENA!!!! Has dado pal'pelo a Pikachu y le has ganado.")
if vida_squirtle == 0:
    print("Lo siento, pero pikachu te ha dado pal'pelo y has perdido.")

print("\nEspero volver a verte pronto")