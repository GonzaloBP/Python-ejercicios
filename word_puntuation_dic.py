import string

# romeoyjuliteconputuacion.txt
fname = input("Ingrese el nombre del archivo:")
try:
    fhands = open(fname)
except:
    print("archivo no se puede abrir", fname)
    exit()
a_dic = dict()
for linea in fhands:
    linea = linea.rstrip()
    linea = linea.translate(linea.maketrans("", "", string.punctuation))
    linea = linea.lower()
    palabras = linea.split()
    for mi_palabra in palabras:
        a_dic[mi_palabra] = a_dic.get(mi_palabra, 0) + 1
print(a_dic)
