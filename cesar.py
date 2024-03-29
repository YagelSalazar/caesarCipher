#!/usr/bin/python3

#alf: abcde..z
#key: a #primera letra del alfabeto 1
#texto plano(plain text): hola
#texto cifrado(cipher text): ipmb

def main():
    texto = input("insertar texto plano: ")
    llave = input("insertar llave: ") #String, cadena de caracteres
    texto_cif = obtener_cifrado(llave,texto)
    f = open('cifrado.txt', 'w')
    f.write(texto_cif)

def obtener_cifrado(llave, texto_plano):
    cif = ""
    size = len(llave)
    for index,val in enumerate(texto_plano): #val es la letra
        c = ord(val) ^ ord(llave[index % size])
        print(hex(c))
        cif = cif + str(hex(c))
    return cif

main()