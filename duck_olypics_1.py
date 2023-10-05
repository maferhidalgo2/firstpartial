def suma(a,b):
  x = a + b
  return x

def resta(a,b):
  x = a - b
  return x 

print("Dame el primer numero :")
a = int(input())
print ("Dame el segundo número")
b = int(input())
print("La suma da",suma(a,b),"y que la resta da",resta(a,b))


def multiplicacion(a,b):
  x = a*b
  return x

def division(a,b):
  x = a/b
  return x

print("Dame el primer numero :")
a = int(input())
print ("Dame el segundo número")
b = int(input())
print("La multiplicacion da",multiplicacion(a,b),"y que la division da",division(a,b))


def multiplicacion(k):
  x=k*1000
  return x

print("Dime los kilometros que has recorrido")
k=int(input())
print("La cantidad de kilometros es",multiplicacion(k))

def triangle_era(b,h):
  x=(b*h)/2
  return x

print("Dime la base del triangulo")
b=int(input())
print("Dime la area del triangulo")
h=int(input())
print("La base del triangulo es",triangle_era(b,h))
