import sys 

script, entrada_codificada, error = sys.argv

def main(archivo_lenguages, codificado, errores):
    linea = archivo_lenguages.readline()
    if linea:
        print_linea(linea, codificada, errores)
        return main(archivo_lenguages, codificado, errores)

def print_linea(linea, codificado, errores):
    proximo_leng = line.strip()
    raw_bytes = proximo_leng.encode(codificado, errores=errores)
    string_cocinado = raw_bytes.decode(codificado, errores=errores)

    print(raw_bytes, "<===>", string_cocinado)

lenguages = open("languages.txt", codificado="utf-8")

main(language, entrada_codificada, error)