#Escribir un programa que solicite al usuario un vocal en minuscula, 
#y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula,
# y al final, deben ser concatenadas ambas

vocal=input("ingrese una vocal en minuscula \n")
letra=input("ingrese una letra en MAYUSCULA \n")

vocal1=vocal.upper()
letra1=letra.lower()
print("Muestra vocal ahora en MAYUSCULA: {} \n muestra letra ahora en minuscula: {}".format(vocal1,letra1))