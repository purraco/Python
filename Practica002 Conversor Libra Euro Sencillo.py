#Vamos a mostar el cambio Libras a Euros

print("Hola, bienvenido: Vamos a aplicar el cambio a la moneda en Libras para pasarlo a Euros.")
print("")

#Preguntamos cuantas libras quiere cambiar a euros
libras = float(input("Por favor, indicame la cantidad en libras --> "))

#Preguntamos el tipo de cambio actual libra - Euro
print("Ten en cuenta que el separador de decimales es el . (punto) y no la , (coma)")
cambio = float(input("Por favor, indica el tipo de cambio de una libra en euros --> "))

#realizamos el cambio
euros = libras*cambio

print("La cantidad que recibiras por tus {} libras serán {} euros".format(libras, euros))
print("")
print("Espero haberte sido de ayuda. Hasta pronto.")