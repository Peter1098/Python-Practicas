#Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:
#Te llamas: <nombre>
#Tu edad es: <edad>
#Eres: <sexo>
nombre=input("Ingresa tu numbre: \n")
edad=int(input("Ingresa tu edad:\n"))
sexo=input("ingresa tu sexo: \n")
 
print("Te llamas:<{}> \n Tu edad es:<{}> \n Eres:<{}>".format(nombre,edad,sexo)) 