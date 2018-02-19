"""
  Created by Ignacio Álvarez García 
  on 19/02/2018 9:44
 """
# Formatos

formatos = "{} {} {}"
print(formatos.format(1, 2, 3, 4))
print(formatos.format('uno', 'dos', 'tres'))
print(formatos.format(formatos, formatos, formatos))
print(formatos.format(
        "Tengo un plan.",
        "Necesito un plan.",
        "Me gusta el plan."
))

if __name__ == '__main__':
    pass