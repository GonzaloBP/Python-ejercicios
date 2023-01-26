from sys import argv
from os.path import exists

script, archivo_fuente, archivo_destino = argv

print(f"Copinado desde {archivo_fuente} al {archivo_destino}")

# podemos hacer esto solo en una linea, COMO ?
archivo_de_entrada = open(archivo_fuente)
datos_in = archivo_de_entrada.read()

print(f"los archivos de entrada tiene {len(datos_in)} bytes de tamaño")

print(f" el archivo destino EXISTE? {exists(archivo_destino)}")
print("Listo, presionar ENTER para continuar, CRTL-C para abortar.")
input()

archivo_resultado = open(archivo_destino,'w')
archivo_resultado.write(datos_in)

print("Todo listo muchachos tu archivito esta escrito, bye bye")

archivo_de_entrada.close()
archivo_resultado.close()