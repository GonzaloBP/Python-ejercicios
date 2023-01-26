from sys import argv

script, filename = argv

print (f" vamos a borrar el contenido de un archivo {filename}")
print("si NO deseas borrarlo presiona CTRL-C ")
print("Si tu quires borrarlo, presiona ENTER")

# Pregunta por el curso de accion a seguir, borrar o cancelar operacion
input("?")

#abrimos el archivo que pasamos como parametro
print("abriendo un archivo")
target = open(filename, 'w')

print("truncando el archivo. ADIOS archivito")
target.truncate()

print("ahora voy a solicitarte que escribas 3 lineas de texto")

linea1 = input("line 1: ")
linea2 = input("line 2: ")
linea3 = input("line 3: ")

print("ahora voy a pasar las lineas que escribiste a un archivo recien borrado")

target.write(linea1)
target.write("\n")
target.write(linea2)
target.write("\n")
target.write(linea3)
target.write("\n")

print("and finalmente, vamos a cerrar el archivo que abrimos al comienzo")

