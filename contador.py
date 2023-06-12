#!/usr/bin/env python3

contador = 0

def incrementa_contador():
    # ... comeca o escopo local
    # assignment `=` `+=` `-=`
    global contador
    contador +=1


incrementa_contador()
incrementa_contador()
incrementa_contador()
incrementa_contador()

print(contador)