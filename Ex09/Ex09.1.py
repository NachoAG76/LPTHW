"""
  Created by Ignacio Álvarez García 
  on 20/02/2018 17:01
 """


def add(a, b):
    print(f"La suma es {a} + {b}")
    return a + b


def resta(a, b):
    print(f"La resta es {a} - {b}")
    return a - b


def multiplicacion(a, b):
    print(f"La multiplicación es {a} * {b}")
    return a + b


def division(a, b):
    print(f"La división es {a} / {b}")
    return a / b


edades = add(10, 15)
pesos = resta(35, 25)
altura = multiplicacion(95, 2)
divide = division(225, 2)

print(f"La suma de edades de Juan y pablo es:", edades, ",peso", pesos, ",altura",
      altura, "y coeficiente", divide)