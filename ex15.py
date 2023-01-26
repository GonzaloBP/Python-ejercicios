from sys import argv

script, filename = argv

txt = open(filename)

print(f"Aqui esta tu archivo {filename}:")
print (txt.read())

print(" Ingresa nuevamente el nombre del archivo:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

