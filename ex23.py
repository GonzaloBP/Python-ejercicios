import sys 

script, entrada_codificada, error = sys.argv

def main(archivo_lenguages, encoding, errors):
    linea = archivo_lenguages.readline()
    if linea:
        print_linea(linea, encoding, errors)
        return main(archivo_lenguages, encoding, errors)

def print_linea(linea, encoding, errors):
    proximo_leng = linea.strip()
    raw_bytes = proximo_leng.encode(encoding, errors=errors)
    string_cocinado = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", string_cocinado)

language = open("languages.txt", encoding="utf-8")

main(language, entrada_codificada, error)