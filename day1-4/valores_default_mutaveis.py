#!/usr/bin/env python3

# set, dict, list
# s = set()
# s.add(1)
#
# d = {}
# d["key"] = "value"
#
# l = []
# l.append(0)


def adiciona_a_lista(valor, lista=None):
    if lista is None:
        lista = []
    lista.append(valor)
    return lista


adiciona_a_lista(4)
adiciona_a_lista(5)
print(adiciona_a_lista(6))
