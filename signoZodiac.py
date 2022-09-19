#Input
dia = int(input("Hola!\nDame tu dia de nacimiento: "))
mes = int(input("Ahora tu mes: "))
meses = [1,2,3,4,5,6,7,8,9,10]
signo = ""
#Logic
if(mes == 1): #Enero
    if(dia <= 20):
        signo = "Capricornio"
    else:
        signo = "Acuario"
if(mes == 2):#Febrero
    if(dia <= 19):
        signo = "Acuario"
    else:
        signo = "Piscis"
if(mes == 3):#Marzo
    if(dia <= 20):
        signo = "Piscis"
    else:
        signo = "Aries"
if(mes == 4):#Abril
    if(dia <= 20):
        signo = "Aries"
    else:
        signo = "Tauro"
if(mes == 5):#Mayo
    if(dia <= 20):
        signo = "Tauro"
    else:
        signo = "Geminis"
if(mes == 6):#Junio
    if(dia <= 21):
        signo = "Geminis"
    else:
        signo = "Cancer"
if(mes == 7):#Julio
   if(dia <= 22):
       signo = "Cancer"
   else:
       signo = "Leo"
if(mes == 8):#Agosto
   if(dia <= 23):
       signo = "Leo"
   else:
       signo = "Virgo"
if(mes == 9):#Septiembre
    if(dia <= 22):
        signo = "Virgo"
    else:
        signo = "Libra"
if(mes == 10):#Octubre
   if(dia <= 22):
       signo = "Libra"
   else:
       signo = "Escorpio"
if(mes == 11):#Noviembre
   if(dia <= 22):
       signo = "Escorpio"
   else:
       signo = "Sagitario"
if(mes == 12):#Diciembre
    if(dia <= 21):
        signo = "Sagitario"
    else:                 
        signo = "Capricornio"
#Out
print("Muy bien!\nTu signo zodiacal es: ",signo)