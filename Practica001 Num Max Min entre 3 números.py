#Vamos a averiguar el núermo mayor y menor entre 3 opciones que no de el oeprador

#Pregunto el nombre del jugador
nombre= input(str("Hola, Bienvenid@: ¿Cuál es tu nombre? --> "))
print("Bienvenid@ "+nombre)

#Explico el juego
print("VAmos a jugar a un juego sencillo. Tienes que darme 3 números entre 1 y 100 ")
print("y yo te diré cual es el mayor y el menor de esos números")

#Pido los 3 numeros
numero1=int(input("Dime el primer número, por favor --> "))
numero2=int(input("Muy Bien. Ahroa dime el segundo, por favor --> "))
numero3=int(input("Perfecto, Por último dime el tercer número --> "))

#muestro los resultados
print("Una vez comnprobados los numeros.....")
print("el número más grande entre {}, {} y {} es {} y el más pequeño es {}".format(numero1, numero2, numero3,
                                                                                     max(numero1, numero2, numero3),
                                                                                     min(numero1, numero2, numero3)))
print("Muchas gracias por participar y hasta pronto")