#!/bin/usr/env python3

"""Imprime apenas os nomes iniciados com a letra B"""

names = ["Bruno", "Joao", "Bernardo", "Barbara", "Brian",]

#for name in names:
#    if name.lower().startswith("b"):
#        print(name)

# estilo funcional
print("Estilo funcional")
print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")

print()
# estilo procedural
print("Estilo procedural")
# 

def starts_with_b(text):
    #return text.startswith(("b", "B"))
    return text[0].lower() == "b"

filtro = filter(starts_with_b, names)
filtro = list(filtro)
for name in filtro:
    print(name)


