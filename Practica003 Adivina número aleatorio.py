#vamos a jugar a que el usuario adivine el numero que estoy pensado entre 1 y 10
#me creo el numero secreto fijo que hay que averiguar
import random
numero_secreto = random.randint(1, 10)
#pongo el núemro de intentos a 1
intento = 1

#Pregunto el nombre y saludo
nombre = input("Hola, ¿cual es tu nombre? --> ")
print("Hola "+nombre)

#cuento loq ue hace el juego
print("Vamos a jugar!!!!  A ver si adivinas el número que estoy pensado entre 1 y 10")
print("TE voy a dar 3 intentos")

#pregunto si quiere jugar
apetece = input("¿Te apetece jugar? ( S/N )-->")

#si le apetece jugar vamos con los intentos
if apetece !="S" and apetece!="s" and apetece != "N" and apetece !="n":
    print("Por favor introduce una respuesta valida:")
    print ("Si quieres jugar introduce S o s , si no quieres jugar introduce N o n. Gracias.")

    #pongo apetece igual a n para que tenga un valor correcto y pueda continuar
    apetece="N"
else:
    #coimpruebo que aptece jugar para continuar
    if apetece =="S" or apetece == "s":

        #Mientras intentos sea menor o igual a 3 permito jugar, sino acaba el juego
        while intento <= 3:

            #indico por que intento vamos
            print("vamos con el intento numero " + str(intento))

            #utilizo try except par comprobar que no hay error
            try:
                #pregunto el número
                numero=int(input("¿Que número crees que estoy pensando (entre 1 y 10)? --> "))

                #compruebo que el valor está entre 1 y 10, que es lo que pedimos
                if intento < 1 or intento > 10:
                    print("Por favor, introduce un número válido entre 1 y 10.")

                #si el valor no es númerico salta error
            except ValueError:
                print("Introduce un valor entre 1 y 10")
            else:
                #compruebo si acierta el numero
                if numero_secreto == numero:
                    print("ENHORABUENA!!!! Eres una maquina, has acertado")

                    #pongo intento a 4 para que termine el programa
                    intento = 4
                    #pongo apetece a n para que acabe el progama
                    apetece="n"
                else:
                    #si falla le pongo mensaje y sumo 1 a intento
                    print("Lo siento, ese no es el número.")
                    intento = intento +1
    else:
        #como no quiere jugar acaba el programa
        print("Pues nada, no jugamos hoy")
print("")
#me despido amablemente
print("Espero verte por aquí pronto "+nombre)