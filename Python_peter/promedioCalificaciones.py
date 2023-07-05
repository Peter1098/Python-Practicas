#Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.
print("ingresa las calificaciones de tus practicas")

practica1=float(input("ingresa calificacion Practica1 \n"))
practica2=float(input("ingresa calificacion Practica2 \n"))
practica3=float(input("ingresa calificacion Practica3 \n"))

print("Ingresa las calificaciones de examen parcial y final")

examenParcial=float(input("ingresa tu calificacion de examen parcial \n"))
examenFinal=float(input("ingresa tu calificacion de examen final \n"))

promedioPractica=(practica1+practica2+practica3)/3
promedio=(promedioPractica+(2*examenParcial)+(3*examenFinal))/6

print("tu promedio es=",promedio)