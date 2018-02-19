"""
  Created by Ignacio Álvarez García 
  on 19/02/2018 10:31
 """
# Lectura de archivos

filename = 'ejemplo'
txt = open(filename, 'r')
print(txt.read())

txt.close()