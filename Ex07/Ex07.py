"""
  Created by Ignacio Álvarez García 
  on 19/02/2018 10:06
 """
# Este módulo proporciona acceso a algunos objetos utilizados o mantenidos por el intérprete y a funciones que interactúan fuertemente con el intérprete.
from sys import argv

script, primero = argv

print("El archivo se llama", script)
print("La primera variable es: ", primero)

prompt ='>>'
print("Hola %s el nombre del programa es %s" %(primero, script))

if __name__ == '__main__':
    pass