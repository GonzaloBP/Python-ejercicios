#   hacer esto en un archivo llamado test_argv.py

from sys import argv

script, nombre_usuario = argv
prompt = '> '

print (f" hola {nombre_usuario}, yo soy el {script} script.")
print (" Me gustaria preguntar algunas cosas")
print (f"Te gusta mi {nombre_usuario} ?" )
me_gusta = input(prompt)

print(f"Donde vives tu {nombre_usuario}")
direccion = input (prompt)

print( "Que clase de computadora tienes?")
computadora = input(prompt)

print(f"""
Bien, me has respondido que {me_gusta} te gusta tu nombre.
Que tu vives en {direccion}. Aunque realmente no se donde esta eso.
Y que tienes una computadora {computadora} ... que bichito lindo
""")

# para ejecutar  en terminar > python test_argv.py  theNoobMaster
