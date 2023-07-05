import math
print('Ecuación cuadrática por fórmula general')
datoA=float(input("ingresa el valor de a \n"))
datoB=float(input("ingresa el valor de b \n"))
datoC=float(input("ingresa el Valor de c \n"))

if ((datoB**2)-(4*datoA*datoB))<0:
    print("no se puede realizar por que no se puede sacar raiz de un numero negativo")
else:
 x1=(-datoB+(math.sqrt(((datoB)**2)-(4*datoA*datoC))))/(2*datoA)
 x2=(-datoB-(math.sqrt(((datoB)**2)-(4*datoA*datoC))))/(2*datoA)
 print("resultado x1=",x1, "Resultado x2=",x2)