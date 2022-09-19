limite = int(input("Ingresa el limite: "))
n=0
e=0
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

while n < limite:
    e += 1/factorial(n)
    n += 1

print("e: ",e)