#!/usr/bin/env python3

def funcao(*args, timeout=10, **kwargs):
    for item in args:
        print(item)

    print(kwargs)

    print(f"timeout {timeout}")


funcao ("Adele", 1, True, [])
funcao(
    "Alice",
    1,
    False,
    timeout=90,
    nome="Atena",
    cidade="São Paulo",
    data="hoje",
    banana=1,
    panela=3,
    teclado=True,
    )