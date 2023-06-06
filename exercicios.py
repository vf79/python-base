#!/bin/usr/env python3
"""
Faça um programa que imprime os números pares de 1 a 200
"""
def numeros_pares():
    for n in range(1,201):
        if n % 2 !=0:
            continue
        print(n)

"""
Alarme de temperatura
Faça um script que pergunta ao usuário qual a temperatura atual e o indice de 
umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo das 
condições

Se temp maior 45: ALERTA!!! Perigo calor extremo
Senão, se temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor úmido
...temp entre 10 e 30: Normal
...temp entre 0 e 10: Frio
...temp <0: ALERTA: Frio extremo
"""
import sys
import logging
log = logging.Logger("alerta")

def alarme_temp_opt():
    info = {
        "temperatura": None,
        "umidade": None,
    }

    keys = info.keys()
    for key in keys:
        try:
            info[key] = float(input(f"Qual a {key}? ").strip())
        except ValueError:
            log.error(f"{key.capitalize()} inválida")
            sys.exit(1)

    temperatura = info["temperatura"]
    umidade = info["umidade"]

    if temperatura > 45:
        print("ALERTA!!! Perigo calor extremo")
    elif temperatura * 3 >= umidade:
        print("ALERTA!!! Perigo calor úmido")
    elif temperatura >= 10 and  temperatura <=30:
        print("Normal")
    elif temperatura >= 0 and  temperatura <=10:
        print("Frio")
    elif temperatura < 0:
        print("ALERTA!!! Frio Extremo")



def alarme_temp():
    try:
        temp = float(input("Qual a temperatura?").strip())
    except ValueError:
        log.error("Temperatura inválida")
        sys.exit(1)
    
    try:
        umidade = float(input("Qual a umidade do ar").strip())
    except ValueError:
        log.error("Umidade inválida")
        sys.exit(1)

"""
Repete vogais
Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.
"""
def repete_vogal():
    words = []
    while True:
        word = input("Digite uma plavra (ou enter para sair):").strip()
        if not word:
            break

        final_word = ""
        for letter in word:
            # TODO: Remover acentuação usando função
            # Usando if tradicional
            """
            if letter.lower() in "aeiou":
                final_word += letter * 2
            else:
                final_word += letter
            """
            # Usando if Ternário
            final_word += letter * 2 if letter.lower() in "aeiouãêóíá" else letter

        words.append(final_word)

    #for word in words:
    #    print(word)
    print(*words, sep="\n")

# numeros_pares()
# alarme_temp_opt()
repete_vogal()