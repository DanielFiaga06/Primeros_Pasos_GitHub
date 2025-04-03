# Ejercicio 1

print("Hola, ya se imprimir frases")
print("\n")

# Ejercicio 2

print("597")
print()

# Ejercicio 3

print("8.5")
print()

# Ejercicio 4

print(1234+532)
print()

# Ejercicio 5

resta1, resta2 = 1234, 532
print(resta1-resta2)
print()

# Ejercicio 6

print(1234*532)
print()

# Ejercicio 7

print(1234/532)
print()

# Ejercicio 8

for i in range(1, 4):
    print(i)
print()

# Ejercicio 9

i = 1
while i <= 9:
    print(i)
    i +=1
print()

# Ejercicio 10

i = 1
while i <= 10000:
    print(i)
    i += 1
print()
# Ejercicio 11

for i in range(5,11):
    print(i)
print()  

# Ejercicio 12

for i in range(5,16):
    print(i)
print()

# Ejercicio 13

i = 5
while i <= 15000:
    print(i)
    i += 1
print()

# Ejercicio 14

palabra = "hola"
for _ in range(200):
    print(palabra)
print()

# Ejercicio 15

for i in range(1,31):
    print(i**2)
print()

# Ejercicio 16

producto = 1
for i in range(1,21):
    producto *= i
print(producto)
print()

# Ejercicio 17

suma = 0
i = 1
while i <= 100:
    suma += i**2
    i+= 1
print(suma)
print()

# Ejercicio 18

numero = int(input("Ingresa un numero entero: "))
suma = 0
for i in range(numero, numero + 100):
    suma += i
print("La suma de los 100 numeros siguientes es",suma)
print()

# Ejercicio 19

tipo_de_cambio = 1.1
euros = float(input("Ingresa la cantidad de euros: "))
dolares = euros * tipo_de_cambio
print(f"{euros} euros son equivalentes a {dolares} dolares.")
print()

# Ejercicio 20

altura = float(input("Ingresa la altura del rectangulo: "))
anchura = float(input("Ingresa la anchura del rectangulo: "))
area = altura * anchura
print(f"El area del rectangulo es",area,"unidades cuadradas")
print()

# Ejercicio 21

numero_1 = float(input("Ingresa el primer numero: "))
numero_2 = float(input("Ingresa el segundo numero: "))
if numero_1 > numero_2:
    print(f"El numero mayor es",numero_1,"y el numero menor es",numero_2)
elif numero_2 > numero_1:
    print(f"El numero mayor es",numero_2,"y el numero menor es",numero_1)
else:
    print("Ambos numeros son iguales")
print()

# Ejercicio 22

entero = int(input("Ingresa un numero entero: "))
print(f"Los números impares menores que",entero,"son:")
for i in range(1,entero,2):
    print(i)
print()

# Ejercicio 23

def euclides(a,b):
    while b !=0:
        a, b = b, a % b
    return a
num_1 = int(input("Ingresa el primer numero: "))
num_2 = int(input("Ingresa el segundo numero: "))
resultado = euclides(num_1,num_2)
print(f"El gcd de {num_1} y {num_2} es {resultado}")
print()

# Ejercicio 24

import math
def resolver_ecuacion(a,b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"Las soluciones de la ecuacion son: x1 = {x1} y x2 = {x2}")
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"La solucion es x = {x}")
    else:
        print("La ecuacion no tiene soluciones reales")
a = float(input("Ingresa el coeficiente a: "))
b = float(input("Ingresa el coeficiente b: "))
c = float(input("Ingresa el coeficiente c: "))
if a == 0:
    print("No es una ecuacion cuadratica, ya que a no puede ser 0")
else:
    resolver_ecuacion(a,b,c)
print()

# Ejercicio 25

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
num_factorial = int(input("Ingresa un numero para calcular su factorial: "))
print(f"El factorial de {num_factorial} es {factorial(num_factorial)}")
print()

def ackermann(x,y):
    if x == 0:
        return y + 1
    elif x > 0 and y == 0:
        return ackermann(x-1, 1)
    elif x > 0 and y > 0:
        return ackermann(x-1,ackermann(x,y-1))
valor_x = int(input("Ingresa el valor de x: "))
valor_y = int(input("Ingresa el valor de y: "))
print(f"El resultado de A{valor_x, valor_y} es {ackermann(valor_x, valor_y)}")
print()

# Ejercicio 26

positivo_1 = int(input("Ingresa el primer numero entero positivo: "))
positivo_2 = int(input("Ingresa el segundo numero entero positivo: "))
positivo_3 = int(input("Ingresa el tercer numero entero positivo: "))
if positivo_1 <= 0 or positivo_2 <= 0 or positivo_3 <= 0:
    print("Por favor, ingresa solamente numeros enteros positivos")
else:
    mayor = max(positivo_1, positivo_2, positivo_3)
    menor = min(positivo_1, positivo_2, positivo_3)
print(f"El numero mayor es {mayor}")
print(f"El numero menor es {menor}")
print()

# Ejercicio 27

def fahrenheit_a_celsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)
def main():
    while True:
        try:
            temp_f = float(input("Ingrese la temperatura en Fahrenheit (999 para salir): "))
            if temp_f == 999:
                print("Programa finalizado")
                break
            temp_c = fahrenheit_a_celsius(temp_f)
            print(f"{temp_f}°F equivale a {temp_c:.2f}°C")
        except ValueError:
            print("Entrada no valida. Por favor, ingrese un numero valido")
if __name__ == "__main__":
    main()
print()

# Ejercicio 28

def switch_ejemplo(valor):
    match valor:
        case 1:
            print("Caso 1: Opción uno seleccionada.")
        case 2:
            print("Caso 2: Opción dos seleccionada.")
        case 3:
            print("Caso 3: Opción tres seleccionada.")
        case _:
            print("Caso por defecto: Opción no reconocida.")

def main():
    for i in range(5):  # Prueba con valores de 0 a 4
        print(f"Probando con valor {i}:")
        switch_ejemplo(i)

if __name__ == "__main__":
    main()
print()

# Ejercicio 29

import sys

def main():
    print("Ingrese datos (CTRL+D en Unix/Linux/macOS o CTRL+Z en Windows para finalizar):")
    try:
        while True:
            linea = input()
            print(f"Leído: {linea}")
    except EOFError:
        print("Fin de la entrada detectado. Programa finalizado.")

if __name__ == "__main__":
    main()
print()

# Ejercicio 30

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def imprimir_primos(hasta):
    print(f"Números primos hasta {hasta}:")
    for num in range(2, hasta + 1):
        if es_primo(num):
            print(num, end=" ")
    print()

def main():
    limite = int(input("Ingrese el límite superior para encontrar números primos: "))
    imprimir_primos(limite)

if __name__ == "__main__":
    main()




