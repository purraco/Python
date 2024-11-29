"""#Vamos a ayudar a elegir movil teniendo en cuenta el sistema operativo (ios o android) si tienes o no dinero
y si te importa o no la cámara"""

#creo una variable con el título para darle formato
titulo= "* Voy a intentar ayudarte a elegir un móvil nuevo con unas sencillas preguntas *"

#para no repetir la pregunta en el código creo una variable
tienes_dinero = "\n¿Tienes dinero? (S/N) --> "

#para no repetir el inicio de todas las respuesta. Esto es por practicar las variables
incio_respuesta = ("Pues te aconsejo un ")

#creo una variable para controlar que se repita si quiere que le ayude
ver_menu_aconsejar = 1

#creo variable para controlar que se repita sistema operativo
ver_sistema_operativo = 1

#formateo e imprimo el titulo como me interesa
print("\n"+ "*"*len(titulo)+"\n"+titulo+"\n"+"*"*len(titulo))

#mientras ver_menu_aconsejar sea igual a 1 meustro el menú. Cuando no quiera ayuda
#lo pongo a 0 para que no aparezca el menú
while ver_menu_aconsejar == 1:
    aconsejar = input ("\n¿Quiéres que intente ayudarte? (S/N)--> ")
    if aconsejar.upper()== "N":
        print("\nGracias y un saludo\n")
        #pongo a 0 ver_menu_aconsejar para que deje de mostar la prgunta y termine el programa
        ver_menu_aconsejar = 0
    elif aconsejar.upper()== "S":
        #mientras ver_sistema_operaticvo igual a 1 muestro este menú
        ver_sistema_operativo = 1
        while ver_sistema_operativo == 1:
            sistema_operativo = input("\n¿Que sistema operativo prefieres?\n"
                                      "A. Android\n"
                                      "B. IOS\n"
                                      "Elije una opción --> ")
            if sistema_operativo.upper() == "A":
                dinero = str(input(tienes_dinero))
                if dinero.upper() == "N":
                    print(incio_respuesta + "Android Chino de 100 euros")
                elif dinero.upper() == "S":
                        importa_camara = input("¿Te importa la calidad de la cámara del móvil (S/N) --> ?")
                        if importa_camara.upper() == "S":
                            print(incio_respuesta + "google Pixel SuperCámara")

                        elif importa_camara.upper() == "N":
                            print(incio_respuesta + "Android calidad-precio")
                #pongo a 0 ver_sistema_operativo para que no se repita el menú
                ver_sistema_operativo = 0
            elif sistema_operativo.upper() == "B":
                dinero = input(tienes_dinero)
                if dinero.upper() == "N":
                    print(incio_respuesta + "iphone de segunda mano")
                elif dinero.upper() == "S":
                    print(incio_respuesta + "iphone Ultra Pro Max")
                # pongo a 0 ver_sistema_operativo para que no se repita el menú
                ver_sistema_operativo = 0
            else:
                print("Por favor, introduce una opción correcta")
    else:
        print("Por favor introduce una opción correcta")