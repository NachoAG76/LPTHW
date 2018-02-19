"""
  Created by Ignacio Álvarez García 
  on 19/02/2018 10:55
 """
# Funciones


def imprime_dos(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2:{arg2}")


def imprime_dos_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2:{arg2}")


def imprime_uno(arg1):
    print(f"arg1: {arg1}")


if __name__ == '__main__':
    imprime_dos("Juan", "Luis")
    imprime_dos_again("Pepe", "Fran")
    imprime_uno("Nacho")