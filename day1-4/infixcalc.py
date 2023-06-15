#!/usr/bin/env python3
"""Calculadora infix.


Funcionamento:

[operacao] [n1] [n2]

Operações:

sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operacao: sum
n1: 5
n2: 4
9

Os resultados serão salvos em `infixcalc.log`
"""
__version__ = "0.1.0"

import os
import sys
import logging
from datetime import datetime

# Logging config
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("PYTHON-BASE", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'f:%(filename)s l:%(lineno)d: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = sys.argv[1:]

valid_operations = {
    "sum": lambda a,b: a + b, 
    "sub": lambda a,b: a - b,
    "mul": lambda a,b: a * b, 
    "div": lambda a,b: a / b,
    }

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USERNAME', 'anonymous')

while True:
    # Validacao
    
    if not arguments:
        operation = input("operação:")
        n1 = input("n1:")
        n2 = input("n2:")
        arguments = [operation, n1, n2]
    elif len(arguments) != 3:
        print("Número de argumentos inválidos")
        print("ex: `sum 5 5`")
        sys.exit(1)

    operation, *nums = arguments

    
    if operation not in valid_operations:
        print("Operação inválida")
        print(valid_operations)
        sys.exit(1)

    validated_nums = []

    for num in nums:
        if not num.replace(".", "").isdigit():
            print(f"Número inválido {num}")
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num)

    try:
        n1, n2 = validated_nums
    except ValueError as e:
        print(f"[Error] {str(e)}")
        sys.exit(1)

    result = valid_operations[operation](n1, n2)

    print(f"O resultado é {result}")

    try:
        with open(filepath, "a") as log_file:
            log_file.write(
                f"[{timestamp}][{user}] - {operation},{n1},{n2} = {result}\n"
            )
    except PermissionError as e:
        log.error(str(e))
        sys.exit(1)
    # print(f"{operation},{n1},{n2}= {result}\n", file=open(filename, "a"))

    arguments = []

    if input("Pressione enter para continuar ou qualquer tecla para sair "):
        break

