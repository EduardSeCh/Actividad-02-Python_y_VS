
import math
from os import system
def areaCuadrado(base,altura):
    return base * altura;

def areaTriangulo(base,altura):
    return base * altura / 2;

def areaCirculo(radio):
    return math.pi * (radio * radio);
print("Que figura va a calcular?")
print("1.Cuadrado")
print("2.Triangulo")
print("3.Circulo")
res = int(input())
int(res) 
if(res==1):
    base = int(input("dame la base: "))
    altura = int(input("dame la altura: "))
    print(areaCuadrado(base,altura))
elif(res==2):
    base = int(input("dame la base: "))
    altura = int(input("dame la altura: "))
    print(areaTriangulo(base,altura))
elif(res==3):
    radio = int(input("dameel radio: "))
    print(areaCirculo(radio))
else:
    print("Dato no valido")
