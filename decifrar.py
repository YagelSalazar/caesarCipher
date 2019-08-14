def main():
    llave = input("insertar llave: ")
    f = open('cifrado.txt', 'r')
    ctexto = f.read()
    texto_plano = ""
    for index,val in enumerate(ctexto):
        c = ord(val) ^ ord(llave[0])
        texto_plano += str(chr(c))
    print("texto plano: ")
    print(texto_plano)

main()