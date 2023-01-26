from sys import argv

script, archivo_entrada = argv


def print_todo(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_una_linea(contador_linea, f):
    print(contador_linea, f.readline())


archivo_actual = open(archivo_entrada)

print("Primero imprimamos todo el archivo: \n")

print_todo(archivo_actual)

print("ahora revovinemos el archivo, como si fuera una cinta")

rewind(archivo_actual)

print("Imprimamos las 3 primeras lineas")

linea_actual = 1

print_una_linea(linea_actual, archivo_actual)

linea_actual = linea_actual + 1

print_una_linea(linea_actual, archivo_actual)

linea_actual = linea_actual + 1

print_una_linea(linea_actual, archivo_actual)
