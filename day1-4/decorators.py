#!/usr/bin/env python3

# decorators
from functools import wraps

## Dobra

def dobra(f):
    @wraps(f)
    def modificador(a, b):
        return f(a * 2, b * 2)
    return modificador



## Aplicando o decorator
def mult(a, b):
    return a * b

#funcao = dobra(funcao)
mult = dobra(mult)
assert mult(2,4)==32
## OU

@dobra
def soma(a, b):
    return a + b


assert soma(1, 2) == 6


## TExto HTML

def bold(f):
    @wraps(f)
    def wrapper(text):
        result = f(text)
        return f"<strong>{result}</strong>"
    return wrapper


def italic(f):
    @wraps(f)
    def wrapper(text):
        result = f(text)
        return f"<i>{result}</i>"
    return wrapper


@italic
@bold
def hello(text):
    return f"Hello {text}"

assert hello("Bruno") == '<i><strong>Hello Bruno</strong></i>'