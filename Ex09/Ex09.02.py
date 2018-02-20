"""
  Created by Ignacio Álvarez García 
  on 20/02/2018 17:18
 """
import sys
script, encoding , error = sys.argv

def main(archivo, encoding, errors):
    linea = archivo.readline()

    if linea:
        print_linea(linea, encoding, errors)
        return main(archivo, encoding, errors)


def print_linea(linea, encoding, errors):
    next_lang = linea.strip()
    rb = next_lang.encode(encoding, errors=errors)
    string = rb.decode(encoding, errors=errors)
    print(rb, "<==>", string)

idiomas = open('lenguajes.txt', encoding="utf-8")


main(idiomas, encoding, error)#Ejecutado desde la consola ,y dando  los argumentos de la línea 6
