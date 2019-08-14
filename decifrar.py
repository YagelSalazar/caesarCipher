#!/usr/bin/python3

def main():
    llave = input("insertar llave: ")
    f = open('cifrado.txt', 'r')
    ctexto = f.read().split("0x")
    texto_plano = ""
    size = len(llave)
    ctexto.remove('')
    for index,val in enumerate(ctexto):
        c = int("0x"+val,16) ^ ord(llave[index % size])
        texto_plano += str(chr(c))
    f.close()
    
    print("texto plano: ")
    print(texto_plano)

main()